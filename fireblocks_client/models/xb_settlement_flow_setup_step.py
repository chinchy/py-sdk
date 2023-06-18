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



from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictStr
from fireblocks_client.models.xb_settlement_asset import XBSettlementAsset

class XBSettlementFlowSetupStep(BaseModel):
    """
    XBSettlementFlowSetupStep
    """
    account_id: StrictStr = Field(..., alias="accountId")
    input_amount: XBSettlementAsset = Field(..., alias="inputAmount")
    output_amount: XBSettlementAsset = Field(..., alias="outputAmount")
    estimated_fee_amount: XBSettlementAsset = Field(..., alias="estimatedFeeAmount")
    estimated_time: StrictFloat = Field(..., alias="estimatedTime", description="The estimated time for executing the step.")
    is_sign_required: StrictBool = Field(..., alias="isSignRequired", description="Whether or not signing is required for executing the step.")
    __properties = ["accountId", "inputAmount", "outputAmount", "estimatedFeeAmount", "estimatedTime", "isSignRequired"]

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
    def from_json(cls, json_str: str) -> XBSettlementFlowSetupStep:
        """Create an instance of XBSettlementFlowSetupStep from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of input_amount
        if self.input_amount:
            _dict['inputAmount'] = self.input_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of output_amount
        if self.output_amount:
            _dict['outputAmount'] = self.output_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of estimated_fee_amount
        if self.estimated_fee_amount:
            _dict['estimatedFeeAmount'] = self.estimated_fee_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> XBSettlementFlowSetupStep:
        """Create an instance of XBSettlementFlowSetupStep from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return XBSettlementFlowSetupStep.parse_obj(obj)

        _obj = XBSettlementFlowSetupStep.parse_obj({
            "account_id": obj.get("accountId"),
            "input_amount": XBSettlementAsset.from_dict(obj.get("inputAmount")) if obj.get("inputAmount") is not None else None,
            "output_amount": XBSettlementAsset.from_dict(obj.get("outputAmount")) if obj.get("outputAmount") is not None else None,
            "estimated_fee_amount": XBSettlementAsset.from_dict(obj.get("estimatedFeeAmount")) if obj.get("estimatedFeeAmount") is not None else None,
            "estimated_time": obj.get("estimatedTime"),
            "is_sign_required": obj.get("isSignRequired")
        })
        return _obj

