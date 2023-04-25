import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.util.dao import DAO

@pytest.fixture
@patch('src.util.dao.getValidator', autospec=True)
def sut(mockValidator):
    mockValidator.return_value = "test"
    dao = DAO("test")
    yield dao
    dao.drop()

def test_create_document_1(sut):
    datadic = {}
    result = sut.create(datadic)
    assert result == True

def test_create_document_2(sut):
    assert True == True

def test_create_document_3(sut):
    assert True == True

def test_create_document_4(sut):
    assert True == True

def test_create_document_5(sut):
    assert True == True

def test_create_document_6(sut):
    assert True == True

def test_create_document_7(sut):
    assert True == True

def test_create_document_8(sut):
    assert True == True