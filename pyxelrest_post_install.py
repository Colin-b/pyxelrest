import argparse
import os
import shutil
import sys
from distutils import log

from pyxelrest import com_server


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        log.info('Creating {0} folder'.format(folder_path))
        os.makedirs(folder_path)


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
        self._register_com_server()

    def _register_com_server(self):
        log.info('Registering COM server...')
        com_server.register_com()
        log.info('COM server registered.')

    def _create_services_configuration(self):
        default_config_file = os.path.join(self.installation_files_folder,
                                           'pyxelrest',
                                           'default_services_configuration.ini')
        if os.path.isfile(default_config_file):
            user_config_file = os.path.join(self.pyxelrest_appdata_config_folder, 'services.ini')
            if not os.path.isfile(user_config_file):
                shutil.copyfile(default_config_file, user_config_file)
                log.info('Services configuration file created.')
        else:
            raise Exception('Default services configuration file cannot be found in provided PyxelRest directory. {0}'
                            .format(default_config_file))

    def _create_pyxelrest_logging_configuration(self):
        self._create_logging_configuration('pyxelrest.log', 'logging.ini')

    def _create_auto_update_logging_configuration(self):
        self._create_logging_configuration('pyxelrest_auto_update.log', 'auto_update_logging.ini')

    def _create_logging_configuration(self, log_file_name, config_file_name):
        config_file_path = os.path.join(self.pyxelrest_appdata_config_folder, config_file_name)
        if not os.path.isfile(config_file_path):
            import jinja2
            template_folder = os.path.join(self.installation_files_folder, 'pyxelrest')
            renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(template_folder), trim_blocks=True)
            log_file_path = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'logs', log_file_name)
            with open(config_file_path, 'w') as generated_file:
                generated_file.write(renderer.get_template('default_logging_configuration.ini.jinja2')
                                     .render(path_to_log_file=log_file_path))
            log.info('{0} logging configuration file created.'.format(config_file_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--install_directory', help='Directory containing PyxelRest files for installation.',
                        default=None, type=str)
    options = parser.parse_args(sys.argv[1:])

    post_install = PostInstall(installation_files_folder=options.install_directory)
    post_install.perform_post_installation_tasks()
