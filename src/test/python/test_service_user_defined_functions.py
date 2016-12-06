"""
This file was generated. DO NOT EDIT manually.
Source file: user_defined_functions.tpl
Generation date \(UTC\): \d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\d.\d\d\d\d\d\d
"""
import xlwings as xw
import requests
import datetime
from requests.exceptions import HTTPError







@xw.func(category='test')
def test_get_test_without_parameter():
    try:
        response = requests.get('http://localhost:8943/test/without/parameter'.format(
), stream=True)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
def test_post_test_without_parameter():
    try:
        response = requests.post('http://localhost:8943/test/without/parameter'.format(
))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
def test_put_test_without_parameter():
    try:
        response = requests.put('http://localhost:8943/test/without/parameter'.format(
))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
def test_delete_test_without_parameter():
    try:
        response = requests.delete('http://localhost:8943/test/without/parameter'.format(
))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
def test_get_test_plain_text_without_parameter():
    try:
        response = requests.get('http://localhost:8943/test/plain/text/without/parameter'.format(
), stream=True)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
def test_post_test_plain_text_without_parameter():
    try:
        response = requests.post('http://localhost:8943/test/plain/text/without/parameter'.format(
))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
def test_put_test_plain_text_without_parameter():
    try:
        response = requests.put('http://localhost:8943/test/plain/text/without/parameter'.format(
))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
def test_delete_test_plain_text_without_parameter():
    try:
        response = requests.delete('http://localhost:8943/test/plain/text/without/parameter'.format(
))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_get_test_plain_text_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.get('http://localhost:8943/test/plain/text/with/all/optional/parameters/types'.format(
), request_parameters, stream=True)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_post_test_plain_text_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.post('http://localhost:8943/test/plain/text/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_put_test_plain_text_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.put('http://localhost:8943/test/plain/text/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_delete_test_plain_text_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.delete('http://localhost:8943/test/plain/text/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
@xw.ret(expand='table')
def test_get_test_json_without_parameter():
    try:
        response = requests.get('http://localhost:8943/test/json/without/parameter'.format(
), stream=True)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
@xw.ret(expand='table')
def test_post_test_json_without_parameter():
    try:
        response = requests.post('http://localhost:8943/test/json/without/parameter'.format(
))

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
@xw.ret(expand='table')
def test_put_test_json_without_parameter():
    try:
        response = requests.put('http://localhost:8943/test/json/without/parameter'.format(
))

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
@xw.ret(expand='table')
def test_delete_test_json_without_parameter():
    try:
        response = requests.delete('http://localhost:8943/test/json/without/parameter'.format(
))

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_get_test_plain_text_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return 'path_integer is required.'

    if not path_integer32:
        return 'path_integer32 is required.'

    if not path_integer64:
        return 'path_integer64 is required.'

    if not path_number:
        return 'path_number is required.'

    if not path_float:
        return 'path_float is required.'

    if not path_double:
        return 'path_double is required.'

    if not path_string:
        return 'path_string is required.'

    if not path_string_byte:
        return 'path_string_byte is required.'

    if not path_string_binary:
        return 'path_string_binary is required.'

    if not path_boolean:
        return 'path_boolean is required.'

    if not path_date:
        return 'path_date is required.'

    if not path_date_time:
        return 'path_date_time is required.'

    if not path_password:
        return 'path_password is required.'

    if not path_array_integer:
        return 'path_array_integer is required.'

    if not path_array_integer32:
        return 'path_array_integer32 is required.'

    if not path_array_integer64:
        return 'path_array_integer64 is required.'

    if not path_array_number:
        return 'path_array_number is required.'

    if not path_array_float:
        return 'path_array_float is required.'

    if not path_array_double:
        return 'path_array_double is required.'

    if not path_array_string:
        return 'path_array_string is required.'

    if not path_array_string_byte:
        return 'path_array_string_byte is required.'

    if not path_array_string_binary:
        return 'path_array_string_binary is required.'

    if not path_array_boolean:
        return 'path_array_boolean is required.'

    if not path_array_date:
        return 'path_array_date is required.'

    if not path_array_date_time:
        return 'path_array_date_time is required.'

    if not path_array_password:
        return 'path_array_password is required.'

    try:
        response = requests.get('http://localhost:8943/test/plain/text/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_post_test_plain_text_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return 'path_integer is required.'

    if not path_integer32:
        return 'path_integer32 is required.'

    if not path_integer64:
        return 'path_integer64 is required.'

    if not path_number:
        return 'path_number is required.'

    if not path_float:
        return 'path_float is required.'

    if not path_double:
        return 'path_double is required.'

    if not path_string:
        return 'path_string is required.'

    if not path_string_byte:
        return 'path_string_byte is required.'

    if not path_string_binary:
        return 'path_string_binary is required.'

    if not path_boolean:
        return 'path_boolean is required.'

    if not path_date:
        return 'path_date is required.'

    if not path_date_time:
        return 'path_date_time is required.'

    if not path_password:
        return 'path_password is required.'

    if not path_array_integer:
        return 'path_array_integer is required.'

    if not path_array_integer32:
        return 'path_array_integer32 is required.'

    if not path_array_integer64:
        return 'path_array_integer64 is required.'

    if not path_array_number:
        return 'path_array_number is required.'

    if not path_array_float:
        return 'path_array_float is required.'

    if not path_array_double:
        return 'path_array_double is required.'

    if not path_array_string:
        return 'path_array_string is required.'

    if not path_array_string_byte:
        return 'path_array_string_byte is required.'

    if not path_array_string_binary:
        return 'path_array_string_binary is required.'

    if not path_array_boolean:
        return 'path_array_boolean is required.'

    if not path_array_date:
        return 'path_array_date is required.'

    if not path_array_date_time:
        return 'path_array_date_time is required.'

    if not path_array_password:
        return 'path_array_password is required.'

    try:
        response = requests.post('http://localhost:8943/test/plain/text/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_put_test_plain_text_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return 'path_integer is required.'

    if not path_integer32:
        return 'path_integer32 is required.'

    if not path_integer64:
        return 'path_integer64 is required.'

    if not path_number:
        return 'path_number is required.'

    if not path_float:
        return 'path_float is required.'

    if not path_double:
        return 'path_double is required.'

    if not path_string:
        return 'path_string is required.'

    if not path_string_byte:
        return 'path_string_byte is required.'

    if not path_string_binary:
        return 'path_string_binary is required.'

    if not path_boolean:
        return 'path_boolean is required.'

    if not path_date:
        return 'path_date is required.'

    if not path_date_time:
        return 'path_date_time is required.'

    if not path_password:
        return 'path_password is required.'

    if not path_array_integer:
        return 'path_array_integer is required.'

    if not path_array_integer32:
        return 'path_array_integer32 is required.'

    if not path_array_integer64:
        return 'path_array_integer64 is required.'

    if not path_array_number:
        return 'path_array_number is required.'

    if not path_array_float:
        return 'path_array_float is required.'

    if not path_array_double:
        return 'path_array_double is required.'

    if not path_array_string:
        return 'path_array_string is required.'

    if not path_array_string_byte:
        return 'path_array_string_byte is required.'

    if not path_array_string_binary:
        return 'path_array_string_binary is required.'

    if not path_array_boolean:
        return 'path_array_boolean is required.'

    if not path_array_date:
        return 'path_array_date is required.'

    if not path_array_date_time:
        return 'path_array_date_time is required.'

    if not path_array_password:
        return 'path_array_password is required.'

    try:
        response = requests.put('http://localhost:8943/test/plain/text/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_delete_test_plain_text_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return 'path_integer is required.'

    if not path_integer32:
        return 'path_integer32 is required.'

    if not path_integer64:
        return 'path_integer64 is required.'

    if not path_number:
        return 'path_number is required.'

    if not path_float:
        return 'path_float is required.'

    if not path_double:
        return 'path_double is required.'

    if not path_string:
        return 'path_string is required.'

    if not path_string_byte:
        return 'path_string_byte is required.'

    if not path_string_binary:
        return 'path_string_binary is required.'

    if not path_boolean:
        return 'path_boolean is required.'

    if not path_date:
        return 'path_date is required.'

    if not path_date_time:
        return 'path_date_time is required.'

    if not path_password:
        return 'path_password is required.'

    if not path_array_integer:
        return 'path_array_integer is required.'

    if not path_array_integer32:
        return 'path_array_integer32 is required.'

    if not path_array_integer64:
        return 'path_array_integer64 is required.'

    if not path_array_number:
        return 'path_array_number is required.'

    if not path_array_float:
        return 'path_array_float is required.'

    if not path_array_double:
        return 'path_array_double is required.'

    if not path_array_string:
        return 'path_array_string is required.'

    if not path_array_string_byte:
        return 'path_array_string_byte is required.'

    if not path_array_string_binary:
        return 'path_array_string_binary is required.'

    if not path_array_boolean:
        return 'path_array_boolean is required.'

    if not path_array_date:
        return 'path_array_date is required.'

    if not path_array_date_time:
        return 'path_array_date_time is required.'

    if not path_array_password:
        return 'path_array_password is required.'

    try:
        response = requests.delete('http://localhost:8943/test/plain/text/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_get_test_json_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return ['query_integer is required.']
    if query_integer:
        if not isinstance(query_integer, int):
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return ['query_integer32 is required.']
    if query_integer32:
        if not isinstance(query_integer32, int):
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return ['query_integer64 is required.']
    if query_integer64:
        if not isinstance(query_integer64, int):
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return ['query_number is required.']
    if query_number:
        if not isinstance(query_number, float):
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if not query_float:
        return ['query_float is required.']
    if query_float:
        if not isinstance(query_float, float):
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if not query_double:
        return ['query_double is required.']
    if query_double:
        if not isinstance(query_double, float):
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if not query_string:
        return ['query_string is required.']
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return ['query_string_byte is required.']
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return ['query_string_binary is required.']
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return ['query_boolean is required.']
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return ['query_date is required.']
    if query_date:
        if not isinstance(query_date, datetime.date):
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return ['query_date_time is required.']
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return ['query_password is required.']
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return ['query_array_integer is required.']
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return ['query_array_integer must contains integers.']
        else:
            if not isinstance(query_array_integer, int):
                return ['query_array_integer must contains integers.']

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return ['query_array_integer32 is required.']
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return ['query_array_integer32 must contains integers.']
        else:
            if not isinstance(query_array_integer32, int):
                return ['query_array_integer32 must contains integers.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return ['query_array_integer64 is required.']
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return ['query_array_integer64 must contains integers.']
        else:
            if not isinstance(query_array_integer64, int):
                return ['query_array_integer64 must contains integers.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return ['query_array_number is required.']
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return ['query_array_number must contains numbers.']
        else:
            if not isinstance(query_array_number, float):
                return ['query_array_number must contains numbers.']

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return ['query_array_float is required.']
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return ['query_array_float must contains numbers.']
        else:
            if not isinstance(query_array_float, float):
                return ['query_array_float must contains numbers.']

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return ['query_array_double is required.']
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return ['query_array_double must contains numbers.']
        else:
            if not isinstance(query_array_double, float):
                return ['query_array_double must contains numbers.']

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return ['query_array_string is required.']
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return ['query_array_string_byte is required.']
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return ['query_array_string_binary is required.']
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return ['query_array_boolean is required.']
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return ['query_array_date is required.']
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return ['query_array_date must contains dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                return ['query_array_date must contains dates.']

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return ['query_array_date_time is required.']
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return ['query_array_date_time must contains date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return ['query_array_date_time must contains date times.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return ['query_array_password is required.']
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.get('http://localhost:8943/test/json/with/all/parameters/types'.format(
), request_parameters, stream=True)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_post_test_json_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return ['query_integer is required.']
    if query_integer:
        if not isinstance(query_integer, int):
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return ['query_integer32 is required.']
    if query_integer32:
        if not isinstance(query_integer32, int):
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return ['query_integer64 is required.']
    if query_integer64:
        if not isinstance(query_integer64, int):
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return ['query_number is required.']
    if query_number:
        if not isinstance(query_number, float):
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if not query_float:
        return ['query_float is required.']
    if query_float:
        if not isinstance(query_float, float):
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if not query_double:
        return ['query_double is required.']
    if query_double:
        if not isinstance(query_double, float):
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if not query_string:
        return ['query_string is required.']
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return ['query_string_byte is required.']
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return ['query_string_binary is required.']
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return ['query_boolean is required.']
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return ['query_date is required.']
    if query_date:
        if not isinstance(query_date, datetime.date):
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return ['query_date_time is required.']
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return ['query_password is required.']
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return ['query_array_integer is required.']
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return ['query_array_integer must contains integers.']
        else:
            if not isinstance(query_array_integer, int):
                return ['query_array_integer must contains integers.']

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return ['query_array_integer32 is required.']
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return ['query_array_integer32 must contains integers.']
        else:
            if not isinstance(query_array_integer32, int):
                return ['query_array_integer32 must contains integers.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return ['query_array_integer64 is required.']
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return ['query_array_integer64 must contains integers.']
        else:
            if not isinstance(query_array_integer64, int):
                return ['query_array_integer64 must contains integers.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return ['query_array_number is required.']
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return ['query_array_number must contains numbers.']
        else:
            if not isinstance(query_array_number, float):
                return ['query_array_number must contains numbers.']

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return ['query_array_float is required.']
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return ['query_array_float must contains numbers.']
        else:
            if not isinstance(query_array_float, float):
                return ['query_array_float must contains numbers.']

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return ['query_array_double is required.']
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return ['query_array_double must contains numbers.']
        else:
            if not isinstance(query_array_double, float):
                return ['query_array_double must contains numbers.']

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return ['query_array_string is required.']
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return ['query_array_string_byte is required.']
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return ['query_array_string_binary is required.']
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return ['query_array_boolean is required.']
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return ['query_array_date is required.']
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return ['query_array_date must contains dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                return ['query_array_date must contains dates.']

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return ['query_array_date_time is required.']
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return ['query_array_date_time must contains date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return ['query_array_date_time must contains date times.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return ['query_array_password is required.']
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.post('http://localhost:8943/test/json/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_put_test_json_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return ['query_integer is required.']
    if query_integer:
        if not isinstance(query_integer, int):
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return ['query_integer32 is required.']
    if query_integer32:
        if not isinstance(query_integer32, int):
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return ['query_integer64 is required.']
    if query_integer64:
        if not isinstance(query_integer64, int):
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return ['query_number is required.']
    if query_number:
        if not isinstance(query_number, float):
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if not query_float:
        return ['query_float is required.']
    if query_float:
        if not isinstance(query_float, float):
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if not query_double:
        return ['query_double is required.']
    if query_double:
        if not isinstance(query_double, float):
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if not query_string:
        return ['query_string is required.']
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return ['query_string_byte is required.']
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return ['query_string_binary is required.']
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return ['query_boolean is required.']
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return ['query_date is required.']
    if query_date:
        if not isinstance(query_date, datetime.date):
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return ['query_date_time is required.']
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return ['query_password is required.']
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return ['query_array_integer is required.']
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return ['query_array_integer must contains integers.']
        else:
            if not isinstance(query_array_integer, int):
                return ['query_array_integer must contains integers.']

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return ['query_array_integer32 is required.']
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return ['query_array_integer32 must contains integers.']
        else:
            if not isinstance(query_array_integer32, int):
                return ['query_array_integer32 must contains integers.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return ['query_array_integer64 is required.']
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return ['query_array_integer64 must contains integers.']
        else:
            if not isinstance(query_array_integer64, int):
                return ['query_array_integer64 must contains integers.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return ['query_array_number is required.']
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return ['query_array_number must contains numbers.']
        else:
            if not isinstance(query_array_number, float):
                return ['query_array_number must contains numbers.']

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return ['query_array_float is required.']
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return ['query_array_float must contains numbers.']
        else:
            if not isinstance(query_array_float, float):
                return ['query_array_float must contains numbers.']

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return ['query_array_double is required.']
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return ['query_array_double must contains numbers.']
        else:
            if not isinstance(query_array_double, float):
                return ['query_array_double must contains numbers.']

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return ['query_array_string is required.']
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return ['query_array_string_byte is required.']
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return ['query_array_string_binary is required.']
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return ['query_array_boolean is required.']
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return ['query_array_date is required.']
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return ['query_array_date must contains dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                return ['query_array_date must contains dates.']

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return ['query_array_date_time is required.']
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return ['query_array_date_time must contains date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return ['query_array_date_time must contains date times.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return ['query_array_password is required.']
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.put('http://localhost:8943/test/json/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_delete_test_json_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return ['query_integer is required.']
    if query_integer:
        if not isinstance(query_integer, int):
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return ['query_integer32 is required.']
    if query_integer32:
        if not isinstance(query_integer32, int):
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return ['query_integer64 is required.']
    if query_integer64:
        if not isinstance(query_integer64, int):
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return ['query_number is required.']
    if query_number:
        if not isinstance(query_number, float):
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if not query_float:
        return ['query_float is required.']
    if query_float:
        if not isinstance(query_float, float):
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if not query_double:
        return ['query_double is required.']
    if query_double:
        if not isinstance(query_double, float):
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if not query_string:
        return ['query_string is required.']
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return ['query_string_byte is required.']
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return ['query_string_binary is required.']
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return ['query_boolean is required.']
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return ['query_date is required.']
    if query_date:
        if not isinstance(query_date, datetime.date):
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return ['query_date_time is required.']
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return ['query_password is required.']
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return ['query_array_integer is required.']
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return ['query_array_integer must contains integers.']
        else:
            if not isinstance(query_array_integer, int):
                return ['query_array_integer must contains integers.']

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return ['query_array_integer32 is required.']
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return ['query_array_integer32 must contains integers.']
        else:
            if not isinstance(query_array_integer32, int):
                return ['query_array_integer32 must contains integers.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return ['query_array_integer64 is required.']
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return ['query_array_integer64 must contains integers.']
        else:
            if not isinstance(query_array_integer64, int):
                return ['query_array_integer64 must contains integers.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return ['query_array_number is required.']
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return ['query_array_number must contains numbers.']
        else:
            if not isinstance(query_array_number, float):
                return ['query_array_number must contains numbers.']

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return ['query_array_float is required.']
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return ['query_array_float must contains numbers.']
        else:
            if not isinstance(query_array_float, float):
                return ['query_array_float must contains numbers.']

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return ['query_array_double is required.']
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return ['query_array_double must contains numbers.']
        else:
            if not isinstance(query_array_double, float):
                return ['query_array_double must contains numbers.']

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return ['query_array_string is required.']
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return ['query_array_string_byte is required.']
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return ['query_array_string_binary is required.']
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return ['query_array_boolean is required.']
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return ['query_array_date is required.']
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return ['query_array_date must contains dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                return ['query_array_date must contains dates.']

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return ['query_array_date_time is required.']
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return ['query_array_date_time must contains date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return ['query_array_date_time must contains date times.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return ['query_array_password is required.']
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.delete('http://localhost:8943/test/json/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_get_test_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.get('http://localhost:8943/test/with/all/optional/parameters/types'.format(
), request_parameters, stream=True)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_post_test_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.post('http://localhost:8943/test/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_put_test_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.put('http://localhost:8943/test/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_delete_test_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.delete('http://localhost:8943/test/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_get_test_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return 'query_integer is required.'
    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return 'query_integer32 is required.'
    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return 'query_integer64 is required.'
    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return 'query_number is required.'
    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if not query_float:
        return 'query_float is required.'
    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if not query_double:
        return 'query_double is required.'
    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if not query_string:
        return 'query_string is required.'
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return 'query_string_byte is required.'
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return 'query_string_binary is required.'
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return 'query_boolean is required.'
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return 'query_date is required.'
    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return 'query_date_time is required.'
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return 'query_password is required.'
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return 'query_array_integer is required.'
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return 'query_array_integer32 is required.'
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return 'query_array_integer64 is required.'
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return 'query_array_number is required.'
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return 'query_array_float is required.'
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return 'query_array_double is required.'
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return 'query_array_string is required.'
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return 'query_array_string_byte is required.'
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return 'query_array_string_binary is required.'
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return 'query_array_boolean is required.'
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return 'query_array_date is required.'
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return 'query_array_date_time is required.'
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return 'query_array_password is required.'
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.get('http://localhost:8943/test/with/all/parameters/types'.format(
), request_parameters, stream=True)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_post_test_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return 'query_integer is required.'
    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return 'query_integer32 is required.'
    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return 'query_integer64 is required.'
    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return 'query_number is required.'
    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if not query_float:
        return 'query_float is required.'
    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if not query_double:
        return 'query_double is required.'
    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if not query_string:
        return 'query_string is required.'
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return 'query_string_byte is required.'
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return 'query_string_binary is required.'
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return 'query_boolean is required.'
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return 'query_date is required.'
    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return 'query_date_time is required.'
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return 'query_password is required.'
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return 'query_array_integer is required.'
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return 'query_array_integer32 is required.'
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return 'query_array_integer64 is required.'
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return 'query_array_number is required.'
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return 'query_array_float is required.'
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return 'query_array_double is required.'
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return 'query_array_string is required.'
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return 'query_array_string_byte is required.'
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return 'query_array_string_binary is required.'
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return 'query_array_boolean is required.'
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return 'query_array_date is required.'
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return 'query_array_date_time is required.'
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return 'query_array_password is required.'
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.post('http://localhost:8943/test/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_put_test_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return 'query_integer is required.'
    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return 'query_integer32 is required.'
    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return 'query_integer64 is required.'
    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return 'query_number is required.'
    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if not query_float:
        return 'query_float is required.'
    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if not query_double:
        return 'query_double is required.'
    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if not query_string:
        return 'query_string is required.'
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return 'query_string_byte is required.'
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return 'query_string_binary is required.'
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return 'query_boolean is required.'
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return 'query_date is required.'
    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return 'query_date_time is required.'
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return 'query_password is required.'
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return 'query_array_integer is required.'
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return 'query_array_integer32 is required.'
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return 'query_array_integer64 is required.'
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return 'query_array_number is required.'
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return 'query_array_float is required.'
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return 'query_array_double is required.'
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return 'query_array_string is required.'
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return 'query_array_string_byte is required.'
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return 'query_array_string_binary is required.'
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return 'query_array_boolean is required.'
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return 'query_array_date is required.'
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return 'query_array_date_time is required.'
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return 'query_array_password is required.'
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.put('http://localhost:8943/test/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_delete_test_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return 'query_integer is required.'
    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return 'query_integer32 is required.'
    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return 'query_integer64 is required.'
    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return 'query_number is required.'
    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if not query_float:
        return 'query_float is required.'
    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if not query_double:
        return 'query_double is required.'
    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if not query_string:
        return 'query_string is required.'
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return 'query_string_byte is required.'
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return 'query_string_binary is required.'
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return 'query_boolean is required.'
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return 'query_date is required.'
    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return 'query_date_time is required.'
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return 'query_password is required.'
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return 'query_array_integer is required.'
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return 'query_array_integer32 is required.'
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return 'query_array_integer64 is required.'
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return 'query_array_number is required.'
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return 'query_array_float is required.'
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return 'query_array_double is required.'
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return 'query_array_string is required.'
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return 'query_array_string_byte is required.'
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return 'query_array_string_binary is required.'
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return 'query_array_boolean is required.'
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return 'query_array_date is required.'
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return 'query_array_date_time is required.'
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return 'query_array_password is required.'
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.delete('http://localhost:8943/test/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_get_test_json_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return ['query_array_integer must contains integers.']
        else:
            if not isinstance(query_array_integer, int):
                return ['query_array_integer must contains integers.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return ['query_array_integer32 must contains integers.']
        else:
            if not isinstance(query_array_integer32, int):
                return ['query_array_integer32 must contains integers.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return ['query_array_integer64 must contains integers.']
        else:
            if not isinstance(query_array_integer64, int):
                return ['query_array_integer64 must contains integers.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return ['query_array_number must contains numbers.']
        else:
            if not isinstance(query_array_number, float):
                return ['query_array_number must contains numbers.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return ['query_array_float must contains numbers.']
        else:
            if not isinstance(query_array_float, float):
                return ['query_array_float must contains numbers.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return ['query_array_double must contains numbers.']
        else:
            if not isinstance(query_array_double, float):
                return ['query_array_double must contains numbers.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return ['query_array_date must contains dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                return ['query_array_date must contains dates.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return ['query_array_date_time must contains date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return ['query_array_date_time must contains date times.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.get('http://localhost:8943/test/json/with/all/optional/parameters/types'.format(
), request_parameters, stream=True)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_post_test_json_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return ['query_array_integer must contains integers.']
        else:
            if not isinstance(query_array_integer, int):
                return ['query_array_integer must contains integers.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return ['query_array_integer32 must contains integers.']
        else:
            if not isinstance(query_array_integer32, int):
                return ['query_array_integer32 must contains integers.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return ['query_array_integer64 must contains integers.']
        else:
            if not isinstance(query_array_integer64, int):
                return ['query_array_integer64 must contains integers.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return ['query_array_number must contains numbers.']
        else:
            if not isinstance(query_array_number, float):
                return ['query_array_number must contains numbers.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return ['query_array_float must contains numbers.']
        else:
            if not isinstance(query_array_float, float):
                return ['query_array_float must contains numbers.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return ['query_array_double must contains numbers.']
        else:
            if not isinstance(query_array_double, float):
                return ['query_array_double must contains numbers.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return ['query_array_date must contains dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                return ['query_array_date must contains dates.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return ['query_array_date_time must contains date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return ['query_array_date_time must contains date times.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.post('http://localhost:8943/test/json/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_put_test_json_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return ['query_array_integer must contains integers.']
        else:
            if not isinstance(query_array_integer, int):
                return ['query_array_integer must contains integers.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return ['query_array_integer32 must contains integers.']
        else:
            if not isinstance(query_array_integer32, int):
                return ['query_array_integer32 must contains integers.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return ['query_array_integer64 must contains integers.']
        else:
            if not isinstance(query_array_integer64, int):
                return ['query_array_integer64 must contains integers.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return ['query_array_number must contains numbers.']
        else:
            if not isinstance(query_array_number, float):
                return ['query_array_number must contains numbers.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return ['query_array_float must contains numbers.']
        else:
            if not isinstance(query_array_float, float):
                return ['query_array_float must contains numbers.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return ['query_array_double must contains numbers.']
        else:
            if not isinstance(query_array_double, float):
                return ['query_array_double must contains numbers.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return ['query_array_date must contains dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                return ['query_array_date must contains dates.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return ['query_array_date_time must contains date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return ['query_array_date_time must contains date times.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.put('http://localhost:8943/test/json/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_delete_test_json_with_all_optional_parameters_types(query_integer=None, query_integer32=None, query_integer64=None, query_number=None, query_float=None, query_double=None, query_string=None, query_string_byte=None, query_string_binary=None, query_boolean=None, query_date=None, query_date_time=None, query_password=None, query_array_integer=None, query_array_integer32=None, query_array_integer64=None, query_array_number=None, query_array_float=None, query_array_double=None, query_array_string=None, query_array_string_byte=None, query_array_string_binary=None, query_array_boolean=None, query_array_date=None, query_array_date_time=None, query_array_password=None):
    request_parameters = {}
    request_body = {}

    if query_integer:
        if not isinstance(query_integer, int):
            return ['query_integer must be an integer.']

        request_parameters['query_integer'] = query_integer

    if query_integer32:
        if not isinstance(query_integer32, int):
            return ['query_integer32 must be an integer.']

        request_parameters['query_integer32'] = query_integer32

    if query_integer64:
        if not isinstance(query_integer64, int):
            return ['query_integer64 must be an integer.']

        request_parameters['query_integer64'] = query_integer64

    if query_number:
        if not isinstance(query_number, float):
            return ['query_number must be a number.']

        request_parameters['query_number'] = query_number

    if query_float:
        if not isinstance(query_float, float):
            return ['query_float must be a number.']

        request_parameters['query_float'] = query_float

    if query_double:
        if not isinstance(query_double, float):
            return ['query_double must be a number.']

        request_parameters['query_double'] = query_double

    if query_string:

        request_parameters['query_string'] = query_string

    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return ['query_boolean must be either "true" or "false".']
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if query_date:
        if not isinstance(query_date, datetime.date):
            return ['query_date must be a date.']

        request_parameters['query_date'] = query_date

    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return ['query_date_time must be a date time.']

        request_parameters['query_date_time'] = query_date_time

    if query_password:

        request_parameters['query_password'] = query_password

    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return ['query_array_integer must contains integers.']
        else:
            if not isinstance(query_array_integer, int):
                return ['query_array_integer must contains integers.']

        request_parameters['query_array_integer'] = query_array_integer

    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return ['query_array_integer32 must contains integers.']
        else:
            if not isinstance(query_array_integer32, int):
                return ['query_array_integer32 must contains integers.']

        request_parameters['query_array_integer32'] = query_array_integer32

    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return ['query_array_integer64 must contains integers.']
        else:
            if not isinstance(query_array_integer64, int):
                return ['query_array_integer64 must contains integers.']

        request_parameters['query_array_integer64'] = query_array_integer64

    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return ['query_array_number must contains numbers.']
        else:
            if not isinstance(query_array_number, float):
                return ['query_array_number must contains numbers.']

        request_parameters['query_array_number'] = query_array_number

    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return ['query_array_float must contains numbers.']
        else:
            if not isinstance(query_array_float, float):
                return ['query_array_float must contains numbers.']

        request_parameters['query_array_float'] = query_array_float

    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return ['query_array_double must contains numbers.']
        else:
            if not isinstance(query_array_double, float):
                return ['query_array_double must contains numbers.']

        request_parameters['query_array_double'] = query_array_double

    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return ['query_array_date must contains dates.']
        else:
            if not isinstance(query_array_date, datetime.date):
                return ['query_array_date must contains dates.']

        request_parameters['query_array_date'] = query_array_date

    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return ['query_array_date_time must contains date times.']
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return ['query_array_date_time must contains date times.']

        request_parameters['query_array_date_time'] = query_array_date_time

    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.delete('http://localhost:8943/test/json/with/all/optional/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_get_test_json_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return ['path_integer is required.']

    if not path_integer32:
        return ['path_integer32 is required.']

    if not path_integer64:
        return ['path_integer64 is required.']

    if not path_number:
        return ['path_number is required.']

    if not path_float:
        return ['path_float is required.']

    if not path_double:
        return ['path_double is required.']

    if not path_string:
        return ['path_string is required.']

    if not path_string_byte:
        return ['path_string_byte is required.']

    if not path_string_binary:
        return ['path_string_binary is required.']

    if not path_boolean:
        return ['path_boolean is required.']

    if not path_date:
        return ['path_date is required.']

    if not path_date_time:
        return ['path_date_time is required.']

    if not path_password:
        return ['path_password is required.']

    if not path_array_integer:
        return ['path_array_integer is required.']

    if not path_array_integer32:
        return ['path_array_integer32 is required.']

    if not path_array_integer64:
        return ['path_array_integer64 is required.']

    if not path_array_number:
        return ['path_array_number is required.']

    if not path_array_float:
        return ['path_array_float is required.']

    if not path_array_double:
        return ['path_array_double is required.']

    if not path_array_string:
        return ['path_array_string is required.']

    if not path_array_string_byte:
        return ['path_array_string_byte is required.']

    if not path_array_string_binary:
        return ['path_array_string_binary is required.']

    if not path_array_boolean:
        return ['path_array_boolean is required.']

    if not path_array_date:
        return ['path_array_date is required.']

    if not path_array_date_time:
        return ['path_array_date_time is required.']

    if not path_array_password:
        return ['path_array_password is required.']

    try:
        response = requests.get('http://localhost:8943/test/json/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True)

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_post_test_json_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return ['path_integer is required.']

    if not path_integer32:
        return ['path_integer32 is required.']

    if not path_integer64:
        return ['path_integer64 is required.']

    if not path_number:
        return ['path_number is required.']

    if not path_float:
        return ['path_float is required.']

    if not path_double:
        return ['path_double is required.']

    if not path_string:
        return ['path_string is required.']

    if not path_string_byte:
        return ['path_string_byte is required.']

    if not path_string_binary:
        return ['path_string_binary is required.']

    if not path_boolean:
        return ['path_boolean is required.']

    if not path_date:
        return ['path_date is required.']

    if not path_date_time:
        return ['path_date_time is required.']

    if not path_password:
        return ['path_password is required.']

    if not path_array_integer:
        return ['path_array_integer is required.']

    if not path_array_integer32:
        return ['path_array_integer32 is required.']

    if not path_array_integer64:
        return ['path_array_integer64 is required.']

    if not path_array_number:
        return ['path_array_number is required.']

    if not path_array_float:
        return ['path_array_float is required.']

    if not path_array_double:
        return ['path_array_double is required.']

    if not path_array_string:
        return ['path_array_string is required.']

    if not path_array_string_byte:
        return ['path_array_string_byte is required.']

    if not path_array_string_binary:
        return ['path_array_string_binary is required.']

    if not path_array_boolean:
        return ['path_array_boolean is required.']

    if not path_array_date:
        return ['path_array_date is required.']

    if not path_array_date_time:
        return ['path_array_date_time is required.']

    if not path_array_password:
        return ['path_array_password is required.']

    try:
        response = requests.post('http://localhost:8943/test/json/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_put_test_json_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return ['path_integer is required.']

    if not path_integer32:
        return ['path_integer32 is required.']

    if not path_integer64:
        return ['path_integer64 is required.']

    if not path_number:
        return ['path_number is required.']

    if not path_float:
        return ['path_float is required.']

    if not path_double:
        return ['path_double is required.']

    if not path_string:
        return ['path_string is required.']

    if not path_string_byte:
        return ['path_string_byte is required.']

    if not path_string_binary:
        return ['path_string_binary is required.']

    if not path_boolean:
        return ['path_boolean is required.']

    if not path_date:
        return ['path_date is required.']

    if not path_date_time:
        return ['path_date_time is required.']

    if not path_password:
        return ['path_password is required.']

    if not path_array_integer:
        return ['path_array_integer is required.']

    if not path_array_integer32:
        return ['path_array_integer32 is required.']

    if not path_array_integer64:
        return ['path_array_integer64 is required.']

    if not path_array_number:
        return ['path_array_number is required.']

    if not path_array_float:
        return ['path_array_float is required.']

    if not path_array_double:
        return ['path_array_double is required.']

    if not path_array_string:
        return ['path_array_string is required.']

    if not path_array_string_byte:
        return ['path_array_string_byte is required.']

    if not path_array_string_binary:
        return ['path_array_string_binary is required.']

    if not path_array_boolean:
        return ['path_array_boolean is required.']

    if not path_array_date:
        return ['path_array_date is required.']

    if not path_array_date_time:
        return ['path_array_date_time is required.']

    if not path_array_password:
        return ['path_array_password is required.']

    try:
        response = requests.put('http://localhost:8943/test/json/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_delete_test_json_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return ['path_integer is required.']

    if not path_integer32:
        return ['path_integer32 is required.']

    if not path_integer64:
        return ['path_integer64 is required.']

    if not path_number:
        return ['path_number is required.']

    if not path_float:
        return ['path_float is required.']

    if not path_double:
        return ['path_double is required.']

    if not path_string:
        return ['path_string is required.']

    if not path_string_byte:
        return ['path_string_byte is required.']

    if not path_string_binary:
        return ['path_string_binary is required.']

    if not path_boolean:
        return ['path_boolean is required.']

    if not path_date:
        return ['path_date is required.']

    if not path_date_time:
        return ['path_date_time is required.']

    if not path_password:
        return ['path_password is required.']

    if not path_array_integer:
        return ['path_array_integer is required.']

    if not path_array_integer32:
        return ['path_array_integer32 is required.']

    if not path_array_integer64:
        return ['path_array_integer64 is required.']

    if not path_array_number:
        return ['path_array_number is required.']

    if not path_array_float:
        return ['path_array_float is required.']

    if not path_array_double:
        return ['path_array_double is required.']

    if not path_array_string:
        return ['path_array_string is required.']

    if not path_array_string_byte:
        return ['path_array_string_byte is required.']

    if not path_array_string_binary:
        return ['path_array_string_binary is required.']

    if not path_array_boolean:
        return ['path_array_boolean is required.']

    if not path_array_date:
        return ['path_array_date is required.']

    if not path_array_date_time:
        return ['path_array_date_time is required.']

    if not path_array_password:
        return ['path_array_password is required.']

    try:
        response = requests.delete('http://localhost:8943/test/json/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_json = response.json()
        response.close()
        return to_list(response_json)
    except Exception as error:
        return [response.text[:255] if response else error.message[:255]]


@xw.func(category='test')
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
def test_get_test_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return 'path_integer is required.'

    if not path_integer32:
        return 'path_integer32 is required.'

    if not path_integer64:
        return 'path_integer64 is required.'

    if not path_number:
        return 'path_number is required.'

    if not path_float:
        return 'path_float is required.'

    if not path_double:
        return 'path_double is required.'

    if not path_string:
        return 'path_string is required.'

    if not path_string_byte:
        return 'path_string_byte is required.'

    if not path_string_binary:
        return 'path_string_binary is required.'

    if not path_boolean:
        return 'path_boolean is required.'

    if not path_date:
        return 'path_date is required.'

    if not path_date_time:
        return 'path_date_time is required.'

    if not path_password:
        return 'path_password is required.'

    if not path_array_integer:
        return 'path_array_integer is required.'

    if not path_array_integer32:
        return 'path_array_integer32 is required.'

    if not path_array_integer64:
        return 'path_array_integer64 is required.'

    if not path_array_number:
        return 'path_array_number is required.'

    if not path_array_float:
        return 'path_array_float is required.'

    if not path_array_double:
        return 'path_array_double is required.'

    if not path_array_string:
        return 'path_array_string is required.'

    if not path_array_string_byte:
        return 'path_array_string_byte is required.'

    if not path_array_string_binary:
        return 'path_array_string_binary is required.'

    if not path_array_boolean:
        return 'path_array_boolean is required.'

    if not path_array_date:
        return 'path_array_date is required.'

    if not path_array_date_time:
        return 'path_array_date_time is required.'

    if not path_array_password:
        return 'path_array_password is required.'

    try:
        response = requests.get('http://localhost:8943/test/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password), stream=True)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_post_test_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return 'path_integer is required.'

    if not path_integer32:
        return 'path_integer32 is required.'

    if not path_integer64:
        return 'path_integer64 is required.'

    if not path_number:
        return 'path_number is required.'

    if not path_float:
        return 'path_float is required.'

    if not path_double:
        return 'path_double is required.'

    if not path_string:
        return 'path_string is required.'

    if not path_string_byte:
        return 'path_string_byte is required.'

    if not path_string_binary:
        return 'path_string_binary is required.'

    if not path_boolean:
        return 'path_boolean is required.'

    if not path_date:
        return 'path_date is required.'

    if not path_date_time:
        return 'path_date_time is required.'

    if not path_password:
        return 'path_password is required.'

    if not path_array_integer:
        return 'path_array_integer is required.'

    if not path_array_integer32:
        return 'path_array_integer32 is required.'

    if not path_array_integer64:
        return 'path_array_integer64 is required.'

    if not path_array_number:
        return 'path_array_number is required.'

    if not path_array_float:
        return 'path_array_float is required.'

    if not path_array_double:
        return 'path_array_double is required.'

    if not path_array_string:
        return 'path_array_string is required.'

    if not path_array_string_byte:
        return 'path_array_string_byte is required.'

    if not path_array_string_binary:
        return 'path_array_string_binary is required.'

    if not path_array_boolean:
        return 'path_array_boolean is required.'

    if not path_array_date:
        return 'path_array_date is required.'

    if not path_array_date_time:
        return 'path_array_date_time is required.'

    if not path_array_password:
        return 'path_array_password is required.'

    try:
        response = requests.post('http://localhost:8943/test/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_put_test_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return 'path_integer is required.'

    if not path_integer32:
        return 'path_integer32 is required.'

    if not path_integer64:
        return 'path_integer64 is required.'

    if not path_number:
        return 'path_number is required.'

    if not path_float:
        return 'path_float is required.'

    if not path_double:
        return 'path_double is required.'

    if not path_string:
        return 'path_string is required.'

    if not path_string_byte:
        return 'path_string_byte is required.'

    if not path_string_binary:
        return 'path_string_binary is required.'

    if not path_boolean:
        return 'path_boolean is required.'

    if not path_date:
        return 'path_date is required.'

    if not path_date_time:
        return 'path_date_time is required.'

    if not path_password:
        return 'path_password is required.'

    if not path_array_integer:
        return 'path_array_integer is required.'

    if not path_array_integer32:
        return 'path_array_integer32 is required.'

    if not path_array_integer64:
        return 'path_array_integer64 is required.'

    if not path_array_number:
        return 'path_array_number is required.'

    if not path_array_float:
        return 'path_array_float is required.'

    if not path_array_double:
        return 'path_array_double is required.'

    if not path_array_string:
        return 'path_array_string is required.'

    if not path_array_string_byte:
        return 'path_array_string_byte is required.'

    if not path_array_string_binary:
        return 'path_array_string_binary is required.'

    if not path_array_boolean:
        return 'path_array_boolean is required.'

    if not path_array_date:
        return 'path_array_date is required.'

    if not path_array_date_time:
        return 'path_array_date_time is required.'

    if not path_array_password:
        return 'path_array_password is required.'

    try:
        response = requests.put('http://localhost:8943/test/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_delete_test_with_all_paths_types(path_integer, path_integer32, path_integer64, path_number, path_float, path_double, path_string, path_string_byte, path_string_binary, path_boolean, path_date, path_date_time, path_password, path_array_integer, path_array_integer32, path_array_integer64, path_array_number, path_array_float, path_array_double, path_array_string, path_array_string_byte, path_array_string_binary, path_array_boolean, path_array_date, path_array_date_time, path_array_password):
    if not path_integer:
        return 'path_integer is required.'

    if not path_integer32:
        return 'path_integer32 is required.'

    if not path_integer64:
        return 'path_integer64 is required.'

    if not path_number:
        return 'path_number is required.'

    if not path_float:
        return 'path_float is required.'

    if not path_double:
        return 'path_double is required.'

    if not path_string:
        return 'path_string is required.'

    if not path_string_byte:
        return 'path_string_byte is required.'

    if not path_string_binary:
        return 'path_string_binary is required.'

    if not path_boolean:
        return 'path_boolean is required.'

    if not path_date:
        return 'path_date is required.'

    if not path_date_time:
        return 'path_date_time is required.'

    if not path_password:
        return 'path_password is required.'

    if not path_array_integer:
        return 'path_array_integer is required.'

    if not path_array_integer32:
        return 'path_array_integer32 is required.'

    if not path_array_integer64:
        return 'path_array_integer64 is required.'

    if not path_array_number:
        return 'path_array_number is required.'

    if not path_array_float:
        return 'path_array_float is required.'

    if not path_array_double:
        return 'path_array_double is required.'

    if not path_array_string:
        return 'path_array_string is required.'

    if not path_array_string_byte:
        return 'path_array_string_byte is required.'

    if not path_array_string_binary:
        return 'path_array_string_binary is required.'

    if not path_array_boolean:
        return 'path_array_boolean is required.'

    if not path_array_date:
        return 'path_array_date is required.'

    if not path_array_date_time:
        return 'path_array_date_time is required.'

    if not path_array_password:
        return 'path_array_password is required.'

    try:
        response = requests.delete('http://localhost:8943/test/with/all/paths/types'.format(
        path_integer=path_integer,         path_integer32=path_integer32,         path_integer64=path_integer64,         path_number=path_number,         path_float=path_float,         path_double=path_double,         path_string=path_string,         path_string_byte=path_string_byte,         path_string_binary=path_string_binary,         path_boolean=path_boolean,         path_date=path_date,         path_date_time=path_date_time,         path_password=path_password,         path_array_integer=path_array_integer,         path_array_integer32=path_array_integer32,         path_array_integer64=path_array_integer64,         path_array_number=path_array_number,         path_array_float=path_array_float,         path_array_double=path_array_double,         path_array_string=path_array_string,         path_array_string_byte=path_array_string_byte,         path_array_string_binary=path_array_string_binary,         path_array_boolean=path_array_boolean,         path_array_date=path_array_date,         path_array_date_time=path_array_date_time,         path_array_password=path_array_password))

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_get_test_plain_text_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return 'query_integer is required.'
    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return 'query_integer32 is required.'
    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return 'query_integer64 is required.'
    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return 'query_number is required.'
    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if not query_float:
        return 'query_float is required.'
    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if not query_double:
        return 'query_double is required.'
    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if not query_string:
        return 'query_string is required.'
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return 'query_string_byte is required.'
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return 'query_string_binary is required.'
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return 'query_boolean is required.'
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return 'query_date is required.'
    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return 'query_date_time is required.'
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return 'query_password is required.'
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return 'query_array_integer is required.'
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return 'query_array_integer32 is required.'
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return 'query_array_integer64 is required.'
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return 'query_array_number is required.'
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return 'query_array_float is required.'
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return 'query_array_double is required.'
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return 'query_array_string is required.'
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return 'query_array_string_byte is required.'
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return 'query_array_string_binary is required.'
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return 'query_array_boolean is required.'
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return 'query_array_date is required.'
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return 'query_array_date_time is required.'
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return 'query_array_password is required.'
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.get('http://localhost:8943/test/plain/text/with/all/parameters/types'.format(
), request_parameters, stream=True)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_post_test_plain_text_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return 'query_integer is required.'
    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return 'query_integer32 is required.'
    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return 'query_integer64 is required.'
    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return 'query_number is required.'
    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if not query_float:
        return 'query_float is required.'
    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if not query_double:
        return 'query_double is required.'
    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if not query_string:
        return 'query_string is required.'
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return 'query_string_byte is required.'
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return 'query_string_binary is required.'
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return 'query_boolean is required.'
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return 'query_date is required.'
    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return 'query_date_time is required.'
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return 'query_password is required.'
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return 'query_array_integer is required.'
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return 'query_array_integer32 is required.'
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return 'query_array_integer64 is required.'
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return 'query_array_number is required.'
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return 'query_array_float is required.'
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return 'query_array_double is required.'
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return 'query_array_string is required.'
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return 'query_array_string_byte is required.'
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return 'query_array_string_binary is required.'
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return 'query_array_boolean is required.'
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return 'query_array_date is required.'
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return 'query_array_date_time is required.'
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return 'query_array_password is required.'
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.post('http://localhost:8943/test/plain/text/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_put_test_plain_text_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return 'query_integer is required.'
    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return 'query_integer32 is required.'
    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return 'query_integer64 is required.'
    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return 'query_number is required.'
    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if not query_float:
        return 'query_float is required.'
    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if not query_double:
        return 'query_double is required.'
    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if not query_string:
        return 'query_string is required.'
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return 'query_string_byte is required.'
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return 'query_string_binary is required.'
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return 'query_boolean is required.'
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return 'query_date is required.'
    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return 'query_date_time is required.'
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return 'query_password is required.'
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return 'query_array_integer is required.'
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return 'query_array_integer32 is required.'
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return 'query_array_integer64 is required.'
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return 'query_array_number is required.'
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return 'query_array_float is required.'
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return 'query_array_double is required.'
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return 'query_array_string is required.'
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return 'query_array_string_byte is required.'
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return 'query_array_string_binary is required.'
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return 'query_array_boolean is required.'
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return 'query_array_date is required.'
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return 'query_array_date_time is required.'
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return 'query_array_password is required.'
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.put('http://localhost:8943/test/plain/text/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


@xw.func(category='test')
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
def test_delete_test_plain_text_with_all_parameters_types(query_integer, query_integer32, query_integer64, query_number, query_float, query_double, query_string, query_string_byte, query_string_binary, query_boolean, query_date, query_date_time, query_password, query_array_integer, query_array_integer32, query_array_integer64, query_array_number, query_array_float, query_array_double, query_array_string, query_array_string_byte, query_array_string_binary, query_array_boolean, query_array_date, query_array_date_time, query_array_password):
    request_parameters = {}
    request_body = {}

    if not query_integer:
        return 'query_integer is required.'
    if query_integer:
        if not isinstance(query_integer, int):
            return 'query_integer must be an integer.'

        request_parameters['query_integer'] = query_integer

    if not query_integer32:
        return 'query_integer32 is required.'
    if query_integer32:
        if not isinstance(query_integer32, int):
            return 'query_integer32 must be an integer.'

        request_parameters['query_integer32'] = query_integer32

    if not query_integer64:
        return 'query_integer64 is required.'
    if query_integer64:
        if not isinstance(query_integer64, int):
            return 'query_integer64 must be an integer.'

        request_parameters['query_integer64'] = query_integer64

    if not query_number:
        return 'query_number is required.'
    if query_number:
        if not isinstance(query_number, float):
            return 'query_number must be a number.'

        request_parameters['query_number'] = query_number

    if not query_float:
        return 'query_float is required.'
    if query_float:
        if not isinstance(query_float, float):
            return 'query_float must be a number.'

        request_parameters['query_float'] = query_float

    if not query_double:
        return 'query_double is required.'
    if query_double:
        if not isinstance(query_double, float):
            return 'query_double must be a number.'

        request_parameters['query_double'] = query_double

    if not query_string:
        return 'query_string is required.'
    if query_string:

        request_parameters['query_string'] = query_string

    if not query_string_byte:
        return 'query_string_byte is required.'
    if query_string_byte:

        request_parameters['query_string_byte'] = query_string_byte

    if not query_string_binary:
        return 'query_string_binary is required.'
    if query_string_binary:

        request_parameters['query_string_binary'] = query_string_binary

    if not query_boolean:
        return 'query_boolean is required.'
    if query_boolean:
        if query_boolean not in ['true', 'false']:
            return 'query_boolean must be either "true" or "false".'
        query_boolean = query_boolean == 'true'

        request_parameters['query_boolean'] = query_boolean

    if not query_date:
        return 'query_date is required.'
    if query_date:
        if not isinstance(query_date, datetime.date):
            return 'query_date must be a date.'

        request_parameters['query_date'] = query_date

    if not query_date_time:
        return 'query_date_time is required.'
    if query_date_time:
        if not isinstance(query_date_time, datetime.datetime):
            return 'query_date_time must be a date time.'

        request_parameters['query_date_time'] = query_date_time

    if not query_password:
        return 'query_password is required.'
    if query_password:

        request_parameters['query_password'] = query_password

    if not query_array_integer:
        return 'query_array_integer is required.'
    if query_array_integer:
        if isinstance(query_array_integer, list):
            for query_array_integer_item in query_array_integer:
                if not isinstance(query_array_integer_item, int):
                    return 'query_array_integer must contains integers.'
        else:
            if not isinstance(query_array_integer, int):
                return 'query_array_integer must contains integers.'

        request_parameters['query_array_integer'] = query_array_integer

    if not query_array_integer32:
        return 'query_array_integer32 is required.'
    if query_array_integer32:
        if isinstance(query_array_integer32, list):
            for query_array_integer32_item in query_array_integer32:
                if not isinstance(query_array_integer32_item, int):
                    return 'query_array_integer32 must contains integers.'
        else:
            if not isinstance(query_array_integer32, int):
                return 'query_array_integer32 must contains integers.'

        request_parameters['query_array_integer32'] = query_array_integer32

    if not query_array_integer64:
        return 'query_array_integer64 is required.'
    if query_array_integer64:
        if isinstance(query_array_integer64, list):
            for query_array_integer64_item in query_array_integer64:
                if not isinstance(query_array_integer64_item, int):
                    return 'query_array_integer64 must contains integers.'
        else:
            if not isinstance(query_array_integer64, int):
                return 'query_array_integer64 must contains integers.'

        request_parameters['query_array_integer64'] = query_array_integer64

    if not query_array_number:
        return 'query_array_number is required.'
    if query_array_number:
        if isinstance(query_array_number, list):
            for query_array_number_item in query_array_number:
                if not isinstance(query_array_number_item, float):
                    return 'query_array_number must contains numbers.'
        else:
            if not isinstance(query_array_number, float):
                return 'query_array_number must contains numbers.'

        request_parameters['query_array_number'] = query_array_number

    if not query_array_float:
        return 'query_array_float is required.'
    if query_array_float:
        if isinstance(query_array_float, list):
            for query_array_float_item in query_array_float:
                if not isinstance(query_array_float_item, float):
                    return 'query_array_float must contains numbers.'
        else:
            if not isinstance(query_array_float, float):
                return 'query_array_float must contains numbers.'

        request_parameters['query_array_float'] = query_array_float

    if not query_array_double:
        return 'query_array_double is required.'
    if query_array_double:
        if isinstance(query_array_double, list):
            for query_array_double_item in query_array_double:
                if not isinstance(query_array_double_item, float):
                    return 'query_array_double must contains numbers.'
        else:
            if not isinstance(query_array_double, float):
                return 'query_array_double must contains numbers.'

        request_parameters['query_array_double'] = query_array_double

    if not query_array_string:
        return 'query_array_string is required.'
    if query_array_string:

        request_parameters['query_array_string'] = query_array_string

    if not query_array_string_byte:
        return 'query_array_string_byte is required.'
    if query_array_string_byte:

        request_parameters['query_array_string_byte'] = query_array_string_byte

    if not query_array_string_binary:
        return 'query_array_string_binary is required.'
    if query_array_string_binary:

        request_parameters['query_array_string_binary'] = query_array_string_binary

    if not query_array_boolean:
        return 'query_array_boolean is required.'
    if query_array_boolean:

        request_parameters['query_array_boolean'] = query_array_boolean

    if not query_array_date:
        return 'query_array_date is required.'
    if query_array_date:
        if isinstance(query_array_date, list):
            for query_array_date_item in query_array_date:
                if not isinstance(query_array_date_item, datetime.date):
                    return 'query_array_date must contains dates.'
        else:
            if not isinstance(query_array_date, datetime.date):
                return 'query_array_date must contains dates.'

        request_parameters['query_array_date'] = query_array_date

    if not query_array_date_time:
        return 'query_array_date_time is required.'
    if query_array_date_time:
        if isinstance(query_array_date_time, list):
            for query_array_date_time_item in query_array_date_time:
                if not isinstance(query_array_date_time_item, datetime.datetime):
                    return 'query_array_date_time must contains date times.'
        else:
            if not isinstance(query_array_date_time, datetime.datetime):
                return 'query_array_date_time must contains date times.'

        request_parameters['query_array_date_time'] = query_array_date_time

    if not query_array_password:
        return 'query_array_password is required.'
    if query_array_password:

        request_parameters['query_array_password'] = query_array_password

    try:
        response = requests.delete('http://localhost:8943/test/plain/text/with/all/parameters/types'.format(
), data=request_body, params=request_parameters)

        response_content = response.content
        response.close()
        response.raise_for_status()
        return response_content[:255]
    except HTTPError as http_error:
        return http_error.message[:255]
    except Exception as error:
        return response.text[:255] if response else error.message[:255]


def flattened_list_of_dicts(list_of_dicts):
    """
    Transform a list of dictionaries into a list of lists.
    First list is the header (first dictionary keys)
    Other lists are containing dictionary values.
    """
    flat_list = []
    header_list = list(list_of_dicts[0].keys())
    flat_list.append(header_list)
    for dictionary in list_of_dicts:
        flat_list.append(list(dictionary.values()))
    return flat_list


def to_list(data):
    """
    Transform this data into a list (if needed).
    If data is a dictionary:
        - If empty return a list with an empty string in it
        - If there is a single key and value is a list, then do not handle the key and return the list.
        - Otherwise return a list containing 2 lists, the keys and the values.
    If data is a list:
        - If this is a list of dictionaries, return a list of list containing keys (as first list) and values
        - Otherwise return this list
    Else:
        - Return a new list containing this item
    """
    if isinstance(data, dict):
        if len(data) == 0:
            return ['']
        if len(data) == 1:
            value = next(iter(data.values()))
            if isinstance(value, list):
                return to_list(value)
        return [list(data.keys()), list(data.values())]
    if isinstance(data, list):
        if len(data) == 0:
            return ['']
        if isinstance(data[0], dict):
            return flattened_list_of_dicts(data)
        return data
    return [data]