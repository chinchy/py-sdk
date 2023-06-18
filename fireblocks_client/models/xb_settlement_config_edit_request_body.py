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
from pydantic import BaseModel, Field, StrictStr, conint
from fireblocks_client.models.xb_settlement_config_steps_record import XBSettlementConfigStepsRecord

class XBSettlementConfigEditRequestBody(BaseModel):
    """
    XBSettlementConfigEditRequestBody
    """
    name: StrictStr = Field(..., description="The name for the cross-border settlement configuration")
    steps: XBSettlementConfigStepsRecord = ...
    conversion_slippage_basis_points: Optional[conint(strict=True, le=10000, ge=0)] = Field(10000, alias="conversionSlippageBasisPoints", description="Slippage configuarion in basis points, the default value is 10% ")
    __properties = ["name", "steps", "conversionSlippageBasisPoints"]

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
    def from_json(cls, json_str: str) -> XBSettlementConfigEditRequestBody:
        """Create an instance of XBSettlementConfigEditRequestBody from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of steps
        if self.steps:
            _dict['steps'] = self.steps.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> XBSettlementConfigEditRequestBody:
        """Create an instance of XBSettlementConfigEditRequestBody from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return XBSettlementConfigEditRequestBody.parse_obj(obj)

        _obj = XBSettlementConfigEditRequestBody.parse_obj({
            "name": obj.get("name"),
            "steps": XBSettlementConfigStepsRecord.from_dict(obj.get("steps")) if obj.get("steps") is not None else None,
            "conversion_slippage_basis_points": obj.get("conversionSlippageBasisPoints") if obj.get("conversionSlippageBasisPoints") is not None else 10000
        })
        return _obj

