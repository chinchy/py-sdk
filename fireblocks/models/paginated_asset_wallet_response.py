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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks.models.asset_wallet import AssetWallet
from fireblocks.models.paginated_asset_wallet_response_paging import PaginatedAssetWalletResponsePaging
from typing import Optional, Set
from typing_extensions import Self

class PaginatedAssetWalletResponse(BaseModel):
    """
    PaginatedAssetWalletResponse
    """ # noqa: E501
    asset_wallets: Optional[List[AssetWallet]] = Field(default=None, alias="assetWallets")
    paging: Optional[PaginatedAssetWalletResponsePaging] = None
    __properties: ClassVar[List[str]] = ["assetWallets", "paging"]

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
        """Create an instance of PaginatedAssetWalletResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in asset_wallets (list)
        _items = []
        if self.asset_wallets:
            for _item_asset_wallets in self.asset_wallets:
                if _item_asset_wallets:
                    _items.append(_item_asset_wallets.to_dict())
            _dict['assetWallets'] = _items
        # override the default output from pydantic by calling `to_dict()` of paging
        if self.paging:
            _dict['paging'] = self.paging.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaginatedAssetWalletResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assetWallets": [AssetWallet.from_dict(_item) for _item in obj["assetWallets"]] if obj.get("assetWallets") is not None else None,
            "paging": PaginatedAssetWalletResponsePaging.from_dict(obj["paging"]) if obj.get("paging") is not None else None
        })
        return _obj


