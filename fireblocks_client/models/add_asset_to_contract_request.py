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
from pydantic import BaseModel, Field, StrictStr

class AddAssetToContractRequest(BaseModel):
    """
    AddAssetToContractRequest
    """
    address: StrictStr = Field(..., description="The contract's address (or xpub) of the wallet")
    tag: Optional[StrictStr] = Field(None, description="The destination tag, for XRP wallets")
    __properties = ["address", "tag"]

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
    def from_json(cls, json_str: str) -> AddAssetToContractRequest:
        """Create an instance of AddAssetToContractRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddAssetToContractRequest:
        """Create an instance of AddAssetToContractRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AddAssetToContractRequest.parse_obj(obj)

        _obj = AddAssetToContractRequest.parse_obj({
            "address": obj.get("address"),
            "tag": obj.get("tag")
        })
        return _obj

