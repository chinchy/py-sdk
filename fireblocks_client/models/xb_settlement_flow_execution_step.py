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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictStr
from fireblocks_client.models.xb_settlement_asset import XBSettlementAsset
from fireblocks_client.models.xb_settlement_flow_execution_step_status import XBSettlementFlowExecutionStepStatus

class XBSettlementFlowExecutionStep(BaseModel):
    """
    XBSettlementFlowExecutionStep
    """
    id: StrictStr = Field(..., description="A unique id for the step execution")
    account_id: StrictStr = Field(..., alias="accountId")
    status: XBSettlementFlowExecutionStepStatus = ...
    input_amount: XBSettlementAsset = Field(..., alias="inputAmount")
    output_amount: Optional[XBSettlementAsset] = Field(None, alias="outputAmount")
    fee: Optional[XBSettlementAsset] = None
    started_at: Optional[StrictFloat] = Field(None, alias="startedAt", description="The step execution start time in epoch format.")
    completed_at: Optional[StrictFloat] = Field(None, alias="completedAt", description="The step execution end time in epoch format.")
    is_sign_required: StrictBool = Field(..., alias="isSignRequired", description="Whether or not signing is required for executing the step.")
    __properties = ["id", "accountId", "status", "inputAmount", "outputAmount", "fee", "startedAt", "completedAt", "isSignRequired"]

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
    def from_json(cls, json_str: str) -> XBSettlementFlowExecutionStep:
        """Create an instance of XBSettlementFlowExecutionStep from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fee
        if self.fee:
            _dict['fee'] = self.fee.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> XBSettlementFlowExecutionStep:
        """Create an instance of XBSettlementFlowExecutionStep from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return XBSettlementFlowExecutionStep.parse_obj(obj)

        _obj = XBSettlementFlowExecutionStep.parse_obj({
            "id": obj.get("id"),
            "account_id": obj.get("accountId"),
            "status": obj.get("status"),
            "input_amount": XBSettlementAsset.from_dict(obj.get("inputAmount")) if obj.get("inputAmount") is not None else None,
            "output_amount": XBSettlementAsset.from_dict(obj.get("outputAmount")) if obj.get("outputAmount") is not None else None,
            "fee": XBSettlementAsset.from_dict(obj.get("fee")) if obj.get("fee") is not None else None,
            "started_at": obj.get("startedAt"),
            "completed_at": obj.get("completedAt"),
            "is_sign_required": obj.get("isSignRequired")
        })
        return _obj

