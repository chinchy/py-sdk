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
from pydantic import BaseModel, Field, StrictFloat, StrictStr, ValidationError, validator
from typing import Any, List, Literal
from pydantic import StrictStr, Field, validate_arguments

TRANSACTIONREQUESTGASPRICE_ONE_OF_SCHEMAS = ["float", "str"]

class TransactionRequestGasPrice(BaseModel):
    """
    For non-EIP-1559, EVM-based transactions. Price per gas unit (in Ethereum this is specified in Gwei).  Note: Only two of the three arguments can be specified in a single transaction: `gasLimit`, `gasPrice` and `networkFee`. Fireblocks recommends using a numeric string for accurate precision.  Although a number input exists, it is deprecated.
    """
    # data type: str
    oneof_schema_1_validator: Optional[StrictStr] = Field(None, description="Numeric string (recommended)")
    # data type: float
    oneof_schema_2_validator: Optional[StrictFloat] = Field(None, description="Number (deprecated)")
    actual_instance: Any
    one_of_schemas: List[str] = Literal[TRANSACTIONREQUESTGASPRICE_ONE_OF_SCHEMAS]

    class Config:
        validate_assignment = True
        arbitrary_types_allowed = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: str
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # validate data type: float
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransactionRequestGasPrice with oneOf schemas: float, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TransactionRequestGasPrice with oneOf schemas: float, str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> TransactionRequestGasPrice:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> TransactionRequestGasPrice:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into str
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into float
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransactionRequestGasPrice with oneOf schemas: float, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TransactionRequestGasPrice with oneOf schemas: float, str. Details: " + ", ".join(error_messages))
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

