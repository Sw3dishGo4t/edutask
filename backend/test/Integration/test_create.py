import pytest
import unittest.mock as mock
from unittest.mock import patch
from src.util.dao import DAO

@pytest.fixture
@patch('src.util.dao.getValidator', autospec=True)
def sut(mockValidator):
    mockValidator.return_value = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["title", "description"],
        "properties": {
            "title": {
                "bsonType": "string",
                "description": "the title of a task must be determined",
                "uniqueItems": True
            }, 
            "description": {
                "bsonType": "string",
                "description": "the description of a task must be determined"
            }
        }
    }
}
    dao = DAO("test")
    datadic =  {
            "title": "Improve Devtools",
            "description": "Upgrade the tools used for web development. In order to keep web development effective, the right choice of tools is critical. This video presents seven interesting tools: BundlePhobia, CloudCraft, Figma, Fontflipper, Visbug, Insomnia, and Flare."
        }
    dao.create(datadic)
    return dao
    

def test_create_document_1(sut):
    datadic2 =  {
                "title": "Devtools",
                "description": "Upgrade the tools used for web development. In order to keep web development effective, the right choice of tools is critical. This video presents seven interesting tools: BundlePhobia, CloudCraft, Figma, Fontflipper, Visbug, Insomnia, and Flare."
            }
    result = sut.create(datadic2)
    sut.drop()
    assert result['title'] == datadic2['title']

def test_create_document_2(sut):
    datadic2 =  {
                "title": "Improve Devtools",
                "description": "Upgrade the tools used for web development. In order to keep web development effective, the right choice of tools is critical. This video presents seven interesting tools: BundlePhobia, CloudCraft, Figma, Fontflipper, Visbug, Insomnia, and Flare."
            }
    with pytest.raises(Exception):
        sut.create(datadic2)
        sut.drop()

def test_create_document_3(sut):
    datadic2 =  {
                "title": "Devtools",
                "description": 2
                }
    with pytest.raises(Exception):
        result = sut.create(datadic2)
        sut.drop()

def test_create_document_4(sut):
    datadic2 =  {
                "title": "Devtools"
                }
    with pytest.raises(Exception):
        result = sut.create(datadic2)
        sut.drop()

def test_create_document_5(sut):
    datadic2 =  {
                "title": "Improve Devtools",
                "description": 2
                }
    with pytest.raises(Exception):
        result = sut.create(datadic2)
        sut.drop()

def test_create_document_6(sut):
    datadic2 =  {
                "title": "Improve Devtools"
                }
    with pytest.raises(Exception):
        result = sut.create(datadic2)
        sut.drop()

def test_create_document_7(sut):
    datadic2 =  {
                "title": 3
                }
    with pytest.raises(Exception):
        result = sut.create(datadic2)
        sut.drop()

def test_create_document_8(sut):
    datadic2 =  {
                "title": "Improve Devtools",
                "nope": 2
                }
    with pytest.raises(Exception):
        result = sut.create(datadic2)
        sut.drop()