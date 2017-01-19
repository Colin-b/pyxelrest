from .pyxelrestlogging import *
import logging
from importlib import import_module
try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload

logging.info('Loading PyxelRest from module folder...')
try:
    # TODO This is temporary until xlwings force a python reload instead
    reload(import_module('.pyxelrest', package='pyxelrest'))
    from .pyxelrest import *
    logging.info('PyxelRest loaded from module folder.')
except:
    logging.exception('Unable to load PyxelRest from module folder.')