import pytest
import unittest.mock as mock
from src.controllers.usercontroller import UserController

def test_getUser1():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = ["TestUser"]
    sut = UserController(mockdao)
    email = "test.test@gmail.com"
    
    assert sut.get_user_by_email(email) == "TestUser"
def test_getUser2():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = ["TestUser"]
    sut = UserController(mockdao)
    email = "test.test"
    with pytest.raises(ValueError):
        sut.get_user_by_email(email)
def test_getUser3():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = []
    sut = UserController(mockdao)
    email = "test.test@gmail.com"
    with pytest.raises(Exception):
         sut.get_user_by_email(email)
def test_getUser4():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = []
    sut = UserController(mockdao)
    email = "test.test"
    with pytest.raises(ValueError):
        sut.get_user_by_email(email)