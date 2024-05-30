"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pytest
import json
import ast
from fireblocks.unknown_model import create_unknown_model, UnknownBaseModel

@pytest.fixture
def unknown_model_example():
    data = {"name": "John Doe", "age": 25}
    model = create_unknown_model(data)
    return data, model.parse_obj(data)

def test_create_unknown_model(unknown_model_example):
    data, model = unknown_model_example

    assert isinstance(model, UnknownBaseModel)
    assert model.dict() == data

def test_to_json(unknown_model_example):
    data, model = unknown_model_example

    json_data = model.to_json()
    assert json.loads(json_data) == data

def test_to_dict(unknown_model_example):
    data, model = unknown_model_example

    dict_data = model.to_dict()
    assert dict_data == data

def test_to_str(unknown_model_example):
    data, model = unknown_model_example

    str_data = model.to_str()
    assert type(str_data) == str
    assert ast.literal_eval(str_data) == ast.literal_eval(str(data))