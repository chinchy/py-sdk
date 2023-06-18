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

class DropTransactionRequest(BaseModel):
    """
    DropTransactionRequest
    """
    tx_id: Optional[StrictStr] = Field(None, alias="txId")
    fee_level: Optional[StrictStr] = Field(None, alias="feeLevel")
    gas_price: Optional[StrictStr] = Field(None, alias="gasPrice")
    __properties = ["txId", "feeLevel", "gasPrice"]

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
    def from_json(cls, json_str: str) -> DropTransactionRequest:
        """Create an instance of DropTransactionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DropTransactionRequest:
        """Create an instance of DropTransactionRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DropTransactionRequest.parse_obj(obj)

        _obj = DropTransactionRequest.parse_obj({
            "tx_id": obj.get("txId"),
            "fee_level": obj.get("feeLevel"),
            "gas_price": obj.get("gasPrice")
        })
        return _obj

