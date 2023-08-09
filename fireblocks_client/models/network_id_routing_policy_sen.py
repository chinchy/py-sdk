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
from fireblocks_client.models.custom_fiat_routing_dest import CustomFiatRoutingDest
from fireblocks_client.models.none_network_routing_dest import NoneNetworkRoutingDest
from typing import Any, List, Literal
from pydantic import Field, validate_arguments

NETWORKIDROUTINGPOLICYSEN_ONE_OF_SCHEMAS = ["CustomFiatRoutingDest", "NoneNetworkRoutingDest"]

class NetworkIdRoutingPolicySen(BaseModel):
    """
    NetworkIdRoutingPolicySen
    """
    # data type: CustomFiatRoutingDest
    oneof_schema_1_validator: Optional[CustomFiatRoutingDest] = None
    # data type: NoneNetworkRoutingDest
    oneof_schema_2_validator: Optional[NoneNetworkRoutingDest] = None
    actual_instance: Any
    one_of_schemas: List[str] = Literal[NETWORKIDROUTINGPOLICYSEN_ONE_OF_SCHEMAS]

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: CustomFiatRoutingDest
        if type(v) is not CustomFiatRoutingDest:
            error_messages.append(f"Error! Input type `{type(v)}` is not `CustomFiatRoutingDest`")
        else:
            match += 1

        # validate data type: NoneNetworkRoutingDest
        if type(v) is not NoneNetworkRoutingDest:
            error_messages.append(f"Error! Input type `{type(v)}` is not `NoneNetworkRoutingDest`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into NetworkIdRoutingPolicySen with oneOf schemas: CustomFiatRoutingDest, NoneNetworkRoutingDest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into NetworkIdRoutingPolicySen with oneOf schemas: CustomFiatRoutingDest, NoneNetworkRoutingDest. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> NetworkIdRoutingPolicySen:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> NetworkIdRoutingPolicySen:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into CustomFiatRoutingDest
        try:
            instance.actual_instance = CustomFiatRoutingDest.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into NoneNetworkRoutingDest
        try:
            instance.actual_instance = NoneNetworkRoutingDest.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into NetworkIdRoutingPolicySen with oneOf schemas: CustomFiatRoutingDest, NoneNetworkRoutingDest. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into NetworkIdRoutingPolicySen with oneOf schemas: CustomFiatRoutingDest, NoneNetworkRoutingDest. Details: " + ", ".join(error_messages))
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

