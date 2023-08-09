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


from typing import List
from pydantic import BaseModel, Field, conlist
from fireblocks_client.models.policy_check_result import PolicyCheckResult
from fireblocks_client.models.policy_metadata import PolicyMetadata
from fireblocks_client.models.policy_rule import PolicyRule
from fireblocks_client.models.policy_status import PolicyStatus

class PublishResult(BaseModel):
    """
    Response object of the publish policy operation
    """
    status: PolicyStatus = ...
    rules: conlist(PolicyRule) = ...
    check_result: PolicyCheckResult = Field(..., alias="checkResult")
    metadata: PolicyMetadata = ...
    __properties = ["status", "rules", "checkResult", "metadata"]

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
    def from_json(cls, json_str: str) -> PublishResult:
        """Create an instance of PublishResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of check_result
        if self.check_result:
            _dict['checkResult'] = self.check_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PublishResult:
        """Create an instance of PublishResult from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PublishResult.parse_obj(obj)

        _obj = PublishResult.parse_obj({
            "status": obj.get("status"),
            "rules": [PolicyRule.from_dict(_item) for _item in obj.get("rules")] if obj.get("rules") is not None else None,
            "check_result": PolicyCheckResult.from_dict(obj.get("checkResult")) if obj.get("checkResult") is not None else None,
            "metadata": PolicyMetadata.from_dict(obj.get("metadata")) if obj.get("metadata") is not None else None
        })
        return _obj

