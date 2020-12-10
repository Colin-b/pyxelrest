from importlib import reload, import_module

from pyxelrest.version import __version__
from pyxelrest._exceptions import PyxelRestException


GENERATE_UDF_ON_IMPORT = True


def _raw(response):
    if response.headers["content-type"] == "application/json":
        return response.json()

    return response.text


def load(config: dict, to_response: callable = _raw):
    """
    :param config: Configuration of all the REST API.
    :param to_response: Callable converting a requests.Response into the actual response returned by the functions.
    """
    global GENERATE_UDF_ON_IMPORT

    GENERATE_UDF_ON_IMPORT = False
    _generator = reload(import_module("pyxelrest._generator"))

    GENERATE_UDF_ON_IMPORT = True

    for service in config.values():
        service.setdefault(
            "formulas",
            {
                "dynamic_array": {
                    "lock_excel": False,
                    # Do not prefix functions with service name
                    "prefix": "",
                    # Raise HTTP exception
                    "raise_exception": True,
                    "convert_response": to_response,
                }
            },
        )

    services = _generator.load_services(config)
    _generator.generate_python_file(services)
    _generator.load_user_defined_functions(services)
