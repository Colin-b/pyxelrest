"""
Each time the pyxelrest module is imported it will generate xlwings User Defined Functions.
"""
import os
import datetime

import jinja2

from vba import vba_restricted_keywords
from swagger_service import load_services

try:
    # Python 3
    from configparser import ConfigParser
except ImportError:
    # Python 2
    from ConfigParser import ConfigParser




def user_defined_functions(services):
    """
    Create xlwings User Defined Functions according to user_defined_functions template.
    :return: A string containing python code with all xlwings UDFs.
    """
    renderer = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), trim_blocks=True)
    return renderer.get_template('user_defined_functions.tpl').render(
        current_utc_time=datetime.datetime.utcnow().isoformat(),
        services=services,
        modified_parameters={value: key for key, value in vba_restricted_keywords.items()}
    )


def generate_user_defined_functions(services):
    """
    Create user_defined_functions.py python file containing generated xlwings User Defined Functions.
    :return: None
    """
    with open(os.path.join(os.path.dirname(__file__), 'user_defined_functions.py'), 'w') as generated_file:
        generated_file.write(user_defined_functions(services))




services = load_services()
generate_user_defined_functions(services)


from user_defined_functions import *

# Uncomment to debug Microsoft Excel UDF calls.
if __name__ == '__main__':
    xw.serve()
