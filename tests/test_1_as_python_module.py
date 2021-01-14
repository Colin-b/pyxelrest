import datetime

import pytest
import requests
from requests import PreparedRequest
from responses import RequestsMock

from tests.test_petstore import petstore_service


def _get_request(responses: RequestsMock, url: str) -> PreparedRequest:
    for call in responses.calls:
        if call.request.url == url:
            # Pop out verified request (to be able to check multiple requests)
            responses.calls._calls.remove(call)
            return call.request


@pytest.fixture
def test_api_service(responses: RequestsMock):
    responses.add(
        responses.GET,
        url="http://test/",
        json={
            "swagger": "2.0",
            "paths": {
                "/text": {
                    "get": {
                        "operationId": "get_text",
                        "responses": {"200": {"description": "return value"}},
                    }
                }
            },
        },
        match_querystring=True,
    )


def load_as_python_module():
    import pyxelrest

    pyxelrest.load(
        {
            "petstore": {
                "open_api": {
                    "definition": "http://petstore.swagger.io/v2/swagger.json"
                },
            },
            "text_api": {
                "open_api": {"definition": "http://test/"},
            },
        }
    )


def test_get_order_by_id(responses: RequestsMock, petstore_service, test_api_service):
    load_as_python_module()
    responses.add(
        responses.POST,
        url="https://petstore.swagger.io/v2/store/order",
        json={
            "id": 10,
            "petId": 222222,
            "quantity": 1,
            "status": "placed",
            "complete": False,
            "shipDate": "2020-12-02",
        },
        match_querystring=True,
    )

    from pyxelrest.generated import petstore

    now = datetime.datetime.utcnow()
    now_str = now.isoformat().encode()
    assert petstore.placeOrder(
        id=10, petId=222222, quantity=1, shipDate=now, status="placed", complete=False
    ) == {
        "id": 10,
        "petId": 222222,
        "quantity": 1,
        "status": "placed",
        "complete": False,
        "shipDate": "2020-12-02",
    }
    assert (
        _get_request(responses, "https://petstore.swagger.io/v2/store/order").body
        == b"""{"id": 10, "petId": 222222, "quantity": 1, "shipDate": \""""
        + now_str
        + b"""", "status": "placed", "complete": false}"""
    )

    responses.add(
        responses.GET,
        url="https://petstore.swagger.io/v2/store/order/10",
        json={
            "id": 10,
            "petId": 222222,
            "quantity": 1,
            "status": "placed",
            "complete": False,
            "shipDate": "2020-12-02",
        },
        match_querystring=True,
    )
    assert petstore.getOrderById(10) == {
        "id": 10,
        "petId": 222222,
        "quantity": 1,
        "status": "placed",
        "complete": False,
        "shipDate": "2020-12-02",
    }


def test_get_user_by_name(responses: RequestsMock, petstore_service, test_api_service):
    load_as_python_module()
    responses.add(
        responses.POST,
        url="https://petstore.swagger.io/v2/user",
        json={},
        match_querystring=True,
    )

    from pyxelrest.generated import petstore

    petstore.createUser(
        id=666666,
        username="JD",
        firstName="John",
        lastName="Doe",
        email="jdoe@petstore.com",
        password="azerty",
        phone="0123456789",
        userStatus=0,
    )
    assert (
        _get_request(responses, "https://petstore.swagger.io/v2/user").body
        == b"""{"id": 666666, "username": "JD", "firstName": "John", "lastName": "Doe", "email": "jdoe@petstore.com", "password": "azerty", "phone": "0123456789", "userStatus": 0}"""
    )

    responses.add(
        responses.GET,
        url="https://petstore.swagger.io/v2/user/JD",
        json={
            "id": 666666,
            "username": "JD",
            "firstName": "John",
            "lastName": "Doe",
            "email": "jdoe@petstore.com",
            "password": "azerty",
            "phone": "0123456789",
            "userStatus": 0,
        },
        match_querystring=True,
    )

    assert petstore.getUserByName("JD") == {
        "id": 666666,
        "username": "JD",
        "firstName": "John",
        "lastName": "Doe",
        "email": "jdoe@petstore.com",
        "password": "azerty",
        "phone": "0123456789",
        "userStatus": 0,
    }


def test_raw_text_response(responses: RequestsMock, test_api_service):
    load_as_python_module()
    responses.add(
        responses.GET,
        url="http://test/text",
        body=b"This is the content of the response.",
        match_querystring=True,
    )

    from pyxelrest.generated import text_api

    assert text_api.get_text() == "This is the content of the response."


def test_http_error_response(responses: RequestsMock, test_api_service):
    load_as_python_module()
    responses.add(
        responses.GET,
        url="http://test/text",
        body=b"This is the content of the response.",
        status=500,
        match_querystring=True,
    )

    from pyxelrest.generated import text_api

    with pytest.raises(requests.exceptions.HTTPError):
        text_api.get_text()
