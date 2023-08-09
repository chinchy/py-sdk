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

class DestinationTransferPeerPathResponse(BaseModel):
    """
    DestinationTransferPeerPathResponse
    """
    type: StrictStr = ...
    sub_type: Optional[StrictStr] = Field(None, alias="subType", description="In case the type is set to `EXCHANGE_ACCOUNT` or `FIAT_ACCOUNT`, the specific exchange vendor name or fiat vendor name.In case the type is set to `INTERNAL_WALLET` or `EXTERNAL_WALLET`, the subType is set to `Internal` or `External`.")
    id: Optional[StrictStr] = Field(None, description="The ID of the peer. You can retrieve the ID of each venue object using the endpoints for [listing vault accounts](https://developers.fireblocks.com/reference/get_vault-accounts-paged), [listing exchange account](https://developers.fireblocks.com/reference/get_exchange-accounts), [listing fiat accounts](https://developers.fireblocks.com/reference/get_fiat-accounts), [listing internal wallets](https://developers.fireblocks.com/reference/get_internal-wallets), [listing external wallets](https://developers.fireblocks.com/reference/get_external-wallets), [listing network connections](https://developers.fireblocks.com/reference/get_network-connections). For the other types, this parameter is not needed.")
    name: Optional[StrictStr] = Field(None, description="The name of the peer.")
    wallet_id: Optional[StrictStr] = Field(None, alias="walletId")
    __properties = ["type", "subType", "id", "name", "walletId"]

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
    def from_json(cls, json_str: str) -> DestinationTransferPeerPathResponse:
        """Create an instance of DestinationTransferPeerPathResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DestinationTransferPeerPathResponse:
        """Create an instance of DestinationTransferPeerPathResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DestinationTransferPeerPathResponse.parse_obj(obj)

        _obj = DestinationTransferPeerPathResponse.parse_obj({
            "type": obj.get("type"),
            "sub_type": obj.get("subType"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "wallet_id": obj.get("walletId")
        })
        return _obj

