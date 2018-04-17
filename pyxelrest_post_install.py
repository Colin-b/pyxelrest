import argparse
from distutils import log
import os
import shutil
import sys
import yaml
try:
    # Python 3
    from configparser import ConfigParser
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        log.info('Creating {0} folder'.format(folder_path))
        os.makedirs(folder_path)


def convert_ini_to_yml(ini_file_path, yml_file_path):
    try:
        config_parser = ConfigParser(interpolation=None)
        if config_parser.read(ini_file_path):
            yaml_content = {
                service_name: convert_ini_service_to_yml(config_parser, service_name)
                for service_name in config_parser.sections()
            }
            with open(yml_file_path, 'w') as yml_file:
                yaml.dump(yaml_content, yml_file, default_flow_style=False)
            os.remove(ini_file_path)
    except:
        log.warn('Unable to convert ini services configuration file to yml.')


def convert_ini_service_to_yml(config_parser, service_name):
    yml_content = {}
    for key, value in config_parser.items(service_name):
        if 'methods' == key:
            yml_content[key] = [method.strip() for method in value.split(',')]
        elif 'security_details' == key:
            convert_security_details_to_yml(yml_content, value)
        elif 'advanced_configuration' == key:
            convert_advanced_configuration_to_yml(yml_content, value)
        elif 'swagger_url' == key:
            yml_content.setdefault('open_api', {})['definition'] = value
        elif 'service_host' == key:
            yml_content.setdefault('open_api', {})['service_host'] = value
        else:
            yml_content[key] = value
    return yml_content


def convert_security_details_to_yml(yml_content, security_details):
    yml_oauth2 = {}
    yml_basic = {}
    for security_detail in security_details.split(','):
        key, value = security_detail.split('=', maxsplit=1)
        if key in ['port', 'success_display_time', 'failure_display_time']:
            yml_oauth2[key] = int(value)
        elif 'timeout' == key:
            yml_oauth2[key] = float(value)
        elif key.startswith('oauth2.'):
            yml_oauth2[key[7:]] = value
        elif 'username' == key:
            yml_basic['username'] = value
        elif 'password' == key:
            yml_basic['password'] = value
        else:
            yml_oauth2[key] = value

    if yml_oauth2:
        yml_content['oauth2'] = yml_oauth2
    if yml_basic:
        yml_content['basic'] = yml_basic


def convert_advanced_configuration_to_yml(yml_content, advanced_configuration):
    for security_detail in advanced_configuration.split(','):
        key, value = security_detail.split('=', maxsplit=1)
        if key in ['connect_timeout', 'read_timeout']:
            yml_content[key] = float(value)
        elif 'swagger_read_timeout' == key:
            yml_content.setdefault('open_api', {})['definition_read_timeout'] = float(value)
        elif 'max_retries' == key:
            yml_content[key] = int(value)
        elif key.startswith('header.'):
            headers = yml_content.setdefault('headers', {})
            headers[key[7:]] = value
        elif 'tags' == key:
            yml_content.setdefault('open_api', {})['selected_tags'] = [tag.strip() for tag in value.split(';')]
        elif 'udf_return_type' == key:
            new_return_types = {'asynchronous': 'sync_auto_expand', 'synchronous': 'vba_compatible'}
            yml_content['udf'] = {
                'return_types': [new_return_types.get(return_type.strip()) for return_type in value.split(';')]
            }
        elif 'rely_on_definitions' == key:
            yml_content.setdefault('open_api', {})['rely_on_definitions'] = value == 'True'
        else:
            yml_content[key] = value


class PostInstall:
    def __init__(self, installation_files_folder=None):
        if not sys.platform.startswith('win'):
            raise Exception('PyxelRest can only be installed on Microsoft Windows.')

        self.installation_files_folder = installation_files_folder or os.path.abspath(os.path.dirname(__file__))
        self.pyxelrest_appdata_folder = os.path.join(os.getenv('APPDATA'), 'pyxelrest')
        self.pyxelrest_appdata_logs_folder = os.path.join(self.pyxelrest_appdata_folder, 'logs')
        self.pyxelrest_appdata_config_folder = os.path.join(self.pyxelrest_appdata_folder, 'configuration')

    def perform_post_installation_tasks(self):
        create_folder(self.pyxelrest_appdata_folder)
        create_folder(self.pyxelrest_appdata_logs_folder)
        create_folder(self.pyxelrest_appdata_config_folder)
        self._create_services_configuration()
        self._create_pyxelrest_logging_configuration()
        self._create_auto_update_logging_configuration()

    def _create_services_configuration(self):
        default_config_file = os.path.join(self.installation_files_folder,
                                           'pyxelrest',
                                           'default_services_configuration.yml')
        if os.path.isfile(default_config_file):
            ini_user_config_file = os.path.join(self.pyxelrest_appdata_config_folder, 'services.ini')
            user_config_file = os.path.join(self.pyxelrest_appdata_config_folder, 'services.yml')
            if os.path.isfile(ini_user_config_file):
                convert_ini_to_yml(ini_user_config_file, user_config_file)
            if not os.path.isfile(user_config_file):
                shutil.copyfile(default_config_file, user_config_file)
                log.info('Services configuration file created.')
        else:
            raise Exception('Default services configuration file cannot be found in provided PyxelRest directory. {0}'
                            .format(default_config_file))

    def _create_pyxelrest_logging_configuration(self):
        self._create_logging_configuration('pyxelrest.log', 'logging.yml')
        self._delete_deprecated_logging_configuration('logging.ini')

    def _create_auto_update_logging_configuration(self):
        self._create_logging_configuration('pyxelrest_auto_update.log', 'auto_update_logging.yml')
        self._delete_deprecated_logging_configuration('auto_update_logging.ini')

    def _delete_deprecated_logging_configuration(self, ini_config_file_name):
        try:
            init_config_file_path = os.path.join(self.pyxelrest_appdata_config_folder, ini_config_file_name)
            if os.path.isfile(init_config_file_path):
                os.remove(init_config_file_path)
        except:
            log.warn('{0} logging configuration file cannot be removed.'.format(ini_config_file_name))

    def _create_logging_configuration(self, log_file_name, config_file_name):
        config_file_path = os.path.join(self.pyxelrest_appdata_config_folder, config_file_name)
        # Always keep default logging configuration up to date as logger name / parsing logic might change
        import jinja2
        template_folder = os.path.join(self.installation_files_folder, 'pyxelrest')
        renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(template_folder), trim_blocks=True)
        log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', log_file_name)
        with open(config_file_path, 'w') as generated_file:
            generated_file.write(renderer.get_template('default_logging_configuration.yml.jinja2')
                                 .render(path_to_log_file=log_file_path))
        log.info('{0} logging configuration file created.'.format(config_file_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--install_directory', help='Directory containing PyxelRest files for installation.',
                        default=None, type=str)
    options = parser.parse_args(sys.argv[1:])

    post_install = PostInstall(installation_files_folder=options.install_directory)
    post_install.perform_post_installation_tasks()
