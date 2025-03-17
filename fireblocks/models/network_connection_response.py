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
from fireblocks.models.network_channel import NetworkChannel
from fireblocks.models.network_connection_routing_policy_value import NetworkConnectionRoutingPolicyValue
from fireblocks.models.network_connection_status import NetworkConnectionStatus
from fireblocks.models.network_id import NetworkId
from typing import Optional, Set
from typing_extensions import Self

class NetworkConnectionResponse(BaseModel):
    """
    NetworkConnectionResponse
    """ # noqa: E501
    id: StrictStr
    local_channel: Optional[NetworkChannel] = Field(default=None, description="Deprecated - Replaced by `localNetworkId`", alias="localChannel")
    remote_channel: Optional[NetworkChannel] = Field(default=None, description="Deprecated - Replaced by `remoteNetworkId`", alias="remoteChannel")
    status: NetworkConnectionStatus
    local_network_id: NetworkId = Field(alias="localNetworkId")
    remote_network_id: NetworkId = Field(alias="remoteNetworkId")
    routing_policy: Dict[str, NetworkConnectionRoutingPolicyValue] = Field(alias="routingPolicy")
    __properties: ClassVar[List[str]] = ["id", "localChannel", "remoteChannel", "status", "localNetworkId", "remoteNetworkId", "routingPolicy"]

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
        """Create an instance of NetworkConnectionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of local_channel
        if self.local_channel:
            _dict['localChannel'] = self.local_channel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remote_channel
        if self.remote_channel:
            _dict['remoteChannel'] = self.remote_channel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of local_network_id
        if self.local_network_id:
            _dict['localNetworkId'] = self.local_network_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of remote_network_id
        if self.remote_network_id:
            _dict['remoteNetworkId'] = self.remote_network_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in routing_policy (dict)
        _field_dict = {}
        if self.routing_policy:
            for _key_routing_policy in self.routing_policy:
                if self.routing_policy[_key_routing_policy]:
                    _field_dict[_key_routing_policy] = self.routing_policy[_key_routing_policy].to_dict()
            _dict['routingPolicy'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NetworkConnectionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "localChannel": NetworkChannel.from_dict(obj["localChannel"]) if obj.get("localChannel") is not None else None,
            "remoteChannel": NetworkChannel.from_dict(obj["remoteChannel"]) if obj.get("remoteChannel") is not None else None,
            "status": obj.get("status"),
            "localNetworkId": NetworkId.from_dict(obj["localNetworkId"]) if obj.get("localNetworkId") is not None else None,
            "remoteNetworkId": NetworkId.from_dict(obj["remoteNetworkId"]) if obj.get("remoteNetworkId") is not None else None,
            "routingPolicy": dict(
                (_k, NetworkConnectionRoutingPolicyValue.from_dict(_v))
                for _k, _v in obj["routingPolicy"].items()
            )
            if obj.get("routingPolicy") is not None
            else None
        })
        return _obj


