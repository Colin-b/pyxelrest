import datetime

import pytest
from responses import RequestsMock

from testsutils import loader


@pytest.fixture
def petstore_service(responses: RequestsMock):
    loader.load("petstore_services.yml")


def test_get_order_by_id(petstore_service):
    from pyxelrest import pyxelrestgenerator

    now = datetime.datetime.utcnow()
    new_order_response = pyxelrestgenerator.petstore_placeOrder(
        id=10, petId=222222, quantity=1, shipDate=now, status="placed", complete=False
    )
    # Petstore is replying with server time...
    del new_order_response[1][3]
    assert new_order_response == [
        ["id", "petId", "quantity", "shipDate", "status", "complete"],
        [10, 222222, 1, "placed", False],
    ]

    get_order_response = pyxelrestgenerator.petstore_getOrderById(10)
    # Petstore is replying with server time...
    del get_order_response[1][3]
    assert get_order_response == [
        ["id", "petId", "quantity", "shipDate", "status", "complete"],
        [10, 222222, 1, "placed", False],
    ]


def test_get_user_by_name(petstore_service):
    from pyxelrest import pyxelrestgenerator

    pyxelrestgenerator.petstore_createUser(
        id=666666,
        username="JD",
        firstName="John",
        lastName="Doe",
        email="jdoe@petstore.com",
        password="azerty",
        phone="0123456789",
        userStatus=0,
    )
    assert pyxelrestgenerator.petstore_getUserByName("JD") == [
        [
            "id",
            "username",
            "firstName",
            "lastName",
            "email",
            "password",
            "phone",
            "userStatus",
        ],
        [666666, "JD", "John", "Doe", "jdoe@petstore.com", "azerty", "0123456789", 0],
    ]
