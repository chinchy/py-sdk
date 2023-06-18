# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class SystemMessageInfo(BaseModel):
    """
    SystemMessageInfo
    """
    type: Optional[StrictStr] = None
    message: Optional[StrictStr] = Field(None, description="A response from Fireblocks that communicates a message about the health of the process being performed. If this object is returned with data, you should expect potential delays or incomplete transaction statuses.")
    __properties = ["type", "message"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('WARN', 'BLOCK'):
            raise ValueError("must be one of enum values ('WARN', 'BLOCK')")
        return v

    class Config:
        populate_by_name = True
        validate_assignment = True
        arbitrary_types_allowed = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SystemMessageInfo:
        """Create an instance of SystemMessageInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SystemMessageInfo:
        """Create an instance of SystemMessageInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SystemMessageInfo.parse_obj(obj)

        _obj = SystemMessageInfo.parse_obj({
            "type": obj.get("type"),
            "message": obj.get("message")
        })
        return _obj

