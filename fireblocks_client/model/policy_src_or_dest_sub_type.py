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


class PolicySrcOrDestSubType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    * EXTERNAL - A whitelisted wallet assigned as external is typically used for addresses managed by your clients and counterparties
* INTERNAL - A whitelisted wallet assigned as internal, is typically used for addresses that you control outside of your Fireblocks workspace
* CONTRACT - A whitelisted wallet assigned as contract is for identifying and managing external smart contracts
* EXCHANGETEST - Exchanges which operate only on testnet assets
* "*" - All subtypes

    """


    class MetaOapg:
        enum_value_to_name = {
            "EXTERNAL": "EXTERNAL",
            "INTERNAL": "INTERNAL",
            "CONTRACT": "CONTRACT",
            "EXCHANGETEST": "EXCHANGETEST",
            "*": "ASTERISK",
        }
    
    @schemas.classproperty
    def EXTERNAL(cls):
        return cls("EXTERNAL")
    
    @schemas.classproperty
    def INTERNAL(cls):
        return cls("INTERNAL")
    
    @schemas.classproperty
    def CONTRACT(cls):
        return cls("CONTRACT")
    
    @schemas.classproperty
    def EXCHANGETEST(cls):
        return cls("EXCHANGETEST")
    
    @schemas.classproperty
    def ASTERISK(cls):
        return cls("*")
