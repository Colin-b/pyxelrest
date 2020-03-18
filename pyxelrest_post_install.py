import argparse
from distutils import log
import os
import shutil
import sys


def create_folder(folder_path: str):
    if not os.path.exists(folder_path):
        log.info(f"Creating {folder_path} folder")
        os.makedirs(folder_path)


class PostInstall:
    def __init__(self, *, installation_files_folder: str = None):
        if not sys.platform.startswith("win"):
            raise Exception("PyxelRest can only be installed on Microsoft Windows.")

        self.installation_files_folder = installation_files_folder or os.path.abspath(
            os.path.dirname(__file__)
        )
        self.pyxelrest_appdata_folder = os.path.join(os.getenv("APPDATA"), "pyxelrest")
        self.pyxelrest_appdata_logs_folder = os.path.join(
            self.pyxelrest_appdata_folder, "logs"
        )
        self.pyxelrest_appdata_config_folder = os.path.join(
            self.pyxelrest_appdata_folder, "configuration"
        )

    def perform_post_installation_tasks(self):
        create_folder(self.pyxelrest_appdata_folder)
        create_folder(self.pyxelrest_appdata_logs_folder)
        create_folder(self.pyxelrest_appdata_config_folder)
        self._create_services_configuration()
        self._create_pyxelrest_logging_configuration()

    def _create_services_configuration(self):
        default_config_file = os.path.join(
            self.installation_files_folder,
            "pyxelrest",
            "default_services_configuration.yml",
        )
        if os.path.isfile(default_config_file):
            user_config_file = os.path.join(
                self.pyxelrest_appdata_config_folder, "services.yml"
            )
            if not os.path.isfile(user_config_file):
                shutil.copyfile(default_config_file, user_config_file)
                log.info("Services configuration file created.")
        else:
            raise Exception(
                f"Default services configuration file cannot be found in provided PyxelRest directory. {default_config_file}"
            )

    def _create_pyxelrest_logging_configuration(self):
        config_file_path = os.path.join(
            self.pyxelrest_appdata_config_folder, "logging.yml"
        )
        # Always keep default logging configuration up to date as logger name / parsing logic might change
        import jinja2

        template_folder = os.path.join(self.installation_files_folder, "pyxelrest")
        renderer = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_folder), trim_blocks=True
        )
        log_file_path = os.path.join(
            os.getenv("APPDATA"), "pyxelrest", "logs", "pyxelrest.log"
        )
        with open(config_file_path, "w") as generated_file:
            generated_file.write(
                renderer.get_template(
                    "default_logging_configuration.yml.jinja2"
                ).render(path_to_log_file=log_file_path)
            )
        log.info(f"{config_file_path} logging configuration file created.")


def main(*args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--install_directory",
        help="Directory containing PyxelRest files for installation.",
        default=None,
        type=str,
    )
    options = parser.parse_args(args if args else None)
    post_install = PostInstall(installation_files_folder=options.install_directory)
    post_install.perform_post_installation_tasks()


if __name__ == "__main__":
    main()
