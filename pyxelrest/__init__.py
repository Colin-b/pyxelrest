import os

# Set to False in order to avoid generating UDFs on loading pyxelrestgenerator
GENERATE_UDF_ON_IMPORT = True

SERVICES_CONFIGURATION_FILE_PATH = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'services.yml')
LOGGING_CONFIGURATION_FILE_PATH = os.path.join(os.getenv('APPDATA'), 'pyxelrest', 'configuration', 'logging.yml')


def load(config):
    global GENERATE_UDF_ON_IMPORT

    GENERATE_UDF_ON_IMPORT = False
    from pyxelrest import pyxelrestgenerator, open_api
    GENERATE_UDF_ON_IMPORT = True

    # Send raw results and propagate exceptions by default
    for service in config.values():
        result = service.setdefault('result', {})
        result.setdefault('flatten', False)
        result.setdefault('raise_exception', True)

        udf = service.setdefault('udf', {})
        udf.setdefault('shift_result', False)

    services = open_api.load_services(config)
    pyxelrestgenerator.generate_python_file(services)
    pyxelrestgenerator.load_user_defined_functions(services)

