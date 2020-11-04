from distutils import log
import os
import sys


def create_folder(folder_path: str):
    if not os.path.exists(folder_path):
        log.info(f"Creating {folder_path} folder")
        os.makedirs(folder_path)


class PostInstall:
    def __init__(self):
        if not sys.platform.startswith("win"):
            raise Exception("PyxelRest can only be installed on Microsoft Windows.")

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
        self._create_pyxelrest_logging_configuration()

    def _create_pyxelrest_logging_configuration(self):
        config_file_path = os.path.join(
            self.pyxelrest_appdata_config_folder, "logging.yml"
        )
        log_file_path = os.path.join(
            self.pyxelrest_appdata_logs_folder, "pyxelrest.log"
        )
        # Always override default logging configuration as logger name might change
        with open(config_file_path, "w") as generated_file:
            generated_file.write(f"""version: 1
formatters:
  clean:
    format: '%(asctime)s [%(threadName)s] [%(levelname)s] %(message)s'
handlers:
  daily_rotating:
    class: logging.handlers.TimedRotatingFileHandler
    formatter: clean
    filename: {log_file_path}
    when: 'D'
    backupCount: 10
loggers:
  pyxelrest:
    level: DEBUG
  xlwings:
    level: DEBUG
  requests_auth:
    level: DEBUG
  requests.packages.urllib3:
    level: DEBUG
root:
  level: INFO
  handlers: [daily_rotating]
""")
        log.info(f"{config_file_path} logging configuration file created.")


def main():
    post_install = PostInstall()
    post_install.perform_post_installation_tasks()


if __name__ == "__main__":
    main()
