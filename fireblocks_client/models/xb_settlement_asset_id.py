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
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from fireblocks_client.models.xb_settlement_crypto_asset import XBSettlementCryptoAsset
from fireblocks_client.models.xb_settlement_fiat_asset import XBSettlementFiatAsset
from typing import Any, List, Literal
from pydantic import StrictStr, Field, validate_arguments

XBSETTLEMENTASSETID_ONE_OF_SCHEMAS = ["XBSettlementCryptoAsset", "XBSettlementFiatAsset"]

class XBSettlementAssetID(BaseModel):
    """
    XBSettlementAssetID
    """
    # data type: XBSettlementFiatAsset
    oneof_schema_1_validator: Optional[XBSettlementFiatAsset] = None
    # data type: XBSettlementCryptoAsset
    oneof_schema_2_validator: Optional[XBSettlementCryptoAsset] = None
    actual_instance: Any
    one_of_schemas: List[str] = Literal[XBSETTLEMENTASSETID_ONE_OF_SCHEMAS]

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: XBSettlementFiatAsset
        if type(v) is not XBSettlementFiatAsset:
            error_messages.append(f"Error! Input type `{type(v)}` is not `XBSettlementFiatAsset`")
        else:
            match += 1

        # validate data type: XBSettlementCryptoAsset
        if type(v) is not XBSettlementCryptoAsset:
            error_messages.append(f"Error! Input type `{type(v)}` is not `XBSettlementCryptoAsset`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into XBSettlementAssetID with oneOf schemas: XBSettlementCryptoAsset, XBSettlementFiatAsset. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into XBSettlementAssetID with oneOf schemas: XBSettlementCryptoAsset, XBSettlementFiatAsset. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> XBSettlementAssetID:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> XBSettlementAssetID:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into XBSettlementFiatAsset
        try:
            instance.actual_instance = XBSettlementFiatAsset.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into XBSettlementCryptoAsset
        try:
            instance.actual_instance = XBSettlementCryptoAsset.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into XBSettlementAssetID with oneOf schemas: XBSettlementCryptoAsset, XBSettlementFiatAsset. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into XBSettlementAssetID with oneOf schemas: XBSettlementCryptoAsset, XBSettlementFiatAsset. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

