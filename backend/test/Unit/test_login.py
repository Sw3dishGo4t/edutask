import pytest
import unittest.mock as mock
from src.controllers.usercontroller import UserController

@pytest.mark.unit
def test_getUser1():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = ["TestUser"]
    sut = UserController(mockdao)
    email = "test.test@gmail.com"
    
    assert sut.get_user_by_email(email) == "TestUser"

@pytest.mark.unit
def test_getUser2():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = ["TestUser"]
    sut = UserController(mockdao)
    email = "test.test"
    with pytest.raises(ValueError):
        sut.get_user_by_email(email)

@pytest.mark.unit
def test_getUser3():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = []
    sut = UserController(mockdao)
    email = "test.test@gmail.com"
    with pytest.raises(Exception):
         sut.get_user_by_email(email)

@pytest.mark.unit
def test_getUser4():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = []
    sut = UserController(mockdao)
    email = "test.test"
    with pytest.raises(ValueError):
        sut.get_user_by_email(email)