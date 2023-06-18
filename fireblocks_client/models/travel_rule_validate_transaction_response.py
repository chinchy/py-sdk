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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist

class TravelRuleValidateTransactionResponse(BaseModel):
    """
    TravelRuleValidateTransactionResponse
    """
    is_valid: StrictBool = Field(..., alias="isValid", description="\"isValid\" will tell you if you have collected all the information needed for the travel rule data transfer. Once this field = \"true\", you can move on to the next step which is to transfer the front-end information to your back-end and perform Travel Rule Transaction create")
    type: StrictStr = Field(..., description="\"type\" will tell you if the virtual asset value converted to FIAT value of the withdrawal request is above (=TRAVELRULE) or below (=BELOW_THRESHOLD) the threshold in your jurisdiction. If it is to an unhosted wallet which does not require travel rule information to be sent and only collected, it will say NON_CUSTODIAL.")
    beneficiary_address_type: StrictStr = Field(..., alias="beneficiaryAddressType", description="\"beneficiaryAddressType\" will tell you if your blockchain analytics provider or internal address book has been able to identify the wallet address.")
    address_source: StrictStr = Field(..., alias="addressSource", description="\"addressSource\" will tell you if the address was found in your internal address book or identified by the blockchain analytics provider.")
    beneficiary_vas_pdid: StrictStr = Field(..., alias="beneficiaryVASPdid", description="The VASP DID of the beneficiary VASP")
    beneficiary_vas_pname: StrictStr = Field(..., alias="beneficiaryVASPname", description="\"beneficiaryVASPname\" will tell you the name of the VASP that has been identified as the owner of the wallet address. This name is used in a subsequent call to get its DID.")
    warnings: conlist(StrictStr) = Field(..., description="\"errors/warnings\" will tell you what information about the beneficiary you need to collect from the sender.")
    __properties = ["isValid", "type", "beneficiaryAddressType", "addressSource", "beneficiaryVASPdid", "beneficiaryVASPname", "warnings"]

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
    def from_json(cls, json_str: str) -> TravelRuleValidateTransactionResponse:
        """Create an instance of TravelRuleValidateTransactionResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TravelRuleValidateTransactionResponse:
        """Create an instance of TravelRuleValidateTransactionResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TravelRuleValidateTransactionResponse.parse_obj(obj)

        _obj = TravelRuleValidateTransactionResponse.parse_obj({
            "is_valid": obj.get("isValid"),
            "type": obj.get("type"),
            "beneficiary_address_type": obj.get("beneficiaryAddressType"),
            "address_source": obj.get("addressSource"),
            "beneficiary_vas_pdid": obj.get("beneficiaryVASPdid"),
            "beneficiary_vas_pname": obj.get("beneficiaryVASPname"),
            "warnings": obj.get("warnings")
        })
        return _obj

