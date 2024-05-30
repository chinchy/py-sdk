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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks.models.network_id_routing_policy_value import NetworkIdRoutingPolicyValue
from typing import Optional, Set
from typing_extensions import Self

class CreateNetworkIdRequest(BaseModel):
    """
    CreateNetworkIdRequest
    """ # noqa: E501
    name: StrictStr
    routing_policy: Optional[Dict[str, NetworkIdRoutingPolicyValue]] = Field(default=None, alias="routingPolicy")
    __properties: ClassVar[List[str]] = ["name", "routingPolicy"]

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
        """Create an instance of CreateNetworkIdRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each value in routing_policy (dict)
        _field_dict = {}
        if self.routing_policy:
            for _key in self.routing_policy:
                if self.routing_policy[_key]:
                    _field_dict[_key] = self.routing_policy[_key].to_dict()
            _dict['routingPolicy'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateNetworkIdRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "routingPolicy": dict(
                (_k, NetworkIdRoutingPolicyValue.from_dict(_v))
                for _k, _v in obj["routingPolicy"].items()
            )
            if obj.get("routingPolicy") is not None
            else None
        })
        return _obj


