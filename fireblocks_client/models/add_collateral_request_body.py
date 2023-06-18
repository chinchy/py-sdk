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
from pydantic import BaseModel, Field, StrictBool
from fireblocks_client.models.transaction_request import TransactionRequest

class AddCollateralRequestBody(BaseModel):
    """
    AddCollateralRequestBody
    """
    transaction_request: Optional[TransactionRequest] = Field(None, alias="transactionRequest")
    is_src_collateral: Optional[StrictBool] = Field(None, alias="isSrcCollateral", description="optional")
    __properties = ["transactionRequest", "isSrcCollateral"]

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
    def from_json(cls, json_str: str) -> AddCollateralRequestBody:
        """Create an instance of AddCollateralRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of transaction_request
        if self.transaction_request:
            _dict['transactionRequest'] = self.transaction_request.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddCollateralRequestBody:
        """Create an instance of AddCollateralRequestBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AddCollateralRequestBody.parse_obj(obj)

        _obj = AddCollateralRequestBody.parse_obj({
            "transaction_request": TransactionRequest.from_dict(obj.get("transactionRequest")) if obj.get("transactionRequest") is not None else None,
            "is_src_collateral": obj.get("isSrcCollateral")
        })
        return _obj

