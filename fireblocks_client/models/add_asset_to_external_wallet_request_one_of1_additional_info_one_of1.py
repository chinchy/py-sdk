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

class AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf1(BaseModel):
    """
    AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf1
    """
    account_holder_given_name: StrictStr = Field(..., alias="accountHolderGivenName")
    account_holder_surname: Optional[StrictStr] = Field(None, alias="accountHolderSurname")
    account_holder_city: StrictStr = Field(..., alias="accountHolderCity")
    account_holder_country: StrictStr = Field(..., alias="accountHolderCountry")
    account_holder_address1: StrictStr = Field(..., alias="accountHolderAddress1")
    account_holder_address2: Optional[StrictStr] = Field(None, alias="accountHolderAddress2")
    account_holder_district: Optional[StrictStr] = Field(None, alias="accountHolderDistrict")
    account_holder_postal_code: StrictStr = Field(..., alias="accountHolderPostalCode")
    aba_routing_number: StrictStr = Field(..., alias="abaRoutingNumber")
    aba_account_number: StrictStr = Field(..., alias="abaAccountNumber")
    aba_country: StrictStr = Field(..., alias="abaCountry")
    __properties = ["accountHolderGivenName", "accountHolderSurname", "accountHolderCity", "accountHolderCountry", "accountHolderAddress1", "accountHolderAddress2", "accountHolderDistrict", "accountHolderPostalCode", "abaRoutingNumber", "abaAccountNumber", "abaCountry"]

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
    def from_json(cls, json_str: str) -> AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf1:
        """Create an instance of AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf1:
        """Create an instance of AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf1 from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf1.parse_obj(obj)

        _obj = AddAssetToExternalWalletRequestOneOf1AdditionalInfoOneOf1.parse_obj({
            "account_holder_given_name": obj.get("accountHolderGivenName"),
            "account_holder_surname": obj.get("accountHolderSurname"),
            "account_holder_city": obj.get("accountHolderCity"),
            "account_holder_country": obj.get("accountHolderCountry"),
            "account_holder_address1": obj.get("accountHolderAddress1"),
            "account_holder_address2": obj.get("accountHolderAddress2"),
            "account_holder_district": obj.get("accountHolderDistrict"),
            "account_holder_postal_code": obj.get("accountHolderPostalCode"),
            "aba_routing_number": obj.get("abaRoutingNumber"),
            "aba_account_number": obj.get("abaAccountNumber"),
            "aba_country": obj.get("abaCountry")
        })
        return _obj

