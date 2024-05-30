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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from fireblocks.models.asset_metadata_dto import AssetMetadataDto
from fireblocks.models.collection_metadata_dto import CollectionMetadataDto
from fireblocks.models.contract_metadata_dto import ContractMetadataDto
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

TOKENLINKDTOTOKENMETADATA_ONE_OF_SCHEMAS = ["AssetMetadataDto", "CollectionMetadataDto", "ContractMetadataDto"]

class TokenLinkDtoTokenMetadata(BaseModel):
    """
    The token's metadata
    """
    # data type: AssetMetadataDto
    oneof_schema_1_validator: Optional[AssetMetadataDto] = None
    # data type: CollectionMetadataDto
    oneof_schema_2_validator: Optional[CollectionMetadataDto] = None
    # data type: ContractMetadataDto
    oneof_schema_3_validator: Optional[ContractMetadataDto] = None
    actual_instance: Optional[Union[AssetMetadataDto, CollectionMetadataDto, ContractMetadataDto]] = None
    one_of_schemas: Set[str] = { "AssetMetadataDto", "CollectionMetadataDto", "ContractMetadataDto" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = TokenLinkDtoTokenMetadata.model_construct()
        error_messages = []
        match = 0
        # validate data type: AssetMetadataDto
        if not isinstance(v, AssetMetadataDto):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AssetMetadataDto`")
        else:
            match += 1
        # validate data type: CollectionMetadataDto
        if not isinstance(v, CollectionMetadataDto):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CollectionMetadataDto`")
        else:
            match += 1
        # validate data type: ContractMetadataDto
        if not isinstance(v, ContractMetadataDto):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ContractMetadataDto`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TokenLinkDtoTokenMetadata with oneOf schemas: AssetMetadataDto, CollectionMetadataDto, ContractMetadataDto. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TokenLinkDtoTokenMetadata with oneOf schemas: AssetMetadataDto, CollectionMetadataDto, ContractMetadataDto. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AssetMetadataDto
        try:
            instance.actual_instance = AssetMetadataDto.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CollectionMetadataDto
        try:
            instance.actual_instance = CollectionMetadataDto.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ContractMetadataDto
        try:
            instance.actual_instance = ContractMetadataDto.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TokenLinkDtoTokenMetadata with oneOf schemas: AssetMetadataDto, CollectionMetadataDto, ContractMetadataDto. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TokenLinkDtoTokenMetadata with oneOf schemas: AssetMetadataDto, CollectionMetadataDto, ContractMetadataDto. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AssetMetadataDto, CollectionMetadataDto, ContractMetadataDto]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


