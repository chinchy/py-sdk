# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fireblocks_client import schemas  # noqa: F401


class AssetTypeResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "name",
            "id",
            "type",
        }
        
        class properties:
            id = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ALGO_ASSET(cls):
                    return cls("ALGO_ASSET")
                
                @schemas.classproperty
                def BASE_ASSET(cls):
                    return cls("BASE_ASSET")
                
                @schemas.classproperty
                def BEP20(cls):
                    return cls("BEP20")
                
                @schemas.classproperty
                def COMPOUND(cls):
                    return cls("COMPOUND")
                
                @schemas.classproperty
                def ERC20(cls):
                    return cls("ERC20")
                
                @schemas.classproperty
                def FIAT(cls):
                    return cls("FIAT")
                
                @schemas.classproperty
                def SOL_ASSET(cls):
                    return cls("SOL_ASSET")
                
                @schemas.classproperty
                def TRON_TRC20(cls):
                    return cls("TRON_TRC20")
                
                @schemas.classproperty
                def XLM_ASSET(cls):
                    return cls("XLM_ASSET")
                
                @schemas.classproperty
                def XDB_ASSET(cls):
                    return cls("XDB_ASSET")
            contractAddress = schemas.StrSchema
            nativeAsset = schemas.StrSchema
            decimals = schemas.NumberSchema
            __annotations__ = {
                "id": id,
                "name": name,
                "type": type,
                "contractAddress": contractAddress,
                "nativeAsset": nativeAsset,
                "decimals": decimals,
            }
    
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractAddress"]) -> MetaOapg.properties.contractAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nativeAsset"]) -> MetaOapg.properties.nativeAsset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["decimals"]) -> MetaOapg.properties.decimals: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "type", "contractAddress", "nativeAsset", "decimals", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractAddress"]) -> typing.Union[MetaOapg.properties.contractAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nativeAsset"]) -> typing.Union[MetaOapg.properties.nativeAsset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["decimals"]) -> typing.Union[MetaOapg.properties.decimals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "type", "contractAddress", "nativeAsset", "decimals", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        contractAddress: typing.Union[MetaOapg.properties.contractAddress, str, schemas.Unset] = schemas.unset,
        nativeAsset: typing.Union[MetaOapg.properties.nativeAsset, str, schemas.Unset] = schemas.unset,
        decimals: typing.Union[MetaOapg.properties.decimals, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AssetTypeResponse':
        return super().__new__(
            cls,
            *_args,
            name=name,
            id=id,
            type=type,
            contractAddress=contractAddress,
            nativeAsset=nativeAsset,
            decimals=decimals,
            _configuration=_configuration,
            **kwargs,
        )
