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


from typing import Any, Optional
from pydantic import BaseModel, Field, StrictStr
from fireblocks_client.models.aml_screening_result import AmlScreeningResult
from fireblocks_client.models.authorization_info import AuthorizationInfo
from fireblocks_client.models.destination_transfer_peer_path_response import DestinationTransferPeerPathResponse

class TransactionResponseDestination(BaseModel):
    """
    TransactionResponseDestination
    """
    destination_address: Optional[Any] = Field(None, alias="destinationAddress", description="Address where the asset was transferred.")
    destination_address_description: Optional[Any] = Field(None, alias="destinationAddressDescription", description="Description of the address.")
    amount: Optional[StrictStr] = Field(None, description="The amount to be sent to this destination.")
    amount_usd: Optional[StrictStr] = Field(None, alias="amountUSD", description="The USD value of the requested amount.")
    aml_screening_result: Optional[AmlScreeningResult] = Field(None, alias="amlScreeningResult")
    destination: Optional[DestinationTransferPeerPathResponse] = None
    authorization_info: Optional[AuthorizationInfo] = Field(None, alias="authorizationInfo")
    __properties = ["destinationAddress", "destinationAddressDescription", "amount", "amountUSD", "amlScreeningResult", "destination", "authorizationInfo"]

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
    def from_json(cls, json_str: str) -> TransactionResponseDestination:
        """Create an instance of TransactionResponseDestination from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of aml_screening_result
        if self.aml_screening_result:
            _dict['amlScreeningResult'] = self.aml_screening_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of authorization_info
        if self.authorization_info:
            _dict['authorizationInfo'] = self.authorization_info.to_dict()
        # set to None if destination_address (nullable) is None
        # and __fields_set__ contains the field
        if self.destination_address is None and "destination_address" in self.__fields_set__:
            _dict['destinationAddress'] = None

        # set to None if destination_address_description (nullable) is None
        # and __fields_set__ contains the field
        if self.destination_address_description is None and "destination_address_description" in self.__fields_set__:
            _dict['destinationAddressDescription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionResponseDestination:
        """Create an instance of TransactionResponseDestination from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TransactionResponseDestination.parse_obj(obj)

        _obj = TransactionResponseDestination.parse_obj({
            "destination_address": obj.get("destinationAddress"),
            "destination_address_description": obj.get("destinationAddressDescription"),
            "amount": obj.get("amount"),
            "amount_usd": obj.get("amountUSD"),
            "aml_screening_result": AmlScreeningResult.from_dict(obj.get("amlScreeningResult")) if obj.get("amlScreeningResult") is not None else None,
            "destination": DestinationTransferPeerPathResponse.from_dict(obj.get("destination")) if obj.get("destination") is not None else None,
            "authorization_info": AuthorizationInfo.from_dict(obj.get("authorizationInfo")) if obj.get("authorizationInfo") is not None else None
        })
        return _obj

