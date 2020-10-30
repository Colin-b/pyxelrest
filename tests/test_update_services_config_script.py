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

