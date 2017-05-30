"""
This file was generated. DO NOT EDIT manually.
Source file: user_defined_functions.jinja2
Generation date \(UTC\): \d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d.\d\d\d\d\d\d
"""
import xlwings as xw
import requests
import requests.exceptions
import datetime
import logging
import ujson
from collections import OrderedDict
import pandas
from fast_deserializer import Flattenizer
from definition_deserializer import Response
import definition_deserializer
import authentication







@xw.func(category='usual_parameters_test', call_in_wizard=False)
def usual_parameters_test_get_test_date():
    logging.info("Calling usual_parameters_test_get_test_date...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8943/test/date'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_get_test_date ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('format', 'date'), ('type', 'string')]))]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_get_test_date.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_get_test_date response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_get_test_date.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
def usual_parameters_test_get_test_date_time():
    logging.info("Calling usual_parameters_test_get_test_date_time...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8943/test/datetime'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_get_test_date_time ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')]))]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_get_test_date_time.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_get_test_date_time response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_get_test_date_time.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def usual_parameters_test_get_test_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling usual_parameters_test_get_test_with_all_optional_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.get('http://localhost:8943/test/with/all/optional/parameters/types'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_get_test_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_get_test_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_get_test_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_get_test_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def usual_parameters_test_post_test_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling usual_parameters_test_post_test_with_all_optional_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.post('http://localhost:8943/test/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_post_test_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_post_test_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_post_test_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_post_test_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def usual_parameters_test_put_test_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling usual_parameters_test_put_test_with_all_optional_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.put('http://localhost:8943/test/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_put_test_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_put_test_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_put_test_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_put_test_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def usual_parameters_test_delete_test_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling usual_parameters_test_delete_test_with_all_optional_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.delete('http://localhost:8943/test/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_delete_test_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_delete_test_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_delete_test_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_delete_test_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def usual_parameters_test_get_test_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling usual_parameters_test_get_test_with_all_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return 'query_integer is required.'
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return 'query_integer32 is required.'
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return 'query_integer64 is required.'
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return 'query_number is required.'
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return 'query_float is required.'
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return 'query_double is required.'
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return 'query_string is required.'
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return 'query_string_byte is required.'
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return 'query_string_binary is required.'
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return 'query_boolean is required.'
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return 'query_date is required.'
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return 'query_date_time is required.'
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return 'query_password is required.'
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return 'query_array_integer is required.'
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return 'query_array_integer32 is required.'
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return 'query_array_integer64 is required.'
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return 'query_array_number is required.'
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return 'query_array_float is required.'
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return 'query_array_double is required.'
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return 'query_array_string_byte is required.'
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return 'query_array_string_binary is required.'
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return 'query_array_boolean is required.'
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return 'query_array_date is required.'
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return 'query_array_date_time is required.'
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return 'query_array_password is required.'
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.get('http://localhost:8943/test/with/all/parameters/types'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_get_test_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_get_test_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_get_test_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_get_test_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def usual_parameters_test_post_test_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling usual_parameters_test_post_test_with_all_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return 'query_integer is required.'
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return 'query_integer32 is required.'
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return 'query_integer64 is required.'
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return 'query_number is required.'
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return 'query_float is required.'
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return 'query_double is required.'
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return 'query_string is required.'
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return 'query_string_byte is required.'
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return 'query_string_binary is required.'
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return 'query_boolean is required.'
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return 'query_date is required.'
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return 'query_date_time is required.'
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return 'query_password is required.'
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return 'query_array_integer is required.'
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return 'query_array_integer32 is required.'
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return 'query_array_integer64 is required.'
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return 'query_array_number is required.'
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return 'query_array_float is required.'
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return 'query_array_double is required.'
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return 'query_array_string_byte is required.'
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return 'query_array_string_binary is required.'
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return 'query_array_boolean is required.'
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return 'query_array_date is required.'
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return 'query_array_date_time is required.'
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return 'query_array_password is required.'
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.post('http://localhost:8943/test/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_post_test_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_post_test_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_post_test_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_post_test_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def usual_parameters_test_put_test_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling usual_parameters_test_put_test_with_all_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return 'query_integer is required.'
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return 'query_integer32 is required.'
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return 'query_integer64 is required.'
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return 'query_number is required.'
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return 'query_float is required.'
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return 'query_double is required.'
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return 'query_string is required.'
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return 'query_string_byte is required.'
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return 'query_string_binary is required.'
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return 'query_boolean is required.'
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return 'query_date is required.'
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return 'query_date_time is required.'
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return 'query_password is required.'
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return 'query_array_integer is required.'
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return 'query_array_integer32 is required.'
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return 'query_array_integer64 is required.'
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return 'query_array_number is required.'
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return 'query_array_float is required.'
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return 'query_array_double is required.'
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return 'query_array_string_byte is required.'
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return 'query_array_string_binary is required.'
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return 'query_array_boolean is required.'
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return 'query_array_date is required.'
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return 'query_array_date_time is required.'
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return 'query_array_password is required.'
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.put('http://localhost:8943/test/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_put_test_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_put_test_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_put_test_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_put_test_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def usual_parameters_test_delete_test_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling usual_parameters_test_delete_test_with_all_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return 'query_integer is required.'
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return 'query_integer32 is required.'
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return 'query_integer64 is required.'
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return 'query_number is required.'
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return 'query_float is required.'
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return 'query_double is required.'
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return 'query_string is required.'
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return 'query_string_byte is required.'
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return 'query_string_binary is required.'
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return 'query_boolean is required.'
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return 'query_date is required.'
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return 'query_date_time is required.'
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return 'query_password is required.'
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return 'query_array_integer is required.'
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return 'query_array_integer32 is required.'
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return 'query_array_integer64 is required.'
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return 'query_array_number is required.'
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return 'query_array_float is required.'
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return 'query_array_double is required.'
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return 'query_array_string_byte is required.'
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return 'query_array_string_binary is required.'
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return 'query_array_boolean is required.'
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return 'query_array_date is required.'
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return 'query_array_date_time is required.'
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return 'query_array_password is required.'
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.delete('http://localhost:8943/test/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_delete_test_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_delete_test_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_delete_test_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_delete_test_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
def usual_parameters_test_get_test_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling usual_parameters_test_get_test_with_all_paths_types...")
    request_header = {}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return 'path_integer is required.'

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return 'path_integer32 is required.'

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return 'path_integer64 is required.'

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return 'path_number is required.'

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return 'path_float is required.'

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return 'path_double is required.'

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return 'path_string is required.'

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return 'path_string_byte is required.'

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return 'path_string_binary is required.'

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return 'path_boolean is required.'

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return 'path_date is required.'

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return 'path_date_time is required.'

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return 'path_password is required.'

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return 'path_array_integer is required.'

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return 'path_array_integer32 is required.'

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return 'path_array_integer64 is required.'

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return 'path_array_number is required.'

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return 'path_array_float is required.'

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return 'path_array_double is required.'

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return 'path_array_string is required.'

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return 'path_array_string_byte is required.'

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return 'path_array_string_binary is required.'

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return 'path_array_boolean is required.'

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return 'path_array_date is required.'

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return 'path_array_date_time is required.'

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return 'path_array_password is required.'


    response = None
    try:
        response = requests.get('http://localhost:8943/test/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_get_test_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_get_test_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_get_test_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_get_test_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
def usual_parameters_test_post_test_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling usual_parameters_test_post_test_with_all_paths_types...")
    request_header = {}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return 'path_integer is required.'

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return 'path_integer32 is required.'

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return 'path_integer64 is required.'

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return 'path_number is required.'

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return 'path_float is required.'

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return 'path_double is required.'

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return 'path_string is required.'

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return 'path_string_byte is required.'

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return 'path_string_binary is required.'

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return 'path_boolean is required.'

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return 'path_date is required.'

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return 'path_date_time is required.'

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return 'path_password is required.'

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return 'path_array_integer is required.'

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return 'path_array_integer32 is required.'

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return 'path_array_integer64 is required.'

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return 'path_array_number is required.'

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return 'path_array_float is required.'

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return 'path_array_double is required.'

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return 'path_array_string is required.'

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return 'path_array_string_byte is required.'

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return 'path_array_string_binary is required.'

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return 'path_array_boolean is required.'

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return 'path_array_date is required.'

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return 'path_array_date_time is required.'

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return 'path_array_password is required.'


    response = None
    try:
        response = requests.post('http://localhost:8943/test/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_post_test_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_post_test_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_post_test_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_post_test_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
def usual_parameters_test_put_test_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling usual_parameters_test_put_test_with_all_paths_types...")
    request_header = {}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return 'path_integer is required.'

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return 'path_integer32 is required.'

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return 'path_integer64 is required.'

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return 'path_number is required.'

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return 'path_float is required.'

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return 'path_double is required.'

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return 'path_string is required.'

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return 'path_string_byte is required.'

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return 'path_string_binary is required.'

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return 'path_boolean is required.'

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return 'path_date is required.'

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return 'path_date_time is required.'

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return 'path_password is required.'

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return 'path_array_integer is required.'

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return 'path_array_integer32 is required.'

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return 'path_array_integer64 is required.'

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return 'path_array_number is required.'

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return 'path_array_float is required.'

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return 'path_array_double is required.'

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return 'path_array_string is required.'

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return 'path_array_string_byte is required.'

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return 'path_array_string_binary is required.'

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return 'path_array_boolean is required.'

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return 'path_array_date is required.'

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return 'path_array_date_time is required.'

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return 'path_array_password is required.'


    response = None
    try:
        response = requests.put('http://localhost:8943/test/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_put_test_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_put_test_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_put_test_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_put_test_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='usual_parameters_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
def usual_parameters_test_delete_test_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling usual_parameters_test_delete_test_with_all_paths_types...")
    request_header = {}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return 'path_integer is required.'

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return 'path_integer32 is required.'

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return 'path_integer64 is required.'

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return 'path_number is required.'

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return 'path_float is required.'

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return 'path_double is required.'

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return 'path_string is required.'

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return 'path_string_byte is required.'

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return 'path_string_binary is required.'

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return 'path_boolean is required.'

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return 'path_date is required.'

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return 'path_date_time is required.'

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return 'path_password is required.'

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return 'path_array_integer is required.'

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return 'path_array_integer32 is required.'

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return 'path_array_integer64 is required.'

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return 'path_array_number is required.'

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return 'path_array_float is required.'

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return 'path_array_double is required.'

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return 'path_array_string is required.'

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return 'path_array_string_byte is required.'

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return 'path_array_string_binary is required.'

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return 'path_array_boolean is required.'

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return 'path_array_date is required.'

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return 'path_array_date_time is required.'

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return 'path_array_password is required.'


    response = None
    try:
        response = requests.delete('http://localhost:8943/test/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_delete_test_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_delete_test_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling usual_parameters_test_delete_test_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_delete_test_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='filtered_tags_test', call_in_wizard=False)
def filtered_tags_test_get_test_with_tags():
    logging.info("Calling filtered_tags_test_get_test_with_tags...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8944/test/with/tags'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for filtered_tags_test_get_test_with_tags ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling filtered_tags_test_get_test_with_tags.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling filtered_tags_test_get_test_with_tags response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling filtered_tags_test_get_test_with_tags.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='filtered_tags_test', call_in_wizard=False)
def filtered_tags_test_post_test_with_tags():
    logging.info("Calling filtered_tags_test_post_test_with_tags...")
    request_header = {}

    response = None
    try:
        response = requests.post('http://localhost:8944/test/with/tags'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for filtered_tags_test_post_test_with_tags ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling filtered_tags_test_post_test_with_tags.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling filtered_tags_test_post_test_with_tags response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling filtered_tags_test_post_test_with_tags.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='filtered_tags_test', call_in_wizard=False)
def filtered_tags_test_put_test_with_tags():
    logging.info("Calling filtered_tags_test_put_test_with_tags...")
    request_header = {}

    response = None
    try:
        response = requests.put('http://localhost:8944/test/with/tags'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for filtered_tags_test_put_test_with_tags ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling filtered_tags_test_put_test_with_tags.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling filtered_tags_test_put_test_with_tags response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling filtered_tags_test_put_test_with_tags.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_empty_dictionary():
    logging.info("Calling values_false_test_get_test_with_empty_dictionary...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/empty/dictionary'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_empty_dictionary ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/EmptyDictionary')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_empty_dictionary.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling values_false_test_get_test_with_empty_dictionary response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_empty_dictionary.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_empty_list():
    logging.info("Calling values_false_test_get_test_with_empty_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/empty/list'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_empty_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/EmptyList')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_empty_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling values_false_test_get_test_with_empty_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_empty_list.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_empty_string():
    logging.info("Calling values_false_test_get_test_with_empty_string...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/empty/string'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_empty_string ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/EmptyString')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_empty_string.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling values_false_test_get_test_with_empty_string response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_empty_string.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_false_boolean():
    logging.info("Calling values_false_test_get_test_with_false_boolean...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/false/boolean'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_false_boolean ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/FalseBoolean')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_false_boolean.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling values_false_test_get_test_with_false_boolean response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_false_boolean.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_zero_float():
    logging.info("Calling values_false_test_get_test_with_zero_float...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/zero/float'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_zero_float ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/ZeroFloat')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_zero_float.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling values_false_test_get_test_with_zero_float response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_zero_float.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_zero_integer():
    logging.info("Calling values_false_test_get_test_with_zero_integer...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/zero/integer'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_zero_integer ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/ZeroInteger')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_zero_integer.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling values_false_test_get_test_with_zero_integer response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_zero_integer.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='output_order_test', call_in_wizard=False)
@xw.arg('date_visual_basic', dates=datetime.date, doc='date')
@xw.arg('curve', doc='curvename')
@xw.arg('ts', doc='timeslot')
@xw.arg('mat', doc='maturity')
def output_order_test_get_test_price_unordered(date_visual_basic=None, curve=None, ts=None, mat=None):
    logging.info("Calling output_order_test_get_test_price_unordered...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if date_visual_basic is not None:
        if not isinstance(date_visual_basic, datetime.date):
            logging.error('date_visual_basic must be a date.')
            return 'date_visual_basic must be a date.'

        request_parameters['date'] = date_visual_basic

    if curve is not None:

        request_parameters['curve'] = curve

    if ts is not None:

        request_parameters['ts'] = ts

    if mat is not None:

        request_parameters['mat'] = mat


    response = None
    try:
        response = requests.get('http://localhost:8946/price/unordered'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for output_order_test_get_test_price_unordered ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Price')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Price', OrderedDict([('required', ['curve', 'date', 'mat', 'ts']), ('type', 'object'), ('properties', OrderedDict([('ts', OrderedDict([('type', 'string'), ('description', 'timeslot'), ('maxLength', 2)])), ('date', OrderedDict([('type', 'string'), ('description', 'date'), ('format', 'date')])), ('curve', OrderedDict([('type', 'string'), ('description', 'curvename'), ('maxLength', 20)])), ('mat', OrderedDict([('type', 'string'), ('description', 'maturity'), ('maxLength', 4)]))])), ('title', 'RealizedPrice')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling output_order_test_get_test_price_unordered.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling output_order_test_get_test_price_unordered response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling output_order_test_get_test_price_unordered.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_empty_nested_list():
    logging.info("Calling nested_data_test_get_test_dict_with_empty_nested_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/empty/nested/list'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_empty_nested_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_empty_nested_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_empty_nested_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_empty_nested_list.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_four_imbricated_levels():
    logging.info("Calling nested_data_test_get_test_dict_with_four_imbricated_levels...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/four/imbricated/levels'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_four_imbricated_levels ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_four_imbricated_levels.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_four_imbricated_levels response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_four_imbricated_levels.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_list():
    logging.info("Calling nested_data_test_get_test_dict_with_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/list'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation')]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_list.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_list_of_different_size():
    logging.info("Calling nested_data_test_get_test_dict_with_list_of_different_size...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/list/of/different/size'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_list_of_different_size ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation')]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_list_of_different_size.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_list_of_different_size response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_list_of_different_size.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys():
    logging.info("Calling nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/multiple/imbricated/levels/and/duplicate/keys'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_three_imbricated_levels():
    logging.info("Calling nested_data_test_get_test_dict_with_three_imbricated_levels...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/three/imbricated/levels'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_three_imbricated_levels ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_three_imbricated_levels.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_three_imbricated_levels response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_three_imbricated_levels.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_various_columns():
    logging.info("Calling nested_data_test_get_test_dict_with_various_columns...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/various/columns'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_various_columns ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation')]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_various_columns.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_various_columns response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_various_columns.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_empty_dict():
    logging.info("Calling nested_data_test_get_test_empty_dict...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/empty/dict'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_empty_dict ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_empty_dict.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_empty_dict response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_empty_dict.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_empty_list():
    logging.info("Calling nested_data_test_get_test_empty_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/empty/list'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_empty_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_empty_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_empty_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_empty_list.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_list_of_dict():
    logging.info("Calling nested_data_test_get_test_list_of_dict...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/list/of/dict'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_list_of_dict ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_list_of_dict.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_list_of_dict response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_list_of_dict.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_one_dict_entry_with_a_list():
    logging.info("Calling nested_data_test_get_test_one_dict_entry_with_a_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/one/dict/entry/with/a/list'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_one_dict_entry_with_a_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column1List')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_one_dict_entry_with_a_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_one_dict_entry_with_a_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_one_dict_entry_with_a_list.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_one_dict_entry_with_a_list_of_dict():
    logging.info("Calling nested_data_test_get_test_one_dict_entry_with_a_list_of_dict...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/one/dict/entry/with/a/list/of/dict'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_one_dict_entry_with_a_list_of_dict ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column1')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_one_dict_entry_with_a_list_of_dict.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_one_dict_entry_with_a_list_of_dict response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_one_dict_entry_with_a_list_of_dict.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_one_level_dict():
    logging.info("Calling nested_data_test_get_test_one_level_dict...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/one/level/dict'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_one_level_dict ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column2And3')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_one_level_dict.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_one_level_dict response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_one_level_dict.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_one_level_list():
    logging.info("Calling nested_data_test_get_test_one_level_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/one/level/list'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_one_level_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_one_level_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling nested_data_test_get_test_one_level_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_one_level_list.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='vba_keywords_test', call_in_wizard=False)
@xw.arg('addhandler_visual_basic', doc='')
@xw.arg('addressof_visual_basic', doc='')
@xw.arg('alias_visual_basic', doc='')
@xw.arg('and_visual_basic', doc='')
@xw.arg('andalso_visual_basic', doc='')
@xw.arg('as_visual_basic', doc='')
@xw.arg('boolean_visual_basic', doc='')
@xw.arg('byref_visual_basic', doc='')
@xw.arg('byte_visual_basic', doc='')
@xw.arg('byval_visual_basic', doc='')
@xw.arg('call_visual_basic', doc='')
@xw.arg('case_visual_basic', doc='')
@xw.arg('catch_visual_basic', doc='')
@xw.arg('cbool_visual_basic', doc='')
@xw.arg('cbyte_visual_basic', doc='')
@xw.arg('cchar_visual_basic', doc='')
@xw.arg('cdate_visual_basic', doc='')
@xw.arg('cdbl_visual_basic', doc='')
@xw.arg('cdec_visual_basic', doc='')
@xw.arg('char_visual_basic', doc='')
@xw.arg('cint_visual_basic', doc='')
@xw.arg('class_visual_basic', doc='')
@xw.arg('clng_visual_basic', doc='')
@xw.arg('cobj_visual_basic', doc='')
@xw.arg('const_visual_basic', doc='')
@xw.arg('continue_visual_basic', doc='')
@xw.arg('csbyte_visual_basic', doc='')
@xw.arg('cshort_visual_basic', doc='')
@xw.arg('csng_visual_basic', doc='')
@xw.arg('cstr_visual_basic', doc='')
@xw.arg('ctype_visual_basic', doc='')
@xw.arg('cuint_visual_basic', doc='')
@xw.arg('culng_visual_basic', doc='')
@xw.arg('currency_visual_basic', doc='')
@xw.arg('cushort_visual_basic', doc='')
@xw.arg('date_visual_basic', doc='')
@xw.arg('decimal_visual_basic', doc='')
@xw.arg('declare_visual_basic', doc='')
@xw.arg('default_visual_basic', doc='')
@xw.arg('delegate_visual_basic', doc='')
@xw.arg('dim_visual_basic', doc='')
@xw.arg('directcast_visual_basic', doc='')
@xw.arg('do_visual_basic', doc='')
@xw.arg('double_visual_basic', doc='')
@xw.arg('each_visual_basic', doc='')
@xw.arg('else_visual_basic', doc='')
@xw.arg('elseif_visual_basic', doc='')
@xw.arg('end_visual_basic', doc='')
@xw.arg('endif_visual_basic', doc='')
@xw.arg('enum_visual_basic', doc='')
@xw.arg('erase_visual_basic', doc='')
@xw.arg('error_visual_basic', doc='')
@xw.arg('event_visual_basic', doc='')
@xw.arg('exit_visual_basic', doc='')
@xw.arg('finally_visual_basic', doc='')
@xw.arg('for_visual_basic', doc='')
@xw.arg('friend_visual_basic', doc='')
@xw.arg('function_visual_basic', doc='')
@xw.arg('get_visual_basic', doc='')
@xw.arg('gettype_visual_basic', doc='')
@xw.arg('getxmlnamespace_visual_basic', doc='')
@xw.arg('global_visual_basic', doc='')
@xw.arg('gosub_visual_basic', doc='')
@xw.arg('goto_visual_basic', doc='')
@xw.arg('handles_visual_basic', doc='')
@xw.arg('if_visual_basic', doc='')
@xw.arg('implements_visual_basic', doc='')
@xw.arg('imports_visual_basic', doc='')
@xw.arg('in_visual_basic', doc='')
@xw.arg('inherits_visual_basic', doc='')
@xw.arg('integer_visual_basic', doc='')
@xw.arg('interface_visual_basic', doc='')
@xw.arg('is_visual_basic', doc='')
@xw.arg('isnot_visual_basic', doc='')
@xw.arg('let_visual_basic', doc='')
@xw.arg('lib_visual_basic', doc='')
@xw.arg('like_visual_basic', doc='')
@xw.arg('long_visual_basic', doc='')
@xw.arg('loop_visual_basic', doc='')
@xw.arg('me_visual_basic', doc='')
@xw.arg('mod_visual_basic', doc='')
@xw.arg('module_visual_basic', doc='')
@xw.arg('mustinherit_visual_basic', doc='')
@xw.arg('mustoverride_visual_basic', doc='')
@xw.arg('mybase_visual_basic', doc='')
@xw.arg('myclass_visual_basic', doc='')
@xw.arg('namespace_visual_basic', doc='')
@xw.arg('narrowing_visual_basic', doc='')
@xw.arg('new_visual_basic', doc='')
@xw.arg('next_visual_basic', doc='')
@xw.arg('not_visual_basic', doc='')
@xw.arg('nothing_visual_basic', doc='')
@xw.arg('notinheritable_visual_basic', doc='')
@xw.arg('notoverridable_visual_basic', doc='')
@xw.arg('object_visual_basic', doc='')
@xw.arg('of_visual_basic', doc='')
@xw.arg('on_visual_basic', doc='')
@xw.arg('operator_visual_basic', doc='')
@xw.arg('option_visual_basic', doc='')
@xw.arg('optional_visual_basic', doc='')
@xw.arg('or_visual_basic', doc='')
@xw.arg('orelse_visual_basic', doc='')
@xw.arg('overloads_visual_basic', doc='')
@xw.arg('overridable_visual_basic', doc='')
@xw.arg('overrides_visual_basic', doc='')
@xw.arg('paramarray_visual_basic', doc='')
@xw.arg('partial_visual_basic', doc='')
@xw.arg('private_visual_basic', doc='')
@xw.arg('property_visual_basic', doc='')
@xw.arg('protected_visual_basic', doc='')
@xw.arg('public_visual_basic', doc='')
@xw.arg('raiseevent_visual_basic', doc='')
@xw.arg('readonly_visual_basic', doc='')
@xw.arg('redim_visual_basic', doc='')
@xw.arg('rem_visual_basic', doc='')
@xw.arg('removehandler_visual_basic', doc='')
@xw.arg('resume_visual_basic', doc='')
@xw.arg('return_visual_basic', doc='')
@xw.arg('sbyte_visual_basic', doc='')
@xw.arg('select_visual_basic', doc='')
@xw.arg('set_visual_basic', doc='')
@xw.arg('shadows_visual_basic', doc='')
@xw.arg('shared_visual_basic', doc='')
@xw.arg('short_visual_basic', doc='')
@xw.arg('single_visual_basic', doc='')
@xw.arg('static_visual_basic', doc='')
@xw.arg('step_visual_basic', doc='')
@xw.arg('stop_visual_basic', doc='')
@xw.arg('string_visual_basic', doc='')
@xw.arg('structure_visual_basic', doc='')
@xw.arg('sub_visual_basic', doc='')
@xw.arg('synclock_visual_basic', doc='')
@xw.arg('then_visual_basic', doc='')
@xw.arg('throw_visual_basic', doc='')
@xw.arg('to_visual_basic', doc='')
@xw.arg('try_visual_basic', doc='')
@xw.arg('trycast_visual_basic', doc='')
@xw.arg('type_visual_basic', doc='')
@xw.arg('typeof_visual_basic', doc='')
@xw.arg('uinteger_visual_basic', doc='')
@xw.arg('ulong_visual_basic', doc='')
@xw.arg('ushort_visual_basic', doc='')
@xw.arg('using_visual_basic', doc='')
@xw.arg('variant_visual_basic', doc='')
@xw.arg('wend_visual_basic', doc='')
@xw.arg('when_visual_basic', doc='')
@xw.arg('while_visual_basic', doc='')
@xw.arg('widening_visual_basic', doc='')
@xw.arg('with_visual_basic', doc='')
@xw.arg('withevents_visual_basic', doc='')
@xw.arg('writeonly_visual_basic', doc='')
@xw.arg('xor_visual_basic', doc='')
@xw.ret(expand='table')
def vba_keywords_test_get_test_vba_restricted_keywords(addhandler_visual_basic, addressof_visual_basic, alias_visual_basic, and_visual_basic, andalso_visual_basic, as_visual_basic, boolean_visual_basic, byref_visual_basic, byte_visual_basic, byval_visual_basic, call_visual_basic, case_visual_basic, catch_visual_basic, cbool_visual_basic, cbyte_visual_basic, cchar_visual_basic, cdate_visual_basic, cdbl_visual_basic, cdec_visual_basic, char_visual_basic, cint_visual_basic, class_visual_basic, clng_visual_basic, cobj_visual_basic, const_visual_basic, continue_visual_basic, csbyte_visual_basic, cshort_visual_basic, csng_visual_basic, cstr_visual_basic, ctype_visual_basic, cuint_visual_basic, culng_visual_basic, currency_visual_basic, cushort_visual_basic, date_visual_basic, decimal_visual_basic, declare_visual_basic, default_visual_basic, delegate_visual_basic, dim_visual_basic, directcast_visual_basic, do_visual_basic, double_visual_basic, each_visual_basic, else_visual_basic, elseif_visual_basic, end_visual_basic, endif_visual_basic, enum_visual_basic, erase_visual_basic, error_visual_basic, event_visual_basic, exit_visual_basic, finally_visual_basic, for_visual_basic, friend_visual_basic, function_visual_basic, get_visual_basic, gettype_visual_basic, getxmlnamespace_visual_basic, global_visual_basic, gosub_visual_basic, goto_visual_basic, handles_visual_basic, if_visual_basic, implements_visual_basic, imports_visual_basic, in_visual_basic, inherits_visual_basic, integer_visual_basic, interface_visual_basic, is_visual_basic, isnot_visual_basic, let_visual_basic, lib_visual_basic, like_visual_basic, long_visual_basic, loop_visual_basic, me_visual_basic, mod_visual_basic, module_visual_basic, mustinherit_visual_basic, mustoverride_visual_basic, mybase_visual_basic, myclass_visual_basic, namespace_visual_basic, narrowing_visual_basic, new_visual_basic, next_visual_basic, not_visual_basic, nothing_visual_basic, notinheritable_visual_basic, notoverridable_visual_basic, object_visual_basic, of_visual_basic, on_visual_basic, operator_visual_basic, option_visual_basic, optional_visual_basic, or_visual_basic, orelse_visual_basic, overloads_visual_basic, overridable_visual_basic, overrides_visual_basic, paramarray_visual_basic, partial_visual_basic, private_visual_basic, property_visual_basic, protected_visual_basic, public_visual_basic, raiseevent_visual_basic, readonly_visual_basic, redim_visual_basic, rem_visual_basic, removehandler_visual_basic, resume_visual_basic, return_visual_basic, sbyte_visual_basic, select_visual_basic, set_visual_basic, shadows_visual_basic, shared_visual_basic, short_visual_basic, single_visual_basic, static_visual_basic, step_visual_basic, stop_visual_basic, string_visual_basic, structure_visual_basic, sub_visual_basic, synclock_visual_basic, then_visual_basic, throw_visual_basic, to_visual_basic, try_visual_basic, trycast_visual_basic, type_visual_basic, typeof_visual_basic, uinteger_visual_basic, ulong_visual_basic, ushort_visual_basic, using_visual_basic, variant_visual_basic, wend_visual_basic, when_visual_basic, while_visual_basic, widening_visual_basic, with_visual_basic, withevents_visual_basic, writeonly_visual_basic, xor_visual_basic):
    logging.info("Calling vba_keywords_test_get_test_vba_restricted_keywords...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if addhandler_visual_basic is None or isinstance(addhandler_visual_basic, list) and all(x is None for x in addhandler_visual_basic):
        logging.error('addhandler_visual_basic is required.')
        return ['addhandler_visual_basic is required.']
    if addhandler_visual_basic is not None:

        request_parameters['addhandler'] = addhandler_visual_basic

    if addressof_visual_basic is None or isinstance(addressof_visual_basic, list) and all(x is None for x in addressof_visual_basic):
        logging.error('addressof_visual_basic is required.')
        return ['addressof_visual_basic is required.']
    if addressof_visual_basic is not None:

        request_parameters['addressof'] = addressof_visual_basic

    if alias_visual_basic is None or isinstance(alias_visual_basic, list) and all(x is None for x in alias_visual_basic):
        logging.error('alias_visual_basic is required.')
        return ['alias_visual_basic is required.']
    if alias_visual_basic is not None:

        request_parameters['alias'] = alias_visual_basic

    if and_visual_basic is None or isinstance(and_visual_basic, list) and all(x is None for x in and_visual_basic):
        logging.error('and_visual_basic is required.')
        return ['and_visual_basic is required.']
    if and_visual_basic is not None:

        request_parameters['and'] = and_visual_basic

    if andalso_visual_basic is None or isinstance(andalso_visual_basic, list) and all(x is None for x in andalso_visual_basic):
        logging.error('andalso_visual_basic is required.')
        return ['andalso_visual_basic is required.']
    if andalso_visual_basic is not None:

        request_parameters['andalso'] = andalso_visual_basic

    if as_visual_basic is None or isinstance(as_visual_basic, list) and all(x is None for x in as_visual_basic):
        logging.error('as_visual_basic is required.')
        return ['as_visual_basic is required.']
    if as_visual_basic is not None:

        request_parameters['as'] = as_visual_basic

    if boolean_visual_basic is None or isinstance(boolean_visual_basic, list) and all(x is None for x in boolean_visual_basic):
        logging.error('boolean_visual_basic is required.')
        return ['boolean_visual_basic is required.']
    if boolean_visual_basic is not None:

        request_parameters['boolean'] = boolean_visual_basic

    if byref_visual_basic is None or isinstance(byref_visual_basic, list) and all(x is None for x in byref_visual_basic):
        logging.error('byref_visual_basic is required.')
        return ['byref_visual_basic is required.']
    if byref_visual_basic is not None:

        request_parameters['byref'] = byref_visual_basic

    if byte_visual_basic is None or isinstance(byte_visual_basic, list) and all(x is None for x in byte_visual_basic):
        logging.error('byte_visual_basic is required.')
        return ['byte_visual_basic is required.']
    if byte_visual_basic is not None:

        request_parameters['byte'] = byte_visual_basic

    if byval_visual_basic is None or isinstance(byval_visual_basic, list) and all(x is None for x in byval_visual_basic):
        logging.error('byval_visual_basic is required.')
        return ['byval_visual_basic is required.']
    if byval_visual_basic is not None:

        request_parameters['byval'] = byval_visual_basic

    if call_visual_basic is None or isinstance(call_visual_basic, list) and all(x is None for x in call_visual_basic):
        logging.error('call_visual_basic is required.')
        return ['call_visual_basic is required.']
    if call_visual_basic is not None:

        request_parameters['call'] = call_visual_basic

    if case_visual_basic is None or isinstance(case_visual_basic, list) and all(x is None for x in case_visual_basic):
        logging.error('case_visual_basic is required.')
        return ['case_visual_basic is required.']
    if case_visual_basic is not None:

        request_parameters['case'] = case_visual_basic

    if catch_visual_basic is None or isinstance(catch_visual_basic, list) and all(x is None for x in catch_visual_basic):
        logging.error('catch_visual_basic is required.')
        return ['catch_visual_basic is required.']
    if catch_visual_basic is not None:

        request_parameters['catch'] = catch_visual_basic

    if cbool_visual_basic is None or isinstance(cbool_visual_basic, list) and all(x is None for x in cbool_visual_basic):
        logging.error('cbool_visual_basic is required.')
        return ['cbool_visual_basic is required.']
    if cbool_visual_basic is not None:

        request_parameters['cbool'] = cbool_visual_basic

    if cbyte_visual_basic is None or isinstance(cbyte_visual_basic, list) and all(x is None for x in cbyte_visual_basic):
        logging.error('cbyte_visual_basic is required.')
        return ['cbyte_visual_basic is required.']
    if cbyte_visual_basic is not None:

        request_parameters['cbyte'] = cbyte_visual_basic

    if cchar_visual_basic is None or isinstance(cchar_visual_basic, list) and all(x is None for x in cchar_visual_basic):
        logging.error('cchar_visual_basic is required.')
        return ['cchar_visual_basic is required.']
    if cchar_visual_basic is not None:

        request_parameters['cchar'] = cchar_visual_basic

    if cdate_visual_basic is None or isinstance(cdate_visual_basic, list) and all(x is None for x in cdate_visual_basic):
        logging.error('cdate_visual_basic is required.')
        return ['cdate_visual_basic is required.']
    if cdate_visual_basic is not None:

        request_parameters['cdate'] = cdate_visual_basic

    if cdbl_visual_basic is None or isinstance(cdbl_visual_basic, list) and all(x is None for x in cdbl_visual_basic):
        logging.error('cdbl_visual_basic is required.')
        return ['cdbl_visual_basic is required.']
    if cdbl_visual_basic is not None:

        request_parameters['cdbl'] = cdbl_visual_basic

    if cdec_visual_basic is None or isinstance(cdec_visual_basic, list) and all(x is None for x in cdec_visual_basic):
        logging.error('cdec_visual_basic is required.')
        return ['cdec_visual_basic is required.']
    if cdec_visual_basic is not None:

        request_parameters['cdec'] = cdec_visual_basic

    if char_visual_basic is None or isinstance(char_visual_basic, list) and all(x is None for x in char_visual_basic):
        logging.error('char_visual_basic is required.')
        return ['char_visual_basic is required.']
    if char_visual_basic is not None:

        request_parameters['char'] = char_visual_basic

    if cint_visual_basic is None or isinstance(cint_visual_basic, list) and all(x is None for x in cint_visual_basic):
        logging.error('cint_visual_basic is required.')
        return ['cint_visual_basic is required.']
    if cint_visual_basic is not None:

        request_parameters['cint'] = cint_visual_basic

    if class_visual_basic is None or isinstance(class_visual_basic, list) and all(x is None for x in class_visual_basic):
        logging.error('class_visual_basic is required.')
        return ['class_visual_basic is required.']
    if class_visual_basic is not None:

        request_parameters['class'] = class_visual_basic

    if clng_visual_basic is None or isinstance(clng_visual_basic, list) and all(x is None for x in clng_visual_basic):
        logging.error('clng_visual_basic is required.')
        return ['clng_visual_basic is required.']
    if clng_visual_basic is not None:

        request_parameters['clng'] = clng_visual_basic

    if cobj_visual_basic is None or isinstance(cobj_visual_basic, list) and all(x is None for x in cobj_visual_basic):
        logging.error('cobj_visual_basic is required.')
        return ['cobj_visual_basic is required.']
    if cobj_visual_basic is not None:

        request_parameters['cobj'] = cobj_visual_basic

    if const_visual_basic is None or isinstance(const_visual_basic, list) and all(x is None for x in const_visual_basic):
        logging.error('const_visual_basic is required.')
        return ['const_visual_basic is required.']
    if const_visual_basic is not None:

        request_parameters['const'] = const_visual_basic

    if continue_visual_basic is None or isinstance(continue_visual_basic, list) and all(x is None for x in continue_visual_basic):
        logging.error('continue_visual_basic is required.')
        return ['continue_visual_basic is required.']
    if continue_visual_basic is not None:

        request_parameters['continue'] = continue_visual_basic

    if csbyte_visual_basic is None or isinstance(csbyte_visual_basic, list) and all(x is None for x in csbyte_visual_basic):
        logging.error('csbyte_visual_basic is required.')
        return ['csbyte_visual_basic is required.']
    if csbyte_visual_basic is not None:

        request_parameters['csbyte'] = csbyte_visual_basic

    if cshort_visual_basic is None or isinstance(cshort_visual_basic, list) and all(x is None for x in cshort_visual_basic):
        logging.error('cshort_visual_basic is required.')
        return ['cshort_visual_basic is required.']
    if cshort_visual_basic is not None:

        request_parameters['cshort'] = cshort_visual_basic

    if csng_visual_basic is None or isinstance(csng_visual_basic, list) and all(x is None for x in csng_visual_basic):
        logging.error('csng_visual_basic is required.')
        return ['csng_visual_basic is required.']
    if csng_visual_basic is not None:

        request_parameters['csng'] = csng_visual_basic

    if cstr_visual_basic is None or isinstance(cstr_visual_basic, list) and all(x is None for x in cstr_visual_basic):
        logging.error('cstr_visual_basic is required.')
        return ['cstr_visual_basic is required.']
    if cstr_visual_basic is not None:

        request_parameters['cstr'] = cstr_visual_basic

    if ctype_visual_basic is None or isinstance(ctype_visual_basic, list) and all(x is None for x in ctype_visual_basic):
        logging.error('ctype_visual_basic is required.')
        return ['ctype_visual_basic is required.']
    if ctype_visual_basic is not None:

        request_parameters['ctype'] = ctype_visual_basic

    if cuint_visual_basic is None or isinstance(cuint_visual_basic, list) and all(x is None for x in cuint_visual_basic):
        logging.error('cuint_visual_basic is required.')
        return ['cuint_visual_basic is required.']
    if cuint_visual_basic is not None:

        request_parameters['cuint'] = cuint_visual_basic

    if culng_visual_basic is None or isinstance(culng_visual_basic, list) and all(x is None for x in culng_visual_basic):
        logging.error('culng_visual_basic is required.')
        return ['culng_visual_basic is required.']
    if culng_visual_basic is not None:

        request_parameters['culng'] = culng_visual_basic

    if currency_visual_basic is None or isinstance(currency_visual_basic, list) and all(x is None for x in currency_visual_basic):
        logging.error('currency_visual_basic is required.')
        return ['currency_visual_basic is required.']
    if currency_visual_basic is not None:

        request_parameters['currency'] = currency_visual_basic

    if cushort_visual_basic is None or isinstance(cushort_visual_basic, list) and all(x is None for x in cushort_visual_basic):
        logging.error('cushort_visual_basic is required.')
        return ['cushort_visual_basic is required.']
    if cushort_visual_basic is not None:

        request_parameters['cushort'] = cushort_visual_basic

    if date_visual_basic is None or isinstance(date_visual_basic, list) and all(x is None for x in date_visual_basic):
        logging.error('date_visual_basic is required.')
        return ['date_visual_basic is required.']
    if date_visual_basic is not None:

        request_parameters['date'] = date_visual_basic

    if decimal_visual_basic is None or isinstance(decimal_visual_basic, list) and all(x is None for x in decimal_visual_basic):
        logging.error('decimal_visual_basic is required.')
        return ['decimal_visual_basic is required.']
    if decimal_visual_basic is not None:

        request_parameters['decimal'] = decimal_visual_basic

    if declare_visual_basic is None or isinstance(declare_visual_basic, list) and all(x is None for x in declare_visual_basic):
        logging.error('declare_visual_basic is required.')
        return ['declare_visual_basic is required.']
    if declare_visual_basic is not None:

        request_parameters['declare'] = declare_visual_basic

    if default_visual_basic is None or isinstance(default_visual_basic, list) and all(x is None for x in default_visual_basic):
        logging.error('default_visual_basic is required.')
        return ['default_visual_basic is required.']
    if default_visual_basic is not None:

        request_parameters['default'] = default_visual_basic

    if delegate_visual_basic is None or isinstance(delegate_visual_basic, list) and all(x is None for x in delegate_visual_basic):
        logging.error('delegate_visual_basic is required.')
        return ['delegate_visual_basic is required.']
    if delegate_visual_basic is not None:

        request_parameters['delegate'] = delegate_visual_basic

    if dim_visual_basic is None or isinstance(dim_visual_basic, list) and all(x is None for x in dim_visual_basic):
        logging.error('dim_visual_basic is required.')
        return ['dim_visual_basic is required.']
    if dim_visual_basic is not None:

        request_parameters['dim'] = dim_visual_basic

    if directcast_visual_basic is None or isinstance(directcast_visual_basic, list) and all(x is None for x in directcast_visual_basic):
        logging.error('directcast_visual_basic is required.')
        return ['directcast_visual_basic is required.']
    if directcast_visual_basic is not None:

        request_parameters['directcast'] = directcast_visual_basic

    if do_visual_basic is None or isinstance(do_visual_basic, list) and all(x is None for x in do_visual_basic):
        logging.error('do_visual_basic is required.')
        return ['do_visual_basic is required.']
    if do_visual_basic is not None:

        request_parameters['do'] = do_visual_basic

    if double_visual_basic is None or isinstance(double_visual_basic, list) and all(x is None for x in double_visual_basic):
        logging.error('double_visual_basic is required.')
        return ['double_visual_basic is required.']
    if double_visual_basic is not None:

        request_parameters['double'] = double_visual_basic

    if each_visual_basic is None or isinstance(each_visual_basic, list) and all(x is None for x in each_visual_basic):
        logging.error('each_visual_basic is required.')
        return ['each_visual_basic is required.']
    if each_visual_basic is not None:

        request_parameters['each'] = each_visual_basic

    if else_visual_basic is None or isinstance(else_visual_basic, list) and all(x is None for x in else_visual_basic):
        logging.error('else_visual_basic is required.')
        return ['else_visual_basic is required.']
    if else_visual_basic is not None:

        request_parameters['else'] = else_visual_basic

    if elseif_visual_basic is None or isinstance(elseif_visual_basic, list) and all(x is None for x in elseif_visual_basic):
        logging.error('elseif_visual_basic is required.')
        return ['elseif_visual_basic is required.']
    if elseif_visual_basic is not None:

        request_parameters['elseif'] = elseif_visual_basic

    if end_visual_basic is None or isinstance(end_visual_basic, list) and all(x is None for x in end_visual_basic):
        logging.error('end_visual_basic is required.')
        return ['end_visual_basic is required.']
    if end_visual_basic is not None:

        request_parameters['end'] = end_visual_basic

    if endif_visual_basic is None or isinstance(endif_visual_basic, list) and all(x is None for x in endif_visual_basic):
        logging.error('endif_visual_basic is required.')
        return ['endif_visual_basic is required.']
    if endif_visual_basic is not None:

        request_parameters['endif'] = endif_visual_basic

    if enum_visual_basic is None or isinstance(enum_visual_basic, list) and all(x is None for x in enum_visual_basic):
        logging.error('enum_visual_basic is required.')
        return ['enum_visual_basic is required.']
    if enum_visual_basic is not None:

        request_parameters['enum'] = enum_visual_basic

    if erase_visual_basic is None or isinstance(erase_visual_basic, list) and all(x is None for x in erase_visual_basic):
        logging.error('erase_visual_basic is required.')
        return ['erase_visual_basic is required.']
    if erase_visual_basic is not None:

        request_parameters['erase'] = erase_visual_basic

    if error_visual_basic is None or isinstance(error_visual_basic, list) and all(x is None for x in error_visual_basic):
        logging.error('error_visual_basic is required.')
        return ['error_visual_basic is required.']
    if error_visual_basic is not None:

        request_parameters['error'] = error_visual_basic

    if event_visual_basic is None or isinstance(event_visual_basic, list) and all(x is None for x in event_visual_basic):
        logging.error('event_visual_basic is required.')
        return ['event_visual_basic is required.']
    if event_visual_basic is not None:

        request_parameters['event'] = event_visual_basic

    if exit_visual_basic is None or isinstance(exit_visual_basic, list) and all(x is None for x in exit_visual_basic):
        logging.error('exit_visual_basic is required.')
        return ['exit_visual_basic is required.']
    if exit_visual_basic is not None:

        request_parameters['exit'] = exit_visual_basic

    if finally_visual_basic is None or isinstance(finally_visual_basic, list) and all(x is None for x in finally_visual_basic):
        logging.error('finally_visual_basic is required.')
        return ['finally_visual_basic is required.']
    if finally_visual_basic is not None:

        request_parameters['finally'] = finally_visual_basic

    if for_visual_basic is None or isinstance(for_visual_basic, list) and all(x is None for x in for_visual_basic):
        logging.error('for_visual_basic is required.')
        return ['for_visual_basic is required.']
    if for_visual_basic is not None:

        request_parameters['for'] = for_visual_basic

    if friend_visual_basic is None or isinstance(friend_visual_basic, list) and all(x is None for x in friend_visual_basic):
        logging.error('friend_visual_basic is required.')
        return ['friend_visual_basic is required.']
    if friend_visual_basic is not None:

        request_parameters['friend'] = friend_visual_basic

    if function_visual_basic is None or isinstance(function_visual_basic, list) and all(x is None for x in function_visual_basic):
        logging.error('function_visual_basic is required.')
        return ['function_visual_basic is required.']
    if function_visual_basic is not None:

        request_parameters['function'] = function_visual_basic

    if get_visual_basic is None or isinstance(get_visual_basic, list) and all(x is None for x in get_visual_basic):
        logging.error('get_visual_basic is required.')
        return ['get_visual_basic is required.']
    if get_visual_basic is not None:

        request_parameters['get'] = get_visual_basic

    if gettype_visual_basic is None or isinstance(gettype_visual_basic, list) and all(x is None for x in gettype_visual_basic):
        logging.error('gettype_visual_basic is required.')
        return ['gettype_visual_basic is required.']
    if gettype_visual_basic is not None:

        request_parameters['gettype'] = gettype_visual_basic

    if getxmlnamespace_visual_basic is None or isinstance(getxmlnamespace_visual_basic, list) and all(x is None for x in getxmlnamespace_visual_basic):
        logging.error('getxmlnamespace_visual_basic is required.')
        return ['getxmlnamespace_visual_basic is required.']
    if getxmlnamespace_visual_basic is not None:

        request_parameters['getxmlnamespace'] = getxmlnamespace_visual_basic

    if global_visual_basic is None or isinstance(global_visual_basic, list) and all(x is None for x in global_visual_basic):
        logging.error('global_visual_basic is required.')
        return ['global_visual_basic is required.']
    if global_visual_basic is not None:

        request_parameters['global'] = global_visual_basic

    if gosub_visual_basic is None or isinstance(gosub_visual_basic, list) and all(x is None for x in gosub_visual_basic):
        logging.error('gosub_visual_basic is required.')
        return ['gosub_visual_basic is required.']
    if gosub_visual_basic is not None:

        request_parameters['gosub'] = gosub_visual_basic

    if goto_visual_basic is None or isinstance(goto_visual_basic, list) and all(x is None for x in goto_visual_basic):
        logging.error('goto_visual_basic is required.')
        return ['goto_visual_basic is required.']
    if goto_visual_basic is not None:

        request_parameters['goto'] = goto_visual_basic

    if handles_visual_basic is None or isinstance(handles_visual_basic, list) and all(x is None for x in handles_visual_basic):
        logging.error('handles_visual_basic is required.')
        return ['handles_visual_basic is required.']
    if handles_visual_basic is not None:

        request_parameters['handles'] = handles_visual_basic

    if if_visual_basic is None or isinstance(if_visual_basic, list) and all(x is None for x in if_visual_basic):
        logging.error('if_visual_basic is required.')
        return ['if_visual_basic is required.']
    if if_visual_basic is not None:

        request_parameters['if'] = if_visual_basic

    if implements_visual_basic is None or isinstance(implements_visual_basic, list) and all(x is None for x in implements_visual_basic):
        logging.error('implements_visual_basic is required.')
        return ['implements_visual_basic is required.']
    if implements_visual_basic is not None:

        request_parameters['implements'] = implements_visual_basic

    if imports_visual_basic is None or isinstance(imports_visual_basic, list) and all(x is None for x in imports_visual_basic):
        logging.error('imports_visual_basic is required.')
        return ['imports_visual_basic is required.']
    if imports_visual_basic is not None:

        request_parameters['imports'] = imports_visual_basic

    if in_visual_basic is None or isinstance(in_visual_basic, list) and all(x is None for x in in_visual_basic):
        logging.error('in_visual_basic is required.')
        return ['in_visual_basic is required.']
    if in_visual_basic is not None:

        request_parameters['in'] = in_visual_basic

    if inherits_visual_basic is None or isinstance(inherits_visual_basic, list) and all(x is None for x in inherits_visual_basic):
        logging.error('inherits_visual_basic is required.')
        return ['inherits_visual_basic is required.']
    if inherits_visual_basic is not None:

        request_parameters['inherits'] = inherits_visual_basic

    if integer_visual_basic is None or isinstance(integer_visual_basic, list) and all(x is None for x in integer_visual_basic):
        logging.error('integer_visual_basic is required.')
        return ['integer_visual_basic is required.']
    if integer_visual_basic is not None:

        request_parameters['integer'] = integer_visual_basic

    if interface_visual_basic is None or isinstance(interface_visual_basic, list) and all(x is None for x in interface_visual_basic):
        logging.error('interface_visual_basic is required.')
        return ['interface_visual_basic is required.']
    if interface_visual_basic is not None:

        request_parameters['interface'] = interface_visual_basic

    if is_visual_basic is None or isinstance(is_visual_basic, list) and all(x is None for x in is_visual_basic):
        logging.error('is_visual_basic is required.')
        return ['is_visual_basic is required.']
    if is_visual_basic is not None:

        request_parameters['is'] = is_visual_basic

    if isnot_visual_basic is None or isinstance(isnot_visual_basic, list) and all(x is None for x in isnot_visual_basic):
        logging.error('isnot_visual_basic is required.')
        return ['isnot_visual_basic is required.']
    if isnot_visual_basic is not None:

        request_parameters['isnot'] = isnot_visual_basic

    if let_visual_basic is None or isinstance(let_visual_basic, list) and all(x is None for x in let_visual_basic):
        logging.error('let_visual_basic is required.')
        return ['let_visual_basic is required.']
    if let_visual_basic is not None:

        request_parameters['let'] = let_visual_basic

    if lib_visual_basic is None or isinstance(lib_visual_basic, list) and all(x is None for x in lib_visual_basic):
        logging.error('lib_visual_basic is required.')
        return ['lib_visual_basic is required.']
    if lib_visual_basic is not None:

        request_parameters['lib'] = lib_visual_basic

    if like_visual_basic is None or isinstance(like_visual_basic, list) and all(x is None for x in like_visual_basic):
        logging.error('like_visual_basic is required.')
        return ['like_visual_basic is required.']
    if like_visual_basic is not None:

        request_parameters['like'] = like_visual_basic

    if long_visual_basic is None or isinstance(long_visual_basic, list) and all(x is None for x in long_visual_basic):
        logging.error('long_visual_basic is required.')
        return ['long_visual_basic is required.']
    if long_visual_basic is not None:

        request_parameters['long'] = long_visual_basic

    if loop_visual_basic is None or isinstance(loop_visual_basic, list) and all(x is None for x in loop_visual_basic):
        logging.error('loop_visual_basic is required.')
        return ['loop_visual_basic is required.']
    if loop_visual_basic is not None:

        request_parameters['loop'] = loop_visual_basic

    if me_visual_basic is None or isinstance(me_visual_basic, list) and all(x is None for x in me_visual_basic):
        logging.error('me_visual_basic is required.')
        return ['me_visual_basic is required.']
    if me_visual_basic is not None:

        request_parameters['me'] = me_visual_basic

    if mod_visual_basic is None or isinstance(mod_visual_basic, list) and all(x is None for x in mod_visual_basic):
        logging.error('mod_visual_basic is required.')
        return ['mod_visual_basic is required.']
    if mod_visual_basic is not None:

        request_parameters['mod'] = mod_visual_basic

    if module_visual_basic is None or isinstance(module_visual_basic, list) and all(x is None for x in module_visual_basic):
        logging.error('module_visual_basic is required.')
        return ['module_visual_basic is required.']
    if module_visual_basic is not None:

        request_parameters['module'] = module_visual_basic

    if mustinherit_visual_basic is None or isinstance(mustinherit_visual_basic, list) and all(x is None for x in mustinherit_visual_basic):
        logging.error('mustinherit_visual_basic is required.')
        return ['mustinherit_visual_basic is required.']
    if mustinherit_visual_basic is not None:

        request_parameters['mustinherit'] = mustinherit_visual_basic

    if mustoverride_visual_basic is None or isinstance(mustoverride_visual_basic, list) and all(x is None for x in mustoverride_visual_basic):
        logging.error('mustoverride_visual_basic is required.')
        return ['mustoverride_visual_basic is required.']
    if mustoverride_visual_basic is not None:

        request_parameters['mustoverride'] = mustoverride_visual_basic

    if mybase_visual_basic is None or isinstance(mybase_visual_basic, list) and all(x is None for x in mybase_visual_basic):
        logging.error('mybase_visual_basic is required.')
        return ['mybase_visual_basic is required.']
    if mybase_visual_basic is not None:

        request_parameters['mybase'] = mybase_visual_basic

    if myclass_visual_basic is None or isinstance(myclass_visual_basic, list) and all(x is None for x in myclass_visual_basic):
        logging.error('myclass_visual_basic is required.')
        return ['myclass_visual_basic is required.']
    if myclass_visual_basic is not None:

        request_parameters['myclass'] = myclass_visual_basic

    if namespace_visual_basic is None or isinstance(namespace_visual_basic, list) and all(x is None for x in namespace_visual_basic):
        logging.error('namespace_visual_basic is required.')
        return ['namespace_visual_basic is required.']
    if namespace_visual_basic is not None:

        request_parameters['namespace'] = namespace_visual_basic

    if narrowing_visual_basic is None or isinstance(narrowing_visual_basic, list) and all(x is None for x in narrowing_visual_basic):
        logging.error('narrowing_visual_basic is required.')
        return ['narrowing_visual_basic is required.']
    if narrowing_visual_basic is not None:

        request_parameters['narrowing'] = narrowing_visual_basic

    if new_visual_basic is None or isinstance(new_visual_basic, list) and all(x is None for x in new_visual_basic):
        logging.error('new_visual_basic is required.')
        return ['new_visual_basic is required.']
    if new_visual_basic is not None:

        request_parameters['new'] = new_visual_basic

    if next_visual_basic is None or isinstance(next_visual_basic, list) and all(x is None for x in next_visual_basic):
        logging.error('next_visual_basic is required.')
        return ['next_visual_basic is required.']
    if next_visual_basic is not None:

        request_parameters['next'] = next_visual_basic

    if not_visual_basic is None or isinstance(not_visual_basic, list) and all(x is None for x in not_visual_basic):
        logging.error('not_visual_basic is required.')
        return ['not_visual_basic is required.']
    if not_visual_basic is not None:

        request_parameters['not'] = not_visual_basic

    if nothing_visual_basic is None or isinstance(nothing_visual_basic, list) and all(x is None for x in nothing_visual_basic):
        logging.error('nothing_visual_basic is required.')
        return ['nothing_visual_basic is required.']
    if nothing_visual_basic is not None:

        request_parameters['nothing'] = nothing_visual_basic

    if notinheritable_visual_basic is None or isinstance(notinheritable_visual_basic, list) and all(x is None for x in notinheritable_visual_basic):
        logging.error('notinheritable_visual_basic is required.')
        return ['notinheritable_visual_basic is required.']
    if notinheritable_visual_basic is not None:

        request_parameters['notinheritable'] = notinheritable_visual_basic

    if notoverridable_visual_basic is None or isinstance(notoverridable_visual_basic, list) and all(x is None for x in notoverridable_visual_basic):
        logging.error('notoverridable_visual_basic is required.')
        return ['notoverridable_visual_basic is required.']
    if notoverridable_visual_basic is not None:

        request_parameters['notoverridable'] = notoverridable_visual_basic

    if object_visual_basic is None or isinstance(object_visual_basic, list) and all(x is None for x in object_visual_basic):
        logging.error('object_visual_basic is required.')
        return ['object_visual_basic is required.']
    if object_visual_basic is not None:

        request_parameters['object'] = object_visual_basic

    if of_visual_basic is None or isinstance(of_visual_basic, list) and all(x is None for x in of_visual_basic):
        logging.error('of_visual_basic is required.')
        return ['of_visual_basic is required.']
    if of_visual_basic is not None:

        request_parameters['of'] = of_visual_basic

    if on_visual_basic is None or isinstance(on_visual_basic, list) and all(x is None for x in on_visual_basic):
        logging.error('on_visual_basic is required.')
        return ['on_visual_basic is required.']
    if on_visual_basic is not None:

        request_parameters['on'] = on_visual_basic

    if operator_visual_basic is None or isinstance(operator_visual_basic, list) and all(x is None for x in operator_visual_basic):
        logging.error('operator_visual_basic is required.')
        return ['operator_visual_basic is required.']
    if operator_visual_basic is not None:

        request_parameters['operator'] = operator_visual_basic

    if option_visual_basic is None or isinstance(option_visual_basic, list) and all(x is None for x in option_visual_basic):
        logging.error('option_visual_basic is required.')
        return ['option_visual_basic is required.']
    if option_visual_basic is not None:

        request_parameters['option'] = option_visual_basic

    if optional_visual_basic is None or isinstance(optional_visual_basic, list) and all(x is None for x in optional_visual_basic):
        logging.error('optional_visual_basic is required.')
        return ['optional_visual_basic is required.']
    if optional_visual_basic is not None:

        request_parameters['optional'] = optional_visual_basic

    if or_visual_basic is None or isinstance(or_visual_basic, list) and all(x is None for x in or_visual_basic):
        logging.error('or_visual_basic is required.')
        return ['or_visual_basic is required.']
    if or_visual_basic is not None:

        request_parameters['or'] = or_visual_basic

    if orelse_visual_basic is None or isinstance(orelse_visual_basic, list) and all(x is None for x in orelse_visual_basic):
        logging.error('orelse_visual_basic is required.')
        return ['orelse_visual_basic is required.']
    if orelse_visual_basic is not None:

        request_parameters['orelse'] = orelse_visual_basic

    if overloads_visual_basic is None or isinstance(overloads_visual_basic, list) and all(x is None for x in overloads_visual_basic):
        logging.error('overloads_visual_basic is required.')
        return ['overloads_visual_basic is required.']
    if overloads_visual_basic is not None:

        request_parameters['overloads'] = overloads_visual_basic

    if overridable_visual_basic is None or isinstance(overridable_visual_basic, list) and all(x is None for x in overridable_visual_basic):
        logging.error('overridable_visual_basic is required.')
        return ['overridable_visual_basic is required.']
    if overridable_visual_basic is not None:

        request_parameters['overridable'] = overridable_visual_basic

    if overrides_visual_basic is None or isinstance(overrides_visual_basic, list) and all(x is None for x in overrides_visual_basic):
        logging.error('overrides_visual_basic is required.')
        return ['overrides_visual_basic is required.']
    if overrides_visual_basic is not None:

        request_parameters['overrides'] = overrides_visual_basic

    if paramarray_visual_basic is None or isinstance(paramarray_visual_basic, list) and all(x is None for x in paramarray_visual_basic):
        logging.error('paramarray_visual_basic is required.')
        return ['paramarray_visual_basic is required.']
    if paramarray_visual_basic is not None:

        request_parameters['paramarray'] = paramarray_visual_basic

    if partial_visual_basic is None or isinstance(partial_visual_basic, list) and all(x is None for x in partial_visual_basic):
        logging.error('partial_visual_basic is required.')
        return ['partial_visual_basic is required.']
    if partial_visual_basic is not None:

        request_parameters['partial'] = partial_visual_basic

    if private_visual_basic is None or isinstance(private_visual_basic, list) and all(x is None for x in private_visual_basic):
        logging.error('private_visual_basic is required.')
        return ['private_visual_basic is required.']
    if private_visual_basic is not None:

        request_parameters['private'] = private_visual_basic

    if property_visual_basic is None or isinstance(property_visual_basic, list) and all(x is None for x in property_visual_basic):
        logging.error('property_visual_basic is required.')
        return ['property_visual_basic is required.']
    if property_visual_basic is not None:

        request_parameters['property'] = property_visual_basic

    if protected_visual_basic is None or isinstance(protected_visual_basic, list) and all(x is None for x in protected_visual_basic):
        logging.error('protected_visual_basic is required.')
        return ['protected_visual_basic is required.']
    if protected_visual_basic is not None:

        request_parameters['protected'] = protected_visual_basic

    if public_visual_basic is None or isinstance(public_visual_basic, list) and all(x is None for x in public_visual_basic):
        logging.error('public_visual_basic is required.')
        return ['public_visual_basic is required.']
    if public_visual_basic is not None:

        request_parameters['public'] = public_visual_basic

    if raiseevent_visual_basic is None or isinstance(raiseevent_visual_basic, list) and all(x is None for x in raiseevent_visual_basic):
        logging.error('raiseevent_visual_basic is required.')
        return ['raiseevent_visual_basic is required.']
    if raiseevent_visual_basic is not None:

        request_parameters['raiseevent'] = raiseevent_visual_basic

    if readonly_visual_basic is None or isinstance(readonly_visual_basic, list) and all(x is None for x in readonly_visual_basic):
        logging.error('readonly_visual_basic is required.')
        return ['readonly_visual_basic is required.']
    if readonly_visual_basic is not None:

        request_parameters['readonly'] = readonly_visual_basic

    if redim_visual_basic is None or isinstance(redim_visual_basic, list) and all(x is None for x in redim_visual_basic):
        logging.error('redim_visual_basic is required.')
        return ['redim_visual_basic is required.']
    if redim_visual_basic is not None:

        request_parameters['redim'] = redim_visual_basic

    if rem_visual_basic is None or isinstance(rem_visual_basic, list) and all(x is None for x in rem_visual_basic):
        logging.error('rem_visual_basic is required.')
        return ['rem_visual_basic is required.']
    if rem_visual_basic is not None:

        request_parameters['rem'] = rem_visual_basic

    if removehandler_visual_basic is None or isinstance(removehandler_visual_basic, list) and all(x is None for x in removehandler_visual_basic):
        logging.error('removehandler_visual_basic is required.')
        return ['removehandler_visual_basic is required.']
    if removehandler_visual_basic is not None:

        request_parameters['removehandler'] = removehandler_visual_basic

    if resume_visual_basic is None or isinstance(resume_visual_basic, list) and all(x is None for x in resume_visual_basic):
        logging.error('resume_visual_basic is required.')
        return ['resume_visual_basic is required.']
    if resume_visual_basic is not None:

        request_parameters['resume'] = resume_visual_basic

    if return_visual_basic is None or isinstance(return_visual_basic, list) and all(x is None for x in return_visual_basic):
        logging.error('return_visual_basic is required.')
        return ['return_visual_basic is required.']
    if return_visual_basic is not None:

        request_parameters['return'] = return_visual_basic

    if sbyte_visual_basic is None or isinstance(sbyte_visual_basic, list) and all(x is None for x in sbyte_visual_basic):
        logging.error('sbyte_visual_basic is required.')
        return ['sbyte_visual_basic is required.']
    if sbyte_visual_basic is not None:

        request_parameters['sbyte'] = sbyte_visual_basic

    if select_visual_basic is None or isinstance(select_visual_basic, list) and all(x is None for x in select_visual_basic):
        logging.error('select_visual_basic is required.')
        return ['select_visual_basic is required.']
    if select_visual_basic is not None:

        request_parameters['select'] = select_visual_basic

    if set_visual_basic is None or isinstance(set_visual_basic, list) and all(x is None for x in set_visual_basic):
        logging.error('set_visual_basic is required.')
        return ['set_visual_basic is required.']
    if set_visual_basic is not None:

        request_parameters['set'] = set_visual_basic

    if shadows_visual_basic is None or isinstance(shadows_visual_basic, list) and all(x is None for x in shadows_visual_basic):
        logging.error('shadows_visual_basic is required.')
        return ['shadows_visual_basic is required.']
    if shadows_visual_basic is not None:

        request_parameters['shadows'] = shadows_visual_basic

    if shared_visual_basic is None or isinstance(shared_visual_basic, list) and all(x is None for x in shared_visual_basic):
        logging.error('shared_visual_basic is required.')
        return ['shared_visual_basic is required.']
    if shared_visual_basic is not None:

        request_parameters['shared'] = shared_visual_basic

    if short_visual_basic is None or isinstance(short_visual_basic, list) and all(x is None for x in short_visual_basic):
        logging.error('short_visual_basic is required.')
        return ['short_visual_basic is required.']
    if short_visual_basic is not None:

        request_parameters['short'] = short_visual_basic

    if single_visual_basic is None or isinstance(single_visual_basic, list) and all(x is None for x in single_visual_basic):
        logging.error('single_visual_basic is required.')
        return ['single_visual_basic is required.']
    if single_visual_basic is not None:

        request_parameters['single'] = single_visual_basic

    if static_visual_basic is None or isinstance(static_visual_basic, list) and all(x is None for x in static_visual_basic):
        logging.error('static_visual_basic is required.')
        return ['static_visual_basic is required.']
    if static_visual_basic is not None:

        request_parameters['static'] = static_visual_basic

    if step_visual_basic is None or isinstance(step_visual_basic, list) and all(x is None for x in step_visual_basic):
        logging.error('step_visual_basic is required.')
        return ['step_visual_basic is required.']
    if step_visual_basic is not None:

        request_parameters['step'] = step_visual_basic

    if stop_visual_basic is None or isinstance(stop_visual_basic, list) and all(x is None for x in stop_visual_basic):
        logging.error('stop_visual_basic is required.')
        return ['stop_visual_basic is required.']
    if stop_visual_basic is not None:

        request_parameters['stop'] = stop_visual_basic

    if string_visual_basic is None or isinstance(string_visual_basic, list) and all(x is None for x in string_visual_basic):
        logging.error('string_visual_basic is required.')
        return ['string_visual_basic is required.']
    if string_visual_basic is not None:

        request_parameters['string'] = string_visual_basic

    if structure_visual_basic is None or isinstance(structure_visual_basic, list) and all(x is None for x in structure_visual_basic):
        logging.error('structure_visual_basic is required.')
        return ['structure_visual_basic is required.']
    if structure_visual_basic is not None:

        request_parameters['structure'] = structure_visual_basic

    if sub_visual_basic is None or isinstance(sub_visual_basic, list) and all(x is None for x in sub_visual_basic):
        logging.error('sub_visual_basic is required.')
        return ['sub_visual_basic is required.']
    if sub_visual_basic is not None:

        request_parameters['sub'] = sub_visual_basic

    if synclock_visual_basic is None or isinstance(synclock_visual_basic, list) and all(x is None for x in synclock_visual_basic):
        logging.error('synclock_visual_basic is required.')
        return ['synclock_visual_basic is required.']
    if synclock_visual_basic is not None:

        request_parameters['synclock'] = synclock_visual_basic

    if then_visual_basic is None or isinstance(then_visual_basic, list) and all(x is None for x in then_visual_basic):
        logging.error('then_visual_basic is required.')
        return ['then_visual_basic is required.']
    if then_visual_basic is not None:

        request_parameters['then'] = then_visual_basic

    if throw_visual_basic is None or isinstance(throw_visual_basic, list) and all(x is None for x in throw_visual_basic):
        logging.error('throw_visual_basic is required.')
        return ['throw_visual_basic is required.']
    if throw_visual_basic is not None:

        request_parameters['throw'] = throw_visual_basic

    if to_visual_basic is None or isinstance(to_visual_basic, list) and all(x is None for x in to_visual_basic):
        logging.error('to_visual_basic is required.')
        return ['to_visual_basic is required.']
    if to_visual_basic is not None:

        request_parameters['to'] = to_visual_basic

    if try_visual_basic is None or isinstance(try_visual_basic, list) and all(x is None for x in try_visual_basic):
        logging.error('try_visual_basic is required.')
        return ['try_visual_basic is required.']
    if try_visual_basic is not None:

        request_parameters['try'] = try_visual_basic

    if trycast_visual_basic is None or isinstance(trycast_visual_basic, list) and all(x is None for x in trycast_visual_basic):
        logging.error('trycast_visual_basic is required.')
        return ['trycast_visual_basic is required.']
    if trycast_visual_basic is not None:

        request_parameters['trycast'] = trycast_visual_basic

    if type_visual_basic is None or isinstance(type_visual_basic, list) and all(x is None for x in type_visual_basic):
        logging.error('type_visual_basic is required.')
        return ['type_visual_basic is required.']
    if type_visual_basic is not None:

        request_parameters['type'] = type_visual_basic

    if typeof_visual_basic is None or isinstance(typeof_visual_basic, list) and all(x is None for x in typeof_visual_basic):
        logging.error('typeof_visual_basic is required.')
        return ['typeof_visual_basic is required.']
    if typeof_visual_basic is not None:

        request_parameters['typeof'] = typeof_visual_basic

    if uinteger_visual_basic is None or isinstance(uinteger_visual_basic, list) and all(x is None for x in uinteger_visual_basic):
        logging.error('uinteger_visual_basic is required.')
        return ['uinteger_visual_basic is required.']
    if uinteger_visual_basic is not None:

        request_parameters['uinteger'] = uinteger_visual_basic

    if ulong_visual_basic is None or isinstance(ulong_visual_basic, list) and all(x is None for x in ulong_visual_basic):
        logging.error('ulong_visual_basic is required.')
        return ['ulong_visual_basic is required.']
    if ulong_visual_basic is not None:

        request_parameters['ulong'] = ulong_visual_basic

    if ushort_visual_basic is None or isinstance(ushort_visual_basic, list) and all(x is None for x in ushort_visual_basic):
        logging.error('ushort_visual_basic is required.')
        return ['ushort_visual_basic is required.']
    if ushort_visual_basic is not None:

        request_parameters['ushort'] = ushort_visual_basic

    if using_visual_basic is None or isinstance(using_visual_basic, list) and all(x is None for x in using_visual_basic):
        logging.error('using_visual_basic is required.')
        return ['using_visual_basic is required.']
    if using_visual_basic is not None:

        request_parameters['using'] = using_visual_basic

    if variant_visual_basic is None or isinstance(variant_visual_basic, list) and all(x is None for x in variant_visual_basic):
        logging.error('variant_visual_basic is required.')
        return ['variant_visual_basic is required.']
    if variant_visual_basic is not None:

        request_parameters['variant'] = variant_visual_basic

    if wend_visual_basic is None or isinstance(wend_visual_basic, list) and all(x is None for x in wend_visual_basic):
        logging.error('wend_visual_basic is required.')
        return ['wend_visual_basic is required.']
    if wend_visual_basic is not None:

        request_parameters['wend'] = wend_visual_basic

    if when_visual_basic is None or isinstance(when_visual_basic, list) and all(x is None for x in when_visual_basic):
        logging.error('when_visual_basic is required.')
        return ['when_visual_basic is required.']
    if when_visual_basic is not None:

        request_parameters['when'] = when_visual_basic

    if while_visual_basic is None or isinstance(while_visual_basic, list) and all(x is None for x in while_visual_basic):
        logging.error('while_visual_basic is required.')
        return ['while_visual_basic is required.']
    if while_visual_basic is not None:

        request_parameters['while'] = while_visual_basic

    if widening_visual_basic is None or isinstance(widening_visual_basic, list) and all(x is None for x in widening_visual_basic):
        logging.error('widening_visual_basic is required.')
        return ['widening_visual_basic is required.']
    if widening_visual_basic is not None:

        request_parameters['widening'] = widening_visual_basic

    if with_visual_basic is None or isinstance(with_visual_basic, list) and all(x is None for x in with_visual_basic):
        logging.error('with_visual_basic is required.')
        return ['with_visual_basic is required.']
    if with_visual_basic is not None:

        request_parameters['with'] = with_visual_basic

    if withevents_visual_basic is None or isinstance(withevents_visual_basic, list) and all(x is None for x in withevents_visual_basic):
        logging.error('withevents_visual_basic is required.')
        return ['withevents_visual_basic is required.']
    if withevents_visual_basic is not None:

        request_parameters['withevents'] = withevents_visual_basic

    if writeonly_visual_basic is None or isinstance(writeonly_visual_basic, list) and all(x is None for x in writeonly_visual_basic):
        logging.error('writeonly_visual_basic is required.')
        return ['writeonly_visual_basic is required.']
    if writeonly_visual_basic is not None:

        request_parameters['writeonly'] = writeonly_visual_basic

    if xor_visual_basic is None or isinstance(xor_visual_basic, list) and all(x is None for x in xor_visual_basic):
        logging.error('xor_visual_basic is required.')
        return ['xor_visual_basic is required.']
    if xor_visual_basic is not None:

        request_parameters['xor'] = xor_visual_basic


    response = None
    try:
        response = requests.get('http://localhost:8949/test/vba/restricted/keywords'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for vba_keywords_test_get_test_vba_restricted_keywords ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('$ref', '#/definitions/VBAKeywords')]))]))])
            all_definitions = OrderedDict([('VBAKeywords', OrderedDict([('properties', OrderedDict([('addhandler', OrderedDict()), ('addressof', OrderedDict()), ('alias', OrderedDict()), ('and', OrderedDict()), ('andalso', OrderedDict()), ('as', OrderedDict()), ('boolean', OrderedDict()), ('byref', OrderedDict()), ('byte', OrderedDict()), ('byval', OrderedDict()), ('call', OrderedDict()), ('case', OrderedDict()), ('catch', OrderedDict()), ('cbool', OrderedDict()), ('cbyte', OrderedDict()), ('cchar', OrderedDict()), ('cdate', OrderedDict()), ('cdbl', OrderedDict()), ('cdec', OrderedDict()), ('char', OrderedDict()), ('cint', OrderedDict()), ('class', OrderedDict()), ('clng', OrderedDict()), ('cobj', OrderedDict()), ('const', OrderedDict()), ('continue', OrderedDict()), ('csbyte', OrderedDict()), ('cshort', OrderedDict()), ('csng', OrderedDict()), ('cstr', OrderedDict()), ('ctype', OrderedDict()), ('cuint', OrderedDict()), ('culng', OrderedDict()), ('currency', OrderedDict()), ('cushort', OrderedDict()), ('date', OrderedDict()), ('decimal', OrderedDict()), ('declare', OrderedDict()), ('default', OrderedDict()), ('delegate', OrderedDict()), ('dim', OrderedDict()), ('directcast', OrderedDict()), ('do', OrderedDict()), ('double', OrderedDict()), ('each', OrderedDict()), ('else', OrderedDict()), ('elseif', OrderedDict()), ('end', OrderedDict()), ('endif', OrderedDict()), ('enum', OrderedDict()), ('erase', OrderedDict()), ('error', OrderedDict()), ('event', OrderedDict()), ('exit', OrderedDict()), ('finally', OrderedDict()), ('for', OrderedDict()), ('friend', OrderedDict()), ('function', OrderedDict()), ('get', OrderedDict()), ('gettype', OrderedDict()), ('getxmlnamespace', OrderedDict()), ('global', OrderedDict()), ('gosub', OrderedDict()), ('goto', OrderedDict()), ('handles', OrderedDict()), ('if', OrderedDict()), ('implements', OrderedDict()), ('imports', OrderedDict()), ('in', OrderedDict()), ('inherits', OrderedDict()), ('integer', OrderedDict()), ('interface', OrderedDict()), ('is', OrderedDict()), ('isnot', OrderedDict()), ('let', OrderedDict()), ('lib', OrderedDict()), ('like', OrderedDict()), ('long', OrderedDict()), ('loop', OrderedDict()), ('me', OrderedDict()), ('mod', OrderedDict()), ('module', OrderedDict()), ('mustinherit', OrderedDict()), ('mustoverride', OrderedDict()), ('mybase', OrderedDict()), ('myclass', OrderedDict()), ('namespace', OrderedDict()), ('narrowing', OrderedDict()), ('new', OrderedDict()), ('next', OrderedDict()), ('not', OrderedDict()), ('nothing', OrderedDict()), ('notinheritable', OrderedDict()), ('notoverridable', OrderedDict()), ('object', OrderedDict()), ('of', OrderedDict()), ('on', OrderedDict()), ('operator', OrderedDict()), ('option', OrderedDict()), ('optional', OrderedDict()), ('or', OrderedDict()), ('orelse', OrderedDict()), ('overloads', OrderedDict()), ('overridable', OrderedDict()), ('overrides', OrderedDict()), ('paramarray', OrderedDict()), ('partial', OrderedDict()), ('private', OrderedDict()), ('property', OrderedDict()), ('protected', OrderedDict()), ('public', OrderedDict()), ('raiseevent', OrderedDict()), ('readonly', OrderedDict()), ('redim', OrderedDict()), ('rem', OrderedDict()), ('removehandler', OrderedDict()), ('resume', OrderedDict()), ('return', OrderedDict()), ('sbyte', OrderedDict()), ('select', OrderedDict()), ('set', OrderedDict()), ('shadows', OrderedDict()), ('shared', OrderedDict()), ('short', OrderedDict()), ('single', OrderedDict()), ('static', OrderedDict()), ('step', OrderedDict()), ('stop', OrderedDict()), ('string', OrderedDict()), ('structure', OrderedDict()), ('sub', OrderedDict()), ('synclock', OrderedDict()), ('then', OrderedDict()), ('throw', OrderedDict()), ('to', OrderedDict()), ('try', OrderedDict()), ('trycast', OrderedDict()), ('type', OrderedDict()), ('typeof', OrderedDict()), ('uinteger', OrderedDict()), ('ulong', OrderedDict()), ('ushort', OrderedDict()), ('using', OrderedDict()), ('variant', OrderedDict()), ('wend', OrderedDict()), ('when', OrderedDict()), ('while', OrderedDict()), ('widening', OrderedDict()), ('with', OrderedDict()), ('withevents', OrderedDict()), ('writeonly', OrderedDict()), ('xor', OrderedDict())]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling vba_keywords_test_get_test_vba_restricted_keywords.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling vba_keywords_test_get_test_vba_restricted_keywords response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling vba_keywords_test_get_test_vba_restricted_keywords.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='vba_keywords_test', call_in_wizard=False)
@xw.arg('addhandler_visual_basic', doc='')
@xw.arg('addressof_visual_basic', doc='')
@xw.arg('alias_visual_basic', doc='')
@xw.arg('and_visual_basic', doc='')
@xw.arg('andalso_visual_basic', doc='')
@xw.arg('as_visual_basic', doc='')
@xw.arg('boolean_visual_basic', doc='')
@xw.arg('byref_visual_basic', doc='')
@xw.arg('byte_visual_basic', doc='')
@xw.arg('byval_visual_basic', doc='')
@xw.arg('call_visual_basic', doc='')
@xw.arg('case_visual_basic', doc='')
@xw.arg('catch_visual_basic', doc='')
@xw.arg('cbool_visual_basic', doc='')
@xw.arg('cbyte_visual_basic', doc='')
@xw.arg('cchar_visual_basic', doc='')
@xw.arg('cdate_visual_basic', doc='')
@xw.arg('cdbl_visual_basic', doc='')
@xw.arg('cdec_visual_basic', doc='')
@xw.arg('char_visual_basic', doc='')
@xw.arg('cint_visual_basic', doc='')
@xw.arg('class_visual_basic', doc='')
@xw.arg('clng_visual_basic', doc='')
@xw.arg('cobj_visual_basic', doc='')
@xw.arg('const_visual_basic', doc='')
@xw.arg('continue_visual_basic', doc='')
@xw.arg('csbyte_visual_basic', doc='')
@xw.arg('cshort_visual_basic', doc='')
@xw.arg('csng_visual_basic', doc='')
@xw.arg('cstr_visual_basic', doc='')
@xw.arg('ctype_visual_basic', doc='')
@xw.arg('cuint_visual_basic', doc='')
@xw.arg('culng_visual_basic', doc='')
@xw.arg('currency_visual_basic', doc='')
@xw.arg('cushort_visual_basic', doc='')
@xw.arg('date_visual_basic', doc='')
@xw.arg('decimal_visual_basic', doc='')
@xw.arg('declare_visual_basic', doc='')
@xw.arg('default_visual_basic', doc='')
@xw.arg('delegate_visual_basic', doc='')
@xw.arg('dim_visual_basic', doc='')
@xw.arg('directcast_visual_basic', doc='')
@xw.arg('do_visual_basic', doc='')
@xw.arg('double_visual_basic', doc='')
@xw.arg('each_visual_basic', doc='')
@xw.arg('else_visual_basic', doc='')
@xw.arg('elseif_visual_basic', doc='')
@xw.arg('end_visual_basic', doc='')
@xw.arg('endif_visual_basic', doc='')
@xw.arg('enum_visual_basic', doc='')
@xw.arg('erase_visual_basic', doc='')
@xw.arg('error_visual_basic', doc='')
@xw.arg('event_visual_basic', doc='')
@xw.arg('exit_visual_basic', doc='')
@xw.arg('finally_visual_basic', doc='')
@xw.arg('for_visual_basic', doc='')
@xw.arg('friend_visual_basic', doc='')
@xw.arg('function_visual_basic', doc='')
@xw.arg('get_visual_basic', doc='')
@xw.arg('gettype_visual_basic', doc='')
@xw.arg('getxmlnamespace_visual_basic', doc='')
@xw.arg('global_visual_basic', doc='')
@xw.arg('gosub_visual_basic', doc='')
@xw.arg('goto_visual_basic', doc='')
@xw.arg('handles_visual_basic', doc='')
@xw.arg('if_visual_basic', doc='')
@xw.arg('implements_visual_basic', doc='')
@xw.arg('imports_visual_basic', doc='')
@xw.arg('in_visual_basic', doc='')
@xw.arg('inherits_visual_basic', doc='')
@xw.arg('integer_visual_basic', doc='')
@xw.arg('interface_visual_basic', doc='')
@xw.arg('is_visual_basic', doc='')
@xw.arg('isnot_visual_basic', doc='')
@xw.arg('let_visual_basic', doc='')
@xw.arg('lib_visual_basic', doc='')
@xw.arg('like_visual_basic', doc='')
@xw.arg('long_visual_basic', doc='')
@xw.arg('loop_visual_basic', doc='')
@xw.arg('me_visual_basic', doc='')
@xw.arg('mod_visual_basic', doc='')
@xw.arg('module_visual_basic', doc='')
@xw.arg('mustinherit_visual_basic', doc='')
@xw.arg('mustoverride_visual_basic', doc='')
@xw.arg('mybase_visual_basic', doc='')
@xw.arg('myclass_visual_basic', doc='')
@xw.arg('namespace_visual_basic', doc='')
@xw.arg('narrowing_visual_basic', doc='')
@xw.arg('new_visual_basic', doc='')
@xw.arg('next_visual_basic', doc='')
@xw.arg('not_visual_basic', doc='')
@xw.arg('nothing_visual_basic', doc='')
@xw.arg('notinheritable_visual_basic', doc='')
@xw.arg('notoverridable_visual_basic', doc='')
@xw.arg('object_visual_basic', doc='')
@xw.arg('of_visual_basic', doc='')
@xw.arg('on_visual_basic', doc='')
@xw.arg('operator_visual_basic', doc='')
@xw.arg('option_visual_basic', doc='')
@xw.arg('optional_visual_basic', doc='')
@xw.arg('or_visual_basic', doc='')
@xw.arg('orelse_visual_basic', doc='')
@xw.arg('overloads_visual_basic', doc='')
@xw.arg('overridable_visual_basic', doc='')
@xw.arg('overrides_visual_basic', doc='')
@xw.arg('paramarray_visual_basic', doc='')
@xw.arg('partial_visual_basic', doc='')
@xw.arg('private_visual_basic', doc='')
@xw.arg('property_visual_basic', doc='')
@xw.arg('protected_visual_basic', doc='')
@xw.arg('public_visual_basic', doc='')
@xw.arg('raiseevent_visual_basic', doc='')
@xw.arg('readonly_visual_basic', doc='')
@xw.arg('redim_visual_basic', doc='')
@xw.arg('rem_visual_basic', doc='')
@xw.arg('removehandler_visual_basic', doc='')
@xw.arg('resume_visual_basic', doc='')
@xw.arg('return_visual_basic', doc='')
@xw.arg('sbyte_visual_basic', doc='')
@xw.arg('select_visual_basic', doc='')
@xw.arg('set_visual_basic', doc='')
@xw.arg('shadows_visual_basic', doc='')
@xw.arg('shared_visual_basic', doc='')
@xw.arg('short_visual_basic', doc='')
@xw.arg('single_visual_basic', doc='')
@xw.arg('static_visual_basic', doc='')
@xw.arg('step_visual_basic', doc='')
@xw.arg('stop_visual_basic', doc='')
@xw.arg('string_visual_basic', doc='')
@xw.arg('structure_visual_basic', doc='')
@xw.arg('sub_visual_basic', doc='')
@xw.arg('synclock_visual_basic', doc='')
@xw.arg('then_visual_basic', doc='')
@xw.arg('throw_visual_basic', doc='')
@xw.arg('to_visual_basic', doc='')
@xw.arg('try_visual_basic', doc='')
@xw.arg('trycast_visual_basic', doc='')
@xw.arg('type_visual_basic', doc='')
@xw.arg('typeof_visual_basic', doc='')
@xw.arg('uinteger_visual_basic', doc='')
@xw.arg('ulong_visual_basic', doc='')
@xw.arg('ushort_visual_basic', doc='')
@xw.arg('using_visual_basic', doc='')
@xw.arg('variant_visual_basic', doc='')
@xw.arg('wend_visual_basic', doc='')
@xw.arg('when_visual_basic', doc='')
@xw.arg('while_visual_basic', doc='')
@xw.arg('widening_visual_basic', doc='')
@xw.arg('with_visual_basic', doc='')
@xw.arg('withevents_visual_basic', doc='')
@xw.arg('writeonly_visual_basic', doc='')
@xw.arg('xor_visual_basic', doc='')
@xw.ret(expand='table')
def vba_keywords_test_post_test_vba_restricted_keywords(addhandler_visual_basic, addressof_visual_basic, alias_visual_basic, and_visual_basic, andalso_visual_basic, as_visual_basic, boolean_visual_basic, byref_visual_basic, byte_visual_basic, byval_visual_basic, call_visual_basic, case_visual_basic, catch_visual_basic, cbool_visual_basic, cbyte_visual_basic, cchar_visual_basic, cdate_visual_basic, cdbl_visual_basic, cdec_visual_basic, char_visual_basic, cint_visual_basic, class_visual_basic, clng_visual_basic, cobj_visual_basic, const_visual_basic, continue_visual_basic, csbyte_visual_basic, cshort_visual_basic, csng_visual_basic, cstr_visual_basic, ctype_visual_basic, cuint_visual_basic, culng_visual_basic, currency_visual_basic, cushort_visual_basic, date_visual_basic, decimal_visual_basic, declare_visual_basic, default_visual_basic, delegate_visual_basic, dim_visual_basic, directcast_visual_basic, do_visual_basic, double_visual_basic, each_visual_basic, else_visual_basic, elseif_visual_basic, end_visual_basic, endif_visual_basic, enum_visual_basic, erase_visual_basic, error_visual_basic, event_visual_basic, exit_visual_basic, finally_visual_basic, for_visual_basic, friend_visual_basic, function_visual_basic, get_visual_basic, gettype_visual_basic, getxmlnamespace_visual_basic, global_visual_basic, gosub_visual_basic, goto_visual_basic, handles_visual_basic, if_visual_basic, implements_visual_basic, imports_visual_basic, in_visual_basic, inherits_visual_basic, integer_visual_basic, interface_visual_basic, is_visual_basic, isnot_visual_basic, let_visual_basic, lib_visual_basic, like_visual_basic, long_visual_basic, loop_visual_basic, me_visual_basic, mod_visual_basic, module_visual_basic, mustinherit_visual_basic, mustoverride_visual_basic, mybase_visual_basic, myclass_visual_basic, namespace_visual_basic, narrowing_visual_basic, new_visual_basic, next_visual_basic, not_visual_basic, nothing_visual_basic, notinheritable_visual_basic, notoverridable_visual_basic, object_visual_basic, of_visual_basic, on_visual_basic, operator_visual_basic, option_visual_basic, optional_visual_basic, or_visual_basic, orelse_visual_basic, overloads_visual_basic, overridable_visual_basic, overrides_visual_basic, paramarray_visual_basic, partial_visual_basic, private_visual_basic, property_visual_basic, protected_visual_basic, public_visual_basic, raiseevent_visual_basic, readonly_visual_basic, redim_visual_basic, rem_visual_basic, removehandler_visual_basic, resume_visual_basic, return_visual_basic, sbyte_visual_basic, select_visual_basic, set_visual_basic, shadows_visual_basic, shared_visual_basic, short_visual_basic, single_visual_basic, static_visual_basic, step_visual_basic, stop_visual_basic, string_visual_basic, structure_visual_basic, sub_visual_basic, synclock_visual_basic, then_visual_basic, throw_visual_basic, to_visual_basic, try_visual_basic, trycast_visual_basic, type_visual_basic, typeof_visual_basic, uinteger_visual_basic, ulong_visual_basic, ushort_visual_basic, using_visual_basic, variant_visual_basic, wend_visual_basic, when_visual_basic, while_visual_basic, widening_visual_basic, with_visual_basic, withevents_visual_basic, writeonly_visual_basic, xor_visual_basic):
    logging.info("Calling vba_keywords_test_post_test_vba_restricted_keywords...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if addhandler_visual_basic is None or isinstance(addhandler_visual_basic, list) and all(x is None for x in addhandler_visual_basic):
        logging.error('addhandler_visual_basic is required.')
        return ['addhandler_visual_basic is required.']
    if addhandler_visual_basic is not None:

        request_parameters['addhandler'] = addhandler_visual_basic

    if addressof_visual_basic is None or isinstance(addressof_visual_basic, list) and all(x is None for x in addressof_visual_basic):
        logging.error('addressof_visual_basic is required.')
        return ['addressof_visual_basic is required.']
    if addressof_visual_basic is not None:

        request_parameters['addressof'] = addressof_visual_basic

    if alias_visual_basic is None or isinstance(alias_visual_basic, list) and all(x is None for x in alias_visual_basic):
        logging.error('alias_visual_basic is required.')
        return ['alias_visual_basic is required.']
    if alias_visual_basic is not None:

        request_parameters['alias'] = alias_visual_basic

    if and_visual_basic is None or isinstance(and_visual_basic, list) and all(x is None for x in and_visual_basic):
        logging.error('and_visual_basic is required.')
        return ['and_visual_basic is required.']
    if and_visual_basic is not None:

        request_parameters['and'] = and_visual_basic

    if andalso_visual_basic is None or isinstance(andalso_visual_basic, list) and all(x is None for x in andalso_visual_basic):
        logging.error('andalso_visual_basic is required.')
        return ['andalso_visual_basic is required.']
    if andalso_visual_basic is not None:

        request_parameters['andalso'] = andalso_visual_basic

    if as_visual_basic is None or isinstance(as_visual_basic, list) and all(x is None for x in as_visual_basic):
        logging.error('as_visual_basic is required.')
        return ['as_visual_basic is required.']
    if as_visual_basic is not None:

        request_parameters['as'] = as_visual_basic

    if boolean_visual_basic is None or isinstance(boolean_visual_basic, list) and all(x is None for x in boolean_visual_basic):
        logging.error('boolean_visual_basic is required.')
        return ['boolean_visual_basic is required.']
    if boolean_visual_basic is not None:

        request_parameters['boolean'] = boolean_visual_basic

    if byref_visual_basic is None or isinstance(byref_visual_basic, list) and all(x is None for x in byref_visual_basic):
        logging.error('byref_visual_basic is required.')
        return ['byref_visual_basic is required.']
    if byref_visual_basic is not None:

        request_parameters['byref'] = byref_visual_basic

    if byte_visual_basic is None or isinstance(byte_visual_basic, list) and all(x is None for x in byte_visual_basic):
        logging.error('byte_visual_basic is required.')
        return ['byte_visual_basic is required.']
    if byte_visual_basic is not None:

        request_parameters['byte'] = byte_visual_basic

    if byval_visual_basic is None or isinstance(byval_visual_basic, list) and all(x is None for x in byval_visual_basic):
        logging.error('byval_visual_basic is required.')
        return ['byval_visual_basic is required.']
    if byval_visual_basic is not None:

        request_parameters['byval'] = byval_visual_basic

    if call_visual_basic is None or isinstance(call_visual_basic, list) and all(x is None for x in call_visual_basic):
        logging.error('call_visual_basic is required.')
        return ['call_visual_basic is required.']
    if call_visual_basic is not None:

        request_parameters['call'] = call_visual_basic

    if case_visual_basic is None or isinstance(case_visual_basic, list) and all(x is None for x in case_visual_basic):
        logging.error('case_visual_basic is required.')
        return ['case_visual_basic is required.']
    if case_visual_basic is not None:

        request_parameters['case'] = case_visual_basic

    if catch_visual_basic is None or isinstance(catch_visual_basic, list) and all(x is None for x in catch_visual_basic):
        logging.error('catch_visual_basic is required.')
        return ['catch_visual_basic is required.']
    if catch_visual_basic is not None:

        request_parameters['catch'] = catch_visual_basic

    if cbool_visual_basic is None or isinstance(cbool_visual_basic, list) and all(x is None for x in cbool_visual_basic):
        logging.error('cbool_visual_basic is required.')
        return ['cbool_visual_basic is required.']
    if cbool_visual_basic is not None:

        request_parameters['cbool'] = cbool_visual_basic

    if cbyte_visual_basic is None or isinstance(cbyte_visual_basic, list) and all(x is None for x in cbyte_visual_basic):
        logging.error('cbyte_visual_basic is required.')
        return ['cbyte_visual_basic is required.']
    if cbyte_visual_basic is not None:

        request_parameters['cbyte'] = cbyte_visual_basic

    if cchar_visual_basic is None or isinstance(cchar_visual_basic, list) and all(x is None for x in cchar_visual_basic):
        logging.error('cchar_visual_basic is required.')
        return ['cchar_visual_basic is required.']
    if cchar_visual_basic is not None:

        request_parameters['cchar'] = cchar_visual_basic

    if cdate_visual_basic is None or isinstance(cdate_visual_basic, list) and all(x is None for x in cdate_visual_basic):
        logging.error('cdate_visual_basic is required.')
        return ['cdate_visual_basic is required.']
    if cdate_visual_basic is not None:

        request_parameters['cdate'] = cdate_visual_basic

    if cdbl_visual_basic is None or isinstance(cdbl_visual_basic, list) and all(x is None for x in cdbl_visual_basic):
        logging.error('cdbl_visual_basic is required.')
        return ['cdbl_visual_basic is required.']
    if cdbl_visual_basic is not None:

        request_parameters['cdbl'] = cdbl_visual_basic

    if cdec_visual_basic is None or isinstance(cdec_visual_basic, list) and all(x is None for x in cdec_visual_basic):
        logging.error('cdec_visual_basic is required.')
        return ['cdec_visual_basic is required.']
    if cdec_visual_basic is not None:

        request_parameters['cdec'] = cdec_visual_basic

    if char_visual_basic is None or isinstance(char_visual_basic, list) and all(x is None for x in char_visual_basic):
        logging.error('char_visual_basic is required.')
        return ['char_visual_basic is required.']
    if char_visual_basic is not None:

        request_parameters['char'] = char_visual_basic

    if cint_visual_basic is None or isinstance(cint_visual_basic, list) and all(x is None for x in cint_visual_basic):
        logging.error('cint_visual_basic is required.')
        return ['cint_visual_basic is required.']
    if cint_visual_basic is not None:

        request_parameters['cint'] = cint_visual_basic

    if class_visual_basic is None or isinstance(class_visual_basic, list) and all(x is None for x in class_visual_basic):
        logging.error('class_visual_basic is required.')
        return ['class_visual_basic is required.']
    if class_visual_basic is not None:

        request_parameters['class'] = class_visual_basic

    if clng_visual_basic is None or isinstance(clng_visual_basic, list) and all(x is None for x in clng_visual_basic):
        logging.error('clng_visual_basic is required.')
        return ['clng_visual_basic is required.']
    if clng_visual_basic is not None:

        request_parameters['clng'] = clng_visual_basic

    if cobj_visual_basic is None or isinstance(cobj_visual_basic, list) and all(x is None for x in cobj_visual_basic):
        logging.error('cobj_visual_basic is required.')
        return ['cobj_visual_basic is required.']
    if cobj_visual_basic is not None:

        request_parameters['cobj'] = cobj_visual_basic

    if const_visual_basic is None or isinstance(const_visual_basic, list) and all(x is None for x in const_visual_basic):
        logging.error('const_visual_basic is required.')
        return ['const_visual_basic is required.']
    if const_visual_basic is not None:

        request_parameters['const'] = const_visual_basic

    if continue_visual_basic is None or isinstance(continue_visual_basic, list) and all(x is None for x in continue_visual_basic):
        logging.error('continue_visual_basic is required.')
        return ['continue_visual_basic is required.']
    if continue_visual_basic is not None:

        request_parameters['continue'] = continue_visual_basic

    if csbyte_visual_basic is None or isinstance(csbyte_visual_basic, list) and all(x is None for x in csbyte_visual_basic):
        logging.error('csbyte_visual_basic is required.')
        return ['csbyte_visual_basic is required.']
    if csbyte_visual_basic is not None:

        request_parameters['csbyte'] = csbyte_visual_basic

    if cshort_visual_basic is None or isinstance(cshort_visual_basic, list) and all(x is None for x in cshort_visual_basic):
        logging.error('cshort_visual_basic is required.')
        return ['cshort_visual_basic is required.']
    if cshort_visual_basic is not None:

        request_parameters['cshort'] = cshort_visual_basic

    if csng_visual_basic is None or isinstance(csng_visual_basic, list) and all(x is None for x in csng_visual_basic):
        logging.error('csng_visual_basic is required.')
        return ['csng_visual_basic is required.']
    if csng_visual_basic is not None:

        request_parameters['csng'] = csng_visual_basic

    if cstr_visual_basic is None or isinstance(cstr_visual_basic, list) and all(x is None for x in cstr_visual_basic):
        logging.error('cstr_visual_basic is required.')
        return ['cstr_visual_basic is required.']
    if cstr_visual_basic is not None:

        request_parameters['cstr'] = cstr_visual_basic

    if ctype_visual_basic is None or isinstance(ctype_visual_basic, list) and all(x is None for x in ctype_visual_basic):
        logging.error('ctype_visual_basic is required.')
        return ['ctype_visual_basic is required.']
    if ctype_visual_basic is not None:

        request_parameters['ctype'] = ctype_visual_basic

    if cuint_visual_basic is None or isinstance(cuint_visual_basic, list) and all(x is None for x in cuint_visual_basic):
        logging.error('cuint_visual_basic is required.')
        return ['cuint_visual_basic is required.']
    if cuint_visual_basic is not None:

        request_parameters['cuint'] = cuint_visual_basic

    if culng_visual_basic is None or isinstance(culng_visual_basic, list) and all(x is None for x in culng_visual_basic):
        logging.error('culng_visual_basic is required.')
        return ['culng_visual_basic is required.']
    if culng_visual_basic is not None:

        request_parameters['culng'] = culng_visual_basic

    if currency_visual_basic is None or isinstance(currency_visual_basic, list) and all(x is None for x in currency_visual_basic):
        logging.error('currency_visual_basic is required.')
        return ['currency_visual_basic is required.']
    if currency_visual_basic is not None:

        request_parameters['currency'] = currency_visual_basic

    if cushort_visual_basic is None or isinstance(cushort_visual_basic, list) and all(x is None for x in cushort_visual_basic):
        logging.error('cushort_visual_basic is required.')
        return ['cushort_visual_basic is required.']
    if cushort_visual_basic is not None:

        request_parameters['cushort'] = cushort_visual_basic

    if date_visual_basic is None or isinstance(date_visual_basic, list) and all(x is None for x in date_visual_basic):
        logging.error('date_visual_basic is required.')
        return ['date_visual_basic is required.']
    if date_visual_basic is not None:

        request_parameters['date'] = date_visual_basic

    if decimal_visual_basic is None or isinstance(decimal_visual_basic, list) and all(x is None for x in decimal_visual_basic):
        logging.error('decimal_visual_basic is required.')
        return ['decimal_visual_basic is required.']
    if decimal_visual_basic is not None:

        request_parameters['decimal'] = decimal_visual_basic

    if declare_visual_basic is None or isinstance(declare_visual_basic, list) and all(x is None for x in declare_visual_basic):
        logging.error('declare_visual_basic is required.')
        return ['declare_visual_basic is required.']
    if declare_visual_basic is not None:

        request_parameters['declare'] = declare_visual_basic

    if default_visual_basic is None or isinstance(default_visual_basic, list) and all(x is None for x in default_visual_basic):
        logging.error('default_visual_basic is required.')
        return ['default_visual_basic is required.']
    if default_visual_basic is not None:

        request_parameters['default'] = default_visual_basic

    if delegate_visual_basic is None or isinstance(delegate_visual_basic, list) and all(x is None for x in delegate_visual_basic):
        logging.error('delegate_visual_basic is required.')
        return ['delegate_visual_basic is required.']
    if delegate_visual_basic is not None:

        request_parameters['delegate'] = delegate_visual_basic

    if dim_visual_basic is None or isinstance(dim_visual_basic, list) and all(x is None for x in dim_visual_basic):
        logging.error('dim_visual_basic is required.')
        return ['dim_visual_basic is required.']
    if dim_visual_basic is not None:

        request_parameters['dim'] = dim_visual_basic

    if directcast_visual_basic is None or isinstance(directcast_visual_basic, list) and all(x is None for x in directcast_visual_basic):
        logging.error('directcast_visual_basic is required.')
        return ['directcast_visual_basic is required.']
    if directcast_visual_basic is not None:

        request_parameters['directcast'] = directcast_visual_basic

    if do_visual_basic is None or isinstance(do_visual_basic, list) and all(x is None for x in do_visual_basic):
        logging.error('do_visual_basic is required.')
        return ['do_visual_basic is required.']
    if do_visual_basic is not None:

        request_parameters['do'] = do_visual_basic

    if double_visual_basic is None or isinstance(double_visual_basic, list) and all(x is None for x in double_visual_basic):
        logging.error('double_visual_basic is required.')
        return ['double_visual_basic is required.']
    if double_visual_basic is not None:

        request_parameters['double'] = double_visual_basic

    if each_visual_basic is None or isinstance(each_visual_basic, list) and all(x is None for x in each_visual_basic):
        logging.error('each_visual_basic is required.')
        return ['each_visual_basic is required.']
    if each_visual_basic is not None:

        request_parameters['each'] = each_visual_basic

    if else_visual_basic is None or isinstance(else_visual_basic, list) and all(x is None for x in else_visual_basic):
        logging.error('else_visual_basic is required.')
        return ['else_visual_basic is required.']
    if else_visual_basic is not None:

        request_parameters['else'] = else_visual_basic

    if elseif_visual_basic is None or isinstance(elseif_visual_basic, list) and all(x is None for x in elseif_visual_basic):
        logging.error('elseif_visual_basic is required.')
        return ['elseif_visual_basic is required.']
    if elseif_visual_basic is not None:

        request_parameters['elseif'] = elseif_visual_basic

    if end_visual_basic is None or isinstance(end_visual_basic, list) and all(x is None for x in end_visual_basic):
        logging.error('end_visual_basic is required.')
        return ['end_visual_basic is required.']
    if end_visual_basic is not None:

        request_parameters['end'] = end_visual_basic

    if endif_visual_basic is None or isinstance(endif_visual_basic, list) and all(x is None for x in endif_visual_basic):
        logging.error('endif_visual_basic is required.')
        return ['endif_visual_basic is required.']
    if endif_visual_basic is not None:

        request_parameters['endif'] = endif_visual_basic

    if enum_visual_basic is None or isinstance(enum_visual_basic, list) and all(x is None for x in enum_visual_basic):
        logging.error('enum_visual_basic is required.')
        return ['enum_visual_basic is required.']
    if enum_visual_basic is not None:

        request_parameters['enum'] = enum_visual_basic

    if erase_visual_basic is None or isinstance(erase_visual_basic, list) and all(x is None for x in erase_visual_basic):
        logging.error('erase_visual_basic is required.')
        return ['erase_visual_basic is required.']
    if erase_visual_basic is not None:

        request_parameters['erase'] = erase_visual_basic

    if error_visual_basic is None or isinstance(error_visual_basic, list) and all(x is None for x in error_visual_basic):
        logging.error('error_visual_basic is required.')
        return ['error_visual_basic is required.']
    if error_visual_basic is not None:

        request_parameters['error'] = error_visual_basic

    if event_visual_basic is None or isinstance(event_visual_basic, list) and all(x is None for x in event_visual_basic):
        logging.error('event_visual_basic is required.')
        return ['event_visual_basic is required.']
    if event_visual_basic is not None:

        request_parameters['event'] = event_visual_basic

    if exit_visual_basic is None or isinstance(exit_visual_basic, list) and all(x is None for x in exit_visual_basic):
        logging.error('exit_visual_basic is required.')
        return ['exit_visual_basic is required.']
    if exit_visual_basic is not None:

        request_parameters['exit'] = exit_visual_basic

    if finally_visual_basic is None or isinstance(finally_visual_basic, list) and all(x is None for x in finally_visual_basic):
        logging.error('finally_visual_basic is required.')
        return ['finally_visual_basic is required.']
    if finally_visual_basic is not None:

        request_parameters['finally'] = finally_visual_basic

    if for_visual_basic is None or isinstance(for_visual_basic, list) and all(x is None for x in for_visual_basic):
        logging.error('for_visual_basic is required.')
        return ['for_visual_basic is required.']
    if for_visual_basic is not None:

        request_parameters['for'] = for_visual_basic

    if friend_visual_basic is None or isinstance(friend_visual_basic, list) and all(x is None for x in friend_visual_basic):
        logging.error('friend_visual_basic is required.')
        return ['friend_visual_basic is required.']
    if friend_visual_basic is not None:

        request_parameters['friend'] = friend_visual_basic

    if function_visual_basic is None or isinstance(function_visual_basic, list) and all(x is None for x in function_visual_basic):
        logging.error('function_visual_basic is required.')
        return ['function_visual_basic is required.']
    if function_visual_basic is not None:

        request_parameters['function'] = function_visual_basic

    if get_visual_basic is None or isinstance(get_visual_basic, list) and all(x is None for x in get_visual_basic):
        logging.error('get_visual_basic is required.')
        return ['get_visual_basic is required.']
    if get_visual_basic is not None:

        request_parameters['get'] = get_visual_basic

    if gettype_visual_basic is None or isinstance(gettype_visual_basic, list) and all(x is None for x in gettype_visual_basic):
        logging.error('gettype_visual_basic is required.')
        return ['gettype_visual_basic is required.']
    if gettype_visual_basic is not None:

        request_parameters['gettype'] = gettype_visual_basic

    if getxmlnamespace_visual_basic is None or isinstance(getxmlnamespace_visual_basic, list) and all(x is None for x in getxmlnamespace_visual_basic):
        logging.error('getxmlnamespace_visual_basic is required.')
        return ['getxmlnamespace_visual_basic is required.']
    if getxmlnamespace_visual_basic is not None:

        request_parameters['getxmlnamespace'] = getxmlnamespace_visual_basic

    if global_visual_basic is None or isinstance(global_visual_basic, list) and all(x is None for x in global_visual_basic):
        logging.error('global_visual_basic is required.')
        return ['global_visual_basic is required.']
    if global_visual_basic is not None:

        request_parameters['global'] = global_visual_basic

    if gosub_visual_basic is None or isinstance(gosub_visual_basic, list) and all(x is None for x in gosub_visual_basic):
        logging.error('gosub_visual_basic is required.')
        return ['gosub_visual_basic is required.']
    if gosub_visual_basic is not None:

        request_parameters['gosub'] = gosub_visual_basic

    if goto_visual_basic is None or isinstance(goto_visual_basic, list) and all(x is None for x in goto_visual_basic):
        logging.error('goto_visual_basic is required.')
        return ['goto_visual_basic is required.']
    if goto_visual_basic is not None:

        request_parameters['goto'] = goto_visual_basic

    if handles_visual_basic is None or isinstance(handles_visual_basic, list) and all(x is None for x in handles_visual_basic):
        logging.error('handles_visual_basic is required.')
        return ['handles_visual_basic is required.']
    if handles_visual_basic is not None:

        request_parameters['handles'] = handles_visual_basic

    if if_visual_basic is None or isinstance(if_visual_basic, list) and all(x is None for x in if_visual_basic):
        logging.error('if_visual_basic is required.')
        return ['if_visual_basic is required.']
    if if_visual_basic is not None:

        request_parameters['if'] = if_visual_basic

    if implements_visual_basic is None or isinstance(implements_visual_basic, list) and all(x is None for x in implements_visual_basic):
        logging.error('implements_visual_basic is required.')
        return ['implements_visual_basic is required.']
    if implements_visual_basic is not None:

        request_parameters['implements'] = implements_visual_basic

    if imports_visual_basic is None or isinstance(imports_visual_basic, list) and all(x is None for x in imports_visual_basic):
        logging.error('imports_visual_basic is required.')
        return ['imports_visual_basic is required.']
    if imports_visual_basic is not None:

        request_parameters['imports'] = imports_visual_basic

    if in_visual_basic is None or isinstance(in_visual_basic, list) and all(x is None for x in in_visual_basic):
        logging.error('in_visual_basic is required.')
        return ['in_visual_basic is required.']
    if in_visual_basic is not None:

        request_parameters['in'] = in_visual_basic

    if inherits_visual_basic is None or isinstance(inherits_visual_basic, list) and all(x is None for x in inherits_visual_basic):
        logging.error('inherits_visual_basic is required.')
        return ['inherits_visual_basic is required.']
    if inherits_visual_basic is not None:

        request_parameters['inherits'] = inherits_visual_basic

    if integer_visual_basic is None or isinstance(integer_visual_basic, list) and all(x is None for x in integer_visual_basic):
        logging.error('integer_visual_basic is required.')
        return ['integer_visual_basic is required.']
    if integer_visual_basic is not None:

        request_parameters['integer'] = integer_visual_basic

    if interface_visual_basic is None or isinstance(interface_visual_basic, list) and all(x is None for x in interface_visual_basic):
        logging.error('interface_visual_basic is required.')
        return ['interface_visual_basic is required.']
    if interface_visual_basic is not None:

        request_parameters['interface'] = interface_visual_basic

    if is_visual_basic is None or isinstance(is_visual_basic, list) and all(x is None for x in is_visual_basic):
        logging.error('is_visual_basic is required.')
        return ['is_visual_basic is required.']
    if is_visual_basic is not None:

        request_parameters['is'] = is_visual_basic

    if isnot_visual_basic is None or isinstance(isnot_visual_basic, list) and all(x is None for x in isnot_visual_basic):
        logging.error('isnot_visual_basic is required.')
        return ['isnot_visual_basic is required.']
    if isnot_visual_basic is not None:

        request_parameters['isnot'] = isnot_visual_basic

    if let_visual_basic is None or isinstance(let_visual_basic, list) and all(x is None for x in let_visual_basic):
        logging.error('let_visual_basic is required.')
        return ['let_visual_basic is required.']
    if let_visual_basic is not None:

        request_parameters['let'] = let_visual_basic

    if lib_visual_basic is None or isinstance(lib_visual_basic, list) and all(x is None for x in lib_visual_basic):
        logging.error('lib_visual_basic is required.')
        return ['lib_visual_basic is required.']
    if lib_visual_basic is not None:

        request_parameters['lib'] = lib_visual_basic

    if like_visual_basic is None or isinstance(like_visual_basic, list) and all(x is None for x in like_visual_basic):
        logging.error('like_visual_basic is required.')
        return ['like_visual_basic is required.']
    if like_visual_basic is not None:

        request_parameters['like'] = like_visual_basic

    if long_visual_basic is None or isinstance(long_visual_basic, list) and all(x is None for x in long_visual_basic):
        logging.error('long_visual_basic is required.')
        return ['long_visual_basic is required.']
    if long_visual_basic is not None:

        request_parameters['long'] = long_visual_basic

    if loop_visual_basic is None or isinstance(loop_visual_basic, list) and all(x is None for x in loop_visual_basic):
        logging.error('loop_visual_basic is required.')
        return ['loop_visual_basic is required.']
    if loop_visual_basic is not None:

        request_parameters['loop'] = loop_visual_basic

    if me_visual_basic is None or isinstance(me_visual_basic, list) and all(x is None for x in me_visual_basic):
        logging.error('me_visual_basic is required.')
        return ['me_visual_basic is required.']
    if me_visual_basic is not None:

        request_parameters['me'] = me_visual_basic

    if mod_visual_basic is None or isinstance(mod_visual_basic, list) and all(x is None for x in mod_visual_basic):
        logging.error('mod_visual_basic is required.')
        return ['mod_visual_basic is required.']
    if mod_visual_basic is not None:

        request_parameters['mod'] = mod_visual_basic

    if module_visual_basic is None or isinstance(module_visual_basic, list) and all(x is None for x in module_visual_basic):
        logging.error('module_visual_basic is required.')
        return ['module_visual_basic is required.']
    if module_visual_basic is not None:

        request_parameters['module'] = module_visual_basic

    if mustinherit_visual_basic is None or isinstance(mustinherit_visual_basic, list) and all(x is None for x in mustinherit_visual_basic):
        logging.error('mustinherit_visual_basic is required.')
        return ['mustinherit_visual_basic is required.']
    if mustinherit_visual_basic is not None:

        request_parameters['mustinherit'] = mustinherit_visual_basic

    if mustoverride_visual_basic is None or isinstance(mustoverride_visual_basic, list) and all(x is None for x in mustoverride_visual_basic):
        logging.error('mustoverride_visual_basic is required.')
        return ['mustoverride_visual_basic is required.']
    if mustoverride_visual_basic is not None:

        request_parameters['mustoverride'] = mustoverride_visual_basic

    if mybase_visual_basic is None or isinstance(mybase_visual_basic, list) and all(x is None for x in mybase_visual_basic):
        logging.error('mybase_visual_basic is required.')
        return ['mybase_visual_basic is required.']
    if mybase_visual_basic is not None:

        request_parameters['mybase'] = mybase_visual_basic

    if myclass_visual_basic is None or isinstance(myclass_visual_basic, list) and all(x is None for x in myclass_visual_basic):
        logging.error('myclass_visual_basic is required.')
        return ['myclass_visual_basic is required.']
    if myclass_visual_basic is not None:

        request_parameters['myclass'] = myclass_visual_basic

    if namespace_visual_basic is None or isinstance(namespace_visual_basic, list) and all(x is None for x in namespace_visual_basic):
        logging.error('namespace_visual_basic is required.')
        return ['namespace_visual_basic is required.']
    if namespace_visual_basic is not None:

        request_parameters['namespace'] = namespace_visual_basic

    if narrowing_visual_basic is None or isinstance(narrowing_visual_basic, list) and all(x is None for x in narrowing_visual_basic):
        logging.error('narrowing_visual_basic is required.')
        return ['narrowing_visual_basic is required.']
    if narrowing_visual_basic is not None:

        request_parameters['narrowing'] = narrowing_visual_basic

    if new_visual_basic is None or isinstance(new_visual_basic, list) and all(x is None for x in new_visual_basic):
        logging.error('new_visual_basic is required.')
        return ['new_visual_basic is required.']
    if new_visual_basic is not None:

        request_parameters['new'] = new_visual_basic

    if next_visual_basic is None or isinstance(next_visual_basic, list) and all(x is None for x in next_visual_basic):
        logging.error('next_visual_basic is required.')
        return ['next_visual_basic is required.']
    if next_visual_basic is not None:

        request_parameters['next'] = next_visual_basic

    if not_visual_basic is None or isinstance(not_visual_basic, list) and all(x is None for x in not_visual_basic):
        logging.error('not_visual_basic is required.')
        return ['not_visual_basic is required.']
    if not_visual_basic is not None:

        request_parameters['not'] = not_visual_basic

    if nothing_visual_basic is None or isinstance(nothing_visual_basic, list) and all(x is None for x in nothing_visual_basic):
        logging.error('nothing_visual_basic is required.')
        return ['nothing_visual_basic is required.']
    if nothing_visual_basic is not None:

        request_parameters['nothing'] = nothing_visual_basic

    if notinheritable_visual_basic is None or isinstance(notinheritable_visual_basic, list) and all(x is None for x in notinheritable_visual_basic):
        logging.error('notinheritable_visual_basic is required.')
        return ['notinheritable_visual_basic is required.']
    if notinheritable_visual_basic is not None:

        request_parameters['notinheritable'] = notinheritable_visual_basic

    if notoverridable_visual_basic is None or isinstance(notoverridable_visual_basic, list) and all(x is None for x in notoverridable_visual_basic):
        logging.error('notoverridable_visual_basic is required.')
        return ['notoverridable_visual_basic is required.']
    if notoverridable_visual_basic is not None:

        request_parameters['notoverridable'] = notoverridable_visual_basic

    if object_visual_basic is None or isinstance(object_visual_basic, list) and all(x is None for x in object_visual_basic):
        logging.error('object_visual_basic is required.')
        return ['object_visual_basic is required.']
    if object_visual_basic is not None:

        request_parameters['object'] = object_visual_basic

    if of_visual_basic is None or isinstance(of_visual_basic, list) and all(x is None for x in of_visual_basic):
        logging.error('of_visual_basic is required.')
        return ['of_visual_basic is required.']
    if of_visual_basic is not None:

        request_parameters['of'] = of_visual_basic

    if on_visual_basic is None or isinstance(on_visual_basic, list) and all(x is None for x in on_visual_basic):
        logging.error('on_visual_basic is required.')
        return ['on_visual_basic is required.']
    if on_visual_basic is not None:

        request_parameters['on'] = on_visual_basic

    if operator_visual_basic is None or isinstance(operator_visual_basic, list) and all(x is None for x in operator_visual_basic):
        logging.error('operator_visual_basic is required.')
        return ['operator_visual_basic is required.']
    if operator_visual_basic is not None:

        request_parameters['operator'] = operator_visual_basic

    if option_visual_basic is None or isinstance(option_visual_basic, list) and all(x is None for x in option_visual_basic):
        logging.error('option_visual_basic is required.')
        return ['option_visual_basic is required.']
    if option_visual_basic is not None:

        request_parameters['option'] = option_visual_basic

    if optional_visual_basic is None or isinstance(optional_visual_basic, list) and all(x is None for x in optional_visual_basic):
        logging.error('optional_visual_basic is required.')
        return ['optional_visual_basic is required.']
    if optional_visual_basic is not None:

        request_parameters['optional'] = optional_visual_basic

    if or_visual_basic is None or isinstance(or_visual_basic, list) and all(x is None for x in or_visual_basic):
        logging.error('or_visual_basic is required.')
        return ['or_visual_basic is required.']
    if or_visual_basic is not None:

        request_parameters['or'] = or_visual_basic

    if orelse_visual_basic is None or isinstance(orelse_visual_basic, list) and all(x is None for x in orelse_visual_basic):
        logging.error('orelse_visual_basic is required.')
        return ['orelse_visual_basic is required.']
    if orelse_visual_basic is not None:

        request_parameters['orelse'] = orelse_visual_basic

    if overloads_visual_basic is None or isinstance(overloads_visual_basic, list) and all(x is None for x in overloads_visual_basic):
        logging.error('overloads_visual_basic is required.')
        return ['overloads_visual_basic is required.']
    if overloads_visual_basic is not None:

        request_parameters['overloads'] = overloads_visual_basic

    if overridable_visual_basic is None or isinstance(overridable_visual_basic, list) and all(x is None for x in overridable_visual_basic):
        logging.error('overridable_visual_basic is required.')
        return ['overridable_visual_basic is required.']
    if overridable_visual_basic is not None:

        request_parameters['overridable'] = overridable_visual_basic

    if overrides_visual_basic is None or isinstance(overrides_visual_basic, list) and all(x is None for x in overrides_visual_basic):
        logging.error('overrides_visual_basic is required.')
        return ['overrides_visual_basic is required.']
    if overrides_visual_basic is not None:

        request_parameters['overrides'] = overrides_visual_basic

    if paramarray_visual_basic is None or isinstance(paramarray_visual_basic, list) and all(x is None for x in paramarray_visual_basic):
        logging.error('paramarray_visual_basic is required.')
        return ['paramarray_visual_basic is required.']
    if paramarray_visual_basic is not None:

        request_parameters['paramarray'] = paramarray_visual_basic

    if partial_visual_basic is None or isinstance(partial_visual_basic, list) and all(x is None for x in partial_visual_basic):
        logging.error('partial_visual_basic is required.')
        return ['partial_visual_basic is required.']
    if partial_visual_basic is not None:

        request_parameters['partial'] = partial_visual_basic

    if private_visual_basic is None or isinstance(private_visual_basic, list) and all(x is None for x in private_visual_basic):
        logging.error('private_visual_basic is required.')
        return ['private_visual_basic is required.']
    if private_visual_basic is not None:

        request_parameters['private'] = private_visual_basic

    if property_visual_basic is None or isinstance(property_visual_basic, list) and all(x is None for x in property_visual_basic):
        logging.error('property_visual_basic is required.')
        return ['property_visual_basic is required.']
    if property_visual_basic is not None:

        request_parameters['property'] = property_visual_basic

    if protected_visual_basic is None or isinstance(protected_visual_basic, list) and all(x is None for x in protected_visual_basic):
        logging.error('protected_visual_basic is required.')
        return ['protected_visual_basic is required.']
    if protected_visual_basic is not None:

        request_parameters['protected'] = protected_visual_basic

    if public_visual_basic is None or isinstance(public_visual_basic, list) and all(x is None for x in public_visual_basic):
        logging.error('public_visual_basic is required.')
        return ['public_visual_basic is required.']
    if public_visual_basic is not None:

        request_parameters['public'] = public_visual_basic

    if raiseevent_visual_basic is None or isinstance(raiseevent_visual_basic, list) and all(x is None for x in raiseevent_visual_basic):
        logging.error('raiseevent_visual_basic is required.')
        return ['raiseevent_visual_basic is required.']
    if raiseevent_visual_basic is not None:

        request_parameters['raiseevent'] = raiseevent_visual_basic

    if readonly_visual_basic is None or isinstance(readonly_visual_basic, list) and all(x is None for x in readonly_visual_basic):
        logging.error('readonly_visual_basic is required.')
        return ['readonly_visual_basic is required.']
    if readonly_visual_basic is not None:

        request_parameters['readonly'] = readonly_visual_basic

    if redim_visual_basic is None or isinstance(redim_visual_basic, list) and all(x is None for x in redim_visual_basic):
        logging.error('redim_visual_basic is required.')
        return ['redim_visual_basic is required.']
    if redim_visual_basic is not None:

        request_parameters['redim'] = redim_visual_basic

    if rem_visual_basic is None or isinstance(rem_visual_basic, list) and all(x is None for x in rem_visual_basic):
        logging.error('rem_visual_basic is required.')
        return ['rem_visual_basic is required.']
    if rem_visual_basic is not None:

        request_parameters['rem'] = rem_visual_basic

    if removehandler_visual_basic is None or isinstance(removehandler_visual_basic, list) and all(x is None for x in removehandler_visual_basic):
        logging.error('removehandler_visual_basic is required.')
        return ['removehandler_visual_basic is required.']
    if removehandler_visual_basic is not None:

        request_parameters['removehandler'] = removehandler_visual_basic

    if resume_visual_basic is None or isinstance(resume_visual_basic, list) and all(x is None for x in resume_visual_basic):
        logging.error('resume_visual_basic is required.')
        return ['resume_visual_basic is required.']
    if resume_visual_basic is not None:

        request_parameters['resume'] = resume_visual_basic

    if return_visual_basic is None or isinstance(return_visual_basic, list) and all(x is None for x in return_visual_basic):
        logging.error('return_visual_basic is required.')
        return ['return_visual_basic is required.']
    if return_visual_basic is not None:

        request_parameters['return'] = return_visual_basic

    if sbyte_visual_basic is None or isinstance(sbyte_visual_basic, list) and all(x is None for x in sbyte_visual_basic):
        logging.error('sbyte_visual_basic is required.')
        return ['sbyte_visual_basic is required.']
    if sbyte_visual_basic is not None:

        request_parameters['sbyte'] = sbyte_visual_basic

    if select_visual_basic is None or isinstance(select_visual_basic, list) and all(x is None for x in select_visual_basic):
        logging.error('select_visual_basic is required.')
        return ['select_visual_basic is required.']
    if select_visual_basic is not None:

        request_parameters['select'] = select_visual_basic

    if set_visual_basic is None or isinstance(set_visual_basic, list) and all(x is None for x in set_visual_basic):
        logging.error('set_visual_basic is required.')
        return ['set_visual_basic is required.']
    if set_visual_basic is not None:

        request_parameters['set'] = set_visual_basic

    if shadows_visual_basic is None or isinstance(shadows_visual_basic, list) and all(x is None for x in shadows_visual_basic):
        logging.error('shadows_visual_basic is required.')
        return ['shadows_visual_basic is required.']
    if shadows_visual_basic is not None:

        request_parameters['shadows'] = shadows_visual_basic

    if shared_visual_basic is None or isinstance(shared_visual_basic, list) and all(x is None for x in shared_visual_basic):
        logging.error('shared_visual_basic is required.')
        return ['shared_visual_basic is required.']
    if shared_visual_basic is not None:

        request_parameters['shared'] = shared_visual_basic

    if short_visual_basic is None or isinstance(short_visual_basic, list) and all(x is None for x in short_visual_basic):
        logging.error('short_visual_basic is required.')
        return ['short_visual_basic is required.']
    if short_visual_basic is not None:

        request_parameters['short'] = short_visual_basic

    if single_visual_basic is None or isinstance(single_visual_basic, list) and all(x is None for x in single_visual_basic):
        logging.error('single_visual_basic is required.')
        return ['single_visual_basic is required.']
    if single_visual_basic is not None:

        request_parameters['single'] = single_visual_basic

    if static_visual_basic is None or isinstance(static_visual_basic, list) and all(x is None for x in static_visual_basic):
        logging.error('static_visual_basic is required.')
        return ['static_visual_basic is required.']
    if static_visual_basic is not None:

        request_parameters['static'] = static_visual_basic

    if step_visual_basic is None or isinstance(step_visual_basic, list) and all(x is None for x in step_visual_basic):
        logging.error('step_visual_basic is required.')
        return ['step_visual_basic is required.']
    if step_visual_basic is not None:

        request_parameters['step'] = step_visual_basic

    if stop_visual_basic is None or isinstance(stop_visual_basic, list) and all(x is None for x in stop_visual_basic):
        logging.error('stop_visual_basic is required.')
        return ['stop_visual_basic is required.']
    if stop_visual_basic is not None:

        request_parameters['stop'] = stop_visual_basic

    if string_visual_basic is None or isinstance(string_visual_basic, list) and all(x is None for x in string_visual_basic):
        logging.error('string_visual_basic is required.')
        return ['string_visual_basic is required.']
    if string_visual_basic is not None:

        request_parameters['string'] = string_visual_basic

    if structure_visual_basic is None or isinstance(structure_visual_basic, list) and all(x is None for x in structure_visual_basic):
        logging.error('structure_visual_basic is required.')
        return ['structure_visual_basic is required.']
    if structure_visual_basic is not None:

        request_parameters['structure'] = structure_visual_basic

    if sub_visual_basic is None or isinstance(sub_visual_basic, list) and all(x is None for x in sub_visual_basic):
        logging.error('sub_visual_basic is required.')
        return ['sub_visual_basic is required.']
    if sub_visual_basic is not None:

        request_parameters['sub'] = sub_visual_basic

    if synclock_visual_basic is None or isinstance(synclock_visual_basic, list) and all(x is None for x in synclock_visual_basic):
        logging.error('synclock_visual_basic is required.')
        return ['synclock_visual_basic is required.']
    if synclock_visual_basic is not None:

        request_parameters['synclock'] = synclock_visual_basic

    if then_visual_basic is None or isinstance(then_visual_basic, list) and all(x is None for x in then_visual_basic):
        logging.error('then_visual_basic is required.')
        return ['then_visual_basic is required.']
    if then_visual_basic is not None:

        request_parameters['then'] = then_visual_basic

    if throw_visual_basic is None or isinstance(throw_visual_basic, list) and all(x is None for x in throw_visual_basic):
        logging.error('throw_visual_basic is required.')
        return ['throw_visual_basic is required.']
    if throw_visual_basic is not None:

        request_parameters['throw'] = throw_visual_basic

    if to_visual_basic is None or isinstance(to_visual_basic, list) and all(x is None for x in to_visual_basic):
        logging.error('to_visual_basic is required.')
        return ['to_visual_basic is required.']
    if to_visual_basic is not None:

        request_parameters['to'] = to_visual_basic

    if try_visual_basic is None or isinstance(try_visual_basic, list) and all(x is None for x in try_visual_basic):
        logging.error('try_visual_basic is required.')
        return ['try_visual_basic is required.']
    if try_visual_basic is not None:

        request_parameters['try'] = try_visual_basic

    if trycast_visual_basic is None or isinstance(trycast_visual_basic, list) and all(x is None for x in trycast_visual_basic):
        logging.error('trycast_visual_basic is required.')
        return ['trycast_visual_basic is required.']
    if trycast_visual_basic is not None:

        request_parameters['trycast'] = trycast_visual_basic

    if type_visual_basic is None or isinstance(type_visual_basic, list) and all(x is None for x in type_visual_basic):
        logging.error('type_visual_basic is required.')
        return ['type_visual_basic is required.']
    if type_visual_basic is not None:

        request_parameters['type'] = type_visual_basic

    if typeof_visual_basic is None or isinstance(typeof_visual_basic, list) and all(x is None for x in typeof_visual_basic):
        logging.error('typeof_visual_basic is required.')
        return ['typeof_visual_basic is required.']
    if typeof_visual_basic is not None:

        request_parameters['typeof'] = typeof_visual_basic

    if uinteger_visual_basic is None or isinstance(uinteger_visual_basic, list) and all(x is None for x in uinteger_visual_basic):
        logging.error('uinteger_visual_basic is required.')
        return ['uinteger_visual_basic is required.']
    if uinteger_visual_basic is not None:

        request_parameters['uinteger'] = uinteger_visual_basic

    if ulong_visual_basic is None or isinstance(ulong_visual_basic, list) and all(x is None for x in ulong_visual_basic):
        logging.error('ulong_visual_basic is required.')
        return ['ulong_visual_basic is required.']
    if ulong_visual_basic is not None:

        request_parameters['ulong'] = ulong_visual_basic

    if ushort_visual_basic is None or isinstance(ushort_visual_basic, list) and all(x is None for x in ushort_visual_basic):
        logging.error('ushort_visual_basic is required.')
        return ['ushort_visual_basic is required.']
    if ushort_visual_basic is not None:

        request_parameters['ushort'] = ushort_visual_basic

    if using_visual_basic is None or isinstance(using_visual_basic, list) and all(x is None for x in using_visual_basic):
        logging.error('using_visual_basic is required.')
        return ['using_visual_basic is required.']
    if using_visual_basic is not None:

        request_parameters['using'] = using_visual_basic

    if variant_visual_basic is None or isinstance(variant_visual_basic, list) and all(x is None for x in variant_visual_basic):
        logging.error('variant_visual_basic is required.')
        return ['variant_visual_basic is required.']
    if variant_visual_basic is not None:

        request_parameters['variant'] = variant_visual_basic

    if wend_visual_basic is None or isinstance(wend_visual_basic, list) and all(x is None for x in wend_visual_basic):
        logging.error('wend_visual_basic is required.')
        return ['wend_visual_basic is required.']
    if wend_visual_basic is not None:

        request_parameters['wend'] = wend_visual_basic

    if when_visual_basic is None or isinstance(when_visual_basic, list) and all(x is None for x in when_visual_basic):
        logging.error('when_visual_basic is required.')
        return ['when_visual_basic is required.']
    if when_visual_basic is not None:

        request_parameters['when'] = when_visual_basic

    if while_visual_basic is None or isinstance(while_visual_basic, list) and all(x is None for x in while_visual_basic):
        logging.error('while_visual_basic is required.')
        return ['while_visual_basic is required.']
    if while_visual_basic is not None:

        request_parameters['while'] = while_visual_basic

    if widening_visual_basic is None or isinstance(widening_visual_basic, list) and all(x is None for x in widening_visual_basic):
        logging.error('widening_visual_basic is required.')
        return ['widening_visual_basic is required.']
    if widening_visual_basic is not None:

        request_parameters['widening'] = widening_visual_basic

    if with_visual_basic is None or isinstance(with_visual_basic, list) and all(x is None for x in with_visual_basic):
        logging.error('with_visual_basic is required.')
        return ['with_visual_basic is required.']
    if with_visual_basic is not None:

        request_parameters['with'] = with_visual_basic

    if withevents_visual_basic is None or isinstance(withevents_visual_basic, list) and all(x is None for x in withevents_visual_basic):
        logging.error('withevents_visual_basic is required.')
        return ['withevents_visual_basic is required.']
    if withevents_visual_basic is not None:

        request_parameters['withevents'] = withevents_visual_basic

    if writeonly_visual_basic is None or isinstance(writeonly_visual_basic, list) and all(x is None for x in writeonly_visual_basic):
        logging.error('writeonly_visual_basic is required.')
        return ['writeonly_visual_basic is required.']
    if writeonly_visual_basic is not None:

        request_parameters['writeonly'] = writeonly_visual_basic

    if xor_visual_basic is None or isinstance(xor_visual_basic, list) and all(x is None for x in xor_visual_basic):
        logging.error('xor_visual_basic is required.')
        return ['xor_visual_basic is required.']
    if xor_visual_basic is not None:

        request_parameters['xor'] = xor_visual_basic


    response = None
    try:
        response = requests.post('http://localhost:8949/test/vba/restricted/keywords'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for vba_keywords_test_post_test_vba_restricted_keywords ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/VBAKeywords'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('VBAKeywords', OrderedDict([('properties', OrderedDict([('addhandler', OrderedDict()), ('addressof', OrderedDict()), ('alias', OrderedDict()), ('and', OrderedDict()), ('andalso', OrderedDict()), ('as', OrderedDict()), ('boolean', OrderedDict()), ('byref', OrderedDict()), ('byte', OrderedDict()), ('byval', OrderedDict()), ('call', OrderedDict()), ('case', OrderedDict()), ('catch', OrderedDict()), ('cbool', OrderedDict()), ('cbyte', OrderedDict()), ('cchar', OrderedDict()), ('cdate', OrderedDict()), ('cdbl', OrderedDict()), ('cdec', OrderedDict()), ('char', OrderedDict()), ('cint', OrderedDict()), ('class', OrderedDict()), ('clng', OrderedDict()), ('cobj', OrderedDict()), ('const', OrderedDict()), ('continue', OrderedDict()), ('csbyte', OrderedDict()), ('cshort', OrderedDict()), ('csng', OrderedDict()), ('cstr', OrderedDict()), ('ctype', OrderedDict()), ('cuint', OrderedDict()), ('culng', OrderedDict()), ('currency', OrderedDict()), ('cushort', OrderedDict()), ('date', OrderedDict()), ('decimal', OrderedDict()), ('declare', OrderedDict()), ('default', OrderedDict()), ('delegate', OrderedDict()), ('dim', OrderedDict()), ('directcast', OrderedDict()), ('do', OrderedDict()), ('double', OrderedDict()), ('each', OrderedDict()), ('else', OrderedDict()), ('elseif', OrderedDict()), ('end', OrderedDict()), ('endif', OrderedDict()), ('enum', OrderedDict()), ('erase', OrderedDict()), ('error', OrderedDict()), ('event', OrderedDict()), ('exit', OrderedDict()), ('finally', OrderedDict()), ('for', OrderedDict()), ('friend', OrderedDict()), ('function', OrderedDict()), ('get', OrderedDict()), ('gettype', OrderedDict()), ('getxmlnamespace', OrderedDict()), ('global', OrderedDict()), ('gosub', OrderedDict()), ('goto', OrderedDict()), ('handles', OrderedDict()), ('if', OrderedDict()), ('implements', OrderedDict()), ('imports', OrderedDict()), ('in', OrderedDict()), ('inherits', OrderedDict()), ('integer', OrderedDict()), ('interface', OrderedDict()), ('is', OrderedDict()), ('isnot', OrderedDict()), ('let', OrderedDict()), ('lib', OrderedDict()), ('like', OrderedDict()), ('long', OrderedDict()), ('loop', OrderedDict()), ('me', OrderedDict()), ('mod', OrderedDict()), ('module', OrderedDict()), ('mustinherit', OrderedDict()), ('mustoverride', OrderedDict()), ('mybase', OrderedDict()), ('myclass', OrderedDict()), ('namespace', OrderedDict()), ('narrowing', OrderedDict()), ('new', OrderedDict()), ('next', OrderedDict()), ('not', OrderedDict()), ('nothing', OrderedDict()), ('notinheritable', OrderedDict()), ('notoverridable', OrderedDict()), ('object', OrderedDict()), ('of', OrderedDict()), ('on', OrderedDict()), ('operator', OrderedDict()), ('option', OrderedDict()), ('optional', OrderedDict()), ('or', OrderedDict()), ('orelse', OrderedDict()), ('overloads', OrderedDict()), ('overridable', OrderedDict()), ('overrides', OrderedDict()), ('paramarray', OrderedDict()), ('partial', OrderedDict()), ('private', OrderedDict()), ('property', OrderedDict()), ('protected', OrderedDict()), ('public', OrderedDict()), ('raiseevent', OrderedDict()), ('readonly', OrderedDict()), ('redim', OrderedDict()), ('rem', OrderedDict()), ('removehandler', OrderedDict()), ('resume', OrderedDict()), ('return', OrderedDict()), ('sbyte', OrderedDict()), ('select', OrderedDict()), ('set', OrderedDict()), ('shadows', OrderedDict()), ('shared', OrderedDict()), ('short', OrderedDict()), ('single', OrderedDict()), ('static', OrderedDict()), ('step', OrderedDict()), ('stop', OrderedDict()), ('string', OrderedDict()), ('structure', OrderedDict()), ('sub', OrderedDict()), ('synclock', OrderedDict()), ('then', OrderedDict()), ('throw', OrderedDict()), ('to', OrderedDict()), ('try', OrderedDict()), ('trycast', OrderedDict()), ('type', OrderedDict()), ('typeof', OrderedDict()), ('uinteger', OrderedDict()), ('ulong', OrderedDict()), ('ushort', OrderedDict()), ('using', OrderedDict()), ('variant', OrderedDict()), ('wend', OrderedDict()), ('when', OrderedDict()), ('while', OrderedDict()), ('widening', OrderedDict()), ('with', OrderedDict()), ('withevents', OrderedDict()), ('writeonly', OrderedDict()), ('xor', OrderedDict())]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling vba_keywords_test_post_test_vba_restricted_keywords.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling vba_keywords_test_post_test_vba_restricted_keywords response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling vba_keywords_test_post_test_vba_restricted_keywords.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='vba_keywords_test', call_in_wizard=False)
@xw.arg('addhandler_visual_basic', doc='')
@xw.arg('addressof_visual_basic', doc='')
@xw.arg('alias_visual_basic', doc='')
@xw.arg('and_visual_basic', doc='')
@xw.arg('andalso_visual_basic', doc='')
@xw.arg('as_visual_basic', doc='')
@xw.arg('boolean_visual_basic', doc='')
@xw.arg('byref_visual_basic', doc='')
@xw.arg('byte_visual_basic', doc='')
@xw.arg('byval_visual_basic', doc='')
@xw.arg('call_visual_basic', doc='')
@xw.arg('case_visual_basic', doc='')
@xw.arg('catch_visual_basic', doc='')
@xw.arg('cbool_visual_basic', doc='')
@xw.arg('cbyte_visual_basic', doc='')
@xw.arg('cchar_visual_basic', doc='')
@xw.arg('cdate_visual_basic', doc='')
@xw.arg('cdbl_visual_basic', doc='')
@xw.arg('cdec_visual_basic', doc='')
@xw.arg('char_visual_basic', doc='')
@xw.arg('cint_visual_basic', doc='')
@xw.arg('class_visual_basic', doc='')
@xw.arg('clng_visual_basic', doc='')
@xw.arg('cobj_visual_basic', doc='')
@xw.arg('const_visual_basic', doc='')
@xw.arg('continue_visual_basic', doc='')
@xw.arg('csbyte_visual_basic', doc='')
@xw.arg('cshort_visual_basic', doc='')
@xw.arg('csng_visual_basic', doc='')
@xw.arg('cstr_visual_basic', doc='')
@xw.arg('ctype_visual_basic', doc='')
@xw.arg('cuint_visual_basic', doc='')
@xw.arg('culng_visual_basic', doc='')
@xw.arg('currency_visual_basic', doc='')
@xw.arg('cushort_visual_basic', doc='')
@xw.arg('date_visual_basic', doc='')
@xw.arg('decimal_visual_basic', doc='')
@xw.arg('declare_visual_basic', doc='')
@xw.arg('default_visual_basic', doc='')
@xw.arg('delegate_visual_basic', doc='')
@xw.arg('dim_visual_basic', doc='')
@xw.arg('directcast_visual_basic', doc='')
@xw.arg('do_visual_basic', doc='')
@xw.arg('double_visual_basic', doc='')
@xw.arg('each_visual_basic', doc='')
@xw.arg('else_visual_basic', doc='')
@xw.arg('elseif_visual_basic', doc='')
@xw.arg('end_visual_basic', doc='')
@xw.arg('endif_visual_basic', doc='')
@xw.arg('enum_visual_basic', doc='')
@xw.arg('erase_visual_basic', doc='')
@xw.arg('error_visual_basic', doc='')
@xw.arg('event_visual_basic', doc='')
@xw.arg('exit_visual_basic', doc='')
@xw.arg('finally_visual_basic', doc='')
@xw.arg('for_visual_basic', doc='')
@xw.arg('friend_visual_basic', doc='')
@xw.arg('function_visual_basic', doc='')
@xw.arg('get_visual_basic', doc='')
@xw.arg('gettype_visual_basic', doc='')
@xw.arg('getxmlnamespace_visual_basic', doc='')
@xw.arg('global_visual_basic', doc='')
@xw.arg('gosub_visual_basic', doc='')
@xw.arg('goto_visual_basic', doc='')
@xw.arg('handles_visual_basic', doc='')
@xw.arg('if_visual_basic', doc='')
@xw.arg('implements_visual_basic', doc='')
@xw.arg('imports_visual_basic', doc='')
@xw.arg('in_visual_basic', doc='')
@xw.arg('inherits_visual_basic', doc='')
@xw.arg('integer_visual_basic', doc='')
@xw.arg('interface_visual_basic', doc='')
@xw.arg('is_visual_basic', doc='')
@xw.arg('isnot_visual_basic', doc='')
@xw.arg('let_visual_basic', doc='')
@xw.arg('lib_visual_basic', doc='')
@xw.arg('like_visual_basic', doc='')
@xw.arg('long_visual_basic', doc='')
@xw.arg('loop_visual_basic', doc='')
@xw.arg('me_visual_basic', doc='')
@xw.arg('mod_visual_basic', doc='')
@xw.arg('module_visual_basic', doc='')
@xw.arg('mustinherit_visual_basic', doc='')
@xw.arg('mustoverride_visual_basic', doc='')
@xw.arg('mybase_visual_basic', doc='')
@xw.arg('myclass_visual_basic', doc='')
@xw.arg('namespace_visual_basic', doc='')
@xw.arg('narrowing_visual_basic', doc='')
@xw.arg('new_visual_basic', doc='')
@xw.arg('next_visual_basic', doc='')
@xw.arg('not_visual_basic', doc='')
@xw.arg('nothing_visual_basic', doc='')
@xw.arg('notinheritable_visual_basic', doc='')
@xw.arg('notoverridable_visual_basic', doc='')
@xw.arg('object_visual_basic', doc='')
@xw.arg('of_visual_basic', doc='')
@xw.arg('on_visual_basic', doc='')
@xw.arg('operator_visual_basic', doc='')
@xw.arg('option_visual_basic', doc='')
@xw.arg('optional_visual_basic', doc='')
@xw.arg('or_visual_basic', doc='')
@xw.arg('orelse_visual_basic', doc='')
@xw.arg('overloads_visual_basic', doc='')
@xw.arg('overridable_visual_basic', doc='')
@xw.arg('overrides_visual_basic', doc='')
@xw.arg('paramarray_visual_basic', doc='')
@xw.arg('partial_visual_basic', doc='')
@xw.arg('private_visual_basic', doc='')
@xw.arg('property_visual_basic', doc='')
@xw.arg('protected_visual_basic', doc='')
@xw.arg('public_visual_basic', doc='')
@xw.arg('raiseevent_visual_basic', doc='')
@xw.arg('readonly_visual_basic', doc='')
@xw.arg('redim_visual_basic', doc='')
@xw.arg('rem_visual_basic', doc='')
@xw.arg('removehandler_visual_basic', doc='')
@xw.arg('resume_visual_basic', doc='')
@xw.arg('return_visual_basic', doc='')
@xw.arg('sbyte_visual_basic', doc='')
@xw.arg('select_visual_basic', doc='')
@xw.arg('set_visual_basic', doc='')
@xw.arg('shadows_visual_basic', doc='')
@xw.arg('shared_visual_basic', doc='')
@xw.arg('short_visual_basic', doc='')
@xw.arg('single_visual_basic', doc='')
@xw.arg('static_visual_basic', doc='')
@xw.arg('step_visual_basic', doc='')
@xw.arg('stop_visual_basic', doc='')
@xw.arg('string_visual_basic', doc='')
@xw.arg('structure_visual_basic', doc='')
@xw.arg('sub_visual_basic', doc='')
@xw.arg('synclock_visual_basic', doc='')
@xw.arg('then_visual_basic', doc='')
@xw.arg('throw_visual_basic', doc='')
@xw.arg('to_visual_basic', doc='')
@xw.arg('try_visual_basic', doc='')
@xw.arg('trycast_visual_basic', doc='')
@xw.arg('type_visual_basic', doc='')
@xw.arg('typeof_visual_basic', doc='')
@xw.arg('uinteger_visual_basic', doc='')
@xw.arg('ulong_visual_basic', doc='')
@xw.arg('ushort_visual_basic', doc='')
@xw.arg('using_visual_basic', doc='')
@xw.arg('variant_visual_basic', doc='')
@xw.arg('wend_visual_basic', doc='')
@xw.arg('when_visual_basic', doc='')
@xw.arg('while_visual_basic', doc='')
@xw.arg('widening_visual_basic', doc='')
@xw.arg('with_visual_basic', doc='')
@xw.arg('withevents_visual_basic', doc='')
@xw.arg('writeonly_visual_basic', doc='')
@xw.arg('xor_visual_basic', doc='')
@xw.ret(expand='table')
def vba_keywords_test_put_test_vba_restricted_keywords(addhandler_visual_basic, addressof_visual_basic, alias_visual_basic, and_visual_basic, andalso_visual_basic, as_visual_basic, boolean_visual_basic, byref_visual_basic, byte_visual_basic, byval_visual_basic, call_visual_basic, case_visual_basic, catch_visual_basic, cbool_visual_basic, cbyte_visual_basic, cchar_visual_basic, cdate_visual_basic, cdbl_visual_basic, cdec_visual_basic, char_visual_basic, cint_visual_basic, class_visual_basic, clng_visual_basic, cobj_visual_basic, const_visual_basic, continue_visual_basic, csbyte_visual_basic, cshort_visual_basic, csng_visual_basic, cstr_visual_basic, ctype_visual_basic, cuint_visual_basic, culng_visual_basic, currency_visual_basic, cushort_visual_basic, date_visual_basic, decimal_visual_basic, declare_visual_basic, default_visual_basic, delegate_visual_basic, dim_visual_basic, directcast_visual_basic, do_visual_basic, double_visual_basic, each_visual_basic, else_visual_basic, elseif_visual_basic, end_visual_basic, endif_visual_basic, enum_visual_basic, erase_visual_basic, error_visual_basic, event_visual_basic, exit_visual_basic, finally_visual_basic, for_visual_basic, friend_visual_basic, function_visual_basic, get_visual_basic, gettype_visual_basic, getxmlnamespace_visual_basic, global_visual_basic, gosub_visual_basic, goto_visual_basic, handles_visual_basic, if_visual_basic, implements_visual_basic, imports_visual_basic, in_visual_basic, inherits_visual_basic, integer_visual_basic, interface_visual_basic, is_visual_basic, isnot_visual_basic, let_visual_basic, lib_visual_basic, like_visual_basic, long_visual_basic, loop_visual_basic, me_visual_basic, mod_visual_basic, module_visual_basic, mustinherit_visual_basic, mustoverride_visual_basic, mybase_visual_basic, myclass_visual_basic, namespace_visual_basic, narrowing_visual_basic, new_visual_basic, next_visual_basic, not_visual_basic, nothing_visual_basic, notinheritable_visual_basic, notoverridable_visual_basic, object_visual_basic, of_visual_basic, on_visual_basic, operator_visual_basic, option_visual_basic, optional_visual_basic, or_visual_basic, orelse_visual_basic, overloads_visual_basic, overridable_visual_basic, overrides_visual_basic, paramarray_visual_basic, partial_visual_basic, private_visual_basic, property_visual_basic, protected_visual_basic, public_visual_basic, raiseevent_visual_basic, readonly_visual_basic, redim_visual_basic, rem_visual_basic, removehandler_visual_basic, resume_visual_basic, return_visual_basic, sbyte_visual_basic, select_visual_basic, set_visual_basic, shadows_visual_basic, shared_visual_basic, short_visual_basic, single_visual_basic, static_visual_basic, step_visual_basic, stop_visual_basic, string_visual_basic, structure_visual_basic, sub_visual_basic, synclock_visual_basic, then_visual_basic, throw_visual_basic, to_visual_basic, try_visual_basic, trycast_visual_basic, type_visual_basic, typeof_visual_basic, uinteger_visual_basic, ulong_visual_basic, ushort_visual_basic, using_visual_basic, variant_visual_basic, wend_visual_basic, when_visual_basic, while_visual_basic, widening_visual_basic, with_visual_basic, withevents_visual_basic, writeonly_visual_basic, xor_visual_basic):
    logging.info("Calling vba_keywords_test_put_test_vba_restricted_keywords...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if addhandler_visual_basic is None or isinstance(addhandler_visual_basic, list) and all(x is None for x in addhandler_visual_basic):
        logging.error('addhandler_visual_basic is required.')
        return ['addhandler_visual_basic is required.']
    if addhandler_visual_basic is not None:

        request_parameters['addhandler'] = addhandler_visual_basic

    if addressof_visual_basic is None or isinstance(addressof_visual_basic, list) and all(x is None for x in addressof_visual_basic):
        logging.error('addressof_visual_basic is required.')
        return ['addressof_visual_basic is required.']
    if addressof_visual_basic is not None:

        request_parameters['addressof'] = addressof_visual_basic

    if alias_visual_basic is None or isinstance(alias_visual_basic, list) and all(x is None for x in alias_visual_basic):
        logging.error('alias_visual_basic is required.')
        return ['alias_visual_basic is required.']
    if alias_visual_basic is not None:

        request_parameters['alias'] = alias_visual_basic

    if and_visual_basic is None or isinstance(and_visual_basic, list) and all(x is None for x in and_visual_basic):
        logging.error('and_visual_basic is required.')
        return ['and_visual_basic is required.']
    if and_visual_basic is not None:

        request_parameters['and'] = and_visual_basic

    if andalso_visual_basic is None or isinstance(andalso_visual_basic, list) and all(x is None for x in andalso_visual_basic):
        logging.error('andalso_visual_basic is required.')
        return ['andalso_visual_basic is required.']
    if andalso_visual_basic is not None:

        request_parameters['andalso'] = andalso_visual_basic

    if as_visual_basic is None or isinstance(as_visual_basic, list) and all(x is None for x in as_visual_basic):
        logging.error('as_visual_basic is required.')
        return ['as_visual_basic is required.']
    if as_visual_basic is not None:

        request_parameters['as'] = as_visual_basic

    if boolean_visual_basic is None or isinstance(boolean_visual_basic, list) and all(x is None for x in boolean_visual_basic):
        logging.error('boolean_visual_basic is required.')
        return ['boolean_visual_basic is required.']
    if boolean_visual_basic is not None:

        request_parameters['boolean'] = boolean_visual_basic

    if byref_visual_basic is None or isinstance(byref_visual_basic, list) and all(x is None for x in byref_visual_basic):
        logging.error('byref_visual_basic is required.')
        return ['byref_visual_basic is required.']
    if byref_visual_basic is not None:

        request_parameters['byref'] = byref_visual_basic

    if byte_visual_basic is None or isinstance(byte_visual_basic, list) and all(x is None for x in byte_visual_basic):
        logging.error('byte_visual_basic is required.')
        return ['byte_visual_basic is required.']
    if byte_visual_basic is not None:

        request_parameters['byte'] = byte_visual_basic

    if byval_visual_basic is None or isinstance(byval_visual_basic, list) and all(x is None for x in byval_visual_basic):
        logging.error('byval_visual_basic is required.')
        return ['byval_visual_basic is required.']
    if byval_visual_basic is not None:

        request_parameters['byval'] = byval_visual_basic

    if call_visual_basic is None or isinstance(call_visual_basic, list) and all(x is None for x in call_visual_basic):
        logging.error('call_visual_basic is required.')
        return ['call_visual_basic is required.']
    if call_visual_basic is not None:

        request_parameters['call'] = call_visual_basic

    if case_visual_basic is None or isinstance(case_visual_basic, list) and all(x is None for x in case_visual_basic):
        logging.error('case_visual_basic is required.')
        return ['case_visual_basic is required.']
    if case_visual_basic is not None:

        request_parameters['case'] = case_visual_basic

    if catch_visual_basic is None or isinstance(catch_visual_basic, list) and all(x is None for x in catch_visual_basic):
        logging.error('catch_visual_basic is required.')
        return ['catch_visual_basic is required.']
    if catch_visual_basic is not None:

        request_parameters['catch'] = catch_visual_basic

    if cbool_visual_basic is None or isinstance(cbool_visual_basic, list) and all(x is None for x in cbool_visual_basic):
        logging.error('cbool_visual_basic is required.')
        return ['cbool_visual_basic is required.']
    if cbool_visual_basic is not None:

        request_parameters['cbool'] = cbool_visual_basic

    if cbyte_visual_basic is None or isinstance(cbyte_visual_basic, list) and all(x is None for x in cbyte_visual_basic):
        logging.error('cbyte_visual_basic is required.')
        return ['cbyte_visual_basic is required.']
    if cbyte_visual_basic is not None:

        request_parameters['cbyte'] = cbyte_visual_basic

    if cchar_visual_basic is None or isinstance(cchar_visual_basic, list) and all(x is None for x in cchar_visual_basic):
        logging.error('cchar_visual_basic is required.')
        return ['cchar_visual_basic is required.']
    if cchar_visual_basic is not None:

        request_parameters['cchar'] = cchar_visual_basic

    if cdate_visual_basic is None or isinstance(cdate_visual_basic, list) and all(x is None for x in cdate_visual_basic):
        logging.error('cdate_visual_basic is required.')
        return ['cdate_visual_basic is required.']
    if cdate_visual_basic is not None:

        request_parameters['cdate'] = cdate_visual_basic

    if cdbl_visual_basic is None or isinstance(cdbl_visual_basic, list) and all(x is None for x in cdbl_visual_basic):
        logging.error('cdbl_visual_basic is required.')
        return ['cdbl_visual_basic is required.']
    if cdbl_visual_basic is not None:

        request_parameters['cdbl'] = cdbl_visual_basic

    if cdec_visual_basic is None or isinstance(cdec_visual_basic, list) and all(x is None for x in cdec_visual_basic):
        logging.error('cdec_visual_basic is required.')
        return ['cdec_visual_basic is required.']
    if cdec_visual_basic is not None:

        request_parameters['cdec'] = cdec_visual_basic

    if char_visual_basic is None or isinstance(char_visual_basic, list) and all(x is None for x in char_visual_basic):
        logging.error('char_visual_basic is required.')
        return ['char_visual_basic is required.']
    if char_visual_basic is not None:

        request_parameters['char'] = char_visual_basic

    if cint_visual_basic is None or isinstance(cint_visual_basic, list) and all(x is None for x in cint_visual_basic):
        logging.error('cint_visual_basic is required.')
        return ['cint_visual_basic is required.']
    if cint_visual_basic is not None:

        request_parameters['cint'] = cint_visual_basic

    if class_visual_basic is None or isinstance(class_visual_basic, list) and all(x is None for x in class_visual_basic):
        logging.error('class_visual_basic is required.')
        return ['class_visual_basic is required.']
    if class_visual_basic is not None:

        request_parameters['class'] = class_visual_basic

    if clng_visual_basic is None or isinstance(clng_visual_basic, list) and all(x is None for x in clng_visual_basic):
        logging.error('clng_visual_basic is required.')
        return ['clng_visual_basic is required.']
    if clng_visual_basic is not None:

        request_parameters['clng'] = clng_visual_basic

    if cobj_visual_basic is None or isinstance(cobj_visual_basic, list) and all(x is None for x in cobj_visual_basic):
        logging.error('cobj_visual_basic is required.')
        return ['cobj_visual_basic is required.']
    if cobj_visual_basic is not None:

        request_parameters['cobj'] = cobj_visual_basic

    if const_visual_basic is None or isinstance(const_visual_basic, list) and all(x is None for x in const_visual_basic):
        logging.error('const_visual_basic is required.')
        return ['const_visual_basic is required.']
    if const_visual_basic is not None:

        request_parameters['const'] = const_visual_basic

    if continue_visual_basic is None or isinstance(continue_visual_basic, list) and all(x is None for x in continue_visual_basic):
        logging.error('continue_visual_basic is required.')
        return ['continue_visual_basic is required.']
    if continue_visual_basic is not None:

        request_parameters['continue'] = continue_visual_basic

    if csbyte_visual_basic is None or isinstance(csbyte_visual_basic, list) and all(x is None for x in csbyte_visual_basic):
        logging.error('csbyte_visual_basic is required.')
        return ['csbyte_visual_basic is required.']
    if csbyte_visual_basic is not None:

        request_parameters['csbyte'] = csbyte_visual_basic

    if cshort_visual_basic is None or isinstance(cshort_visual_basic, list) and all(x is None for x in cshort_visual_basic):
        logging.error('cshort_visual_basic is required.')
        return ['cshort_visual_basic is required.']
    if cshort_visual_basic is not None:

        request_parameters['cshort'] = cshort_visual_basic

    if csng_visual_basic is None or isinstance(csng_visual_basic, list) and all(x is None for x in csng_visual_basic):
        logging.error('csng_visual_basic is required.')
        return ['csng_visual_basic is required.']
    if csng_visual_basic is not None:

        request_parameters['csng'] = csng_visual_basic

    if cstr_visual_basic is None or isinstance(cstr_visual_basic, list) and all(x is None for x in cstr_visual_basic):
        logging.error('cstr_visual_basic is required.')
        return ['cstr_visual_basic is required.']
    if cstr_visual_basic is not None:

        request_parameters['cstr'] = cstr_visual_basic

    if ctype_visual_basic is None or isinstance(ctype_visual_basic, list) and all(x is None for x in ctype_visual_basic):
        logging.error('ctype_visual_basic is required.')
        return ['ctype_visual_basic is required.']
    if ctype_visual_basic is not None:

        request_parameters['ctype'] = ctype_visual_basic

    if cuint_visual_basic is None or isinstance(cuint_visual_basic, list) and all(x is None for x in cuint_visual_basic):
        logging.error('cuint_visual_basic is required.')
        return ['cuint_visual_basic is required.']
    if cuint_visual_basic is not None:

        request_parameters['cuint'] = cuint_visual_basic

    if culng_visual_basic is None or isinstance(culng_visual_basic, list) and all(x is None for x in culng_visual_basic):
        logging.error('culng_visual_basic is required.')
        return ['culng_visual_basic is required.']
    if culng_visual_basic is not None:

        request_parameters['culng'] = culng_visual_basic

    if currency_visual_basic is None or isinstance(currency_visual_basic, list) and all(x is None for x in currency_visual_basic):
        logging.error('currency_visual_basic is required.')
        return ['currency_visual_basic is required.']
    if currency_visual_basic is not None:

        request_parameters['currency'] = currency_visual_basic

    if cushort_visual_basic is None or isinstance(cushort_visual_basic, list) and all(x is None for x in cushort_visual_basic):
        logging.error('cushort_visual_basic is required.')
        return ['cushort_visual_basic is required.']
    if cushort_visual_basic is not None:

        request_parameters['cushort'] = cushort_visual_basic

    if date_visual_basic is None or isinstance(date_visual_basic, list) and all(x is None for x in date_visual_basic):
        logging.error('date_visual_basic is required.')
        return ['date_visual_basic is required.']
    if date_visual_basic is not None:

        request_parameters['date'] = date_visual_basic

    if decimal_visual_basic is None or isinstance(decimal_visual_basic, list) and all(x is None for x in decimal_visual_basic):
        logging.error('decimal_visual_basic is required.')
        return ['decimal_visual_basic is required.']
    if decimal_visual_basic is not None:

        request_parameters['decimal'] = decimal_visual_basic

    if declare_visual_basic is None or isinstance(declare_visual_basic, list) and all(x is None for x in declare_visual_basic):
        logging.error('declare_visual_basic is required.')
        return ['declare_visual_basic is required.']
    if declare_visual_basic is not None:

        request_parameters['declare'] = declare_visual_basic

    if default_visual_basic is None or isinstance(default_visual_basic, list) and all(x is None for x in default_visual_basic):
        logging.error('default_visual_basic is required.')
        return ['default_visual_basic is required.']
    if default_visual_basic is not None:

        request_parameters['default'] = default_visual_basic

    if delegate_visual_basic is None or isinstance(delegate_visual_basic, list) and all(x is None for x in delegate_visual_basic):
        logging.error('delegate_visual_basic is required.')
        return ['delegate_visual_basic is required.']
    if delegate_visual_basic is not None:

        request_parameters['delegate'] = delegate_visual_basic

    if dim_visual_basic is None or isinstance(dim_visual_basic, list) and all(x is None for x in dim_visual_basic):
        logging.error('dim_visual_basic is required.')
        return ['dim_visual_basic is required.']
    if dim_visual_basic is not None:

        request_parameters['dim'] = dim_visual_basic

    if directcast_visual_basic is None or isinstance(directcast_visual_basic, list) and all(x is None for x in directcast_visual_basic):
        logging.error('directcast_visual_basic is required.')
        return ['directcast_visual_basic is required.']
    if directcast_visual_basic is not None:

        request_parameters['directcast'] = directcast_visual_basic

    if do_visual_basic is None or isinstance(do_visual_basic, list) and all(x is None for x in do_visual_basic):
        logging.error('do_visual_basic is required.')
        return ['do_visual_basic is required.']
    if do_visual_basic is not None:

        request_parameters['do'] = do_visual_basic

    if double_visual_basic is None or isinstance(double_visual_basic, list) and all(x is None for x in double_visual_basic):
        logging.error('double_visual_basic is required.')
        return ['double_visual_basic is required.']
    if double_visual_basic is not None:

        request_parameters['double'] = double_visual_basic

    if each_visual_basic is None or isinstance(each_visual_basic, list) and all(x is None for x in each_visual_basic):
        logging.error('each_visual_basic is required.')
        return ['each_visual_basic is required.']
    if each_visual_basic is not None:

        request_parameters['each'] = each_visual_basic

    if else_visual_basic is None or isinstance(else_visual_basic, list) and all(x is None for x in else_visual_basic):
        logging.error('else_visual_basic is required.')
        return ['else_visual_basic is required.']
    if else_visual_basic is not None:

        request_parameters['else'] = else_visual_basic

    if elseif_visual_basic is None or isinstance(elseif_visual_basic, list) and all(x is None for x in elseif_visual_basic):
        logging.error('elseif_visual_basic is required.')
        return ['elseif_visual_basic is required.']
    if elseif_visual_basic is not None:

        request_parameters['elseif'] = elseif_visual_basic

    if end_visual_basic is None or isinstance(end_visual_basic, list) and all(x is None for x in end_visual_basic):
        logging.error('end_visual_basic is required.')
        return ['end_visual_basic is required.']
    if end_visual_basic is not None:

        request_parameters['end'] = end_visual_basic

    if endif_visual_basic is None or isinstance(endif_visual_basic, list) and all(x is None for x in endif_visual_basic):
        logging.error('endif_visual_basic is required.')
        return ['endif_visual_basic is required.']
    if endif_visual_basic is not None:

        request_parameters['endif'] = endif_visual_basic

    if enum_visual_basic is None or isinstance(enum_visual_basic, list) and all(x is None for x in enum_visual_basic):
        logging.error('enum_visual_basic is required.')
        return ['enum_visual_basic is required.']
    if enum_visual_basic is not None:

        request_parameters['enum'] = enum_visual_basic

    if erase_visual_basic is None or isinstance(erase_visual_basic, list) and all(x is None for x in erase_visual_basic):
        logging.error('erase_visual_basic is required.')
        return ['erase_visual_basic is required.']
    if erase_visual_basic is not None:

        request_parameters['erase'] = erase_visual_basic

    if error_visual_basic is None or isinstance(error_visual_basic, list) and all(x is None for x in error_visual_basic):
        logging.error('error_visual_basic is required.')
        return ['error_visual_basic is required.']
    if error_visual_basic is not None:

        request_parameters['error'] = error_visual_basic

    if event_visual_basic is None or isinstance(event_visual_basic, list) and all(x is None for x in event_visual_basic):
        logging.error('event_visual_basic is required.')
        return ['event_visual_basic is required.']
    if event_visual_basic is not None:

        request_parameters['event'] = event_visual_basic

    if exit_visual_basic is None or isinstance(exit_visual_basic, list) and all(x is None for x in exit_visual_basic):
        logging.error('exit_visual_basic is required.')
        return ['exit_visual_basic is required.']
    if exit_visual_basic is not None:

        request_parameters['exit'] = exit_visual_basic

    if finally_visual_basic is None or isinstance(finally_visual_basic, list) and all(x is None for x in finally_visual_basic):
        logging.error('finally_visual_basic is required.')
        return ['finally_visual_basic is required.']
    if finally_visual_basic is not None:

        request_parameters['finally'] = finally_visual_basic

    if for_visual_basic is None or isinstance(for_visual_basic, list) and all(x is None for x in for_visual_basic):
        logging.error('for_visual_basic is required.')
        return ['for_visual_basic is required.']
    if for_visual_basic is not None:

        request_parameters['for'] = for_visual_basic

    if friend_visual_basic is None or isinstance(friend_visual_basic, list) and all(x is None for x in friend_visual_basic):
        logging.error('friend_visual_basic is required.')
        return ['friend_visual_basic is required.']
    if friend_visual_basic is not None:

        request_parameters['friend'] = friend_visual_basic

    if function_visual_basic is None or isinstance(function_visual_basic, list) and all(x is None for x in function_visual_basic):
        logging.error('function_visual_basic is required.')
        return ['function_visual_basic is required.']
    if function_visual_basic is not None:

        request_parameters['function'] = function_visual_basic

    if get_visual_basic is None or isinstance(get_visual_basic, list) and all(x is None for x in get_visual_basic):
        logging.error('get_visual_basic is required.')
        return ['get_visual_basic is required.']
    if get_visual_basic is not None:

        request_parameters['get'] = get_visual_basic

    if gettype_visual_basic is None or isinstance(gettype_visual_basic, list) and all(x is None for x in gettype_visual_basic):
        logging.error('gettype_visual_basic is required.')
        return ['gettype_visual_basic is required.']
    if gettype_visual_basic is not None:

        request_parameters['gettype'] = gettype_visual_basic

    if getxmlnamespace_visual_basic is None or isinstance(getxmlnamespace_visual_basic, list) and all(x is None for x in getxmlnamespace_visual_basic):
        logging.error('getxmlnamespace_visual_basic is required.')
        return ['getxmlnamespace_visual_basic is required.']
    if getxmlnamespace_visual_basic is not None:

        request_parameters['getxmlnamespace'] = getxmlnamespace_visual_basic

    if global_visual_basic is None or isinstance(global_visual_basic, list) and all(x is None for x in global_visual_basic):
        logging.error('global_visual_basic is required.')
        return ['global_visual_basic is required.']
    if global_visual_basic is not None:

        request_parameters['global'] = global_visual_basic

    if gosub_visual_basic is None or isinstance(gosub_visual_basic, list) and all(x is None for x in gosub_visual_basic):
        logging.error('gosub_visual_basic is required.')
        return ['gosub_visual_basic is required.']
    if gosub_visual_basic is not None:

        request_parameters['gosub'] = gosub_visual_basic

    if goto_visual_basic is None or isinstance(goto_visual_basic, list) and all(x is None for x in goto_visual_basic):
        logging.error('goto_visual_basic is required.')
        return ['goto_visual_basic is required.']
    if goto_visual_basic is not None:

        request_parameters['goto'] = goto_visual_basic

    if handles_visual_basic is None or isinstance(handles_visual_basic, list) and all(x is None for x in handles_visual_basic):
        logging.error('handles_visual_basic is required.')
        return ['handles_visual_basic is required.']
    if handles_visual_basic is not None:

        request_parameters['handles'] = handles_visual_basic

    if if_visual_basic is None or isinstance(if_visual_basic, list) and all(x is None for x in if_visual_basic):
        logging.error('if_visual_basic is required.')
        return ['if_visual_basic is required.']
    if if_visual_basic is not None:

        request_parameters['if'] = if_visual_basic

    if implements_visual_basic is None or isinstance(implements_visual_basic, list) and all(x is None for x in implements_visual_basic):
        logging.error('implements_visual_basic is required.')
        return ['implements_visual_basic is required.']
    if implements_visual_basic is not None:

        request_parameters['implements'] = implements_visual_basic

    if imports_visual_basic is None or isinstance(imports_visual_basic, list) and all(x is None for x in imports_visual_basic):
        logging.error('imports_visual_basic is required.')
        return ['imports_visual_basic is required.']
    if imports_visual_basic is not None:

        request_parameters['imports'] = imports_visual_basic

    if in_visual_basic is None or isinstance(in_visual_basic, list) and all(x is None for x in in_visual_basic):
        logging.error('in_visual_basic is required.')
        return ['in_visual_basic is required.']
    if in_visual_basic is not None:

        request_parameters['in'] = in_visual_basic

    if inherits_visual_basic is None or isinstance(inherits_visual_basic, list) and all(x is None for x in inherits_visual_basic):
        logging.error('inherits_visual_basic is required.')
        return ['inherits_visual_basic is required.']
    if inherits_visual_basic is not None:

        request_parameters['inherits'] = inherits_visual_basic

    if integer_visual_basic is None or isinstance(integer_visual_basic, list) and all(x is None for x in integer_visual_basic):
        logging.error('integer_visual_basic is required.')
        return ['integer_visual_basic is required.']
    if integer_visual_basic is not None:

        request_parameters['integer'] = integer_visual_basic

    if interface_visual_basic is None or isinstance(interface_visual_basic, list) and all(x is None for x in interface_visual_basic):
        logging.error('interface_visual_basic is required.')
        return ['interface_visual_basic is required.']
    if interface_visual_basic is not None:

        request_parameters['interface'] = interface_visual_basic

    if is_visual_basic is None or isinstance(is_visual_basic, list) and all(x is None for x in is_visual_basic):
        logging.error('is_visual_basic is required.')
        return ['is_visual_basic is required.']
    if is_visual_basic is not None:

        request_parameters['is'] = is_visual_basic

    if isnot_visual_basic is None or isinstance(isnot_visual_basic, list) and all(x is None for x in isnot_visual_basic):
        logging.error('isnot_visual_basic is required.')
        return ['isnot_visual_basic is required.']
    if isnot_visual_basic is not None:

        request_parameters['isnot'] = isnot_visual_basic

    if let_visual_basic is None or isinstance(let_visual_basic, list) and all(x is None for x in let_visual_basic):
        logging.error('let_visual_basic is required.')
        return ['let_visual_basic is required.']
    if let_visual_basic is not None:

        request_parameters['let'] = let_visual_basic

    if lib_visual_basic is None or isinstance(lib_visual_basic, list) and all(x is None for x in lib_visual_basic):
        logging.error('lib_visual_basic is required.')
        return ['lib_visual_basic is required.']
    if lib_visual_basic is not None:

        request_parameters['lib'] = lib_visual_basic

    if like_visual_basic is None or isinstance(like_visual_basic, list) and all(x is None for x in like_visual_basic):
        logging.error('like_visual_basic is required.')
        return ['like_visual_basic is required.']
    if like_visual_basic is not None:

        request_parameters['like'] = like_visual_basic

    if long_visual_basic is None or isinstance(long_visual_basic, list) and all(x is None for x in long_visual_basic):
        logging.error('long_visual_basic is required.')
        return ['long_visual_basic is required.']
    if long_visual_basic is not None:

        request_parameters['long'] = long_visual_basic

    if loop_visual_basic is None or isinstance(loop_visual_basic, list) and all(x is None for x in loop_visual_basic):
        logging.error('loop_visual_basic is required.')
        return ['loop_visual_basic is required.']
    if loop_visual_basic is not None:

        request_parameters['loop'] = loop_visual_basic

    if me_visual_basic is None or isinstance(me_visual_basic, list) and all(x is None for x in me_visual_basic):
        logging.error('me_visual_basic is required.')
        return ['me_visual_basic is required.']
    if me_visual_basic is not None:

        request_parameters['me'] = me_visual_basic

    if mod_visual_basic is None or isinstance(mod_visual_basic, list) and all(x is None for x in mod_visual_basic):
        logging.error('mod_visual_basic is required.')
        return ['mod_visual_basic is required.']
    if mod_visual_basic is not None:

        request_parameters['mod'] = mod_visual_basic

    if module_visual_basic is None or isinstance(module_visual_basic, list) and all(x is None for x in module_visual_basic):
        logging.error('module_visual_basic is required.')
        return ['module_visual_basic is required.']
    if module_visual_basic is not None:

        request_parameters['module'] = module_visual_basic

    if mustinherit_visual_basic is None or isinstance(mustinherit_visual_basic, list) and all(x is None for x in mustinherit_visual_basic):
        logging.error('mustinherit_visual_basic is required.')
        return ['mustinherit_visual_basic is required.']
    if mustinherit_visual_basic is not None:

        request_parameters['mustinherit'] = mustinherit_visual_basic

    if mustoverride_visual_basic is None or isinstance(mustoverride_visual_basic, list) and all(x is None for x in mustoverride_visual_basic):
        logging.error('mustoverride_visual_basic is required.')
        return ['mustoverride_visual_basic is required.']
    if mustoverride_visual_basic is not None:

        request_parameters['mustoverride'] = mustoverride_visual_basic

    if mybase_visual_basic is None or isinstance(mybase_visual_basic, list) and all(x is None for x in mybase_visual_basic):
        logging.error('mybase_visual_basic is required.')
        return ['mybase_visual_basic is required.']
    if mybase_visual_basic is not None:

        request_parameters['mybase'] = mybase_visual_basic

    if myclass_visual_basic is None or isinstance(myclass_visual_basic, list) and all(x is None for x in myclass_visual_basic):
        logging.error('myclass_visual_basic is required.')
        return ['myclass_visual_basic is required.']
    if myclass_visual_basic is not None:

        request_parameters['myclass'] = myclass_visual_basic

    if namespace_visual_basic is None or isinstance(namespace_visual_basic, list) and all(x is None for x in namespace_visual_basic):
        logging.error('namespace_visual_basic is required.')
        return ['namespace_visual_basic is required.']
    if namespace_visual_basic is not None:

        request_parameters['namespace'] = namespace_visual_basic

    if narrowing_visual_basic is None or isinstance(narrowing_visual_basic, list) and all(x is None for x in narrowing_visual_basic):
        logging.error('narrowing_visual_basic is required.')
        return ['narrowing_visual_basic is required.']
    if narrowing_visual_basic is not None:

        request_parameters['narrowing'] = narrowing_visual_basic

    if new_visual_basic is None or isinstance(new_visual_basic, list) and all(x is None for x in new_visual_basic):
        logging.error('new_visual_basic is required.')
        return ['new_visual_basic is required.']
    if new_visual_basic is not None:

        request_parameters['new'] = new_visual_basic

    if next_visual_basic is None or isinstance(next_visual_basic, list) and all(x is None for x in next_visual_basic):
        logging.error('next_visual_basic is required.')
        return ['next_visual_basic is required.']
    if next_visual_basic is not None:

        request_parameters['next'] = next_visual_basic

    if not_visual_basic is None or isinstance(not_visual_basic, list) and all(x is None for x in not_visual_basic):
        logging.error('not_visual_basic is required.')
        return ['not_visual_basic is required.']
    if not_visual_basic is not None:

        request_parameters['not'] = not_visual_basic

    if nothing_visual_basic is None or isinstance(nothing_visual_basic, list) and all(x is None for x in nothing_visual_basic):
        logging.error('nothing_visual_basic is required.')
        return ['nothing_visual_basic is required.']
    if nothing_visual_basic is not None:

        request_parameters['nothing'] = nothing_visual_basic

    if notinheritable_visual_basic is None or isinstance(notinheritable_visual_basic, list) and all(x is None for x in notinheritable_visual_basic):
        logging.error('notinheritable_visual_basic is required.')
        return ['notinheritable_visual_basic is required.']
    if notinheritable_visual_basic is not None:

        request_parameters['notinheritable'] = notinheritable_visual_basic

    if notoverridable_visual_basic is None or isinstance(notoverridable_visual_basic, list) and all(x is None for x in notoverridable_visual_basic):
        logging.error('notoverridable_visual_basic is required.')
        return ['notoverridable_visual_basic is required.']
    if notoverridable_visual_basic is not None:

        request_parameters['notoverridable'] = notoverridable_visual_basic

    if object_visual_basic is None or isinstance(object_visual_basic, list) and all(x is None for x in object_visual_basic):
        logging.error('object_visual_basic is required.')
        return ['object_visual_basic is required.']
    if object_visual_basic is not None:

        request_parameters['object'] = object_visual_basic

    if of_visual_basic is None or isinstance(of_visual_basic, list) and all(x is None for x in of_visual_basic):
        logging.error('of_visual_basic is required.')
        return ['of_visual_basic is required.']
    if of_visual_basic is not None:

        request_parameters['of'] = of_visual_basic

    if on_visual_basic is None or isinstance(on_visual_basic, list) and all(x is None for x in on_visual_basic):
        logging.error('on_visual_basic is required.')
        return ['on_visual_basic is required.']
    if on_visual_basic is not None:

        request_parameters['on'] = on_visual_basic

    if operator_visual_basic is None or isinstance(operator_visual_basic, list) and all(x is None for x in operator_visual_basic):
        logging.error('operator_visual_basic is required.')
        return ['operator_visual_basic is required.']
    if operator_visual_basic is not None:

        request_parameters['operator'] = operator_visual_basic

    if option_visual_basic is None or isinstance(option_visual_basic, list) and all(x is None for x in option_visual_basic):
        logging.error('option_visual_basic is required.')
        return ['option_visual_basic is required.']
    if option_visual_basic is not None:

        request_parameters['option'] = option_visual_basic

    if optional_visual_basic is None or isinstance(optional_visual_basic, list) and all(x is None for x in optional_visual_basic):
        logging.error('optional_visual_basic is required.')
        return ['optional_visual_basic is required.']
    if optional_visual_basic is not None:

        request_parameters['optional'] = optional_visual_basic

    if or_visual_basic is None or isinstance(or_visual_basic, list) and all(x is None for x in or_visual_basic):
        logging.error('or_visual_basic is required.')
        return ['or_visual_basic is required.']
    if or_visual_basic is not None:

        request_parameters['or'] = or_visual_basic

    if orelse_visual_basic is None or isinstance(orelse_visual_basic, list) and all(x is None for x in orelse_visual_basic):
        logging.error('orelse_visual_basic is required.')
        return ['orelse_visual_basic is required.']
    if orelse_visual_basic is not None:

        request_parameters['orelse'] = orelse_visual_basic

    if overloads_visual_basic is None or isinstance(overloads_visual_basic, list) and all(x is None for x in overloads_visual_basic):
        logging.error('overloads_visual_basic is required.')
        return ['overloads_visual_basic is required.']
    if overloads_visual_basic is not None:

        request_parameters['overloads'] = overloads_visual_basic

    if overridable_visual_basic is None or isinstance(overridable_visual_basic, list) and all(x is None for x in overridable_visual_basic):
        logging.error('overridable_visual_basic is required.')
        return ['overridable_visual_basic is required.']
    if overridable_visual_basic is not None:

        request_parameters['overridable'] = overridable_visual_basic

    if overrides_visual_basic is None or isinstance(overrides_visual_basic, list) and all(x is None for x in overrides_visual_basic):
        logging.error('overrides_visual_basic is required.')
        return ['overrides_visual_basic is required.']
    if overrides_visual_basic is not None:

        request_parameters['overrides'] = overrides_visual_basic

    if paramarray_visual_basic is None or isinstance(paramarray_visual_basic, list) and all(x is None for x in paramarray_visual_basic):
        logging.error('paramarray_visual_basic is required.')
        return ['paramarray_visual_basic is required.']
    if paramarray_visual_basic is not None:

        request_parameters['paramarray'] = paramarray_visual_basic

    if partial_visual_basic is None or isinstance(partial_visual_basic, list) and all(x is None for x in partial_visual_basic):
        logging.error('partial_visual_basic is required.')
        return ['partial_visual_basic is required.']
    if partial_visual_basic is not None:

        request_parameters['partial'] = partial_visual_basic

    if private_visual_basic is None or isinstance(private_visual_basic, list) and all(x is None for x in private_visual_basic):
        logging.error('private_visual_basic is required.')
        return ['private_visual_basic is required.']
    if private_visual_basic is not None:

        request_parameters['private'] = private_visual_basic

    if property_visual_basic is None or isinstance(property_visual_basic, list) and all(x is None for x in property_visual_basic):
        logging.error('property_visual_basic is required.')
        return ['property_visual_basic is required.']
    if property_visual_basic is not None:

        request_parameters['property'] = property_visual_basic

    if protected_visual_basic is None or isinstance(protected_visual_basic, list) and all(x is None for x in protected_visual_basic):
        logging.error('protected_visual_basic is required.')
        return ['protected_visual_basic is required.']
    if protected_visual_basic is not None:

        request_parameters['protected'] = protected_visual_basic

    if public_visual_basic is None or isinstance(public_visual_basic, list) and all(x is None for x in public_visual_basic):
        logging.error('public_visual_basic is required.')
        return ['public_visual_basic is required.']
    if public_visual_basic is not None:

        request_parameters['public'] = public_visual_basic

    if raiseevent_visual_basic is None or isinstance(raiseevent_visual_basic, list) and all(x is None for x in raiseevent_visual_basic):
        logging.error('raiseevent_visual_basic is required.')
        return ['raiseevent_visual_basic is required.']
    if raiseevent_visual_basic is not None:

        request_parameters['raiseevent'] = raiseevent_visual_basic

    if readonly_visual_basic is None or isinstance(readonly_visual_basic, list) and all(x is None for x in readonly_visual_basic):
        logging.error('readonly_visual_basic is required.')
        return ['readonly_visual_basic is required.']
    if readonly_visual_basic is not None:

        request_parameters['readonly'] = readonly_visual_basic

    if redim_visual_basic is None or isinstance(redim_visual_basic, list) and all(x is None for x in redim_visual_basic):
        logging.error('redim_visual_basic is required.')
        return ['redim_visual_basic is required.']
    if redim_visual_basic is not None:

        request_parameters['redim'] = redim_visual_basic

    if rem_visual_basic is None or isinstance(rem_visual_basic, list) and all(x is None for x in rem_visual_basic):
        logging.error('rem_visual_basic is required.')
        return ['rem_visual_basic is required.']
    if rem_visual_basic is not None:

        request_parameters['rem'] = rem_visual_basic

    if removehandler_visual_basic is None or isinstance(removehandler_visual_basic, list) and all(x is None for x in removehandler_visual_basic):
        logging.error('removehandler_visual_basic is required.')
        return ['removehandler_visual_basic is required.']
    if removehandler_visual_basic is not None:

        request_parameters['removehandler'] = removehandler_visual_basic

    if resume_visual_basic is None or isinstance(resume_visual_basic, list) and all(x is None for x in resume_visual_basic):
        logging.error('resume_visual_basic is required.')
        return ['resume_visual_basic is required.']
    if resume_visual_basic is not None:

        request_parameters['resume'] = resume_visual_basic

    if return_visual_basic is None or isinstance(return_visual_basic, list) and all(x is None for x in return_visual_basic):
        logging.error('return_visual_basic is required.')
        return ['return_visual_basic is required.']
    if return_visual_basic is not None:

        request_parameters['return'] = return_visual_basic

    if sbyte_visual_basic is None or isinstance(sbyte_visual_basic, list) and all(x is None for x in sbyte_visual_basic):
        logging.error('sbyte_visual_basic is required.')
        return ['sbyte_visual_basic is required.']
    if sbyte_visual_basic is not None:

        request_parameters['sbyte'] = sbyte_visual_basic

    if select_visual_basic is None or isinstance(select_visual_basic, list) and all(x is None for x in select_visual_basic):
        logging.error('select_visual_basic is required.')
        return ['select_visual_basic is required.']
    if select_visual_basic is not None:

        request_parameters['select'] = select_visual_basic

    if set_visual_basic is None or isinstance(set_visual_basic, list) and all(x is None for x in set_visual_basic):
        logging.error('set_visual_basic is required.')
        return ['set_visual_basic is required.']
    if set_visual_basic is not None:

        request_parameters['set'] = set_visual_basic

    if shadows_visual_basic is None or isinstance(shadows_visual_basic, list) and all(x is None for x in shadows_visual_basic):
        logging.error('shadows_visual_basic is required.')
        return ['shadows_visual_basic is required.']
    if shadows_visual_basic is not None:

        request_parameters['shadows'] = shadows_visual_basic

    if shared_visual_basic is None or isinstance(shared_visual_basic, list) and all(x is None for x in shared_visual_basic):
        logging.error('shared_visual_basic is required.')
        return ['shared_visual_basic is required.']
    if shared_visual_basic is not None:

        request_parameters['shared'] = shared_visual_basic

    if short_visual_basic is None or isinstance(short_visual_basic, list) and all(x is None for x in short_visual_basic):
        logging.error('short_visual_basic is required.')
        return ['short_visual_basic is required.']
    if short_visual_basic is not None:

        request_parameters['short'] = short_visual_basic

    if single_visual_basic is None or isinstance(single_visual_basic, list) and all(x is None for x in single_visual_basic):
        logging.error('single_visual_basic is required.')
        return ['single_visual_basic is required.']
    if single_visual_basic is not None:

        request_parameters['single'] = single_visual_basic

    if static_visual_basic is None or isinstance(static_visual_basic, list) and all(x is None for x in static_visual_basic):
        logging.error('static_visual_basic is required.')
        return ['static_visual_basic is required.']
    if static_visual_basic is not None:

        request_parameters['static'] = static_visual_basic

    if step_visual_basic is None or isinstance(step_visual_basic, list) and all(x is None for x in step_visual_basic):
        logging.error('step_visual_basic is required.')
        return ['step_visual_basic is required.']
    if step_visual_basic is not None:

        request_parameters['step'] = step_visual_basic

    if stop_visual_basic is None or isinstance(stop_visual_basic, list) and all(x is None for x in stop_visual_basic):
        logging.error('stop_visual_basic is required.')
        return ['stop_visual_basic is required.']
    if stop_visual_basic is not None:

        request_parameters['stop'] = stop_visual_basic

    if string_visual_basic is None or isinstance(string_visual_basic, list) and all(x is None for x in string_visual_basic):
        logging.error('string_visual_basic is required.')
        return ['string_visual_basic is required.']
    if string_visual_basic is not None:

        request_parameters['string'] = string_visual_basic

    if structure_visual_basic is None or isinstance(structure_visual_basic, list) and all(x is None for x in structure_visual_basic):
        logging.error('structure_visual_basic is required.')
        return ['structure_visual_basic is required.']
    if structure_visual_basic is not None:

        request_parameters['structure'] = structure_visual_basic

    if sub_visual_basic is None or isinstance(sub_visual_basic, list) and all(x is None for x in sub_visual_basic):
        logging.error('sub_visual_basic is required.')
        return ['sub_visual_basic is required.']
    if sub_visual_basic is not None:

        request_parameters['sub'] = sub_visual_basic

    if synclock_visual_basic is None or isinstance(synclock_visual_basic, list) and all(x is None for x in synclock_visual_basic):
        logging.error('synclock_visual_basic is required.')
        return ['synclock_visual_basic is required.']
    if synclock_visual_basic is not None:

        request_parameters['synclock'] = synclock_visual_basic

    if then_visual_basic is None or isinstance(then_visual_basic, list) and all(x is None for x in then_visual_basic):
        logging.error('then_visual_basic is required.')
        return ['then_visual_basic is required.']
    if then_visual_basic is not None:

        request_parameters['then'] = then_visual_basic

    if throw_visual_basic is None or isinstance(throw_visual_basic, list) and all(x is None for x in throw_visual_basic):
        logging.error('throw_visual_basic is required.')
        return ['throw_visual_basic is required.']
    if throw_visual_basic is not None:

        request_parameters['throw'] = throw_visual_basic

    if to_visual_basic is None or isinstance(to_visual_basic, list) and all(x is None for x in to_visual_basic):
        logging.error('to_visual_basic is required.')
        return ['to_visual_basic is required.']
    if to_visual_basic is not None:

        request_parameters['to'] = to_visual_basic

    if try_visual_basic is None or isinstance(try_visual_basic, list) and all(x is None for x in try_visual_basic):
        logging.error('try_visual_basic is required.')
        return ['try_visual_basic is required.']
    if try_visual_basic is not None:

        request_parameters['try'] = try_visual_basic

    if trycast_visual_basic is None or isinstance(trycast_visual_basic, list) and all(x is None for x in trycast_visual_basic):
        logging.error('trycast_visual_basic is required.')
        return ['trycast_visual_basic is required.']
    if trycast_visual_basic is not None:

        request_parameters['trycast'] = trycast_visual_basic

    if type_visual_basic is None or isinstance(type_visual_basic, list) and all(x is None for x in type_visual_basic):
        logging.error('type_visual_basic is required.')
        return ['type_visual_basic is required.']
    if type_visual_basic is not None:

        request_parameters['type'] = type_visual_basic

    if typeof_visual_basic is None or isinstance(typeof_visual_basic, list) and all(x is None for x in typeof_visual_basic):
        logging.error('typeof_visual_basic is required.')
        return ['typeof_visual_basic is required.']
    if typeof_visual_basic is not None:

        request_parameters['typeof'] = typeof_visual_basic

    if uinteger_visual_basic is None or isinstance(uinteger_visual_basic, list) and all(x is None for x in uinteger_visual_basic):
        logging.error('uinteger_visual_basic is required.')
        return ['uinteger_visual_basic is required.']
    if uinteger_visual_basic is not None:

        request_parameters['uinteger'] = uinteger_visual_basic

    if ulong_visual_basic is None or isinstance(ulong_visual_basic, list) and all(x is None for x in ulong_visual_basic):
        logging.error('ulong_visual_basic is required.')
        return ['ulong_visual_basic is required.']
    if ulong_visual_basic is not None:

        request_parameters['ulong'] = ulong_visual_basic

    if ushort_visual_basic is None or isinstance(ushort_visual_basic, list) and all(x is None for x in ushort_visual_basic):
        logging.error('ushort_visual_basic is required.')
        return ['ushort_visual_basic is required.']
    if ushort_visual_basic is not None:

        request_parameters['ushort'] = ushort_visual_basic

    if using_visual_basic is None or isinstance(using_visual_basic, list) and all(x is None for x in using_visual_basic):
        logging.error('using_visual_basic is required.')
        return ['using_visual_basic is required.']
    if using_visual_basic is not None:

        request_parameters['using'] = using_visual_basic

    if variant_visual_basic is None or isinstance(variant_visual_basic, list) and all(x is None for x in variant_visual_basic):
        logging.error('variant_visual_basic is required.')
        return ['variant_visual_basic is required.']
    if variant_visual_basic is not None:

        request_parameters['variant'] = variant_visual_basic

    if wend_visual_basic is None or isinstance(wend_visual_basic, list) and all(x is None for x in wend_visual_basic):
        logging.error('wend_visual_basic is required.')
        return ['wend_visual_basic is required.']
    if wend_visual_basic is not None:

        request_parameters['wend'] = wend_visual_basic

    if when_visual_basic is None or isinstance(when_visual_basic, list) and all(x is None for x in when_visual_basic):
        logging.error('when_visual_basic is required.')
        return ['when_visual_basic is required.']
    if when_visual_basic is not None:

        request_parameters['when'] = when_visual_basic

    if while_visual_basic is None or isinstance(while_visual_basic, list) and all(x is None for x in while_visual_basic):
        logging.error('while_visual_basic is required.')
        return ['while_visual_basic is required.']
    if while_visual_basic is not None:

        request_parameters['while'] = while_visual_basic

    if widening_visual_basic is None or isinstance(widening_visual_basic, list) and all(x is None for x in widening_visual_basic):
        logging.error('widening_visual_basic is required.')
        return ['widening_visual_basic is required.']
    if widening_visual_basic is not None:

        request_parameters['widening'] = widening_visual_basic

    if with_visual_basic is None or isinstance(with_visual_basic, list) and all(x is None for x in with_visual_basic):
        logging.error('with_visual_basic is required.')
        return ['with_visual_basic is required.']
    if with_visual_basic is not None:

        request_parameters['with'] = with_visual_basic

    if withevents_visual_basic is None or isinstance(withevents_visual_basic, list) and all(x is None for x in withevents_visual_basic):
        logging.error('withevents_visual_basic is required.')
        return ['withevents_visual_basic is required.']
    if withevents_visual_basic is not None:

        request_parameters['withevents'] = withevents_visual_basic

    if writeonly_visual_basic is None or isinstance(writeonly_visual_basic, list) and all(x is None for x in writeonly_visual_basic):
        logging.error('writeonly_visual_basic is required.')
        return ['writeonly_visual_basic is required.']
    if writeonly_visual_basic is not None:

        request_parameters['writeonly'] = writeonly_visual_basic

    if xor_visual_basic is None or isinstance(xor_visual_basic, list) and all(x is None for x in xor_visual_basic):
        logging.error('xor_visual_basic is required.')
        return ['xor_visual_basic is required.']
    if xor_visual_basic is not None:

        request_parameters['xor'] = xor_visual_basic


    response = None
    try:
        response = requests.put('http://localhost:8949/test/vba/restricted/keywords'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for vba_keywords_test_put_test_vba_restricted_keywords ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/VBAKeywords'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('VBAKeywords', OrderedDict([('properties', OrderedDict([('addhandler', OrderedDict()), ('addressof', OrderedDict()), ('alias', OrderedDict()), ('and', OrderedDict()), ('andalso', OrderedDict()), ('as', OrderedDict()), ('boolean', OrderedDict()), ('byref', OrderedDict()), ('byte', OrderedDict()), ('byval', OrderedDict()), ('call', OrderedDict()), ('case', OrderedDict()), ('catch', OrderedDict()), ('cbool', OrderedDict()), ('cbyte', OrderedDict()), ('cchar', OrderedDict()), ('cdate', OrderedDict()), ('cdbl', OrderedDict()), ('cdec', OrderedDict()), ('char', OrderedDict()), ('cint', OrderedDict()), ('class', OrderedDict()), ('clng', OrderedDict()), ('cobj', OrderedDict()), ('const', OrderedDict()), ('continue', OrderedDict()), ('csbyte', OrderedDict()), ('cshort', OrderedDict()), ('csng', OrderedDict()), ('cstr', OrderedDict()), ('ctype', OrderedDict()), ('cuint', OrderedDict()), ('culng', OrderedDict()), ('currency', OrderedDict()), ('cushort', OrderedDict()), ('date', OrderedDict()), ('decimal', OrderedDict()), ('declare', OrderedDict()), ('default', OrderedDict()), ('delegate', OrderedDict()), ('dim', OrderedDict()), ('directcast', OrderedDict()), ('do', OrderedDict()), ('double', OrderedDict()), ('each', OrderedDict()), ('else', OrderedDict()), ('elseif', OrderedDict()), ('end', OrderedDict()), ('endif', OrderedDict()), ('enum', OrderedDict()), ('erase', OrderedDict()), ('error', OrderedDict()), ('event', OrderedDict()), ('exit', OrderedDict()), ('finally', OrderedDict()), ('for', OrderedDict()), ('friend', OrderedDict()), ('function', OrderedDict()), ('get', OrderedDict()), ('gettype', OrderedDict()), ('getxmlnamespace', OrderedDict()), ('global', OrderedDict()), ('gosub', OrderedDict()), ('goto', OrderedDict()), ('handles', OrderedDict()), ('if', OrderedDict()), ('implements', OrderedDict()), ('imports', OrderedDict()), ('in', OrderedDict()), ('inherits', OrderedDict()), ('integer', OrderedDict()), ('interface', OrderedDict()), ('is', OrderedDict()), ('isnot', OrderedDict()), ('let', OrderedDict()), ('lib', OrderedDict()), ('like', OrderedDict()), ('long', OrderedDict()), ('loop', OrderedDict()), ('me', OrderedDict()), ('mod', OrderedDict()), ('module', OrderedDict()), ('mustinherit', OrderedDict()), ('mustoverride', OrderedDict()), ('mybase', OrderedDict()), ('myclass', OrderedDict()), ('namespace', OrderedDict()), ('narrowing', OrderedDict()), ('new', OrderedDict()), ('next', OrderedDict()), ('not', OrderedDict()), ('nothing', OrderedDict()), ('notinheritable', OrderedDict()), ('notoverridable', OrderedDict()), ('object', OrderedDict()), ('of', OrderedDict()), ('on', OrderedDict()), ('operator', OrderedDict()), ('option', OrderedDict()), ('optional', OrderedDict()), ('or', OrderedDict()), ('orelse', OrderedDict()), ('overloads', OrderedDict()), ('overridable', OrderedDict()), ('overrides', OrderedDict()), ('paramarray', OrderedDict()), ('partial', OrderedDict()), ('private', OrderedDict()), ('property', OrderedDict()), ('protected', OrderedDict()), ('public', OrderedDict()), ('raiseevent', OrderedDict()), ('readonly', OrderedDict()), ('redim', OrderedDict()), ('rem', OrderedDict()), ('removehandler', OrderedDict()), ('resume', OrderedDict()), ('return', OrderedDict()), ('sbyte', OrderedDict()), ('select', OrderedDict()), ('set', OrderedDict()), ('shadows', OrderedDict()), ('shared', OrderedDict()), ('short', OrderedDict()), ('single', OrderedDict()), ('static', OrderedDict()), ('step', OrderedDict()), ('stop', OrderedDict()), ('string', OrderedDict()), ('structure', OrderedDict()), ('sub', OrderedDict()), ('synclock', OrderedDict()), ('then', OrderedDict()), ('throw', OrderedDict()), ('to', OrderedDict()), ('try', OrderedDict()), ('trycast', OrderedDict()), ('type', OrderedDict()), ('typeof', OrderedDict()), ('uinteger', OrderedDict()), ('ulong', OrderedDict()), ('ushort', OrderedDict()), ('using', OrderedDict()), ('variant', OrderedDict()), ('wend', OrderedDict()), ('when', OrderedDict()), ('while', OrderedDict()), ('widening', OrderedDict()), ('with', OrderedDict()), ('withevents', OrderedDict()), ('writeonly', OrderedDict()), ('xor', OrderedDict())]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling vba_keywords_test_put_test_vba_restricted_keywords.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling vba_keywords_test_put_test_vba_restricted_keywords response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling vba_keywords_test_put_test_vba_restricted_keywords.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='vba_keywords_test', call_in_wizard=False)
@xw.arg('addhandler_visual_basic', doc='')
@xw.arg('addressof_visual_basic', doc='')
@xw.arg('alias_visual_basic', doc='')
@xw.arg('and_visual_basic', doc='')
@xw.arg('andalso_visual_basic', doc='')
@xw.arg('as_visual_basic', doc='')
@xw.arg('boolean_visual_basic', doc='')
@xw.arg('byref_visual_basic', doc='')
@xw.arg('byte_visual_basic', doc='')
@xw.arg('byval_visual_basic', doc='')
@xw.arg('call_visual_basic', doc='')
@xw.arg('case_visual_basic', doc='')
@xw.arg('catch_visual_basic', doc='')
@xw.arg('cbool_visual_basic', doc='')
@xw.arg('cbyte_visual_basic', doc='')
@xw.arg('cchar_visual_basic', doc='')
@xw.arg('cdate_visual_basic', doc='')
@xw.arg('cdbl_visual_basic', doc='')
@xw.arg('cdec_visual_basic', doc='')
@xw.arg('char_visual_basic', doc='')
@xw.arg('cint_visual_basic', doc='')
@xw.arg('class_visual_basic', doc='')
@xw.arg('clng_visual_basic', doc='')
@xw.arg('cobj_visual_basic', doc='')
@xw.arg('const_visual_basic', doc='')
@xw.arg('continue_visual_basic', doc='')
@xw.arg('csbyte_visual_basic', doc='')
@xw.arg('cshort_visual_basic', doc='')
@xw.arg('csng_visual_basic', doc='')
@xw.arg('cstr_visual_basic', doc='')
@xw.arg('ctype_visual_basic', doc='')
@xw.arg('cuint_visual_basic', doc='')
@xw.arg('culng_visual_basic', doc='')
@xw.arg('currency_visual_basic', doc='')
@xw.arg('cushort_visual_basic', doc='')
@xw.arg('date_visual_basic', doc='')
@xw.arg('decimal_visual_basic', doc='')
@xw.arg('declare_visual_basic', doc='')
@xw.arg('default_visual_basic', doc='')
@xw.arg('delegate_visual_basic', doc='')
@xw.arg('dim_visual_basic', doc='')
@xw.arg('directcast_visual_basic', doc='')
@xw.arg('do_visual_basic', doc='')
@xw.arg('double_visual_basic', doc='')
@xw.arg('each_visual_basic', doc='')
@xw.arg('else_visual_basic', doc='')
@xw.arg('elseif_visual_basic', doc='')
@xw.arg('end_visual_basic', doc='')
@xw.arg('endif_visual_basic', doc='')
@xw.arg('enum_visual_basic', doc='')
@xw.arg('erase_visual_basic', doc='')
@xw.arg('error_visual_basic', doc='')
@xw.arg('event_visual_basic', doc='')
@xw.arg('exit_visual_basic', doc='')
@xw.arg('finally_visual_basic', doc='')
@xw.arg('for_visual_basic', doc='')
@xw.arg('friend_visual_basic', doc='')
@xw.arg('function_visual_basic', doc='')
@xw.arg('get_visual_basic', doc='')
@xw.arg('gettype_visual_basic', doc='')
@xw.arg('getxmlnamespace_visual_basic', doc='')
@xw.arg('global_visual_basic', doc='')
@xw.arg('gosub_visual_basic', doc='')
@xw.arg('goto_visual_basic', doc='')
@xw.arg('handles_visual_basic', doc='')
@xw.arg('if_visual_basic', doc='')
@xw.arg('implements_visual_basic', doc='')
@xw.arg('imports_visual_basic', doc='')
@xw.arg('in_visual_basic', doc='')
@xw.arg('inherits_visual_basic', doc='')
@xw.arg('integer_visual_basic', doc='')
@xw.arg('interface_visual_basic', doc='')
@xw.arg('is_visual_basic', doc='')
@xw.arg('isnot_visual_basic', doc='')
@xw.arg('let_visual_basic', doc='')
@xw.arg('lib_visual_basic', doc='')
@xw.arg('like_visual_basic', doc='')
@xw.arg('long_visual_basic', doc='')
@xw.arg('loop_visual_basic', doc='')
@xw.arg('me_visual_basic', doc='')
@xw.arg('mod_visual_basic', doc='')
@xw.arg('module_visual_basic', doc='')
@xw.arg('mustinherit_visual_basic', doc='')
@xw.arg('mustoverride_visual_basic', doc='')
@xw.arg('mybase_visual_basic', doc='')
@xw.arg('myclass_visual_basic', doc='')
@xw.arg('namespace_visual_basic', doc='')
@xw.arg('narrowing_visual_basic', doc='')
@xw.arg('new_visual_basic', doc='')
@xw.arg('next_visual_basic', doc='')
@xw.arg('not_visual_basic', doc='')
@xw.arg('nothing_visual_basic', doc='')
@xw.arg('notinheritable_visual_basic', doc='')
@xw.arg('notoverridable_visual_basic', doc='')
@xw.arg('object_visual_basic', doc='')
@xw.arg('of_visual_basic', doc='')
@xw.arg('on_visual_basic', doc='')
@xw.arg('operator_visual_basic', doc='')
@xw.arg('option_visual_basic', doc='')
@xw.arg('optional_visual_basic', doc='')
@xw.arg('or_visual_basic', doc='')
@xw.arg('orelse_visual_basic', doc='')
@xw.arg('overloads_visual_basic', doc='')
@xw.arg('overridable_visual_basic', doc='')
@xw.arg('overrides_visual_basic', doc='')
@xw.arg('paramarray_visual_basic', doc='')
@xw.arg('partial_visual_basic', doc='')
@xw.arg('private_visual_basic', doc='')
@xw.arg('property_visual_basic', doc='')
@xw.arg('protected_visual_basic', doc='')
@xw.arg('public_visual_basic', doc='')
@xw.arg('raiseevent_visual_basic', doc='')
@xw.arg('readonly_visual_basic', doc='')
@xw.arg('redim_visual_basic', doc='')
@xw.arg('rem_visual_basic', doc='')
@xw.arg('removehandler_visual_basic', doc='')
@xw.arg('resume_visual_basic', doc='')
@xw.arg('return_visual_basic', doc='')
@xw.arg('sbyte_visual_basic', doc='')
@xw.arg('select_visual_basic', doc='')
@xw.arg('set_visual_basic', doc='')
@xw.arg('shadows_visual_basic', doc='')
@xw.arg('shared_visual_basic', doc='')
@xw.arg('short_visual_basic', doc='')
@xw.arg('single_visual_basic', doc='')
@xw.arg('static_visual_basic', doc='')
@xw.arg('step_visual_basic', doc='')
@xw.arg('stop_visual_basic', doc='')
@xw.arg('string_visual_basic', doc='')
@xw.arg('structure_visual_basic', doc='')
@xw.arg('sub_visual_basic', doc='')
@xw.arg('synclock_visual_basic', doc='')
@xw.arg('then_visual_basic', doc='')
@xw.arg('throw_visual_basic', doc='')
@xw.arg('to_visual_basic', doc='')
@xw.arg('try_visual_basic', doc='')
@xw.arg('trycast_visual_basic', doc='')
@xw.arg('type_visual_basic', doc='')
@xw.arg('typeof_visual_basic', doc='')
@xw.arg('uinteger_visual_basic', doc='')
@xw.arg('ulong_visual_basic', doc='')
@xw.arg('ushort_visual_basic', doc='')
@xw.arg('using_visual_basic', doc='')
@xw.arg('variant_visual_basic', doc='')
@xw.arg('wend_visual_basic', doc='')
@xw.arg('when_visual_basic', doc='')
@xw.arg('while_visual_basic', doc='')
@xw.arg('widening_visual_basic', doc='')
@xw.arg('with_visual_basic', doc='')
@xw.arg('withevents_visual_basic', doc='')
@xw.arg('writeonly_visual_basic', doc='')
@xw.arg('xor_visual_basic', doc='')
@xw.ret(expand='table')
def vba_keywords_test_delete_test_vba_restricted_keywords(addhandler_visual_basic, addressof_visual_basic, alias_visual_basic, and_visual_basic, andalso_visual_basic, as_visual_basic, boolean_visual_basic, byref_visual_basic, byte_visual_basic, byval_visual_basic, call_visual_basic, case_visual_basic, catch_visual_basic, cbool_visual_basic, cbyte_visual_basic, cchar_visual_basic, cdate_visual_basic, cdbl_visual_basic, cdec_visual_basic, char_visual_basic, cint_visual_basic, class_visual_basic, clng_visual_basic, cobj_visual_basic, const_visual_basic, continue_visual_basic, csbyte_visual_basic, cshort_visual_basic, csng_visual_basic, cstr_visual_basic, ctype_visual_basic, cuint_visual_basic, culng_visual_basic, currency_visual_basic, cushort_visual_basic, date_visual_basic, decimal_visual_basic, declare_visual_basic, default_visual_basic, delegate_visual_basic, dim_visual_basic, directcast_visual_basic, do_visual_basic, double_visual_basic, each_visual_basic, else_visual_basic, elseif_visual_basic, end_visual_basic, endif_visual_basic, enum_visual_basic, erase_visual_basic, error_visual_basic, event_visual_basic, exit_visual_basic, finally_visual_basic, for_visual_basic, friend_visual_basic, function_visual_basic, get_visual_basic, gettype_visual_basic, getxmlnamespace_visual_basic, global_visual_basic, gosub_visual_basic, goto_visual_basic, handles_visual_basic, if_visual_basic, implements_visual_basic, imports_visual_basic, in_visual_basic, inherits_visual_basic, integer_visual_basic, interface_visual_basic, is_visual_basic, isnot_visual_basic, let_visual_basic, lib_visual_basic, like_visual_basic, long_visual_basic, loop_visual_basic, me_visual_basic, mod_visual_basic, module_visual_basic, mustinherit_visual_basic, mustoverride_visual_basic, mybase_visual_basic, myclass_visual_basic, namespace_visual_basic, narrowing_visual_basic, new_visual_basic, next_visual_basic, not_visual_basic, nothing_visual_basic, notinheritable_visual_basic, notoverridable_visual_basic, object_visual_basic, of_visual_basic, on_visual_basic, operator_visual_basic, option_visual_basic, optional_visual_basic, or_visual_basic, orelse_visual_basic, overloads_visual_basic, overridable_visual_basic, overrides_visual_basic, paramarray_visual_basic, partial_visual_basic, private_visual_basic, property_visual_basic, protected_visual_basic, public_visual_basic, raiseevent_visual_basic, readonly_visual_basic, redim_visual_basic, rem_visual_basic, removehandler_visual_basic, resume_visual_basic, return_visual_basic, sbyte_visual_basic, select_visual_basic, set_visual_basic, shadows_visual_basic, shared_visual_basic, short_visual_basic, single_visual_basic, static_visual_basic, step_visual_basic, stop_visual_basic, string_visual_basic, structure_visual_basic, sub_visual_basic, synclock_visual_basic, then_visual_basic, throw_visual_basic, to_visual_basic, try_visual_basic, trycast_visual_basic, type_visual_basic, typeof_visual_basic, uinteger_visual_basic, ulong_visual_basic, ushort_visual_basic, using_visual_basic, variant_visual_basic, wend_visual_basic, when_visual_basic, while_visual_basic, widening_visual_basic, with_visual_basic, withevents_visual_basic, writeonly_visual_basic, xor_visual_basic):
    logging.info("Calling vba_keywords_test_delete_test_vba_restricted_keywords...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if addhandler_visual_basic is None or isinstance(addhandler_visual_basic, list) and all(x is None for x in addhandler_visual_basic):
        logging.error('addhandler_visual_basic is required.')
        return ['addhandler_visual_basic is required.']
    if addhandler_visual_basic is not None:

        request_parameters['addhandler'] = addhandler_visual_basic

    if addressof_visual_basic is None or isinstance(addressof_visual_basic, list) and all(x is None for x in addressof_visual_basic):
        logging.error('addressof_visual_basic is required.')
        return ['addressof_visual_basic is required.']
    if addressof_visual_basic is not None:

        request_parameters['addressof'] = addressof_visual_basic

    if alias_visual_basic is None or isinstance(alias_visual_basic, list) and all(x is None for x in alias_visual_basic):
        logging.error('alias_visual_basic is required.')
        return ['alias_visual_basic is required.']
    if alias_visual_basic is not None:

        request_parameters['alias'] = alias_visual_basic

    if and_visual_basic is None or isinstance(and_visual_basic, list) and all(x is None for x in and_visual_basic):
        logging.error('and_visual_basic is required.')
        return ['and_visual_basic is required.']
    if and_visual_basic is not None:

        request_parameters['and'] = and_visual_basic

    if andalso_visual_basic is None or isinstance(andalso_visual_basic, list) and all(x is None for x in andalso_visual_basic):
        logging.error('andalso_visual_basic is required.')
        return ['andalso_visual_basic is required.']
    if andalso_visual_basic is not None:

        request_parameters['andalso'] = andalso_visual_basic

    if as_visual_basic is None or isinstance(as_visual_basic, list) and all(x is None for x in as_visual_basic):
        logging.error('as_visual_basic is required.')
        return ['as_visual_basic is required.']
    if as_visual_basic is not None:

        request_parameters['as'] = as_visual_basic

    if boolean_visual_basic is None or isinstance(boolean_visual_basic, list) and all(x is None for x in boolean_visual_basic):
        logging.error('boolean_visual_basic is required.')
        return ['boolean_visual_basic is required.']
    if boolean_visual_basic is not None:

        request_parameters['boolean'] = boolean_visual_basic

    if byref_visual_basic is None or isinstance(byref_visual_basic, list) and all(x is None for x in byref_visual_basic):
        logging.error('byref_visual_basic is required.')
        return ['byref_visual_basic is required.']
    if byref_visual_basic is not None:

        request_parameters['byref'] = byref_visual_basic

    if byte_visual_basic is None or isinstance(byte_visual_basic, list) and all(x is None for x in byte_visual_basic):
        logging.error('byte_visual_basic is required.')
        return ['byte_visual_basic is required.']
    if byte_visual_basic is not None:

        request_parameters['byte'] = byte_visual_basic

    if byval_visual_basic is None or isinstance(byval_visual_basic, list) and all(x is None for x in byval_visual_basic):
        logging.error('byval_visual_basic is required.')
        return ['byval_visual_basic is required.']
    if byval_visual_basic is not None:

        request_parameters['byval'] = byval_visual_basic

    if call_visual_basic is None or isinstance(call_visual_basic, list) and all(x is None for x in call_visual_basic):
        logging.error('call_visual_basic is required.')
        return ['call_visual_basic is required.']
    if call_visual_basic is not None:

        request_parameters['call'] = call_visual_basic

    if case_visual_basic is None or isinstance(case_visual_basic, list) and all(x is None for x in case_visual_basic):
        logging.error('case_visual_basic is required.')
        return ['case_visual_basic is required.']
    if case_visual_basic is not None:

        request_parameters['case'] = case_visual_basic

    if catch_visual_basic is None or isinstance(catch_visual_basic, list) and all(x is None for x in catch_visual_basic):
        logging.error('catch_visual_basic is required.')
        return ['catch_visual_basic is required.']
    if catch_visual_basic is not None:

        request_parameters['catch'] = catch_visual_basic

    if cbool_visual_basic is None or isinstance(cbool_visual_basic, list) and all(x is None for x in cbool_visual_basic):
        logging.error('cbool_visual_basic is required.')
        return ['cbool_visual_basic is required.']
    if cbool_visual_basic is not None:

        request_parameters['cbool'] = cbool_visual_basic

    if cbyte_visual_basic is None or isinstance(cbyte_visual_basic, list) and all(x is None for x in cbyte_visual_basic):
        logging.error('cbyte_visual_basic is required.')
        return ['cbyte_visual_basic is required.']
    if cbyte_visual_basic is not None:

        request_parameters['cbyte'] = cbyte_visual_basic

    if cchar_visual_basic is None or isinstance(cchar_visual_basic, list) and all(x is None for x in cchar_visual_basic):
        logging.error('cchar_visual_basic is required.')
        return ['cchar_visual_basic is required.']
    if cchar_visual_basic is not None:

        request_parameters['cchar'] = cchar_visual_basic

    if cdate_visual_basic is None or isinstance(cdate_visual_basic, list) and all(x is None for x in cdate_visual_basic):
        logging.error('cdate_visual_basic is required.')
        return ['cdate_visual_basic is required.']
    if cdate_visual_basic is not None:

        request_parameters['cdate'] = cdate_visual_basic

    if cdbl_visual_basic is None or isinstance(cdbl_visual_basic, list) and all(x is None for x in cdbl_visual_basic):
        logging.error('cdbl_visual_basic is required.')
        return ['cdbl_visual_basic is required.']
    if cdbl_visual_basic is not None:

        request_parameters['cdbl'] = cdbl_visual_basic

    if cdec_visual_basic is None or isinstance(cdec_visual_basic, list) and all(x is None for x in cdec_visual_basic):
        logging.error('cdec_visual_basic is required.')
        return ['cdec_visual_basic is required.']
    if cdec_visual_basic is not None:

        request_parameters['cdec'] = cdec_visual_basic

    if char_visual_basic is None or isinstance(char_visual_basic, list) and all(x is None for x in char_visual_basic):
        logging.error('char_visual_basic is required.')
        return ['char_visual_basic is required.']
    if char_visual_basic is not None:

        request_parameters['char'] = char_visual_basic

    if cint_visual_basic is None or isinstance(cint_visual_basic, list) and all(x is None for x in cint_visual_basic):
        logging.error('cint_visual_basic is required.')
        return ['cint_visual_basic is required.']
    if cint_visual_basic is not None:

        request_parameters['cint'] = cint_visual_basic

    if class_visual_basic is None or isinstance(class_visual_basic, list) and all(x is None for x in class_visual_basic):
        logging.error('class_visual_basic is required.')
        return ['class_visual_basic is required.']
    if class_visual_basic is not None:

        request_parameters['class'] = class_visual_basic

    if clng_visual_basic is None or isinstance(clng_visual_basic, list) and all(x is None for x in clng_visual_basic):
        logging.error('clng_visual_basic is required.')
        return ['clng_visual_basic is required.']
    if clng_visual_basic is not None:

        request_parameters['clng'] = clng_visual_basic

    if cobj_visual_basic is None or isinstance(cobj_visual_basic, list) and all(x is None for x in cobj_visual_basic):
        logging.error('cobj_visual_basic is required.')
        return ['cobj_visual_basic is required.']
    if cobj_visual_basic is not None:

        request_parameters['cobj'] = cobj_visual_basic

    if const_visual_basic is None or isinstance(const_visual_basic, list) and all(x is None for x in const_visual_basic):
        logging.error('const_visual_basic is required.')
        return ['const_visual_basic is required.']
    if const_visual_basic is not None:

        request_parameters['const'] = const_visual_basic

    if continue_visual_basic is None or isinstance(continue_visual_basic, list) and all(x is None for x in continue_visual_basic):
        logging.error('continue_visual_basic is required.')
        return ['continue_visual_basic is required.']
    if continue_visual_basic is not None:

        request_parameters['continue'] = continue_visual_basic

    if csbyte_visual_basic is None or isinstance(csbyte_visual_basic, list) and all(x is None for x in csbyte_visual_basic):
        logging.error('csbyte_visual_basic is required.')
        return ['csbyte_visual_basic is required.']
    if csbyte_visual_basic is not None:

        request_parameters['csbyte'] = csbyte_visual_basic

    if cshort_visual_basic is None or isinstance(cshort_visual_basic, list) and all(x is None for x in cshort_visual_basic):
        logging.error('cshort_visual_basic is required.')
        return ['cshort_visual_basic is required.']
    if cshort_visual_basic is not None:

        request_parameters['cshort'] = cshort_visual_basic

    if csng_visual_basic is None or isinstance(csng_visual_basic, list) and all(x is None for x in csng_visual_basic):
        logging.error('csng_visual_basic is required.')
        return ['csng_visual_basic is required.']
    if csng_visual_basic is not None:

        request_parameters['csng'] = csng_visual_basic

    if cstr_visual_basic is None or isinstance(cstr_visual_basic, list) and all(x is None for x in cstr_visual_basic):
        logging.error('cstr_visual_basic is required.')
        return ['cstr_visual_basic is required.']
    if cstr_visual_basic is not None:

        request_parameters['cstr'] = cstr_visual_basic

    if ctype_visual_basic is None or isinstance(ctype_visual_basic, list) and all(x is None for x in ctype_visual_basic):
        logging.error('ctype_visual_basic is required.')
        return ['ctype_visual_basic is required.']
    if ctype_visual_basic is not None:

        request_parameters['ctype'] = ctype_visual_basic

    if cuint_visual_basic is None or isinstance(cuint_visual_basic, list) and all(x is None for x in cuint_visual_basic):
        logging.error('cuint_visual_basic is required.')
        return ['cuint_visual_basic is required.']
    if cuint_visual_basic is not None:

        request_parameters['cuint'] = cuint_visual_basic

    if culng_visual_basic is None or isinstance(culng_visual_basic, list) and all(x is None for x in culng_visual_basic):
        logging.error('culng_visual_basic is required.')
        return ['culng_visual_basic is required.']
    if culng_visual_basic is not None:

        request_parameters['culng'] = culng_visual_basic

    if currency_visual_basic is None or isinstance(currency_visual_basic, list) and all(x is None for x in currency_visual_basic):
        logging.error('currency_visual_basic is required.')
        return ['currency_visual_basic is required.']
    if currency_visual_basic is not None:

        request_parameters['currency'] = currency_visual_basic

    if cushort_visual_basic is None or isinstance(cushort_visual_basic, list) and all(x is None for x in cushort_visual_basic):
        logging.error('cushort_visual_basic is required.')
        return ['cushort_visual_basic is required.']
    if cushort_visual_basic is not None:

        request_parameters['cushort'] = cushort_visual_basic

    if date_visual_basic is None or isinstance(date_visual_basic, list) and all(x is None for x in date_visual_basic):
        logging.error('date_visual_basic is required.')
        return ['date_visual_basic is required.']
    if date_visual_basic is not None:

        request_parameters['date'] = date_visual_basic

    if decimal_visual_basic is None or isinstance(decimal_visual_basic, list) and all(x is None for x in decimal_visual_basic):
        logging.error('decimal_visual_basic is required.')
        return ['decimal_visual_basic is required.']
    if decimal_visual_basic is not None:

        request_parameters['decimal'] = decimal_visual_basic

    if declare_visual_basic is None or isinstance(declare_visual_basic, list) and all(x is None for x in declare_visual_basic):
        logging.error('declare_visual_basic is required.')
        return ['declare_visual_basic is required.']
    if declare_visual_basic is not None:

        request_parameters['declare'] = declare_visual_basic

    if default_visual_basic is None or isinstance(default_visual_basic, list) and all(x is None for x in default_visual_basic):
        logging.error('default_visual_basic is required.')
        return ['default_visual_basic is required.']
    if default_visual_basic is not None:

        request_parameters['default'] = default_visual_basic

    if delegate_visual_basic is None or isinstance(delegate_visual_basic, list) and all(x is None for x in delegate_visual_basic):
        logging.error('delegate_visual_basic is required.')
        return ['delegate_visual_basic is required.']
    if delegate_visual_basic is not None:

        request_parameters['delegate'] = delegate_visual_basic

    if dim_visual_basic is None or isinstance(dim_visual_basic, list) and all(x is None for x in dim_visual_basic):
        logging.error('dim_visual_basic is required.')
        return ['dim_visual_basic is required.']
    if dim_visual_basic is not None:

        request_parameters['dim'] = dim_visual_basic

    if directcast_visual_basic is None or isinstance(directcast_visual_basic, list) and all(x is None for x in directcast_visual_basic):
        logging.error('directcast_visual_basic is required.')
        return ['directcast_visual_basic is required.']
    if directcast_visual_basic is not None:

        request_parameters['directcast'] = directcast_visual_basic

    if do_visual_basic is None or isinstance(do_visual_basic, list) and all(x is None for x in do_visual_basic):
        logging.error('do_visual_basic is required.')
        return ['do_visual_basic is required.']
    if do_visual_basic is not None:

        request_parameters['do'] = do_visual_basic

    if double_visual_basic is None or isinstance(double_visual_basic, list) and all(x is None for x in double_visual_basic):
        logging.error('double_visual_basic is required.')
        return ['double_visual_basic is required.']
    if double_visual_basic is not None:

        request_parameters['double'] = double_visual_basic

    if each_visual_basic is None or isinstance(each_visual_basic, list) and all(x is None for x in each_visual_basic):
        logging.error('each_visual_basic is required.')
        return ['each_visual_basic is required.']
    if each_visual_basic is not None:

        request_parameters['each'] = each_visual_basic

    if else_visual_basic is None or isinstance(else_visual_basic, list) and all(x is None for x in else_visual_basic):
        logging.error('else_visual_basic is required.')
        return ['else_visual_basic is required.']
    if else_visual_basic is not None:

        request_parameters['else'] = else_visual_basic

    if elseif_visual_basic is None or isinstance(elseif_visual_basic, list) and all(x is None for x in elseif_visual_basic):
        logging.error('elseif_visual_basic is required.')
        return ['elseif_visual_basic is required.']
    if elseif_visual_basic is not None:

        request_parameters['elseif'] = elseif_visual_basic

    if end_visual_basic is None or isinstance(end_visual_basic, list) and all(x is None for x in end_visual_basic):
        logging.error('end_visual_basic is required.')
        return ['end_visual_basic is required.']
    if end_visual_basic is not None:

        request_parameters['end'] = end_visual_basic

    if endif_visual_basic is None or isinstance(endif_visual_basic, list) and all(x is None for x in endif_visual_basic):
        logging.error('endif_visual_basic is required.')
        return ['endif_visual_basic is required.']
    if endif_visual_basic is not None:

        request_parameters['endif'] = endif_visual_basic

    if enum_visual_basic is None or isinstance(enum_visual_basic, list) and all(x is None for x in enum_visual_basic):
        logging.error('enum_visual_basic is required.')
        return ['enum_visual_basic is required.']
    if enum_visual_basic is not None:

        request_parameters['enum'] = enum_visual_basic

    if erase_visual_basic is None or isinstance(erase_visual_basic, list) and all(x is None for x in erase_visual_basic):
        logging.error('erase_visual_basic is required.')
        return ['erase_visual_basic is required.']
    if erase_visual_basic is not None:

        request_parameters['erase'] = erase_visual_basic

    if error_visual_basic is None or isinstance(error_visual_basic, list) and all(x is None for x in error_visual_basic):
        logging.error('error_visual_basic is required.')
        return ['error_visual_basic is required.']
    if error_visual_basic is not None:

        request_parameters['error'] = error_visual_basic

    if event_visual_basic is None or isinstance(event_visual_basic, list) and all(x is None for x in event_visual_basic):
        logging.error('event_visual_basic is required.')
        return ['event_visual_basic is required.']
    if event_visual_basic is not None:

        request_parameters['event'] = event_visual_basic

    if exit_visual_basic is None or isinstance(exit_visual_basic, list) and all(x is None for x in exit_visual_basic):
        logging.error('exit_visual_basic is required.')
        return ['exit_visual_basic is required.']
    if exit_visual_basic is not None:

        request_parameters['exit'] = exit_visual_basic

    if finally_visual_basic is None or isinstance(finally_visual_basic, list) and all(x is None for x in finally_visual_basic):
        logging.error('finally_visual_basic is required.')
        return ['finally_visual_basic is required.']
    if finally_visual_basic is not None:

        request_parameters['finally'] = finally_visual_basic

    if for_visual_basic is None or isinstance(for_visual_basic, list) and all(x is None for x in for_visual_basic):
        logging.error('for_visual_basic is required.')
        return ['for_visual_basic is required.']
    if for_visual_basic is not None:

        request_parameters['for'] = for_visual_basic

    if friend_visual_basic is None or isinstance(friend_visual_basic, list) and all(x is None for x in friend_visual_basic):
        logging.error('friend_visual_basic is required.')
        return ['friend_visual_basic is required.']
    if friend_visual_basic is not None:

        request_parameters['friend'] = friend_visual_basic

    if function_visual_basic is None or isinstance(function_visual_basic, list) and all(x is None for x in function_visual_basic):
        logging.error('function_visual_basic is required.')
        return ['function_visual_basic is required.']
    if function_visual_basic is not None:

        request_parameters['function'] = function_visual_basic

    if get_visual_basic is None or isinstance(get_visual_basic, list) and all(x is None for x in get_visual_basic):
        logging.error('get_visual_basic is required.')
        return ['get_visual_basic is required.']
    if get_visual_basic is not None:

        request_parameters['get'] = get_visual_basic

    if gettype_visual_basic is None or isinstance(gettype_visual_basic, list) and all(x is None for x in gettype_visual_basic):
        logging.error('gettype_visual_basic is required.')
        return ['gettype_visual_basic is required.']
    if gettype_visual_basic is not None:

        request_parameters['gettype'] = gettype_visual_basic

    if getxmlnamespace_visual_basic is None or isinstance(getxmlnamespace_visual_basic, list) and all(x is None for x in getxmlnamespace_visual_basic):
        logging.error('getxmlnamespace_visual_basic is required.')
        return ['getxmlnamespace_visual_basic is required.']
    if getxmlnamespace_visual_basic is not None:

        request_parameters['getxmlnamespace'] = getxmlnamespace_visual_basic

    if global_visual_basic is None or isinstance(global_visual_basic, list) and all(x is None for x in global_visual_basic):
        logging.error('global_visual_basic is required.')
        return ['global_visual_basic is required.']
    if global_visual_basic is not None:

        request_parameters['global'] = global_visual_basic

    if gosub_visual_basic is None or isinstance(gosub_visual_basic, list) and all(x is None for x in gosub_visual_basic):
        logging.error('gosub_visual_basic is required.')
        return ['gosub_visual_basic is required.']
    if gosub_visual_basic is not None:

        request_parameters['gosub'] = gosub_visual_basic

    if goto_visual_basic is None or isinstance(goto_visual_basic, list) and all(x is None for x in goto_visual_basic):
        logging.error('goto_visual_basic is required.')
        return ['goto_visual_basic is required.']
    if goto_visual_basic is not None:

        request_parameters['goto'] = goto_visual_basic

    if handles_visual_basic is None or isinstance(handles_visual_basic, list) and all(x is None for x in handles_visual_basic):
        logging.error('handles_visual_basic is required.')
        return ['handles_visual_basic is required.']
    if handles_visual_basic is not None:

        request_parameters['handles'] = handles_visual_basic

    if if_visual_basic is None or isinstance(if_visual_basic, list) and all(x is None for x in if_visual_basic):
        logging.error('if_visual_basic is required.')
        return ['if_visual_basic is required.']
    if if_visual_basic is not None:

        request_parameters['if'] = if_visual_basic

    if implements_visual_basic is None or isinstance(implements_visual_basic, list) and all(x is None for x in implements_visual_basic):
        logging.error('implements_visual_basic is required.')
        return ['implements_visual_basic is required.']
    if implements_visual_basic is not None:

        request_parameters['implements'] = implements_visual_basic

    if imports_visual_basic is None or isinstance(imports_visual_basic, list) and all(x is None for x in imports_visual_basic):
        logging.error('imports_visual_basic is required.')
        return ['imports_visual_basic is required.']
    if imports_visual_basic is not None:

        request_parameters['imports'] = imports_visual_basic

    if in_visual_basic is None or isinstance(in_visual_basic, list) and all(x is None for x in in_visual_basic):
        logging.error('in_visual_basic is required.')
        return ['in_visual_basic is required.']
    if in_visual_basic is not None:

        request_parameters['in'] = in_visual_basic

    if inherits_visual_basic is None or isinstance(inherits_visual_basic, list) and all(x is None for x in inherits_visual_basic):
        logging.error('inherits_visual_basic is required.')
        return ['inherits_visual_basic is required.']
    if inherits_visual_basic is not None:

        request_parameters['inherits'] = inherits_visual_basic

    if integer_visual_basic is None or isinstance(integer_visual_basic, list) and all(x is None for x in integer_visual_basic):
        logging.error('integer_visual_basic is required.')
        return ['integer_visual_basic is required.']
    if integer_visual_basic is not None:

        request_parameters['integer'] = integer_visual_basic

    if interface_visual_basic is None or isinstance(interface_visual_basic, list) and all(x is None for x in interface_visual_basic):
        logging.error('interface_visual_basic is required.')
        return ['interface_visual_basic is required.']
    if interface_visual_basic is not None:

        request_parameters['interface'] = interface_visual_basic

    if is_visual_basic is None or isinstance(is_visual_basic, list) and all(x is None for x in is_visual_basic):
        logging.error('is_visual_basic is required.')
        return ['is_visual_basic is required.']
    if is_visual_basic is not None:

        request_parameters['is'] = is_visual_basic

    if isnot_visual_basic is None or isinstance(isnot_visual_basic, list) and all(x is None for x in isnot_visual_basic):
        logging.error('isnot_visual_basic is required.')
        return ['isnot_visual_basic is required.']
    if isnot_visual_basic is not None:

        request_parameters['isnot'] = isnot_visual_basic

    if let_visual_basic is None or isinstance(let_visual_basic, list) and all(x is None for x in let_visual_basic):
        logging.error('let_visual_basic is required.')
        return ['let_visual_basic is required.']
    if let_visual_basic is not None:

        request_parameters['let'] = let_visual_basic

    if lib_visual_basic is None or isinstance(lib_visual_basic, list) and all(x is None for x in lib_visual_basic):
        logging.error('lib_visual_basic is required.')
        return ['lib_visual_basic is required.']
    if lib_visual_basic is not None:

        request_parameters['lib'] = lib_visual_basic

    if like_visual_basic is None or isinstance(like_visual_basic, list) and all(x is None for x in like_visual_basic):
        logging.error('like_visual_basic is required.')
        return ['like_visual_basic is required.']
    if like_visual_basic is not None:

        request_parameters['like'] = like_visual_basic

    if long_visual_basic is None or isinstance(long_visual_basic, list) and all(x is None for x in long_visual_basic):
        logging.error('long_visual_basic is required.')
        return ['long_visual_basic is required.']
    if long_visual_basic is not None:

        request_parameters['long'] = long_visual_basic

    if loop_visual_basic is None or isinstance(loop_visual_basic, list) and all(x is None for x in loop_visual_basic):
        logging.error('loop_visual_basic is required.')
        return ['loop_visual_basic is required.']
    if loop_visual_basic is not None:

        request_parameters['loop'] = loop_visual_basic

    if me_visual_basic is None or isinstance(me_visual_basic, list) and all(x is None for x in me_visual_basic):
        logging.error('me_visual_basic is required.')
        return ['me_visual_basic is required.']
    if me_visual_basic is not None:

        request_parameters['me'] = me_visual_basic

    if mod_visual_basic is None or isinstance(mod_visual_basic, list) and all(x is None for x in mod_visual_basic):
        logging.error('mod_visual_basic is required.')
        return ['mod_visual_basic is required.']
    if mod_visual_basic is not None:

        request_parameters['mod'] = mod_visual_basic

    if module_visual_basic is None or isinstance(module_visual_basic, list) and all(x is None for x in module_visual_basic):
        logging.error('module_visual_basic is required.')
        return ['module_visual_basic is required.']
    if module_visual_basic is not None:

        request_parameters['module'] = module_visual_basic

    if mustinherit_visual_basic is None or isinstance(mustinherit_visual_basic, list) and all(x is None for x in mustinherit_visual_basic):
        logging.error('mustinherit_visual_basic is required.')
        return ['mustinherit_visual_basic is required.']
    if mustinherit_visual_basic is not None:

        request_parameters['mustinherit'] = mustinherit_visual_basic

    if mustoverride_visual_basic is None or isinstance(mustoverride_visual_basic, list) and all(x is None for x in mustoverride_visual_basic):
        logging.error('mustoverride_visual_basic is required.')
        return ['mustoverride_visual_basic is required.']
    if mustoverride_visual_basic is not None:

        request_parameters['mustoverride'] = mustoverride_visual_basic

    if mybase_visual_basic is None or isinstance(mybase_visual_basic, list) and all(x is None for x in mybase_visual_basic):
        logging.error('mybase_visual_basic is required.')
        return ['mybase_visual_basic is required.']
    if mybase_visual_basic is not None:

        request_parameters['mybase'] = mybase_visual_basic

    if myclass_visual_basic is None or isinstance(myclass_visual_basic, list) and all(x is None for x in myclass_visual_basic):
        logging.error('myclass_visual_basic is required.')
        return ['myclass_visual_basic is required.']
    if myclass_visual_basic is not None:

        request_parameters['myclass'] = myclass_visual_basic

    if namespace_visual_basic is None or isinstance(namespace_visual_basic, list) and all(x is None for x in namespace_visual_basic):
        logging.error('namespace_visual_basic is required.')
        return ['namespace_visual_basic is required.']
    if namespace_visual_basic is not None:

        request_parameters['namespace'] = namespace_visual_basic

    if narrowing_visual_basic is None or isinstance(narrowing_visual_basic, list) and all(x is None for x in narrowing_visual_basic):
        logging.error('narrowing_visual_basic is required.')
        return ['narrowing_visual_basic is required.']
    if narrowing_visual_basic is not None:

        request_parameters['narrowing'] = narrowing_visual_basic

    if new_visual_basic is None or isinstance(new_visual_basic, list) and all(x is None for x in new_visual_basic):
        logging.error('new_visual_basic is required.')
        return ['new_visual_basic is required.']
    if new_visual_basic is not None:

        request_parameters['new'] = new_visual_basic

    if next_visual_basic is None or isinstance(next_visual_basic, list) and all(x is None for x in next_visual_basic):
        logging.error('next_visual_basic is required.')
        return ['next_visual_basic is required.']
    if next_visual_basic is not None:

        request_parameters['next'] = next_visual_basic

    if not_visual_basic is None or isinstance(not_visual_basic, list) and all(x is None for x in not_visual_basic):
        logging.error('not_visual_basic is required.')
        return ['not_visual_basic is required.']
    if not_visual_basic is not None:

        request_parameters['not'] = not_visual_basic

    if nothing_visual_basic is None or isinstance(nothing_visual_basic, list) and all(x is None for x in nothing_visual_basic):
        logging.error('nothing_visual_basic is required.')
        return ['nothing_visual_basic is required.']
    if nothing_visual_basic is not None:

        request_parameters['nothing'] = nothing_visual_basic

    if notinheritable_visual_basic is None or isinstance(notinheritable_visual_basic, list) and all(x is None for x in notinheritable_visual_basic):
        logging.error('notinheritable_visual_basic is required.')
        return ['notinheritable_visual_basic is required.']
    if notinheritable_visual_basic is not None:

        request_parameters['notinheritable'] = notinheritable_visual_basic

    if notoverridable_visual_basic is None or isinstance(notoverridable_visual_basic, list) and all(x is None for x in notoverridable_visual_basic):
        logging.error('notoverridable_visual_basic is required.')
        return ['notoverridable_visual_basic is required.']
    if notoverridable_visual_basic is not None:

        request_parameters['notoverridable'] = notoverridable_visual_basic

    if object_visual_basic is None or isinstance(object_visual_basic, list) and all(x is None for x in object_visual_basic):
        logging.error('object_visual_basic is required.')
        return ['object_visual_basic is required.']
    if object_visual_basic is not None:

        request_parameters['object'] = object_visual_basic

    if of_visual_basic is None or isinstance(of_visual_basic, list) and all(x is None for x in of_visual_basic):
        logging.error('of_visual_basic is required.')
        return ['of_visual_basic is required.']
    if of_visual_basic is not None:

        request_parameters['of'] = of_visual_basic

    if on_visual_basic is None or isinstance(on_visual_basic, list) and all(x is None for x in on_visual_basic):
        logging.error('on_visual_basic is required.')
        return ['on_visual_basic is required.']
    if on_visual_basic is not None:

        request_parameters['on'] = on_visual_basic

    if operator_visual_basic is None or isinstance(operator_visual_basic, list) and all(x is None for x in operator_visual_basic):
        logging.error('operator_visual_basic is required.')
        return ['operator_visual_basic is required.']
    if operator_visual_basic is not None:

        request_parameters['operator'] = operator_visual_basic

    if option_visual_basic is None or isinstance(option_visual_basic, list) and all(x is None for x in option_visual_basic):
        logging.error('option_visual_basic is required.')
        return ['option_visual_basic is required.']
    if option_visual_basic is not None:

        request_parameters['option'] = option_visual_basic

    if optional_visual_basic is None or isinstance(optional_visual_basic, list) and all(x is None for x in optional_visual_basic):
        logging.error('optional_visual_basic is required.')
        return ['optional_visual_basic is required.']
    if optional_visual_basic is not None:

        request_parameters['optional'] = optional_visual_basic

    if or_visual_basic is None or isinstance(or_visual_basic, list) and all(x is None for x in or_visual_basic):
        logging.error('or_visual_basic is required.')
        return ['or_visual_basic is required.']
    if or_visual_basic is not None:

        request_parameters['or'] = or_visual_basic

    if orelse_visual_basic is None or isinstance(orelse_visual_basic, list) and all(x is None for x in orelse_visual_basic):
        logging.error('orelse_visual_basic is required.')
        return ['orelse_visual_basic is required.']
    if orelse_visual_basic is not None:

        request_parameters['orelse'] = orelse_visual_basic

    if overloads_visual_basic is None or isinstance(overloads_visual_basic, list) and all(x is None for x in overloads_visual_basic):
        logging.error('overloads_visual_basic is required.')
        return ['overloads_visual_basic is required.']
    if overloads_visual_basic is not None:

        request_parameters['overloads'] = overloads_visual_basic

    if overridable_visual_basic is None or isinstance(overridable_visual_basic, list) and all(x is None for x in overridable_visual_basic):
        logging.error('overridable_visual_basic is required.')
        return ['overridable_visual_basic is required.']
    if overridable_visual_basic is not None:

        request_parameters['overridable'] = overridable_visual_basic

    if overrides_visual_basic is None or isinstance(overrides_visual_basic, list) and all(x is None for x in overrides_visual_basic):
        logging.error('overrides_visual_basic is required.')
        return ['overrides_visual_basic is required.']
    if overrides_visual_basic is not None:

        request_parameters['overrides'] = overrides_visual_basic

    if paramarray_visual_basic is None or isinstance(paramarray_visual_basic, list) and all(x is None for x in paramarray_visual_basic):
        logging.error('paramarray_visual_basic is required.')
        return ['paramarray_visual_basic is required.']
    if paramarray_visual_basic is not None:

        request_parameters['paramarray'] = paramarray_visual_basic

    if partial_visual_basic is None or isinstance(partial_visual_basic, list) and all(x is None for x in partial_visual_basic):
        logging.error('partial_visual_basic is required.')
        return ['partial_visual_basic is required.']
    if partial_visual_basic is not None:

        request_parameters['partial'] = partial_visual_basic

    if private_visual_basic is None or isinstance(private_visual_basic, list) and all(x is None for x in private_visual_basic):
        logging.error('private_visual_basic is required.')
        return ['private_visual_basic is required.']
    if private_visual_basic is not None:

        request_parameters['private'] = private_visual_basic

    if property_visual_basic is None or isinstance(property_visual_basic, list) and all(x is None for x in property_visual_basic):
        logging.error('property_visual_basic is required.')
        return ['property_visual_basic is required.']
    if property_visual_basic is not None:

        request_parameters['property'] = property_visual_basic

    if protected_visual_basic is None or isinstance(protected_visual_basic, list) and all(x is None for x in protected_visual_basic):
        logging.error('protected_visual_basic is required.')
        return ['protected_visual_basic is required.']
    if protected_visual_basic is not None:

        request_parameters['protected'] = protected_visual_basic

    if public_visual_basic is None or isinstance(public_visual_basic, list) and all(x is None for x in public_visual_basic):
        logging.error('public_visual_basic is required.')
        return ['public_visual_basic is required.']
    if public_visual_basic is not None:

        request_parameters['public'] = public_visual_basic

    if raiseevent_visual_basic is None or isinstance(raiseevent_visual_basic, list) and all(x is None for x in raiseevent_visual_basic):
        logging.error('raiseevent_visual_basic is required.')
        return ['raiseevent_visual_basic is required.']
    if raiseevent_visual_basic is not None:

        request_parameters['raiseevent'] = raiseevent_visual_basic

    if readonly_visual_basic is None or isinstance(readonly_visual_basic, list) and all(x is None for x in readonly_visual_basic):
        logging.error('readonly_visual_basic is required.')
        return ['readonly_visual_basic is required.']
    if readonly_visual_basic is not None:

        request_parameters['readonly'] = readonly_visual_basic

    if redim_visual_basic is None or isinstance(redim_visual_basic, list) and all(x is None for x in redim_visual_basic):
        logging.error('redim_visual_basic is required.')
        return ['redim_visual_basic is required.']
    if redim_visual_basic is not None:

        request_parameters['redim'] = redim_visual_basic

    if rem_visual_basic is None or isinstance(rem_visual_basic, list) and all(x is None for x in rem_visual_basic):
        logging.error('rem_visual_basic is required.')
        return ['rem_visual_basic is required.']
    if rem_visual_basic is not None:

        request_parameters['rem'] = rem_visual_basic

    if removehandler_visual_basic is None or isinstance(removehandler_visual_basic, list) and all(x is None for x in removehandler_visual_basic):
        logging.error('removehandler_visual_basic is required.')
        return ['removehandler_visual_basic is required.']
    if removehandler_visual_basic is not None:

        request_parameters['removehandler'] = removehandler_visual_basic

    if resume_visual_basic is None or isinstance(resume_visual_basic, list) and all(x is None for x in resume_visual_basic):
        logging.error('resume_visual_basic is required.')
        return ['resume_visual_basic is required.']
    if resume_visual_basic is not None:

        request_parameters['resume'] = resume_visual_basic

    if return_visual_basic is None or isinstance(return_visual_basic, list) and all(x is None for x in return_visual_basic):
        logging.error('return_visual_basic is required.')
        return ['return_visual_basic is required.']
    if return_visual_basic is not None:

        request_parameters['return'] = return_visual_basic

    if sbyte_visual_basic is None or isinstance(sbyte_visual_basic, list) and all(x is None for x in sbyte_visual_basic):
        logging.error('sbyte_visual_basic is required.')
        return ['sbyte_visual_basic is required.']
    if sbyte_visual_basic is not None:

        request_parameters['sbyte'] = sbyte_visual_basic

    if select_visual_basic is None or isinstance(select_visual_basic, list) and all(x is None for x in select_visual_basic):
        logging.error('select_visual_basic is required.')
        return ['select_visual_basic is required.']
    if select_visual_basic is not None:

        request_parameters['select'] = select_visual_basic

    if set_visual_basic is None or isinstance(set_visual_basic, list) and all(x is None for x in set_visual_basic):
        logging.error('set_visual_basic is required.')
        return ['set_visual_basic is required.']
    if set_visual_basic is not None:

        request_parameters['set'] = set_visual_basic

    if shadows_visual_basic is None or isinstance(shadows_visual_basic, list) and all(x is None for x in shadows_visual_basic):
        logging.error('shadows_visual_basic is required.')
        return ['shadows_visual_basic is required.']
    if shadows_visual_basic is not None:

        request_parameters['shadows'] = shadows_visual_basic

    if shared_visual_basic is None or isinstance(shared_visual_basic, list) and all(x is None for x in shared_visual_basic):
        logging.error('shared_visual_basic is required.')
        return ['shared_visual_basic is required.']
    if shared_visual_basic is not None:

        request_parameters['shared'] = shared_visual_basic

    if short_visual_basic is None or isinstance(short_visual_basic, list) and all(x is None for x in short_visual_basic):
        logging.error('short_visual_basic is required.')
        return ['short_visual_basic is required.']
    if short_visual_basic is not None:

        request_parameters['short'] = short_visual_basic

    if single_visual_basic is None or isinstance(single_visual_basic, list) and all(x is None for x in single_visual_basic):
        logging.error('single_visual_basic is required.')
        return ['single_visual_basic is required.']
    if single_visual_basic is not None:

        request_parameters['single'] = single_visual_basic

    if static_visual_basic is None or isinstance(static_visual_basic, list) and all(x is None for x in static_visual_basic):
        logging.error('static_visual_basic is required.')
        return ['static_visual_basic is required.']
    if static_visual_basic is not None:

        request_parameters['static'] = static_visual_basic

    if step_visual_basic is None or isinstance(step_visual_basic, list) and all(x is None for x in step_visual_basic):
        logging.error('step_visual_basic is required.')
        return ['step_visual_basic is required.']
    if step_visual_basic is not None:

        request_parameters['step'] = step_visual_basic

    if stop_visual_basic is None or isinstance(stop_visual_basic, list) and all(x is None for x in stop_visual_basic):
        logging.error('stop_visual_basic is required.')
        return ['stop_visual_basic is required.']
    if stop_visual_basic is not None:

        request_parameters['stop'] = stop_visual_basic

    if string_visual_basic is None or isinstance(string_visual_basic, list) and all(x is None for x in string_visual_basic):
        logging.error('string_visual_basic is required.')
        return ['string_visual_basic is required.']
    if string_visual_basic is not None:

        request_parameters['string'] = string_visual_basic

    if structure_visual_basic is None or isinstance(structure_visual_basic, list) and all(x is None for x in structure_visual_basic):
        logging.error('structure_visual_basic is required.')
        return ['structure_visual_basic is required.']
    if structure_visual_basic is not None:

        request_parameters['structure'] = structure_visual_basic

    if sub_visual_basic is None or isinstance(sub_visual_basic, list) and all(x is None for x in sub_visual_basic):
        logging.error('sub_visual_basic is required.')
        return ['sub_visual_basic is required.']
    if sub_visual_basic is not None:

        request_parameters['sub'] = sub_visual_basic

    if synclock_visual_basic is None or isinstance(synclock_visual_basic, list) and all(x is None for x in synclock_visual_basic):
        logging.error('synclock_visual_basic is required.')
        return ['synclock_visual_basic is required.']
    if synclock_visual_basic is not None:

        request_parameters['synclock'] = synclock_visual_basic

    if then_visual_basic is None or isinstance(then_visual_basic, list) and all(x is None for x in then_visual_basic):
        logging.error('then_visual_basic is required.')
        return ['then_visual_basic is required.']
    if then_visual_basic is not None:

        request_parameters['then'] = then_visual_basic

    if throw_visual_basic is None or isinstance(throw_visual_basic, list) and all(x is None for x in throw_visual_basic):
        logging.error('throw_visual_basic is required.')
        return ['throw_visual_basic is required.']
    if throw_visual_basic is not None:

        request_parameters['throw'] = throw_visual_basic

    if to_visual_basic is None or isinstance(to_visual_basic, list) and all(x is None for x in to_visual_basic):
        logging.error('to_visual_basic is required.')
        return ['to_visual_basic is required.']
    if to_visual_basic is not None:

        request_parameters['to'] = to_visual_basic

    if try_visual_basic is None or isinstance(try_visual_basic, list) and all(x is None for x in try_visual_basic):
        logging.error('try_visual_basic is required.')
        return ['try_visual_basic is required.']
    if try_visual_basic is not None:

        request_parameters['try'] = try_visual_basic

    if trycast_visual_basic is None or isinstance(trycast_visual_basic, list) and all(x is None for x in trycast_visual_basic):
        logging.error('trycast_visual_basic is required.')
        return ['trycast_visual_basic is required.']
    if trycast_visual_basic is not None:

        request_parameters['trycast'] = trycast_visual_basic

    if type_visual_basic is None or isinstance(type_visual_basic, list) and all(x is None for x in type_visual_basic):
        logging.error('type_visual_basic is required.')
        return ['type_visual_basic is required.']
    if type_visual_basic is not None:

        request_parameters['type'] = type_visual_basic

    if typeof_visual_basic is None or isinstance(typeof_visual_basic, list) and all(x is None for x in typeof_visual_basic):
        logging.error('typeof_visual_basic is required.')
        return ['typeof_visual_basic is required.']
    if typeof_visual_basic is not None:

        request_parameters['typeof'] = typeof_visual_basic

    if uinteger_visual_basic is None or isinstance(uinteger_visual_basic, list) and all(x is None for x in uinteger_visual_basic):
        logging.error('uinteger_visual_basic is required.')
        return ['uinteger_visual_basic is required.']
    if uinteger_visual_basic is not None:

        request_parameters['uinteger'] = uinteger_visual_basic

    if ulong_visual_basic is None or isinstance(ulong_visual_basic, list) and all(x is None for x in ulong_visual_basic):
        logging.error('ulong_visual_basic is required.')
        return ['ulong_visual_basic is required.']
    if ulong_visual_basic is not None:

        request_parameters['ulong'] = ulong_visual_basic

    if ushort_visual_basic is None or isinstance(ushort_visual_basic, list) and all(x is None for x in ushort_visual_basic):
        logging.error('ushort_visual_basic is required.')
        return ['ushort_visual_basic is required.']
    if ushort_visual_basic is not None:

        request_parameters['ushort'] = ushort_visual_basic

    if using_visual_basic is None or isinstance(using_visual_basic, list) and all(x is None for x in using_visual_basic):
        logging.error('using_visual_basic is required.')
        return ['using_visual_basic is required.']
    if using_visual_basic is not None:

        request_parameters['using'] = using_visual_basic

    if variant_visual_basic is None or isinstance(variant_visual_basic, list) and all(x is None for x in variant_visual_basic):
        logging.error('variant_visual_basic is required.')
        return ['variant_visual_basic is required.']
    if variant_visual_basic is not None:

        request_parameters['variant'] = variant_visual_basic

    if wend_visual_basic is None or isinstance(wend_visual_basic, list) and all(x is None for x in wend_visual_basic):
        logging.error('wend_visual_basic is required.')
        return ['wend_visual_basic is required.']
    if wend_visual_basic is not None:

        request_parameters['wend'] = wend_visual_basic

    if when_visual_basic is None or isinstance(when_visual_basic, list) and all(x is None for x in when_visual_basic):
        logging.error('when_visual_basic is required.')
        return ['when_visual_basic is required.']
    if when_visual_basic is not None:

        request_parameters['when'] = when_visual_basic

    if while_visual_basic is None or isinstance(while_visual_basic, list) and all(x is None for x in while_visual_basic):
        logging.error('while_visual_basic is required.')
        return ['while_visual_basic is required.']
    if while_visual_basic is not None:

        request_parameters['while'] = while_visual_basic

    if widening_visual_basic is None or isinstance(widening_visual_basic, list) and all(x is None for x in widening_visual_basic):
        logging.error('widening_visual_basic is required.')
        return ['widening_visual_basic is required.']
    if widening_visual_basic is not None:

        request_parameters['widening'] = widening_visual_basic

    if with_visual_basic is None or isinstance(with_visual_basic, list) and all(x is None for x in with_visual_basic):
        logging.error('with_visual_basic is required.')
        return ['with_visual_basic is required.']
    if with_visual_basic is not None:

        request_parameters['with'] = with_visual_basic

    if withevents_visual_basic is None or isinstance(withevents_visual_basic, list) and all(x is None for x in withevents_visual_basic):
        logging.error('withevents_visual_basic is required.')
        return ['withevents_visual_basic is required.']
    if withevents_visual_basic is not None:

        request_parameters['withevents'] = withevents_visual_basic

    if writeonly_visual_basic is None or isinstance(writeonly_visual_basic, list) and all(x is None for x in writeonly_visual_basic):
        logging.error('writeonly_visual_basic is required.')
        return ['writeonly_visual_basic is required.']
    if writeonly_visual_basic is not None:

        request_parameters['writeonly'] = writeonly_visual_basic

    if xor_visual_basic is None or isinstance(xor_visual_basic, list) and all(x is None for x in xor_visual_basic):
        logging.error('xor_visual_basic is required.')
        return ['xor_visual_basic is required.']
    if xor_visual_basic is not None:

        request_parameters['xor'] = xor_visual_basic


    response = None
    try:
        response = requests.delete('http://localhost:8949/test/vba/restricted/keywords'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for vba_keywords_test_delete_test_vba_restricted_keywords ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/VBAKeywords'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('VBAKeywords', OrderedDict([('properties', OrderedDict([('addhandler', OrderedDict()), ('addressof', OrderedDict()), ('alias', OrderedDict()), ('and', OrderedDict()), ('andalso', OrderedDict()), ('as', OrderedDict()), ('boolean', OrderedDict()), ('byref', OrderedDict()), ('byte', OrderedDict()), ('byval', OrderedDict()), ('call', OrderedDict()), ('case', OrderedDict()), ('catch', OrderedDict()), ('cbool', OrderedDict()), ('cbyte', OrderedDict()), ('cchar', OrderedDict()), ('cdate', OrderedDict()), ('cdbl', OrderedDict()), ('cdec', OrderedDict()), ('char', OrderedDict()), ('cint', OrderedDict()), ('class', OrderedDict()), ('clng', OrderedDict()), ('cobj', OrderedDict()), ('const', OrderedDict()), ('continue', OrderedDict()), ('csbyte', OrderedDict()), ('cshort', OrderedDict()), ('csng', OrderedDict()), ('cstr', OrderedDict()), ('ctype', OrderedDict()), ('cuint', OrderedDict()), ('culng', OrderedDict()), ('currency', OrderedDict()), ('cushort', OrderedDict()), ('date', OrderedDict()), ('decimal', OrderedDict()), ('declare', OrderedDict()), ('default', OrderedDict()), ('delegate', OrderedDict()), ('dim', OrderedDict()), ('directcast', OrderedDict()), ('do', OrderedDict()), ('double', OrderedDict()), ('each', OrderedDict()), ('else', OrderedDict()), ('elseif', OrderedDict()), ('end', OrderedDict()), ('endif', OrderedDict()), ('enum', OrderedDict()), ('erase', OrderedDict()), ('error', OrderedDict()), ('event', OrderedDict()), ('exit', OrderedDict()), ('finally', OrderedDict()), ('for', OrderedDict()), ('friend', OrderedDict()), ('function', OrderedDict()), ('get', OrderedDict()), ('gettype', OrderedDict()), ('getxmlnamespace', OrderedDict()), ('global', OrderedDict()), ('gosub', OrderedDict()), ('goto', OrderedDict()), ('handles', OrderedDict()), ('if', OrderedDict()), ('implements', OrderedDict()), ('imports', OrderedDict()), ('in', OrderedDict()), ('inherits', OrderedDict()), ('integer', OrderedDict()), ('interface', OrderedDict()), ('is', OrderedDict()), ('isnot', OrderedDict()), ('let', OrderedDict()), ('lib', OrderedDict()), ('like', OrderedDict()), ('long', OrderedDict()), ('loop', OrderedDict()), ('me', OrderedDict()), ('mod', OrderedDict()), ('module', OrderedDict()), ('mustinherit', OrderedDict()), ('mustoverride', OrderedDict()), ('mybase', OrderedDict()), ('myclass', OrderedDict()), ('namespace', OrderedDict()), ('narrowing', OrderedDict()), ('new', OrderedDict()), ('next', OrderedDict()), ('not', OrderedDict()), ('nothing', OrderedDict()), ('notinheritable', OrderedDict()), ('notoverridable', OrderedDict()), ('object', OrderedDict()), ('of', OrderedDict()), ('on', OrderedDict()), ('operator', OrderedDict()), ('option', OrderedDict()), ('optional', OrderedDict()), ('or', OrderedDict()), ('orelse', OrderedDict()), ('overloads', OrderedDict()), ('overridable', OrderedDict()), ('overrides', OrderedDict()), ('paramarray', OrderedDict()), ('partial', OrderedDict()), ('private', OrderedDict()), ('property', OrderedDict()), ('protected', OrderedDict()), ('public', OrderedDict()), ('raiseevent', OrderedDict()), ('readonly', OrderedDict()), ('redim', OrderedDict()), ('rem', OrderedDict()), ('removehandler', OrderedDict()), ('resume', OrderedDict()), ('return', OrderedDict()), ('sbyte', OrderedDict()), ('select', OrderedDict()), ('set', OrderedDict()), ('shadows', OrderedDict()), ('shared', OrderedDict()), ('short', OrderedDict()), ('single', OrderedDict()), ('static', OrderedDict()), ('step', OrderedDict()), ('stop', OrderedDict()), ('string', OrderedDict()), ('structure', OrderedDict()), ('sub', OrderedDict()), ('synclock', OrderedDict()), ('then', OrderedDict()), ('throw', OrderedDict()), ('to', OrderedDict()), ('try', OrderedDict()), ('trycast', OrderedDict()), ('type', OrderedDict()), ('typeof', OrderedDict()), ('uinteger', OrderedDict()), ('ulong', OrderedDict()), ('ushort', OrderedDict()), ('using', OrderedDict()), ('variant', OrderedDict()), ('wend', OrderedDict()), ('when', OrderedDict()), ('while', OrderedDict()), ('widening', OrderedDict()), ('with', OrderedDict()), ('withevents', OrderedDict()), ('writeonly', OrderedDict()), ('xor', OrderedDict())]))]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling vba_keywords_test_delete_test_vba_restricted_keywords.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling vba_keywords_test_delete_test_vba_restricted_keywords response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling vba_keywords_test_delete_test_vba_restricted_keywords.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
@xw.ret(expand='table')
def without_parameter_test_get_test_json_without_parameter():
    logging.info("Calling without_parameter_test_get_test_json_without_parameter...")
    request_header = {'content-type': 'application/json'}

    response = None
    try:
        response = requests.get('http://localhost:8950/test/json/without/parameter'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_get_test_json_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_get_test_json_without_parameter.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_get_test_json_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_get_test_json_without_parameter.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
@xw.ret(expand='table')
def without_parameter_test_post_test_json_without_parameter():
    logging.info("Calling without_parameter_test_post_test_json_without_parameter...")
    request_header = {'content-type': 'application/json'}

    response = None
    try:
        response = requests.post('http://localhost:8950/test/json/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_post_test_json_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_post_test_json_without_parameter.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_post_test_json_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_post_test_json_without_parameter.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
@xw.ret(expand='table')
def without_parameter_test_put_test_json_without_parameter():
    logging.info("Calling without_parameter_test_put_test_json_without_parameter...")
    request_header = {'content-type': 'application/json'}

    response = None
    try:
        response = requests.put('http://localhost:8950/test/json/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_put_test_json_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_put_test_json_without_parameter.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_put_test_json_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_put_test_json_without_parameter.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
@xw.ret(expand='table')
def without_parameter_test_delete_test_json_without_parameter():
    logging.info("Calling without_parameter_test_delete_test_json_without_parameter...")
    request_header = {'content-type': 'application/json'}

    response = None
    try:
        response = requests.delete('http://localhost:8950/test/json/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_delete_test_json_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_delete_test_json_without_parameter.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_delete_test_json_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_delete_test_json_without_parameter.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_get_test_plain_text_without_parameter():
    logging.info("Calling without_parameter_test_get_test_plain_text_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8950/test/plain/text/without/parameter'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_get_test_plain_text_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('type', 'string')]))]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_get_test_plain_text_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_get_test_plain_text_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_get_test_plain_text_without_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_post_test_plain_text_without_parameter():
    logging.info("Calling without_parameter_test_post_test_plain_text_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.post('http://localhost:8950/test/plain/text/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_post_test_plain_text_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_post_test_plain_text_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_post_test_plain_text_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_post_test_plain_text_without_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_put_test_plain_text_without_parameter():
    logging.info("Calling without_parameter_test_put_test_plain_text_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.put('http://localhost:8950/test/plain/text/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_put_test_plain_text_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_put_test_plain_text_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_put_test_plain_text_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_put_test_plain_text_without_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_delete_test_plain_text_without_parameter():
    logging.info("Calling without_parameter_test_delete_test_plain_text_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.delete('http://localhost:8950/test/plain/text/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_delete_test_plain_text_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_delete_test_plain_text_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_delete_test_plain_text_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_delete_test_plain_text_without_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_get_test_without_parameter():
    logging.info("Calling without_parameter_test_get_test_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8950/test/without/parameter'.format(
), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_get_test_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('type', 'string')]))]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_get_test_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_get_test_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_get_test_without_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_post_test_without_parameter():
    logging.info("Calling without_parameter_test_post_test_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.post('http://localhost:8950/test/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_post_test_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'POST performed properly')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_post_test_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_post_test_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_post_test_without_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_put_test_without_parameter():
    logging.info("Calling without_parameter_test_put_test_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.put('http://localhost:8950/test/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_put_test_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'PUT performed properly')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_put_test_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_put_test_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_put_test_without_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_delete_test_without_parameter():
    logging.info("Calling without_parameter_test_delete_test_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.delete('http://localhost:8950/test/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_delete_test_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'DELETE performed properly')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_delete_test_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling without_parameter_test_delete_test_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_delete_test_without_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='header_parameter_test', call_in_wizard=False)
@xw.arg('header_string', doc='header parameter')
def header_parameter_test_get_test_header_parameter(header_string):
    logging.info("Calling header_parameter_test_get_test_header_parameter...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if header_string is None or isinstance(header_string, list) and all(x is None for x in header_string):
        logging.error('header_string is required.')
        return 'header_string is required.'
    if header_string is not None:

        request_header['header_string'] = header_string


    response = None
    try:
        response = requests.get('http://localhost:8951/test/header/parameter'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for header_parameter_test_get_test_header_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Header')]))]))])
            all_definitions = OrderedDict([('Header', OrderedDict([('properties', OrderedDict([('Accept', OrderedDict([('type', 'string')])), ('Accept-Encoding', OrderedDict([('type', 'string')])), ('Connection', OrderedDict([('type', 'string')])), ('Content-Length', OrderedDict([('type', 'string')])), ('Content-Type', OrderedDict([('type', 'string')])), ('Header-String', OrderedDict([('type', 'string')])), ('Host', OrderedDict([('type', 'string')])), ('User-Agent', OrderedDict([('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling header_parameter_test_get_test_header_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling header_parameter_test_get_test_header_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling header_parameter_test_get_test_header_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='form_parameter_test', call_in_wizard=False)
@xw.arg('form_string', doc='form parameter')
def form_parameter_test_post_test_form_parameter(form_string):
    logging.info("Calling form_parameter_test_post_test_form_parameter...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if form_string is None or isinstance(form_string, list) and all(x is None for x in form_string):
        logging.error('form_string is required.')
        return 'form_string is required.'
    if form_string is not None:

        request_payload['form_string'] = form_string


    response = None
    try:
        response = requests.post('http://localhost:8952/test/form/parameter'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for form_parameter_test_post_test_form_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Form')]))]))])
            all_definitions = OrderedDict([('Form', OrderedDict([('properties', OrderedDict([('form_string', OrderedDict([('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling form_parameter_test_post_test_form_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling form_parameter_test_post_test_form_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling form_parameter_test_post_test_form_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='array_parameter_test', call_in_wizard=False)
@xw.arg('query_array_string', doc='string array parameter')
def array_parameter_test_get_test_string_array_parameter(query_array_string):
    logging.info("Calling array_parameter_test_get_test_string_array_parameter...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string


    response = None
    try:
        response = requests.get('http://localhost:8953/test/string/array/parameter'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for array_parameter_test_get_test_string_array_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling array_parameter_test_get_test_string_array_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling array_parameter_test_get_test_string_array_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling array_parameter_test_get_test_string_array_parameter.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
@xw.ret(expand='table')
def json_test_get_test_json_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling json_test_get_test_json_with_all_optional_parameters_types...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return ['query_array_integer must contain integers.']
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return ['query_array_integer must be an integer.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return ['query_array_integer32 must contain integers.']
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return ['query_array_integer32 must be an integer.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return ['query_array_integer64 must contain integers.']
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return ['query_array_integer64 must be an integer.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return ['query_array_number must contain numbers.']
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return ['query_array_number must be a number.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return ['query_array_float must contain numbers.']
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return ['query_array_float must be a number.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return ['query_array_double must contain numbers.']
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return ['query_array_double must be a number.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return ['query_array_boolean must be either "true" or "false".']
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return ['query_array_boolean must contain "true" or "false".']
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return ['query_array_date must contain dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return ['query_array_date must be a date.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return ['query_array_date_time must contain date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return ['query_array_date_time must be a date time.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.get('http://localhost:8954/test/json/with/all/optional/parameters/types'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_get_test_json_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_get_test_json_with_all_optional_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_get_test_json_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_get_test_json_with_all_optional_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
@xw.ret(expand='table')
def json_test_post_test_json_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling json_test_post_test_json_with_all_optional_parameters_types...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return ['query_array_integer must contain integers.']
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return ['query_array_integer must be an integer.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return ['query_array_integer32 must contain integers.']
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return ['query_array_integer32 must be an integer.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return ['query_array_integer64 must contain integers.']
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return ['query_array_integer64 must be an integer.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return ['query_array_number must contain numbers.']
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return ['query_array_number must be a number.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return ['query_array_float must contain numbers.']
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return ['query_array_float must be a number.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return ['query_array_double must contain numbers.']
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return ['query_array_double must be a number.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return ['query_array_boolean must be either "true" or "false".']
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return ['query_array_boolean must contain "true" or "false".']
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return ['query_array_date must contain dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return ['query_array_date must be a date.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return ['query_array_date_time must contain date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return ['query_array_date_time must be a date time.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.post('http://localhost:8954/test/json/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_post_test_json_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_post_test_json_with_all_optional_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_post_test_json_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_post_test_json_with_all_optional_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
@xw.ret(expand='table')
def json_test_put_test_json_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling json_test_put_test_json_with_all_optional_parameters_types...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return ['query_array_integer must contain integers.']
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return ['query_array_integer must be an integer.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return ['query_array_integer32 must contain integers.']
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return ['query_array_integer32 must be an integer.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return ['query_array_integer64 must contain integers.']
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return ['query_array_integer64 must be an integer.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return ['query_array_number must contain numbers.']
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return ['query_array_number must be a number.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return ['query_array_float must contain numbers.']
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return ['query_array_float must be a number.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return ['query_array_double must contain numbers.']
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return ['query_array_double must be a number.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return ['query_array_boolean must be either "true" or "false".']
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return ['query_array_boolean must contain "true" or "false".']
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return ['query_array_date must contain dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return ['query_array_date must be a date.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return ['query_array_date_time must contain date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return ['query_array_date_time must be a date time.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.put('http://localhost:8954/test/json/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_put_test_json_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_put_test_json_with_all_optional_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_put_test_json_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_put_test_json_with_all_optional_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
@xw.ret(expand='table')
def json_test_delete_test_json_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling json_test_delete_test_json_with_all_optional_parameters_types...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return ['query_array_integer must contain integers.']
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return ['query_array_integer must be an integer.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return ['query_array_integer32 must contain integers.']
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return ['query_array_integer32 must be an integer.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return ['query_array_integer64 must contain integers.']
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return ['query_array_integer64 must be an integer.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return ['query_array_number must contain numbers.']
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return ['query_array_number must be a number.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return ['query_array_float must contain numbers.']
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return ['query_array_float must be a number.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return ['query_array_double must contain numbers.']
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return ['query_array_double must be a number.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return ['query_array_boolean must be either "true" or "false".']
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return ['query_array_boolean must contain "true" or "false".']
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return ['query_array_date must contain dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return ['query_array_date must be a date.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return ['query_array_date_time must contain date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return ['query_array_date_time must be a date time.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.delete('http://localhost:8954/test/json/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_delete_test_json_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_delete_test_json_with_all_optional_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_delete_test_json_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_delete_test_json_with_all_optional_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
@xw.ret(expand='table')
def json_test_get_test_json_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling json_test_get_test_json_with_all_parameters_types...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return ['query_integer is required.']
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return ['query_integer32 is required.']
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return ['query_integer64 is required.']
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return ['query_number is required.']
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return ['query_float is required.']
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return ['query_double is required.']
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return ['query_string is required.']
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return ['query_string_byte is required.']
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return ['query_string_binary is required.']
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return ['query_boolean is required.']
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return ['query_date is required.']
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return ['query_date_time is required.']
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return ['query_password is required.']
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return ['query_array_integer is required.']
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return ['query_array_integer must contain integers.']
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return ['query_array_integer must be an integer.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return ['query_array_integer32 is required.']
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return ['query_array_integer32 must contain integers.']
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return ['query_array_integer32 must be an integer.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return ['query_array_integer64 is required.']
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return ['query_array_integer64 must contain integers.']
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return ['query_array_integer64 must be an integer.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return ['query_array_number is required.']
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return ['query_array_number must contain numbers.']
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return ['query_array_number must be a number.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return ['query_array_float is required.']
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return ['query_array_float must contain numbers.']
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return ['query_array_float must be a number.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return ['query_array_double is required.']
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return ['query_array_double must contain numbers.']
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return ['query_array_double must be a number.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return ['query_array_string is required.']
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return ['query_array_string_byte is required.']
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return ['query_array_string_binary is required.']
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return ['query_array_boolean is required.']
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return ['query_array_boolean must be either "true" or "false".']
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return ['query_array_boolean must contain "true" or "false".']
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return ['query_array_date is required.']
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return ['query_array_date must contain dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return ['query_array_date must be a date.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return ['query_array_date_time is required.']
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return ['query_array_date_time must contain date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return ['query_array_date_time must be a date time.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return ['query_array_password is required.']
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.get('http://localhost:8954/test/json/with/all/parameters/types'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_get_test_json_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/AllMandatoryParameters')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_get_test_json_with_all_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_get_test_json_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_get_test_json_with_all_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
@xw.ret(expand='table')
def json_test_post_test_json_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling json_test_post_test_json_with_all_parameters_types...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return ['query_integer is required.']
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return ['query_integer32 is required.']
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return ['query_integer64 is required.']
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return ['query_number is required.']
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return ['query_float is required.']
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return ['query_double is required.']
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return ['query_string is required.']
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return ['query_string_byte is required.']
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return ['query_string_binary is required.']
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return ['query_boolean is required.']
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return ['query_date is required.']
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return ['query_date_time is required.']
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return ['query_password is required.']
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return ['query_array_integer is required.']
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return ['query_array_integer must contain integers.']
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return ['query_array_integer must be an integer.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return ['query_array_integer32 is required.']
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return ['query_array_integer32 must contain integers.']
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return ['query_array_integer32 must be an integer.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return ['query_array_integer64 is required.']
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return ['query_array_integer64 must contain integers.']
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return ['query_array_integer64 must be an integer.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return ['query_array_number is required.']
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return ['query_array_number must contain numbers.']
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return ['query_array_number must be a number.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return ['query_array_float is required.']
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return ['query_array_float must contain numbers.']
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return ['query_array_float must be a number.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return ['query_array_double is required.']
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return ['query_array_double must contain numbers.']
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return ['query_array_double must be a number.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return ['query_array_string is required.']
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return ['query_array_string_byte is required.']
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return ['query_array_string_binary is required.']
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return ['query_array_boolean is required.']
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return ['query_array_boolean must be either "true" or "false".']
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return ['query_array_boolean must contain "true" or "false".']
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return ['query_array_date is required.']
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return ['query_array_date must contain dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return ['query_array_date must be a date.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return ['query_array_date_time is required.']
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return ['query_array_date_time must contain date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return ['query_array_date_time must be a date time.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return ['query_array_password is required.']
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.post('http://localhost:8954/test/json/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_post_test_json_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_post_test_json_with_all_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_post_test_json_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_post_test_json_with_all_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
@xw.ret(expand='table')
def json_test_put_test_json_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling json_test_put_test_json_with_all_parameters_types...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return ['query_integer is required.']
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return ['query_integer32 is required.']
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return ['query_integer64 is required.']
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return ['query_number is required.']
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return ['query_float is required.']
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return ['query_double is required.']
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return ['query_string is required.']
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return ['query_string_byte is required.']
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return ['query_string_binary is required.']
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return ['query_boolean is required.']
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return ['query_date is required.']
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return ['query_date_time is required.']
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return ['query_password is required.']
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return ['query_array_integer is required.']
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return ['query_array_integer must contain integers.']
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return ['query_array_integer must be an integer.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return ['query_array_integer32 is required.']
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return ['query_array_integer32 must contain integers.']
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return ['query_array_integer32 must be an integer.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return ['query_array_integer64 is required.']
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return ['query_array_integer64 must contain integers.']
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return ['query_array_integer64 must be an integer.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return ['query_array_number is required.']
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return ['query_array_number must contain numbers.']
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return ['query_array_number must be a number.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return ['query_array_float is required.']
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return ['query_array_float must contain numbers.']
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return ['query_array_float must be a number.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return ['query_array_double is required.']
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return ['query_array_double must contain numbers.']
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return ['query_array_double must be a number.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return ['query_array_string is required.']
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return ['query_array_string_byte is required.']
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return ['query_array_string_binary is required.']
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return ['query_array_boolean is required.']
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return ['query_array_boolean must be either "true" or "false".']
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return ['query_array_boolean must contain "true" or "false".']
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return ['query_array_date is required.']
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return ['query_array_date must contain dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return ['query_array_date must be a date.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return ['query_array_date_time is required.']
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return ['query_array_date_time must contain date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return ['query_array_date_time must be a date time.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return ['query_array_password is required.']
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.put('http://localhost:8954/test/json/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_put_test_json_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_put_test_json_with_all_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_put_test_json_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_put_test_json_with_all_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
@xw.ret(expand='table')
def json_test_delete_test_json_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling json_test_delete_test_json_with_all_parameters_types...")
    request_header = {'content-type': 'application/json'}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return ['query_integer is required.']
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return ['query_integer32 is required.']
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return ['query_integer64 is required.']
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return ['query_number is required.']
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return ['query_float is required.']
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return ['query_double is required.']
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return ['query_string is required.']
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return ['query_string_byte is required.']
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return ['query_string_binary is required.']
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return ['query_boolean is required.']
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return ['query_date is required.']
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return ['query_date_time is required.']
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return ['query_password is required.']
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return ['query_array_integer is required.']
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return ['query_array_integer must contain integers.']
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return ['query_array_integer must be an integer.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return ['query_array_integer32 is required.']
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return ['query_array_integer32 must contain integers.']
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return ['query_array_integer32 must be an integer.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return ['query_array_integer64 is required.']
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return ['query_array_integer64 must contain integers.']
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return ['query_array_integer64 must be an integer.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return ['query_array_number is required.']
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return ['query_array_number must contain numbers.']
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return ['query_array_number must be a number.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return ['query_array_float is required.']
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return ['query_array_float must contain numbers.']
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return ['query_array_float must be a number.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return ['query_array_double is required.']
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return ['query_array_double must contain numbers.']
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return ['query_array_double must be a number.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return ['query_array_string is required.']
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return ['query_array_string_byte is required.']
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return ['query_array_string_binary is required.']
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return ['query_array_boolean is required.']
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return ['query_array_boolean must be either "true" or "false".']
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return ['query_array_boolean must contain "true" or "false".']
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return ['query_array_date is required.']
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return ['query_array_date must contain dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return ['query_array_date must be a date.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return ['query_array_date_time is required.']
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return ['query_array_date_time must contain date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return ['query_array_date_time must be a date time.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return ['query_array_password is required.']
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.delete('http://localhost:8954/test/json/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_delete_test_json_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_delete_test_json_with_all_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_delete_test_json_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_delete_test_json_with_all_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
@xw.ret(expand='table')
def json_test_get_test_json_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling json_test_get_test_json_with_all_paths_types...")
    request_header = {'content-type': 'application/json'}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return ['path_integer is required.']

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return ['path_integer32 is required.']

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return ['path_integer64 is required.']

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return ['path_number is required.']

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return ['path_float is required.']

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return ['path_double is required.']

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return ['path_string is required.']

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return ['path_string_byte is required.']

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return ['path_string_binary is required.']

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return ['path_boolean is required.']

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return ['path_date is required.']

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return ['path_date_time is required.']

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return ['path_password is required.']

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return ['path_array_integer is required.']

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return ['path_array_integer32 is required.']

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return ['path_array_integer64 is required.']

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return ['path_array_number is required.']

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return ['path_array_float is required.']

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return ['path_array_double is required.']

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return ['path_array_string is required.']

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return ['path_array_string_byte is required.']

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return ['path_array_string_binary is required.']

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return ['path_array_boolean is required.']

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return ['path_array_date is required.']

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return ['path_array_date_time is required.']

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return ['path_array_password is required.']


    response = None
    try:
        response = requests.get('http://localhost:8954/test/json/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_get_test_json_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_get_test_json_with_all_paths_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_get_test_json_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_get_test_json_with_all_paths_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
@xw.ret(expand='table')
def json_test_post_test_json_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling json_test_post_test_json_with_all_paths_types...")
    request_header = {'content-type': 'application/json'}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return ['path_integer is required.']

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return ['path_integer32 is required.']

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return ['path_integer64 is required.']

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return ['path_number is required.']

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return ['path_float is required.']

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return ['path_double is required.']

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return ['path_string is required.']

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return ['path_string_byte is required.']

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return ['path_string_binary is required.']

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return ['path_boolean is required.']

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return ['path_date is required.']

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return ['path_date_time is required.']

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return ['path_password is required.']

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return ['path_array_integer is required.']

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return ['path_array_integer32 is required.']

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return ['path_array_integer64 is required.']

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return ['path_array_number is required.']

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return ['path_array_float is required.']

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return ['path_array_double is required.']

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return ['path_array_string is required.']

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return ['path_array_string_byte is required.']

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return ['path_array_string_binary is required.']

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return ['path_array_boolean is required.']

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return ['path_array_date is required.']

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return ['path_array_date_time is required.']

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return ['path_array_password is required.']


    response = None
    try:
        response = requests.post('http://localhost:8954/test/json/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_post_test_json_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_post_test_json_with_all_paths_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_post_test_json_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_post_test_json_with_all_paths_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
@xw.ret(expand='table')
def json_test_put_test_json_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling json_test_put_test_json_with_all_paths_types...")
    request_header = {'content-type': 'application/json'}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return ['path_integer is required.']

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return ['path_integer32 is required.']

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return ['path_integer64 is required.']

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return ['path_number is required.']

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return ['path_float is required.']

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return ['path_double is required.']

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return ['path_string is required.']

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return ['path_string_byte is required.']

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return ['path_string_binary is required.']

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return ['path_boolean is required.']

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return ['path_date is required.']

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return ['path_date_time is required.']

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return ['path_password is required.']

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return ['path_array_integer is required.']

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return ['path_array_integer32 is required.']

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return ['path_array_integer64 is required.']

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return ['path_array_number is required.']

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return ['path_array_float is required.']

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return ['path_array_double is required.']

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return ['path_array_string is required.']

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return ['path_array_string_byte is required.']

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return ['path_array_string_binary is required.']

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return ['path_array_boolean is required.']

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return ['path_array_date is required.']

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return ['path_array_date_time is required.']

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return ['path_array_password is required.']


    response = None
    try:
        response = requests.put('http://localhost:8954/test/json/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_put_test_json_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_put_test_json_with_all_paths_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_put_test_json_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_put_test_json_with_all_paths_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='json_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
@xw.ret(expand='table')
def json_test_delete_test_json_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling json_test_delete_test_json_with_all_paths_types...")
    request_header = {'content-type': 'application/json'}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return ['path_integer is required.']

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return ['path_integer32 is required.']

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return ['path_integer64 is required.']

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return ['path_number is required.']

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return ['path_float is required.']

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return ['path_double is required.']

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return ['path_string is required.']

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return ['path_string_byte is required.']

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return ['path_string_binary is required.']

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return ['path_boolean is required.']

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return ['path_date is required.']

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return ['path_date_time is required.']

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return ['path_password is required.']

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return ['path_array_integer is required.']

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return ['path_array_integer32 is required.']

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return ['path_array_integer64 is required.']

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return ['path_array_number is required.']

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return ['path_array_float is required.']

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return ['path_array_double is required.']

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return ['path_array_string is required.']

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return ['path_array_string_byte is required.']

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return ['path_array_string_binary is required.']

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return ['path_array_boolean is required.']

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return ['path_array_date is required.']

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return ['path_array_date_time is required.']

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return ['path_array_password is required.']


    response = None
    try:
        response = requests.delete('http://localhost:8954/test/json/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_delete_test_json_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict([('items', OrderedDict([('format', 'date'), ('type', 'string')])), ('type', 'array')])), ('query_array_date_time', OrderedDict([('items', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('type', 'array')])), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict([('format', 'date'), ('type', 'string')])), ('query_date_time', OrderedDict([('format', 'date-time'), ('type', 'string')])), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_delete_test_json_with_all_paths_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling json_test_delete_test_json_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_delete_test_json_with_all_paths_types.")
        return [describe_error(response, error)]

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def plain_text_test_get_test_plain_text_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling plain_text_test_get_test_plain_text_with_all_optional_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.get('http://localhost:8955/test/plain/text/with/all/optional/parameters/types'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_get_test_plain_text_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_get_test_plain_text_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_get_test_plain_text_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_get_test_plain_text_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def plain_text_test_post_test_plain_text_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling plain_text_test_post_test_plain_text_with_all_optional_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.post('http://localhost:8955/test/plain/text/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_post_test_plain_text_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_post_test_plain_text_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_post_test_plain_text_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_post_test_plain_text_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def plain_text_test_put_test_plain_text_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling plain_text_test_put_test_plain_text_with_all_optional_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.put('http://localhost:8955/test/plain/text/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_put_test_plain_text_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_put_test_plain_text_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_put_test_plain_text_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_put_test_plain_text_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def plain_text_test_delete_test_plain_text_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    logging.info("Calling plain_text_test_delete_test_plain_text_with_all_optional_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.delete('http://localhost:8955/test/plain/text/with/all/optional/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_delete_test_plain_text_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_delete_test_plain_text_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_delete_test_plain_text_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_delete_test_plain_text_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def plain_text_test_get_test_plain_text_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling plain_text_test_get_test_plain_text_with_all_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return 'query_integer is required.'
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return 'query_integer32 is required.'
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return 'query_integer64 is required.'
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return 'query_number is required.'
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return 'query_float is required.'
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return 'query_double is required.'
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return 'query_string is required.'
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return 'query_string_byte is required.'
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return 'query_string_binary is required.'
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return 'query_boolean is required.'
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return 'query_date is required.'
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return 'query_date_time is required.'
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return 'query_password is required.'
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return 'query_array_integer is required.'
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return 'query_array_integer32 is required.'
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return 'query_array_integer64 is required.'
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return 'query_array_number is required.'
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return 'query_array_float is required.'
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return 'query_array_double is required.'
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return 'query_array_string_byte is required.'
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return 'query_array_string_binary is required.'
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return 'query_array_boolean is required.'
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return 'query_array_date is required.'
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return 'query_array_date_time is required.'
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return 'query_array_password is required.'
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.get('http://localhost:8955/test/plain/text/with/all/parameters/types'.format(
), request_parameters, stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_get_test_plain_text_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_get_test_plain_text_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_get_test_plain_text_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_get_test_plain_text_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def plain_text_test_post_test_plain_text_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling plain_text_test_post_test_plain_text_with_all_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return 'query_integer is required.'
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return 'query_integer32 is required.'
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return 'query_integer64 is required.'
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return 'query_number is required.'
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return 'query_float is required.'
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return 'query_double is required.'
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return 'query_string is required.'
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return 'query_string_byte is required.'
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return 'query_string_binary is required.'
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return 'query_boolean is required.'
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return 'query_date is required.'
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return 'query_date_time is required.'
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return 'query_password is required.'
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return 'query_array_integer is required.'
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return 'query_array_integer32 is required.'
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return 'query_array_integer64 is required.'
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return 'query_array_number is required.'
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return 'query_array_float is required.'
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return 'query_array_double is required.'
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return 'query_array_string_byte is required.'
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return 'query_array_string_binary is required.'
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return 'query_array_boolean is required.'
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return 'query_array_date is required.'
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return 'query_array_date_time is required.'
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return 'query_array_password is required.'
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.post('http://localhost:8955/test/plain/text/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_post_test_plain_text_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_post_test_plain_text_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_post_test_plain_text_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_post_test_plain_text_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def plain_text_test_put_test_plain_text_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling plain_text_test_put_test_plain_text_with_all_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return 'query_integer is required.'
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return 'query_integer32 is required.'
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return 'query_integer64 is required.'
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return 'query_number is required.'
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return 'query_float is required.'
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return 'query_double is required.'
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return 'query_string is required.'
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return 'query_string_byte is required.'
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return 'query_string_binary is required.'
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return 'query_boolean is required.'
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return 'query_date is required.'
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return 'query_date_time is required.'
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return 'query_password is required.'
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return 'query_array_integer is required.'
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return 'query_array_integer32 is required.'
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return 'query_array_integer64 is required.'
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return 'query_array_number is required.'
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return 'query_array_float is required.'
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return 'query_array_double is required.'
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return 'query_array_string_byte is required.'
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return 'query_array_string_binary is required.'
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return 'query_array_boolean is required.'
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return 'query_array_date is required.'
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return 'query_array_date_time is required.'
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return 'query_array_password is required.'
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.put('http://localhost:8955/test/plain/text/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_put_test_plain_text_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_put_test_plain_text_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_put_test_plain_text_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_put_test_plain_text_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('query_integer', numbers=int, doc='integer parameter')
@xw.arg('query_integer32', numbers=int, doc='integer 32 parameter')
@xw.arg('query_integer64', numbers=int, doc='integer 64 parameter')
@xw.arg('query_number', numbers=float, doc='number parameter')
@xw.arg('query_float', numbers=float, doc='number float parameter')
@xw.arg('query_double', numbers=float, doc='number double parameter')
@xw.arg('query_string', doc='string parameter')
@xw.arg('query_string_byte', doc='string byte parameter')
@xw.arg('query_string_binary', doc='string binary parameter')
@xw.arg('query_boolean', doc='boolean parameter')
@xw.arg('query_date', dates=datetime.date, doc='date parameter')
@xw.arg('query_date_time', dates=datetime.datetime, doc='date time parameter')
@xw.arg('query_password', doc='password parameter')
@xw.arg('query_array_integer', doc='integer array parameter')
@xw.arg('query_array_integer32', doc='integer 32 array parameter')
@xw.arg('query_array_integer64', doc='integer 64 array parameter')
@xw.arg('query_array_number', doc='number array parameter')
@xw.arg('query_array_float', doc='number float array parameter')
@xw.arg('query_array_double', doc='number double array parameter')
@xw.arg('query_array_string', doc='string array parameter')
@xw.arg('query_array_string_byte', doc='string byte array parameter')
@xw.arg('query_array_string_binary', doc='string binary array parameter')
@xw.arg('query_array_boolean', doc='boolean array parameter')
@xw.arg('query_array_date', doc='date array parameter')
@xw.arg('query_array_date_time', doc='date time array parameter')
@xw.arg('query_array_password', doc='password array parameter')
def plain_text_test_delete_test_plain_text_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    logging.info("Calling plain_text_test_delete_test_plain_text_with_all_parameters_types...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if query_integer is None or isinstance(query_integer, list) and all(x is None for x in query_integer):
        logging.error('query_integer is required.')
        return 'query_integer is required.'
    if query_integer is not None:
        if not isinstance(query_integer, int):
            logging.error('query_integer must be an integer.')
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32 is None or isinstance(query_integer32, list) and all(x is None for x in query_integer32):
        logging.error('query_integer32 is required.')
        return 'query_integer32 is required.'
    if query_integer32 is not None:
        if not isinstance(query_integer32, int):
            logging.error('query_integer32 must be an integer.')
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64 is None or isinstance(query_integer64, list) and all(x is None for x in query_integer64):
        logging.error('query_integer64 is required.')
        return 'query_integer64 is required.'
    if query_integer64 is not None:
        if not isinstance(query_integer64, int):
            logging.error('query_integer64 must be an integer.')
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number is None or isinstance(query_number, list) and all(x is None for x in query_number):
        logging.error('query_number is required.')
        return 'query_number is required.'
    if query_number is not None:
        if not isinstance(query_number, float):
            logging.error('query_number must be a number.')
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float is None or isinstance(query_float, list) and all(x is None for x in query_float):
        logging.error('query_float is required.')
        return 'query_float is required.'
    if query_float is not None:
        if not isinstance(query_float, float):
            logging.error('query_float must be a number.')
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double is None or isinstance(query_double, list) and all(x is None for x in query_double):
        logging.error('query_double is required.')
        return 'query_double is required.'
    if query_double is not None:
        if not isinstance(query_double, float):
            logging.error('query_double must be a number.')
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string is None or isinstance(query_string, list) and all(x is None for x in query_string):
        logging.error('query_string is required.')
        return 'query_string is required.'
    if query_string is not None:

        request_parameters['query_string'] = query_string

    if query_string_byte is None or isinstance(query_string_byte, list) and all(x is None for x in query_string_byte):
        logging.error('query_string_byte is required.')
        return 'query_string_byte is required.'
    if query_string_byte is not None:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary is None or isinstance(query_string_binary, list) and all(x is None for x in query_string_binary):
        logging.error('query_string_binary is required.')
        return 'query_string_binary is required.'
    if query_string_binary is not None:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean is None or isinstance(query_boolean, list) and all(x is None for x in query_boolean):
        logging.error('query_boolean is required.')
        return 'query_boolean is required.'
    if query_boolean is not None:
        if query_boolean not in ['true', 'false']:
            logging.error('query_boolean must be either "true" or "false".')
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date is None or isinstance(query_date, list) and all(x is None for x in query_date):
        logging.error('query_date is required.')
        return 'query_date is required.'
    if query_date is not None:
        if not isinstance(query_date, datetime.date):
            logging.error('query_date must be a date.')
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time is None or isinstance(query_date_time, list) and all(x is None for x in query_date_time):
        logging.error('query_date_time is required.')
        return 'query_date_time is required.'
    if query_date_time is not None:
        if not isinstance(query_date_time, datetime.datetime):
            logging.error('query_date_time must be a date time.')
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password is None or isinstance(query_password, list) and all(x is None for x in query_password):
        logging.error('query_password is required.')
        return 'query_password is required.'
    if query_password is not None:

        request_parameters['query_password'] = query_password

    if query_array_integer is None or isinstance(query_array_integer, list) and all(x is None for x in query_array_integer):
        logging.error('query_array_integer is required.')
        return 'query_array_integer is required.'
    if query_array_integer is not None:
        if isinstance(query_array_integer, list):
            query_array_integer = [item for item in query_array_integer if item is not None]
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    logging.error('query_array_integer must contain integers.')
                    return 'query_array_integer must contain integers.'
        else:
            if not isinstance(query_array_integer, int):
                logging.error('query_array_integer must be an integer.')
                return 'query_array_integer must be an integer.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32 is None or isinstance(query_array_integer32, list) and all(x is None for x in query_array_integer32):
        logging.error('query_array_integer32 is required.')
        return 'query_array_integer32 is required.'
    if query_array_integer32 is not None:
        if isinstance(query_array_integer32, list):
            query_array_integer32 = [item for item in query_array_integer32 if item is not None]
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    logging.error('query_array_integer32 must contain integers.')
                    return 'query_array_integer32 must contain integers.'
        else:
            if not isinstance(query_array_integer32, int):
                logging.error('query_array_integer32 must be an integer.')
                return 'query_array_integer32 must be an integer.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64 is None or isinstance(query_array_integer64, list) and all(x is None for x in query_array_integer64):
        logging.error('query_array_integer64 is required.')
        return 'query_array_integer64 is required.'
    if query_array_integer64 is not None:
        if isinstance(query_array_integer64, list):
            query_array_integer64 = [item for item in query_array_integer64 if item is not None]
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    logging.error('query_array_integer64 must contain integers.')
                    return 'query_array_integer64 must contain integers.'
        else:
            if not isinstance(query_array_integer64, int):
                logging.error('query_array_integer64 must be an integer.')
                return 'query_array_integer64 must be an integer.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number is None or isinstance(query_array_number, list) and all(x is None for x in query_array_number):
        logging.error('query_array_number is required.')
        return 'query_array_number is required.'
    if query_array_number is not None:
        if isinstance(query_array_number, list):
            query_array_number = [item for item in query_array_number if item is not None]
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    logging.error('query_array_number must contain numbers.')
                    return 'query_array_number must contain numbers.'
        else:
            if not isinstance(query_array_number, float):
                logging.error('query_array_number must be a number.')
                return 'query_array_number must be a number.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float is None or isinstance(query_array_float, list) and all(x is None for x in query_array_float):
        logging.error('query_array_float is required.')
        return 'query_array_float is required.'
    if query_array_float is not None:
        if isinstance(query_array_float, list):
            query_array_float = [item for item in query_array_float if item is not None]
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    logging.error('query_array_float must contain numbers.')
                    return 'query_array_float must contain numbers.'
        else:
            if not isinstance(query_array_float, float):
                logging.error('query_array_float must be a number.')
                return 'query_array_float must be a number.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double is None or isinstance(query_array_double, list) and all(x is None for x in query_array_double):
        logging.error('query_array_double is required.')
        return 'query_array_double is required.'
    if query_array_double is not None:
        if isinstance(query_array_double, list):
            query_array_double = [item for item in query_array_double if item is not None]
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    logging.error('query_array_double must contain numbers.')
                    return 'query_array_double must contain numbers.'
        else:
            if not isinstance(query_array_double, float):
                logging.error('query_array_double must be a number.')
                return 'query_array_double must be a number.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string is None or isinstance(query_array_string, list) and all(x is None for x in query_array_string):
        logging.error('query_array_string is required.')
        return 'query_array_string is required.'
    if query_array_string is not None:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte is None or isinstance(query_array_string_byte, list) and all(x is None for x in query_array_string_byte):
        logging.error('query_array_string_byte is required.')
        return 'query_array_string_byte is required.'
    if query_array_string_byte is not None:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary is None or isinstance(query_array_string_binary, list) and all(x is None for x in query_array_string_binary):
        logging.error('query_array_string_binary is required.')
        return 'query_array_string_binary is required.'
    if query_array_string_binary is not None:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean is None or isinstance(query_array_boolean, list) and all(x is None for x in query_array_boolean):
        logging.error('query_array_boolean is required.')
        return 'query_array_boolean is required.'
    if query_array_boolean is not None:
        if isinstance(query_array_boolean, list):
            query_array_boolean = [item for item in query_array_boolean if item is not None]
            for query_array_boolean_item in query_array_boolean:
                if query_array_boolean_item not in ['true', 'false']:
                    logging.error('query_array_boolean must be either "true" or "false".')
                    return 'query_array_boolean must be either "true" or "false".'
                else:
                    query_array_boolean_item = query_array_boolean_item == 'true'
        else:
            if query_array_boolean not in ['true', 'false']:
                logging.error('query_array_boolean must contain "true" or "false".')
                return 'query_array_boolean must contain "true" or "false".'
            query_array_boolean = query_array_boolean == 'true'

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date is None or isinstance(query_array_date, list) and all(x is None for x in query_array_date):
        logging.error('query_array_date is required.')
        return 'query_array_date is required.'
    if query_array_date is not None:
        if isinstance(query_array_date, list):
            query_array_date = [item for item in query_array_date if item is not None]
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    logging.error('query_array_date must contain dates.')
                    return 'query_array_date must contain dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                logging.error('query_array_date must be a date.')
                return 'query_array_date must be a date.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time is None or isinstance(query_array_date_time, list) and all(x is None for x in query_array_date_time):
        logging.error('query_array_date_time is required.')
        return 'query_array_date_time is required.'
    if query_array_date_time is not None:
        if isinstance(query_array_date_time, list):
            query_array_date_time = [item for item in query_array_date_time if item is not None]
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    logging.error('query_array_date_time must contain date times.')
                    return 'query_array_date_time must contain date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                logging.error('query_array_date_time must be a date time.')
                return 'query_array_date_time must be a date time.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password is None or isinstance(query_array_password, list) and all(x is None for x in query_array_password):
        logging.error('query_array_password is required.')
        return 'query_array_password is required.'
    if query_array_password is not None:

        request_parameters['query_array_password'] = query_array_password


    response = None
    try:
        response = requests.delete('http://localhost:8955/test/plain/text/with/all/parameters/types'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_delete_test_plain_text_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_delete_test_plain_text_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_delete_test_plain_text_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_delete_test_plain_text_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
def plain_text_test_get_test_plain_text_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling plain_text_test_get_test_plain_text_with_all_paths_types...")
    request_header = {}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return 'path_integer is required.'

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return 'path_integer32 is required.'

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return 'path_integer64 is required.'

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return 'path_number is required.'

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return 'path_float is required.'

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return 'path_double is required.'

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return 'path_string is required.'

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return 'path_string_byte is required.'

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return 'path_string_binary is required.'

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return 'path_boolean is required.'

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return 'path_date is required.'

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return 'path_date_time is required.'

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return 'path_password is required.'

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return 'path_array_integer is required.'

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return 'path_array_integer32 is required.'

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return 'path_array_integer64 is required.'

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return 'path_array_number is required.'

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return 'path_array_float is required.'

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return 'path_array_double is required.'

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return 'path_array_string is required.'

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return 'path_array_string_byte is required.'

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return 'path_array_string_binary is required.'

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return 'path_array_boolean is required.'

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return 'path_array_date is required.'

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return 'path_array_date_time is required.'

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return 'path_array_password is required.'


    response = None
    try:
        response = requests.get('http://localhost:8955/test/plain/text/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True, verify=False, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_get_test_plain_text_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_get_test_plain_text_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_get_test_plain_text_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_get_test_plain_text_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
def plain_text_test_post_test_plain_text_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling plain_text_test_post_test_plain_text_with_all_paths_types...")
    request_header = {}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return 'path_integer is required.'

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return 'path_integer32 is required.'

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return 'path_integer64 is required.'

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return 'path_number is required.'

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return 'path_float is required.'

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return 'path_double is required.'

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return 'path_string is required.'

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return 'path_string_byte is required.'

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return 'path_string_binary is required.'

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return 'path_boolean is required.'

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return 'path_date is required.'

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return 'path_date_time is required.'

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return 'path_password is required.'

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return 'path_array_integer is required.'

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return 'path_array_integer32 is required.'

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return 'path_array_integer64 is required.'

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return 'path_array_number is required.'

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return 'path_array_float is required.'

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return 'path_array_double is required.'

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return 'path_array_string is required.'

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return 'path_array_string_byte is required.'

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return 'path_array_string_binary is required.'

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return 'path_array_boolean is required.'

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return 'path_array_date is required.'

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return 'path_array_date_time is required.'

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return 'path_array_password is required.'


    response = None
    try:
        response = requests.post('http://localhost:8955/test/plain/text/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_post_test_plain_text_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_post_test_plain_text_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_post_test_plain_text_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_post_test_plain_text_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
def plain_text_test_put_test_plain_text_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling plain_text_test_put_test_plain_text_with_all_paths_types...")
    request_header = {}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return 'path_integer is required.'

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return 'path_integer32 is required.'

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return 'path_integer64 is required.'

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return 'path_number is required.'

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return 'path_float is required.'

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return 'path_double is required.'

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return 'path_string is required.'

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return 'path_string_byte is required.'

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return 'path_string_binary is required.'

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return 'path_boolean is required.'

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return 'path_date is required.'

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return 'path_date_time is required.'

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return 'path_password is required.'

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return 'path_array_integer is required.'

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return 'path_array_integer32 is required.'

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return 'path_array_integer64 is required.'

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return 'path_array_number is required.'

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return 'path_array_float is required.'

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return 'path_array_double is required.'

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return 'path_array_string is required.'

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return 'path_array_string_byte is required.'

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return 'path_array_string_binary is required.'

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return 'path_array_boolean is required.'

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return 'path_array_date is required.'

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return 'path_array_date_time is required.'

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return 'path_array_password is required.'


    response = None
    try:
        response = requests.put('http://localhost:8955/test/plain/text/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_put_test_plain_text_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_put_test_plain_text_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_put_test_plain_text_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_put_test_plain_text_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()

@xw.func(category='plain_text_test', call_in_wizard=False)
@xw.arg('path_integer', numbers=int, doc='integer path')
@xw.arg('path_integer32', numbers=int, doc='integer 32 path')
@xw.arg('path_integer64', numbers=int, doc='integer 64 path')
@xw.arg('path_number', numbers=float, doc='number path')
@xw.arg('path_float', numbers=float, doc='number float path')
@xw.arg('path_double', numbers=float, doc='number double path')
@xw.arg('path_string', doc='string path')
@xw.arg('path_string_byte', doc='string byte path')
@xw.arg('path_string_binary', doc='string binary path')
@xw.arg('path_boolean', doc='boolean path')
@xw.arg('path_date', dates=datetime.date, doc='date path')
@xw.arg('path_date_time', dates=datetime.datetime, doc='date time path')
@xw.arg('path_password', doc='password path')
@xw.arg('path_array_integer', doc='integer array path')
@xw.arg('path_array_integer32', doc='integer 32 array path')
@xw.arg('path_array_integer64', doc='integer 64 array path')
@xw.arg('path_array_number', doc='number array path')
@xw.arg('path_array_float', doc='number float array path')
@xw.arg('path_array_double', doc='number double array path')
@xw.arg('path_array_string', doc='string array path')
@xw.arg('path_array_string_byte', doc='string byte array path')
@xw.arg('path_array_string_binary', doc='string binary array path')
@xw.arg('path_array_boolean', doc='boolean array path')
@xw.arg('path_array_date', doc='date array path')
@xw.arg('path_array_date_time', doc='date time array path')
@xw.arg('path_array_password', doc='password array path')
def plain_text_test_delete_test_plain_text_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    logging.info("Calling plain_text_test_delete_test_plain_text_with_all_paths_types...")
    request_header = {}
    if path_integer is None or isinstance(path_integer, list) and all(x is None for x in path_integer):
        logging.error('path_integer is required.')
        return 'path_integer is required.'

    if path_integer32 is None or isinstance(path_integer32, list) and all(x is None for x in path_integer32):
        logging.error('path_integer32 is required.')
        return 'path_integer32 is required.'

    if path_integer64 is None or isinstance(path_integer64, list) and all(x is None for x in path_integer64):
        logging.error('path_integer64 is required.')
        return 'path_integer64 is required.'

    if path_number is None or isinstance(path_number, list) and all(x is None for x in path_number):
        logging.error('path_number is required.')
        return 'path_number is required.'

    if path_float is None or isinstance(path_float, list) and all(x is None for x in path_float):
        logging.error('path_float is required.')
        return 'path_float is required.'

    if path_double is None or isinstance(path_double, list) and all(x is None for x in path_double):
        logging.error('path_double is required.')
        return 'path_double is required.'

    if path_string is None or isinstance(path_string, list) and all(x is None for x in path_string):
        logging.error('path_string is required.')
        return 'path_string is required.'

    if path_string_byte is None or isinstance(path_string_byte, list) and all(x is None for x in path_string_byte):
        logging.error('path_string_byte is required.')
        return 'path_string_byte is required.'

    if path_string_binary is None or isinstance(path_string_binary, list) and all(x is None for x in path_string_binary):
        logging.error('path_string_binary is required.')
        return 'path_string_binary is required.'

    if path_boolean is None or isinstance(path_boolean, list) and all(x is None for x in path_boolean):
        logging.error('path_boolean is required.')
        return 'path_boolean is required.'

    if path_date is None or isinstance(path_date, list) and all(x is None for x in path_date):
        logging.error('path_date is required.')
        return 'path_date is required.'

    if path_date_time is None or isinstance(path_date_time, list) and all(x is None for x in path_date_time):
        logging.error('path_date_time is required.')
        return 'path_date_time is required.'

    if path_password is None or isinstance(path_password, list) and all(x is None for x in path_password):
        logging.error('path_password is required.')
        return 'path_password is required.'

    if path_array_integer is None or isinstance(path_array_integer, list) and all(x is None for x in path_array_integer):
        logging.error('path_array_integer is required.')
        return 'path_array_integer is required.'

    if path_array_integer32 is None or isinstance(path_array_integer32, list) and all(x is None for x in path_array_integer32):
        logging.error('path_array_integer32 is required.')
        return 'path_array_integer32 is required.'

    if path_array_integer64 is None or isinstance(path_array_integer64, list) and all(x is None for x in path_array_integer64):
        logging.error('path_array_integer64 is required.')
        return 'path_array_integer64 is required.'

    if path_array_number is None or isinstance(path_array_number, list) and all(x is None for x in path_array_number):
        logging.error('path_array_number is required.')
        return 'path_array_number is required.'

    if path_array_float is None or isinstance(path_array_float, list) and all(x is None for x in path_array_float):
        logging.error('path_array_float is required.')
        return 'path_array_float is required.'

    if path_array_double is None or isinstance(path_array_double, list) and all(x is None for x in path_array_double):
        logging.error('path_array_double is required.')
        return 'path_array_double is required.'

    if path_array_string is None or isinstance(path_array_string, list) and all(x is None for x in path_array_string):
        logging.error('path_array_string is required.')
        return 'path_array_string is required.'

    if path_array_string_byte is None or isinstance(path_array_string_byte, list) and all(x is None for x in path_array_string_byte):
        logging.error('path_array_string_byte is required.')
        return 'path_array_string_byte is required.'

    if path_array_string_binary is None or isinstance(path_array_string_binary, list) and all(x is None for x in path_array_string_binary):
        logging.error('path_array_string_binary is required.')
        return 'path_array_string_binary is required.'

    if path_array_boolean is None or isinstance(path_array_boolean, list) and all(x is None for x in path_array_boolean):
        logging.error('path_array_boolean is required.')
        return 'path_array_boolean is required.'

    if path_array_date is None or isinstance(path_array_date, list) and all(x is None for x in path_array_date):
        logging.error('path_array_date is required.')
        return 'path_array_date is required.'

    if path_array_date_time is None or isinstance(path_array_date_time, list) and all(x is None for x in path_array_date_time):
        logging.error('path_array_date_time is required.')
        return 'path_array_date_time is required.'

    if path_array_password is None or isinstance(path_array_password, list) and all(x is None for x in path_array_password):
        logging.error('path_array_password is required.')
        return 'path_array_password is required.'


    response = None
    try:
        response = requests.delete('http://localhost:8955/test/plain/text/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_delete_test_plain_text_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            return json_as_list(response, all_responses, all_definitions, False)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_delete_test_plain_text_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response is not None:
            logging.exception("Error occurred while handling plain_text_test_delete_test_plain_text_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_delete_test_plain_text_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response is not None:
            response.close()


def json_as_list(response, all_responses, all_definitions, rely_on_definitions):
    if rely_on_definitions:
        definition_deserializer.all_definitions = {}
        response_text = response.text
        logging.debug('Converting JSON string to corresponding python structure using ujson (relying on definitions)...')
        json_data = ujson.loads(response_text) if response_text != '' else response_text
        return Response(all_responses, response.status_code, all_definitions).rows(json_data)

    logging.debug('Converting JSON string to corresponding python structure...')
    json_data = response.json(object_pairs_hook=OrderedDict) if len(response.content) else ''
    return Flattenizer(all_responses, response.status_code, all_definitions).to_list(json_data)


def msgpackpandas_as_list(msgpack_pandas):
    logging.debug('Converting message pack pandas to list...')
    data = pandas.read_msgpack(msgpack_pandas)
    logging.debug('Converting dictionary to list...')
    header = [header_name.decode() for header_name in data.columns.values.tolist()]
    values = data.values.tolist()
    flatten_data = [header] + values if values else [header]
    logging.debug('Data converted to list.')
    return flatten_data


def describe_error(response, error):
    if response is not None:
        return 'An error occurred. Please check logs for full details: "{0}"'.format(response.text[:198])
    return 'An error occurred. Please check logs for full details: "{0}"'.format(str(error)[:198])