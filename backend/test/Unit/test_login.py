import pytest
import unittest.mock as mock
from src.controllers.usercontroller import UserController

def test_getUser1():
    mockdao = mock.MagicMock()
    mockdao.find.return_value = {'users': "TestUser"}
    sut = UserController
    email = "test.test@gmail.com"
    
    assert sut.get_user_by_email(email) == "TestUser"
def test_getUser2():
    email = "test.test"
    assert True == True
def test_getUser3():
    email = "test.test@gmail.com"
    assert True == True
def test_getUser4():
    email = "test.test"
    assert True == True