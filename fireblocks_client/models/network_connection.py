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
from fireblocks_client.models.network_connection_routing_policy import NetworkConnectionRoutingPolicy

class NetworkConnection(BaseModel):
    """
    NetworkConnection
    """
    local_network_id: StrictStr = Field(..., alias="localNetworkId", description="The network ID of the profile trying to create the connection.")
    remote_network_id: StrictStr = Field(..., alias="remoteNetworkId", description="The network ID the profile is attempting to connect to.")
    routing_policy: Optional[NetworkConnectionRoutingPolicy] = Field(None, alias="routingPolicy")
    __properties = ["localNetworkId", "remoteNetworkId", "routingPolicy"]

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
    def from_json(cls, json_str: str) -> NetworkConnection:
        """Create an instance of NetworkConnection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of routing_policy
        if self.routing_policy:
            _dict['routingPolicy'] = self.routing_policy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NetworkConnection:
        """Create an instance of NetworkConnection from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return NetworkConnection.parse_obj(obj)

        _obj = NetworkConnection.parse_obj({
            "local_network_id": obj.get("localNetworkId"),
            "remote_network_id": obj.get("remoteNetworkId"),
            "routing_policy": NetworkConnectionRoutingPolicy.from_dict(obj.get("routingPolicy")) if obj.get("routingPolicy") is not None else None
        })
        return _obj

