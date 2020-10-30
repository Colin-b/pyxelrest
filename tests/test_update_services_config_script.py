import os.path

import yaml

import pyxelrest.update_services_config


def test_add_all_services_from_file_to_empty_config(tmpdir):
    with open(os.path.join(tmpdir, "services_list.yml"), "w") as services_list:
        yaml.dump({"svc1": {}, "svc2": {}}, services_list)

    updater = pyxelrest.update_services_config.ServicesConfigUpdater("add", os.path.join(tmpdir, "test_config.yml"))
    updater.update_configuration(
        os.path.join(tmpdir, "services_list.yml")
    )

    with open(os.path.join(tmpdir, "test_config.yml")) as test_config:
        assert yaml.load(test_config, Loader=yaml.SafeLoader) == {"svc1": {}, "svc2": {}}


def test_add_one_service_from_file_to_empty_config(tmpdir):
    with open(os.path.join(tmpdir, "services_list.yml"), "w") as services_list:
        yaml.dump({"svc1": {}, "svc2": {}}, services_list)

    updater = pyxelrest.update_services_config.ServicesConfigUpdater("add", os.path.join(tmpdir, "test_config.yml"))
    updater.update_configuration(
        os.path.join(tmpdir, "services_list.yml"), services=["svc2", "svc3"]
    )

    with open(os.path.join(tmpdir, "test_config.yml")) as test_config:
        assert yaml.load(test_config, Loader=yaml.SafeLoader) == {"svc2": {}}


def test_add_all_services_from_directory_to_empty_config(tmpdir):
    os.makedirs(os.path.join(tmpdir, "services"))
    with open(os.path.join(tmpdir, "services", "service1.yml"), "w") as service1:
        yaml.dump({"svc1": {}}, service1)
    with open(os.path.join(tmpdir, "services", "service2.yml"), "w") as service2:
        yaml.dump({"svc2": {}}, service2)

    updater = pyxelrest.update_services_config.ServicesConfigUpdater("add", os.path.join(tmpdir, "test_config.yml"))
    updater.update_configuration(
        os.path.join(tmpdir, "services")
    )

    with open(os.path.join(tmpdir, "test_config.yml")) as test_config:
        assert yaml.load(test_config, Loader=yaml.SafeLoader) == {"svc1": {}, "svc2": {}}


def test_add_a_subset_of_services_from_directory_to_empty_config(tmpdir):
    os.makedirs(os.path.join(tmpdir, "services"))
    with open(os.path.join(tmpdir, "services", "service1.yml"), "w") as service1:
        yaml.dump({"svc1": {}}, service1)
    with open(os.path.join(tmpdir, "services", "service2.yml"), "w") as service2:
        yaml.dump({"svc2": {}}, service2)
    with open(os.path.join(tmpdir, "services", "service3.yml"), "w") as service3:
        yaml.dump({"svc3": {}}, service3)

    updater = pyxelrest.update_services_config.ServicesConfigUpdater("add", os.path.join(tmpdir, "test_config.yml"))
    updater.update_configuration(
        os.path.join(tmpdir, "services"), services=["svc2", "svc3"]
    )

    with open(os.path.join(tmpdir, "test_config.yml")) as test_config:
        assert yaml.load(test_config, Loader=yaml.SafeLoader) == {"svc2": {}, "svc3": {}}


def test_list_services_from_directory(tmpdir, capsys):
    os.makedirs(os.path.join(tmpdir, "services"))
    with open(os.path.join(tmpdir, "services", "service1.yml"), "w") as service1:
        yaml.dump({"svc1": {}}, service1)
    with open(os.path.join(tmpdir, "services", "service2.yml"), "w") as service2:
        yaml.dump({"svc2": {}}, service2)
    with open(os.path.join(tmpdir, "services", "service3.yml"), "w") as service3:
        yaml.dump({"svc3": {}}, service3)

    updater = pyxelrest.update_services_config.ServicesConfigUpdater("list", os.path.join(tmpdir, "test_config.yml"))
    updater.update_configuration(
        os.path.join(tmpdir, "services")
    )

    assert capsys.readouterr().out == """svc1
svc2
svc3
"""


def test_list_subset_of_services_from_directory(tmpdir, capsys):
    os.makedirs(os.path.join(tmpdir, "services"))
    with open(os.path.join(tmpdir, "services", "service1.yml"), "w") as service1:
        yaml.dump({"svc1": {}}, service1)
    with open(os.path.join(tmpdir, "services", "service2.yml"), "w") as service2:
        yaml.dump({"svc2": {"description": "service desc"}}, service2)
    with open(os.path.join(tmpdir, "services", "service3.yml"), "w") as service3:
        yaml.dump({"svc3": {}}, service3)

    updater = pyxelrest.update_services_config.ServicesConfigUpdater("list", os.path.join(tmpdir, "test_config.yml"))
    updater.update_configuration(
        os.path.join(tmpdir, "services"), services=["svc2", "svc3"]
    )

    assert capsys.readouterr().out == """svc2 - service desc
svc3
"""

