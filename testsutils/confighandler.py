import os
import shutil

services_config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'services.ini')
backup_services_config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'services.ini.back')

logging_config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'logging.ini')
backup_logging_config_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'logging.ini.back')


def set_new_configuration(new_configuration_file_name, remove_logging_config):
    if new_configuration_file_name:
        shutil.copyfile(services_config_file_path, backup_services_config_file_path)
        this_dir = os.path.abspath(os.path.dirname(__file__))
        shutil.copyfile(os.path.join(this_dir, new_configuration_file_name), services_config_file_path)
    else:
        shutil.move(services_config_file_path, backup_services_config_file_path)

    if remove_logging_config:
        shutil.move(logging_config_file_path, backup_logging_config_file_path)


def set_initial_configuration():
    if os.path.isfile(backup_services_config_file_path):
        shutil.move(backup_services_config_file_path, services_config_file_path)
    if os.path.isfile(backup_logging_config_file_path):
        shutil.move(backup_logging_config_file_path, logging_config_file_path)
