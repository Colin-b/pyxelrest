import os

# Set to False in order to avoid generating UDFs on loading pyxelrestgenerator
GENERATE_UDF_ON_IMPORT = True

SERVICES_CONFIGURATION_FILE_PATH = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'services.yml')
LOGGING_CONFIGURATION_FILE_PATH = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'logging.yml')
