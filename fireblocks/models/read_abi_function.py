# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks.models.parameter import Parameter
from fireblocks.models.parameter_with_value import ParameterWithValue
from typing import Optional, Set
from typing_extensions import Self

class ReadAbiFunction(BaseModel):
    """
    ReadAbiFunction
    """ # noqa: E501
    state_mutability: StrictStr = Field(alias="stateMutability")
    outputs: Optional[List[Parameter]] = None
    name: Optional[StrictStr] = None
    type: StrictStr
    inputs: List[ParameterWithValue]
    description: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["stateMutability", "outputs", "name", "type", "inputs", "description"]

    @field_validator('state_mutability')
    def state_mutability_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pure', 'view']):
            raise ValueError("must be one of enum values ('pure', 'view')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ReadAbiFunction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in outputs (list)
        _items = []
        if self.outputs:
            for _item_outputs in self.outputs:
                if _item_outputs:
                    _items.append(_item_outputs.to_dict())
            _dict['outputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in inputs (list)
        _items = []
        if self.inputs:
            for _item_inputs in self.inputs:
                if _item_inputs:
                    _items.append(_item_inputs.to_dict())
            _dict['inputs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReadAbiFunction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "stateMutability": obj.get("stateMutability"),
            "outputs": [Parameter.from_dict(_item) for _item in obj["outputs"]] if obj.get("outputs") is not None else None,
            "name": obj.get("name"),
            "type": obj.get("type"),
            "inputs": [ParameterWithValue.from_dict(_item) for _item in obj["inputs"]] if obj.get("inputs") is not None else None,
            "description": obj.get("description")
        })
        return _obj


