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