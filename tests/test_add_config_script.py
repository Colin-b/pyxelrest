import os.path

import yaml
from responses import RequestsMock

import pyxelrest._add_config


def test_add_all_services_from_url_to_empty_config(tmpdir, responses: RequestsMock):
    responses.add(
        method=responses.GET,
        url="https://config_to_retrieve",
        body=yaml.dump({"svc1": {}, "svc2": {}}),
    )

    pyxelrest._add_config.main(
        os.path.join(tmpdir, "non_existing_folder", "test_config.yml"),
        "https://config_to_retrieve",
    )

    with open(
        os.path.join(tmpdir, "non_existing_folder", "test_config.yml")
    ) as test_config:
        assert yaml.load(test_config, Loader=yaml.SafeLoader) == {
            "svc1": {},
            "svc2": {},
        }


def test_add_all_services_from_url_to_existing_config(tmpdir, responses: RequestsMock):
    with open(os.path.join(tmpdir, "test_config.yml"), "w") as test_config:
        yaml.dump({"svc3": {}}, test_config)

    responses.add(
        method=responses.GET,
        url="https://config_to_retrieve",
        body=yaml.dump({"svc1": {}, "svc2": {}}),
    )

    pyxelrest._add_config.main(
        os.path.join(tmpdir, "test_config.yml"), "https://config_to_retrieve"
    )

    with open(os.path.join(tmpdir, "test_config.yml")) as test_config:
        assert yaml.load(test_config, Loader=yaml.SafeLoader) == {
            "svc3": {},
            "svc1": {},
            "svc2": {},
        }


def test_unable_to_load_existing_config(tmpdir, monkeypatch, caplog):
    with open(os.path.join(tmpdir, "test_config.yml"), "w") as test_config:
        yaml.dump({"svc3": {}}, test_config)

    def raise_error(*args, **kwargs):
        raise Exception("yaml load error")

    monkeypatch.setattr(pyxelrest._add_config.yaml, "load", raise_error)

    pyxelrest._add_config.main(
        os.path.join(tmpdir, "test_config.yml"), "https://config_to_retrieve"
    )

    assert caplog.messages == [
        f'Configuration file "{os.path.join(tmpdir, "test_config.yml")}" cannot be read.',
        "Unable to perform services configuration update.",
    ]


def test_error_http_response(tmpdir, responses: RequestsMock, caplog):
    responses.add(
        method=responses.GET,
        url="https://config_to_retrieve",
        status=404,
    )

    pyxelrest._add_config.main(
        os.path.join(tmpdir, "test_config.yml"), "https://config_to_retrieve"
    )

    assert not os.path.exists(os.path.join(tmpdir, "test_config.yml"))
    assert caplog.messages == [
        'Configuration file URL "https://config_to_retrieve" cannot be reached: 404 Client Error: Not Found for url: https://config_to_retrieve/.',
        "Services configuration cannot be updated.",
    ]


def test_unable_to_load_url_config(
    tmpdir, responses: RequestsMock, caplog, monkeypatch
):
    responses.add(
        method=responses.GET,
        url="https://config_to_retrieve",
    )

    updater = pyxelrest._add_config.ServicesConfigUpdater(
        os.path.join(tmpdir, "test_config.yml")
    )

    def raise_error(*args, **kwargs):
        raise Exception("yaml load error")

    monkeypatch.setattr(pyxelrest._add_config.yaml, "load", raise_error)

    updater.update_configuration("https://config_to_retrieve")

    assert not os.path.exists(os.path.join(tmpdir, "test_config.yml"))
    assert caplog.messages == [
        'Configuration file retrieved from URL "https://config_to_retrieve" cannot be loaded: yaml load error',
        "Services configuration cannot be updated.",
    ]


def test_main_error(tmpdir, monkeypatch, caplog):
    with open(os.path.join(tmpdir, "test_config.yml"), "w") as test_config:
        yaml.dump({"svc3": {}}, test_config)

    def raise_error(*args, **kwargs):
        raise Exception("yaml load error")

    monkeypatch.setattr(pyxelrest._add_config.yaml, "load", raise_error)

    pyxelrest._add_config.main(
        os.path.join(tmpdir, "test_config.yml"), "https://config_to_retrieve"
    )
    assert caplog.messages == [
        f'Configuration file "{os.path.join(tmpdir, "test_config.yml")}" cannot be read.',
        "Unable to perform services configuration update.",
    ]
