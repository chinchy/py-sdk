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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fireblocks.models.related_request import RelatedRequest
from fireblocks.models.related_transaction import RelatedTransaction
from fireblocks.models.solana_blockchain_data import SolanaBlockchainData
from fireblocks.models.staking_provider import StakingProvider
from typing import Optional, Set
from typing_extensions import Self

class Delegation(BaseModel):
    """
    Delegation
    """ # noqa: E501
    id: StrictStr = Field(description="The unique identifier of the staking position")
    vault_account_id: StrictStr = Field(description="The source vault account to stake from", alias="vaultAccountId")
    validator_name: StrictStr = Field(description="The destination validator address name", alias="validatorName")
    provider_name: StrictStr = Field(description="The destination validator provider name", alias="providerName")
    chain_descriptor: StrictStr = Field(description="The protocol identifier (e.g. \"ETH\"/ \"SOL\") to use", alias="chainDescriptor")
    amount: StrictStr = Field(description="Amount of tokens to stake, measured in the staked asset unit.")
    rewards_amount: StrictStr = Field(description="The amount staked in the position, measured in the staked asset unit.", alias="rewardsAmount")
    date_created: datetime = Field(description="When was the request made (ISO Date).", alias="dateCreated")
    date_updated: datetime = Field(description="When has the position last changed (ISO Date).", alias="dateUpdated")
    status: StrictStr = Field(description="The current status.")
    related_transactions: List[RelatedTransaction] = Field(description="An array of transaction objects related to this position. Each object includes a 'txId' representing the transaction ID and a 'completed' boolean indicating if the transaction was completed.", alias="relatedTransactions")
    validator_address: StrictStr = Field(description="The destination address of the staking transaction.", alias="validatorAddress")
    provider_id: StakingProvider = Field(alias="providerId")
    available_actions: List[StrictStr] = Field(description="An array of available actions that can be performed. for example, actions like \"unstake\" or \"withdraw\".", alias="availableActions")
    in_progress: StrictBool = Field(description="Indicates whether there is an ongoing action for this position (true if ongoing, false if not).", alias="inProgress")
    in_progress_tx_id: Optional[StrictStr] = Field(default=None, description="The transaction ID of the ongoing request", alias="inProgressTxId")
    blockchain_position_info: SolanaBlockchainData = Field(alias="blockchainPositionInfo")
    related_requests: Optional[List[RelatedRequest]] = Field(default=None, description="An array of partial unstake requests for this position, relevant only for the Lido provider. Each object includes the status of the unstake request, a boolean indicating whether the action is in progress, the amount of tokens to unstake, and the transaction ID of the request. With Lido, a position may have multiple partial unstake requests in different states. This field is optional and not applicable for other providers.", alias="relatedRequests")
    __properties: ClassVar[List[str]] = ["id", "vaultAccountId", "validatorName", "providerName", "chainDescriptor", "amount", "rewardsAmount", "dateCreated", "dateUpdated", "status", "relatedTransactions", "validatorAddress", "providerId", "availableActions", "inProgress", "inProgressTxId", "blockchainPositionInfo", "relatedRequests"]

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
        """Create an instance of Delegation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in related_transactions (list)
        _items = []
        if self.related_transactions:
            for _item_related_transactions in self.related_transactions:
                if _item_related_transactions:
                    _items.append(_item_related_transactions.to_dict())
            _dict['relatedTransactions'] = _items
        # override the default output from pydantic by calling `to_dict()` of blockchain_position_info
        if self.blockchain_position_info:
            _dict['blockchainPositionInfo'] = self.blockchain_position_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in related_requests (list)
        _items = []
        if self.related_requests:
            for _item_related_requests in self.related_requests:
                if _item_related_requests:
                    _items.append(_item_related_requests.to_dict())
            _dict['relatedRequests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Delegation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "vaultAccountId": obj.get("vaultAccountId"),
            "validatorName": obj.get("validatorName"),
            "providerName": obj.get("providerName"),
            "chainDescriptor": obj.get("chainDescriptor"),
            "amount": obj.get("amount"),
            "rewardsAmount": obj.get("rewardsAmount"),
            "dateCreated": obj.get("dateCreated"),
            "dateUpdated": obj.get("dateUpdated"),
            "status": obj.get("status"),
            "relatedTransactions": [RelatedTransaction.from_dict(_item) for _item in obj["relatedTransactions"]] if obj.get("relatedTransactions") is not None else None,
            "validatorAddress": obj.get("validatorAddress"),
            "providerId": obj.get("providerId"),
            "availableActions": obj.get("availableActions"),
            "inProgress": obj.get("inProgress"),
            "inProgressTxId": obj.get("inProgressTxId"),
            "blockchainPositionInfo": SolanaBlockchainData.from_dict(obj["blockchainPositionInfo"]) if obj.get("blockchainPositionInfo") is not None else None,
            "relatedRequests": [RelatedRequest.from_dict(_item) for _item in obj["relatedRequests"]] if obj.get("relatedRequests") is not None else None
        })
        return _obj


