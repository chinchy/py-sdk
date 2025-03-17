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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks.models.blockchain_explorer import BlockchainExplorer
from fireblocks.models.blockchain_media import BlockchainMedia
from typing import Optional, Set
from typing_extensions import Self

class BlockchainMetadata(BaseModel):
    """
    BlockchainMetadata
    """ # noqa: E501
    scope: StrictStr = Field(description="Is blockchain listed on all workspaces? Global or Local")
    deprecated: StrictBool = Field(description="Is blockchain deprecated")
    media: Optional[List[BlockchainMedia]] = Field(default=None, description="Blockchain’s media")
    explorer: Optional[BlockchainExplorer] = None
    __properties: ClassVar[List[str]] = ["scope", "deprecated", "media", "explorer"]

    @field_validator('scope')
    def scope_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Global', 'Local']):
            raise ValueError("must be one of enum values ('Global', 'Local')")
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
        """Create an instance of BlockchainMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in media (list)
        _items = []
        if self.media:
            for _item_media in self.media:
                if _item_media:
                    _items.append(_item_media.to_dict())
            _dict['media'] = _items
        # override the default output from pydantic by calling `to_dict()` of explorer
        if self.explorer:
            _dict['explorer'] = self.explorer.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BlockchainMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "scope": obj.get("scope"),
            "deprecated": obj.get("deprecated"),
            "media": [BlockchainMedia.from_dict(_item) for _item in obj["media"]] if obj.get("media") is not None else None,
            "explorer": BlockchainExplorer.from_dict(obj["explorer"]) if obj.get("explorer") is not None else None
        })
        return _obj


