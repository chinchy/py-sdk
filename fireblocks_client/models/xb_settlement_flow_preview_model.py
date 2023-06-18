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



from pydantic import BaseModel, Field, StrictFloat, StrictStr
from fireblocks_client.models.xb_settlement_asset import XBSettlementAsset
from fireblocks_client.models.xb_settlement_flow_steps_record import XBSettlementFlowStepsRecord

class XBSettlementFlowPreviewModel(BaseModel):
    """
    XBSettlementFlowPreviewModel
    """
    flow_id: StrictStr = Field(..., alias="flowId", description="The unique id for the cross-border flow.")
    config_id: StrictStr = Field(..., alias="configId", description="Cross Bodrder configuraion unique id")
    conversion_rate: StrictStr = Field(..., alias="conversionRate", description="The conversion rate received from the on-ramp or off-ramp.")
    input_amount: XBSettlementAsset = Field(..., alias="inputAmount")
    estimated_output_amount: XBSettlementAsset = Field(..., alias="estimatedOutputAmount")
    total_estimated_fee: XBSettlementAsset = Field(..., alias="totalEstimatedFee")
    total_estimated_time: StrictFloat = Field(..., alias="totalEstimatedTime", description="The total *estimated* time for executing the cross-border flow.")
    steps: XBSettlementFlowStepsRecord = ...
    __properties = ["flowId", "configId", "conversionRate", "inputAmount", "estimatedOutputAmount", "totalEstimatedFee", "totalEstimatedTime", "steps"]

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
    def from_json(cls, json_str: str) -> XBSettlementFlowPreviewModel:
        """Create an instance of XBSettlementFlowPreviewModel from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of estimated_output_amount
        if self.estimated_output_amount:
            _dict['estimatedOutputAmount'] = self.estimated_output_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of total_estimated_fee
        if self.total_estimated_fee:
            _dict['totalEstimatedFee'] = self.total_estimated_fee.to_dict()
        # override the default output from pydantic by calling `to_dict()` of steps
        if self.steps:
            _dict['steps'] = self.steps.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> XBSettlementFlowPreviewModel:
        """Create an instance of XBSettlementFlowPreviewModel from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return XBSettlementFlowPreviewModel.parse_obj(obj)

        _obj = XBSettlementFlowPreviewModel.parse_obj({
            "flow_id": obj.get("flowId"),
            "config_id": obj.get("configId"),
            "conversion_rate": obj.get("conversionRate"),
            "input_amount": XBSettlementAsset.from_dict(obj.get("inputAmount")) if obj.get("inputAmount") is not None else None,
            "estimated_output_amount": XBSettlementAsset.from_dict(obj.get("estimatedOutputAmount")) if obj.get("estimatedOutputAmount") is not None else None,
            "total_estimated_fee": XBSettlementAsset.from_dict(obj.get("totalEstimatedFee")) if obj.get("totalEstimatedFee") is not None else None,
            "total_estimated_time": obj.get("totalEstimatedTime"),
            "steps": XBSettlementFlowStepsRecord.from_dict(obj.get("steps")) if obj.get("steps") is not None else None
        })
        return _obj

