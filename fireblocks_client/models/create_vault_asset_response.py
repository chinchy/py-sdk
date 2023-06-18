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

class CreateVaultAssetResponse(BaseModel):
    """
    CreateVaultAssetResponse
    """
    id: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    legacy_address: Optional[StrictStr] = Field(None, alias="legacyAddress")
    enterprise_address: Optional[StrictStr] = Field(None, alias="enterpriseAddress")
    tag: Optional[StrictStr] = None
    eos_account_name: Optional[StrictStr] = Field(None, alias="eosAccountName")
    status: Optional[StrictStr] = None
    activation_tx_id: Optional[StrictStr] = Field(None, alias="activationTxId")
    __properties = ["id", "address", "legacyAddress", "enterpriseAddress", "tag", "eosAccountName", "status", "activationTxId"]

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
    def from_json(cls, json_str: str) -> CreateVaultAssetResponse:
        """Create an instance of CreateVaultAssetResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateVaultAssetResponse:
        """Create an instance of CreateVaultAssetResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreateVaultAssetResponse.parse_obj(obj)

        _obj = CreateVaultAssetResponse.parse_obj({
            "id": obj.get("id"),
            "address": obj.get("address"),
            "legacy_address": obj.get("legacyAddress"),
            "enterprise_address": obj.get("enterpriseAddress"),
            "tag": obj.get("tag"),
            "eos_account_name": obj.get("eosAccountName"),
            "status": obj.get("status"),
            "activation_tx_id": obj.get("activationTxId")
        })
        return _obj

