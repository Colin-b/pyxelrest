from pyxelrest.version import __version__
from pyxelrest._exceptions import PyxelRestException


GENERATE_UDF_ON_IMPORT = True


def load(config: dict):
    global GENERATE_UDF_ON_IMPORT

    GENERATE_UDF_ON_IMPORT = False
    from pyxelrest import _generator

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
                }
            },
        )

        result = service.setdefault("result", {})
        # Send raw results if not specified otherwise
        result.setdefault("flatten", False)

    services = _generator.load_services(config)
    _generator.generate_python_file(services)
    _generator.load_user_defined_functions(services)
