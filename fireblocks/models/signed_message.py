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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from fireblocks.models.signed_message_signature import SignedMessageSignature
from typing import Optional, Set
from typing_extensions import Self

class SignedMessage(BaseModel):
    """
    A list of signed messages returned for raw signing.
    """ # noqa: E501
    content: Optional[StrictStr] = None
    algorithm: Optional[StrictStr] = None
    derivation_path: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="derivationPath")
    signature: Optional[SignedMessageSignature] = None
    public_key: Optional[StrictStr] = Field(default=None, alias="publicKey")
    __properties: ClassVar[List[str]] = ["content", "algorithm", "derivationPath", "signature", "publicKey"]

    @field_validator('algorithm')
    def algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['MPC_ECDSA_SECP256K1', 'MPC_EDDSA_ED25519']):
            raise ValueError("must be one of enum values ('MPC_ECDSA_SECP256K1', 'MPC_EDDSA_ED25519')")
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
        """Create an instance of SignedMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of signature
        if self.signature:
            _dict['signature'] = self.signature.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SignedMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content": obj.get("content"),
            "algorithm": obj.get("algorithm"),
            "derivationPath": obj.get("derivationPath"),
            "signature": SignedMessageSignature.from_dict(obj["signature"]) if obj.get("signature") is not None else None,
            "publicKey": obj.get("publicKey")
        })
        return _obj


