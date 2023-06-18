# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PayoutInstructionState(str, Enum):
    """
    - NOT_STARTED - waiting to start - TRANSACTION_SENT - an underlying transaction was sent - COMPLETED - completed successfully - FAILED - failed - TRANSLATION_ERROR -lookup of the destination failed (due to changes in the underlying whitelisted external wallet or similar) - SKIPPED- no transaction(s) created for this instruction 
    """

    """
    allowed enum values
    """
    NOT_STARTED = 'NOT_STARTED'
    TRANSACTION_SENT = 'TRANSACTION_SENT'
    COMPLETED = 'COMPLETED'
    FAILED = 'FAILED'
    TRANSLATION_ERROR = 'TRANSLATION_ERROR'
    SKIPPED = 'SKIPPED'

