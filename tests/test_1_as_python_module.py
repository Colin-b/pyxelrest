import datetime

from responses import RequestsMock

from tests.test_petstore import petstore_service


def load_petstore_as_python_module():
    import pyxelrest

    pyxelrest.load(
        {
            "petstore": {
                "open_api": {
                    "definition": "http://petstore.swagger.io/v2/swagger.json"
                },
                "udf_name_prefix": "",
            }
        }
    )


def test_get_order_by_id(responses: RequestsMock, petstore_service):
    load_petstore_as_python_module()
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

    from pyxelrest import user_defined_functions

    now = datetime.datetime.utcnow()
    assert user_defined_functions.placeOrder(
        id=10, petId=222222, quantity=1, shipDate=now, status="placed", complete=False
    ) == {
        "id": 10,
        "petId": 222222,
        "quantity": 1,
        "status": "placed",
        "complete": False,
        "shipDate": "2020-12-02",
    }
    # TODO Assert what is sent to the server

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
    assert user_defined_functions.getOrderById(10) == {
        "id": 10,
        "petId": 222222,
        "quantity": 1,
        "status": "placed",
        "complete": False,
        "shipDate": "2020-12-02",
    }
    # TODO Assert what is sent to the server


def test_get_user_by_name(responses: RequestsMock, petstore_service):
    load_petstore_as_python_module()
    responses.add(
        responses.POST,
        url="https://petstore.swagger.io/v2/user",
        json={},
        match_querystring=True,
    )

    from pyxelrest import user_defined_functions

    user_defined_functions.createUser(
        id=666666,
        username="JD",
        firstName="John",
        lastName="Doe",
        email="jdoe@petstore.com",
        password="azerty",
        phone="0123456789",
        userStatus=0,
    )
    # TODO Assert what is sent to the server

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

    assert user_defined_functions.getUserByName("JD") == {
        "id": 666666,
        "username": "JD",
        "firstName": "John",
        "lastName": "Doe",
        "email": "jdoe@petstore.com",
        "password": "azerty",
        "phone": "0123456789",
        "userStatus": 0,
    }
    # TODO Assert what is sent to the server
