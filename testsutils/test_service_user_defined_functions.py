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
from definition_deserializer import Response
import authentication







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
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_get_test_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_get_test_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_get_test_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_get_test_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_post_test_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_post_test_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_post_test_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_put_test_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_put_test_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_put_test_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_delete_test_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_delete_test_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_delete_test_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_get_test_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_get_test_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_get_test_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_get_test_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_post_test_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_post_test_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_post_test_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_put_test_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_put_test_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_put_test_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_delete_test_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_delete_test_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_delete_test_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for usual_parameters_test_get_test_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_get_test_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_get_test_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_get_test_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_post_test_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_post_test_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_post_test_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_put_test_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_put_test_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_put_test_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling usual_parameters_test_delete_test_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling usual_parameters_test_delete_test_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling usual_parameters_test_delete_test_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='filtered_tags_test', call_in_wizard=False)
def filtered_tags_test_get_test_with_tags():
    logging.info("Calling filtered_tags_test_get_test_with_tags...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8944/test/with/tags'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for filtered_tags_test_get_test_with_tags ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling filtered_tags_test_get_test_with_tags.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling filtered_tags_test_get_test_with_tags response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling filtered_tags_test_get_test_with_tags.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling filtered_tags_test_post_test_with_tags.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling filtered_tags_test_post_test_with_tags response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling filtered_tags_test_post_test_with_tags.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling filtered_tags_test_put_test_with_tags.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling filtered_tags_test_put_test_with_tags response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling filtered_tags_test_put_test_with_tags.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_empty_dictionary():
    logging.info("Calling values_false_test_get_test_with_empty_dictionary...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/empty/dictionary'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_empty_dictionary ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/EmptyDictionary')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_empty_dictionary.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling values_false_test_get_test_with_empty_dictionary response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_empty_dictionary.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_empty_list():
    logging.info("Calling values_false_test_get_test_with_empty_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/empty/list'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_empty_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/EmptyList')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_empty_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling values_false_test_get_test_with_empty_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_empty_list.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_empty_string():
    logging.info("Calling values_false_test_get_test_with_empty_string...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/empty/string'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_empty_string ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/EmptyString')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_empty_string.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling values_false_test_get_test_with_empty_string response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_empty_string.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_false_boolean():
    logging.info("Calling values_false_test_get_test_with_false_boolean...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/false/boolean'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_false_boolean ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/FalseBoolean')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_false_boolean.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling values_false_test_get_test_with_false_boolean response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_false_boolean.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_zero_float():
    logging.info("Calling values_false_test_get_test_with_zero_float...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/zero/float'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_zero_float ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/ZeroFloat')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_zero_float.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling values_false_test_get_test_with_zero_float response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_zero_float.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='values_false_test', call_in_wizard=False)
def values_false_test_get_test_with_zero_integer():
    logging.info("Calling values_false_test_get_test_with_zero_integer...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8945/test/with/zero/integer'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for values_false_test_get_test_with_zero_integer ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/ZeroInteger')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Empty', OrderedDict([('properties', OrderedDict())])), ('EmptyDictionary', OrderedDict([('properties', OrderedDict([('empty_dictionary', OrderedDict([('$ref', '#/definitions/Empty'), ('type', 'object')]))]))])), ('EmptyList', OrderedDict([('properties', OrderedDict([('empty_list', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Empty')])), ('type', 'array')]))]))])), ('EmptyString', OrderedDict([('properties', OrderedDict([('empty_string', OrderedDict([('type', 'string')]))]))])), ('FalseBoolean', OrderedDict([('properties', OrderedDict([('false_boolean', OrderedDict([('type', 'boolean')]))]))])), ('ZeroFloat', OrderedDict([('properties', OrderedDict([('zero_float', OrderedDict([('format', 'float'), ('type', 'number')]))]))])), ('ZeroInteger', OrderedDict([('properties', OrderedDict([('zero_integer', OrderedDict([('format', 'int32'), ('type', 'integer')]))]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling values_false_test_get_test_with_zero_integer.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling values_false_test_get_test_with_zero_integer response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling values_false_test_get_test_with_zero_integer.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='output_order_test', call_in_wizard=False)
@xw.arg('date', dates=datetime.date, doc='date')
@xw.arg('curve', doc='curvename')
@xw.arg('ts', doc='timeslot')
@xw.arg('mat', doc='maturity')
def output_order_test_get_test_price_unordered(date=None, curve=None, ts=None, mat=None):
    logging.info("Calling output_order_test_get_test_price_unordered...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if date is not None:
        if not isinstance(date, datetime.date):
            logging.error('date must be a date.')
            return 'date must be a date.'

        request_parameters['date'] = date

    if curve is not None:
        
        request_parameters['curve'] = curve

    if ts is not None:
        
        request_parameters['ts'] = ts

    if mat is not None:
        
        request_parameters['mat'] = mat


    response = None
    try:
        response = requests.get('http://localhost:8946/price/unordered'.format(
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for output_order_test_get_test_price_unordered ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Price')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Price', OrderedDict([('required', ['curve', 'date', 'mat', 'ts']), ('type', 'object'), ('properties', OrderedDict([('ts', OrderedDict([('type', 'string'), ('description', 'timeslot'), ('maxLength', 2)])), ('date', OrderedDict([('type', 'string'), ('description', 'date'), ('format', 'date')])), ('curve', OrderedDict([('type', 'string'), ('description', 'curvename'), ('maxLength', 20)])), ('mat', OrderedDict([('type', 'string'), ('description', 'maturity'), ('maxLength', 4)]))])), ('title', 'RealizedPrice')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling output_order_test_get_test_price_unordered.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling output_order_test_get_test_price_unordered response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling output_order_test_get_test_price_unordered.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_empty_nested_list():
    logging.info("Calling nested_data_test_get_test_dict_with_empty_nested_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/empty/nested/list'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_empty_nested_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_empty_nested_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_empty_nested_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_empty_nested_list.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_four_imbricated_levels():
    logging.info("Calling nested_data_test_get_test_dict_with_four_imbricated_levels...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/four/imbricated/levels'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_four_imbricated_levels ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_four_imbricated_levels.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_four_imbricated_levels response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_four_imbricated_levels.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys():
    logging.info("Calling nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/multiple/imbricated/levels/and/duplicate/keys'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_multiple_imbricated_levels_and_duplicate_keys.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_dict_with_three_imbricated_levels():
    logging.info("Calling nested_data_test_get_test_dict_with_three_imbricated_levels...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/dict/with/three/imbricated/levels'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_dict_with_three_imbricated_levels ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_dict_with_three_imbricated_levels.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_dict_with_three_imbricated_levels response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_dict_with_three_imbricated_levels.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_empty_dict():
    logging.info("Calling nested_data_test_get_test_empty_dict...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/empty/dict'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_empty_dict ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_empty_dict.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_empty_dict response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_empty_dict.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_empty_list():
    logging.info("Calling nested_data_test_get_test_empty_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/empty/list'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_empty_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_empty_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_empty_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_empty_list.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_list_of_dict():
    logging.info("Calling nested_data_test_get_test_list_of_dict...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/list/of/dict'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_list_of_dict ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_list_of_dict.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_list_of_dict response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_list_of_dict.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_one_dict_entry_with_a_list():
    logging.info("Calling nested_data_test_get_test_one_dict_entry_with_a_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/one/dict/entry/with/a/list'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_one_dict_entry_with_a_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column1List')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_one_dict_entry_with_a_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_one_dict_entry_with_a_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_one_dict_entry_with_a_list.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_one_dict_entry_with_a_list_of_dict():
    logging.info("Calling nested_data_test_get_test_one_dict_entry_with_a_list_of_dict...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/one/dict/entry/with/a/list/of/dict'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_one_dict_entry_with_a_list_of_dict ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column1')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_one_dict_entry_with_a_list_of_dict.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_one_dict_entry_with_a_list_of_dict response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_one_dict_entry_with_a_list_of_dict.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_one_level_dict():
    logging.info("Calling nested_data_test_get_test_one_level_dict...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/one/level/dict'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_one_level_dict ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Column2And3')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_one_level_dict.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_one_level_dict response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_one_level_dict.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='nested_data_test', call_in_wizard=False)
def nested_data_test_get_test_one_level_list():
    logging.info("Calling nested_data_test_get_test_one_level_list...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8947/test/one/level/list'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for nested_data_test_get_test_one_level_list ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('Column', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 2', OrderedDict([('description', 'column2'), ('items', OrderedDict([('$ref', '#/definitions/Column')])), ('type', 'array')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column'), ('type', 'object')])), ('Column1', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/Column2And3')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column1List', OrderedDict([('properties', OrderedDict([('Column 1', OrderedDict([('items', OrderedDict([('type', 'string')])), ('type', 'array')]))])), ('title', 'Column1'), ('type', 'object')])), ('Column2And3', OrderedDict([('properties', OrderedDict([('Column 2', OrderedDict([('description', 'column1'), ('type', 'string')])), ('Column 3', OrderedDict([('description', 'column3'), ('type', 'string')]))])), ('title', 'Column2+3'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling nested_data_test_get_test_one_level_list.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling nested_data_test_get_test_one_level_list response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling nested_data_test_get_test_one_level_list.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='vba_keywords_test', call_in_wizard=False)
@xw.arg('currency_visual_basic', doc='currency parameter')
@xw.arg('end_visual_basic', doc='end parameter')
def vba_keywords_test_get_test_vba_restricted_keywords(currency_visual_basic, end_visual_basic):
    logging.info("Calling vba_keywords_test_get_test_vba_restricted_keywords...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if currency_visual_basic is None or isinstance(currency_visual_basic, list) and all(x is None for x in currency_visual_basic):
        logging.error('currency_visual_basic is required.')
        return 'currency_visual_basic is required.'
    if currency_visual_basic is not None:
        
        request_parameters['currency'] = currency_visual_basic

    if end_visual_basic is None or isinstance(end_visual_basic, list) and all(x is None for x in end_visual_basic):
        logging.error('end_visual_basic is required.')
        return 'end_visual_basic is required.'
    if end_visual_basic is not None:
        
        request_parameters['end'] = end_visual_basic


    response = None
    try:
        response = requests.get('http://localhost:8949/test/vba/restricted/keywords'.format(
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for vba_keywords_test_get_test_vba_restricted_keywords ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('$ref', '#/definitions/Test')]))]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict([('currency', OrderedDict()), ('end', OrderedDict())]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling vba_keywords_test_get_test_vba_restricted_keywords.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling vba_keywords_test_get_test_vba_restricted_keywords response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling vba_keywords_test_get_test_vba_restricted_keywords.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='vba_keywords_test', call_in_wizard=False)
@xw.arg('currency_visual_basic', doc='currency parameter')
@xw.arg('end_visual_basic', doc='end parameter')
def vba_keywords_test_post_test_vba_restricted_keywords(currency_visual_basic, end_visual_basic):
    logging.info("Calling vba_keywords_test_post_test_vba_restricted_keywords...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if currency_visual_basic is None or isinstance(currency_visual_basic, list) and all(x is None for x in currency_visual_basic):
        logging.error('currency_visual_basic is required.')
        return 'currency_visual_basic is required.'
    if currency_visual_basic is not None:
        
        request_parameters['currency'] = currency_visual_basic

    if end_visual_basic is None or isinstance(end_visual_basic, list) and all(x is None for x in end_visual_basic):
        logging.error('end_visual_basic is required.')
        return 'end_visual_basic is required.'
    if end_visual_basic is not None:
        
        request_parameters['end'] = end_visual_basic


    response = None
    try:
        response = requests.post('http://localhost:8949/test/vba/restricted/keywords'.format(
), json=request_payload, params=request_parameters, files=request_files, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for vba_keywords_test_post_test_vba_restricted_keywords ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict([('currency', OrderedDict()), ('end', OrderedDict())]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling vba_keywords_test_post_test_vba_restricted_keywords.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling vba_keywords_test_post_test_vba_restricted_keywords response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling vba_keywords_test_post_test_vba_restricted_keywords.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='vba_keywords_test', call_in_wizard=False)
@xw.arg('currency_visual_basic', doc='currency parameter')
@xw.arg('end_visual_basic', doc='end parameter')
def vba_keywords_test_put_test_vba_restricted_keywords(currency_visual_basic, end_visual_basic):
    logging.info("Calling vba_keywords_test_put_test_vba_restricted_keywords...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if currency_visual_basic is None or isinstance(currency_visual_basic, list) and all(x is None for x in currency_visual_basic):
        logging.error('currency_visual_basic is required.')
        return 'currency_visual_basic is required.'
    if currency_visual_basic is not None:
        
        request_parameters['currency'] = currency_visual_basic

    if end_visual_basic is None or isinstance(end_visual_basic, list) and all(x is None for x in end_visual_basic):
        logging.error('end_visual_basic is required.')
        return 'end_visual_basic is required.'
    if end_visual_basic is not None:
        
        request_parameters['end'] = end_visual_basic


    response = None
    try:
        response = requests.put('http://localhost:8949/test/vba/restricted/keywords'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for vba_keywords_test_put_test_vba_restricted_keywords ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict([('currency', OrderedDict()), ('end', OrderedDict())]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling vba_keywords_test_put_test_vba_restricted_keywords.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling vba_keywords_test_put_test_vba_restricted_keywords response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling vba_keywords_test_put_test_vba_restricted_keywords.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='vba_keywords_test', call_in_wizard=False)
@xw.arg('currency_visual_basic', doc='currency parameter')
@xw.arg('end_visual_basic', doc='end parameter')
def vba_keywords_test_delete_test_vba_restricted_keywords(currency_visual_basic, end_visual_basic):
    logging.info("Calling vba_keywords_test_delete_test_vba_restricted_keywords...")
    request_header = {}
    request_payload = {}
    request_files = {}
    request_parameters = {}

    if currency_visual_basic is None or isinstance(currency_visual_basic, list) and all(x is None for x in currency_visual_basic):
        logging.error('currency_visual_basic is required.')
        return 'currency_visual_basic is required.'
    if currency_visual_basic is not None:
        
        request_parameters['currency'] = currency_visual_basic

    if end_visual_basic is None or isinstance(end_visual_basic, list) and all(x is None for x in end_visual_basic):
        logging.error('end_visual_basic is required.')
        return 'end_visual_basic is required.'
    if end_visual_basic is not None:
        
        request_parameters['end'] = end_visual_basic


    response = None
    try:
        response = requests.delete('http://localhost:8949/test/vba/restricted/keywords'.format(
), json=request_payload, params=request_parameters, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for vba_keywords_test_delete_test_vba_restricted_keywords ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict([('currency', OrderedDict()), ('end', OrderedDict())]))]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling vba_keywords_test_delete_test_vba_restricted_keywords.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling vba_keywords_test_delete_test_vba_restricted_keywords response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling vba_keywords_test_delete_test_vba_restricted_keywords.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
@xw.ret(expand='table')
def without_parameter_test_get_test_json_without_parameter():
    logging.info("Calling without_parameter_test_get_test_json_without_parameter...")
    request_header = {'content-type':'application/json'}

    response = None
    try:
        response = requests.get('http://localhost:8950/test/json/without/parameter'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_get_test_json_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_get_test_json_without_parameter.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_get_test_json_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_get_test_json_without_parameter.")
        return [describe_error(response, error)]

    finally:
        if response:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
@xw.ret(expand='table')
def without_parameter_test_post_test_json_without_parameter():
    logging.info("Calling without_parameter_test_post_test_json_without_parameter...")
    request_header = {'content-type':'application/json'}

    response = None
    try:
        response = requests.post('http://localhost:8950/test/json/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_post_test_json_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_post_test_json_without_parameter.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_post_test_json_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_post_test_json_without_parameter.")
        return [describe_error(response, error)]

    finally:
        if response:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
@xw.ret(expand='table')
def without_parameter_test_put_test_json_without_parameter():
    logging.info("Calling without_parameter_test_put_test_json_without_parameter...")
    request_header = {'content-type':'application/json'}

    response = None
    try:
        response = requests.put('http://localhost:8950/test/json/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_put_test_json_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_put_test_json_without_parameter.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_put_test_json_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_put_test_json_without_parameter.")
        return [describe_error(response, error)]

    finally:
        if response:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
@xw.ret(expand='table')
def without_parameter_test_delete_test_json_without_parameter():
    logging.info("Calling without_parameter_test_delete_test_json_without_parameter...")
    request_header = {'content-type':'application/json'}

    response = None
    try:
        response = requests.delete('http://localhost:8950/test/json/without/parameter'.format(
), proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_delete_test_json_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('$ref', '#/definitions/Test'), ('description', 'return value')]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_delete_test_json_without_parameter.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_delete_test_json_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_delete_test_json_without_parameter.")
        return [describe_error(response, error)]

    finally:
        if response:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_get_test_plain_text_without_parameter():
    logging.info("Calling without_parameter_test_get_test_plain_text_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8950/test/plain/text/without/parameter'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_get_test_plain_text_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('type', 'string')]))]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_get_test_plain_text_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_get_test_plain_text_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_get_test_plain_text_without_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_post_test_plain_text_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_post_test_plain_text_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_post_test_plain_text_without_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_put_test_plain_text_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_put_test_plain_text_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_put_test_plain_text_without_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_delete_test_plain_text_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_delete_test_plain_text_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_delete_test_plain_text_without_parameter.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()

@xw.func(category='without_parameter_test', call_in_wizard=False)
def without_parameter_test_get_test_without_parameter():
    logging.info("Calling without_parameter_test_get_test_without_parameter...")
    request_header = {}

    response = None
    try:
        response = requests.get('http://localhost:8950/test/without/parameter'.format(
), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for without_parameter_test_get_test_without_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value'), ('schema', OrderedDict([('type', 'string')]))]))])
            all_definitions = OrderedDict([('Test', OrderedDict([('properties', OrderedDict())]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_get_test_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_get_test_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_get_test_without_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_post_test_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_post_test_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_post_test_without_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_put_test_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_put_test_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_put_test_without_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling without_parameter_test_delete_test_without_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling without_parameter_test_delete_test_without_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling without_parameter_test_delete_test_without_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for header_parameter_test_get_test_header_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/Header')]))]))])
            all_definitions = OrderedDict([('Header', OrderedDict([('properties', OrderedDict([('Accept', OrderedDict([('type', 'string')])), ('Accept-Encoding', OrderedDict([('type', 'string')])), ('Connection', OrderedDict([('type', 'string')])), ('Content-Length', OrderedDict([('type', 'string')])), ('Content-Type', OrderedDict([('type', 'string')])), ('Header-String', OrderedDict([('type', 'string')])), ('Host', OrderedDict([('type', 'string')])), ('User-Agent', OrderedDict([('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling header_parameter_test_get_test_header_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling header_parameter_test_get_test_header_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling header_parameter_test_get_test_header_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling form_parameter_test_post_test_form_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling form_parameter_test_post_test_form_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling form_parameter_test_post_test_form_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for array_parameter_test_get_test_string_array_parameter ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling array_parameter_test_get_test_string_array_parameter.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling array_parameter_test_get_test_string_array_parameter response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling array_parameter_test_get_test_string_array_parameter.")
        return describe_error(response, error)

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_get_test_json_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_get_test_json_with_all_optional_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_get_test_json_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_get_test_json_with_all_optional_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_post_test_json_with_all_optional_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_post_test_json_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_post_test_json_with_all_optional_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_put_test_json_with_all_optional_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_put_test_json_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_put_test_json_with_all_optional_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_delete_test_json_with_all_optional_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_delete_test_json_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_delete_test_json_with_all_optional_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_get_test_json_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('$ref', '#/definitions/AllMandatoryParameters')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_get_test_json_with_all_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_get_test_json_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_get_test_json_with_all_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_post_test_json_with_all_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_post_test_json_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_post_test_json_with_all_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_put_test_json_with_all_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_put_test_json_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_put_test_json_with_all_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_delete_test_json_with_all_parameters_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_delete_test_json_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_delete_test_json_with_all_parameters_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for json_test_get_test_json_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'successful operation'), ('schema', OrderedDict([('items', OrderedDict([('$ref', '#/definitions/TestObject')])), ('type', 'array')]))]))])
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_get_test_json_with_all_paths_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_get_test_json_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_get_test_json_with_all_paths_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_post_test_json_with_all_paths_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_post_test_json_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_post_test_json_with_all_paths_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_put_test_json_with_all_paths_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_put_test_json_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_put_test_json_with_all_paths_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
    request_header = {'content-type':'application/json'}
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
            all_definitions = OrderedDict([('AllMandatoryParameters', OrderedDict([('properties', OrderedDict([('query_array_boolean', OrderedDict()), ('query_array_date', OrderedDict()), ('query_array_date_time', OrderedDict()), ('query_array_double', OrderedDict()), ('query_array_float', OrderedDict()), ('query_array_integer', OrderedDict()), ('query_array_integer32', OrderedDict()), ('query_array_integer64', OrderedDict()), ('query_array_number', OrderedDict()), ('query_array_password', OrderedDict()), ('query_array_string', OrderedDict()), ('query_array_string_binary', OrderedDict()), ('query_array_string_byte', OrderedDict()), ('query_boolean', OrderedDict()), ('query_date', OrderedDict()), ('query_date_time', OrderedDict()), ('query_double', OrderedDict()), ('query_float', OrderedDict()), ('query_integer', OrderedDict()), ('query_integer32', OrderedDict()), ('query_integer64', OrderedDict()), ('query_number', OrderedDict()), ('query_password', OrderedDict()), ('query_string', OrderedDict()), ('query_string_binary', OrderedDict()), ('query_string_byte', OrderedDict())]))])), ('TestObject', OrderedDict([('properties', OrderedDict([('test', OrderedDict([('description', 'test'), ('type', 'string')]))])), ('title', 'Test'), ('type', 'object')]))])
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling json_test_delete_test_json_with_all_paths_types.")
        return ['Cannot connect to service. Please retry once connection is re-established.']

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling json_test_delete_test_json_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling json_test_delete_test_json_with_all_paths_types.")
        return [describe_error(response, error)]

    finally:
        if response:
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
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_get_test_plain_text_with_all_optional_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_get_test_plain_text_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_get_test_plain_text_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_get_test_plain_text_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_post_test_plain_text_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_post_test_plain_text_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_post_test_plain_text_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_put_test_plain_text_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_put_test_plain_text_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_put_test_plain_text_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_delete_test_plain_text_with_all_optional_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_delete_test_plain_text_with_all_optional_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_delete_test_plain_text_with_all_optional_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
), request_parameters, stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_get_test_plain_text_with_all_parameters_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_get_test_plain_text_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_get_test_plain_text_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_get_test_plain_text_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_post_test_plain_text_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_post_test_plain_text_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_post_test_plain_text_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_put_test_plain_text_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_put_test_plain_text_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_put_test_plain_text_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_delete_test_plain_text_with_all_parameters_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_delete_test_plain_text_with_all_parameters_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_delete_test_plain_text_with_all_parameters_types.")
        return describe_error(response, error)

    finally:
        if response:
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
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True, headers=request_header, proxies={}, timeout=(1.0, None))

        response.raise_for_status()
        logging.info("Valid response received for plain_text_test_get_test_plain_text_with_all_paths_types ({0}).".format(response.request.url))
        if response.headers['content-type'] == 'application/json':
            all_responses = OrderedDict([('200', OrderedDict([('description', 'return value')]))])
            all_definitions = None
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_get_test_plain_text_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_get_test_plain_text_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_get_test_plain_text_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_post_test_plain_text_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_post_test_plain_text_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_post_test_plain_text_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_put_test_plain_text_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_put_test_plain_text_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_put_test_plain_text_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response:
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
            response_text = response.text
            return Response(all_responses, response.status_code, all_definitions).rows(ujson.loads(response_text) if response_text != '' else response_text)
        elif response.headers['content-type'] == 'application/msgpackpandas':
            return msgpackpandas_as_list(response.content)
        else:
            return response.text[:255]
    except requests.exceptions.ConnectionError:
        logging.exception("Connection error occurred while calling plain_text_test_delete_test_plain_text_with_all_paths_types.")
        return 'Cannot connect to service. Please retry once connection is re-established.'

    except Exception as error:
        if response:
            logging.exception("Error occurred while handling plain_text_test_delete_test_plain_text_with_all_paths_types response: {0}.".format(response.text))
        else:
            logging.exception("Error occurred while calling plain_text_test_delete_test_plain_text_with_all_paths_types.")
        return describe_error(response, error)

    finally:
        if response:
            response.close()


def msgpackpandas_as_list(msgpack_pandas):
    logging.warning('Pandas module is required to decode response.')
    return ['Please install pandas module to be able to decode result.']


def describe_error(response, error):
    if response:
        return 'An error occurred: "{0}" for value "{1}"'.format(str(error)[:66], response.text[:155])
    return str(error)[:255]