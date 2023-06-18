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


from typing import Dict, Optional
from pydantic import BaseModel, StrictFloat, StrictStr, validator

class AuthorizationGroups(BaseModel):
    """
    AuthorizationGroups
    """
    th: Optional[StrictFloat] = None
    users: Optional[Dict[str, StrictStr]] = None
    __properties = ["th", "users"]

    @validator('users')
    def users_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('PENDING_AUTHORIZATION', 'APPROVED', 'REJECTED', 'NA'):
            raise ValueError("must be one of enum values ('PENDING_AUTHORIZATION', 'APPROVED', 'REJECTED', 'NA')")
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
    def from_json(cls, json_str: str) -> AuthorizationGroups:
        """Create an instance of AuthorizationGroups from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthorizationGroups:
        """Create an instance of AuthorizationGroups from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AuthorizationGroups.parse_obj(obj)

        _obj = AuthorizationGroups.parse_obj({
            "th": obj.get("th"),
            "users": obj.get("users")
        })
        return _obj

