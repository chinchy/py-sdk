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

class AmountInfo(BaseModel):
    """
    The details of the requested amount to transfer.
    """
    amount: Optional[StrictStr] = Field(None, description="If the transfer is a withdrawal from an exchange, the actual amount that was requested to be transferred. Otherwise, the requested amount.")
    requested_amount: Optional[StrictStr] = Field(None, alias="requestedAmount", description="The amount requested by the user.")
    net_amount: Optional[StrictStr] = Field(None, alias="netAmount", description="The net amount of the transaction, after fee deduction.")
    amount_usd: Optional[StrictStr] = Field(None, alias="amountUSD", description="The USD value of the requested amount.")
    __properties = ["amount", "requestedAmount", "netAmount", "amountUSD"]

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
    def from_json(cls, json_str: str) -> AmountInfo:
        """Create an instance of AmountInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AmountInfo:
        """Create an instance of AmountInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AmountInfo.parse_obj(obj)

        _obj = AmountInfo.parse_obj({
            "amount": obj.get("amount"),
            "requested_amount": obj.get("requestedAmount"),
            "net_amount": obj.get("netAmount"),
            "amount_usd": obj.get("amountUSD")
        })
        return _obj

