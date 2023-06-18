# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import fireblocks_client
from fireblocks_client.api.fiat_accounts_api import FiatAccountsApi  # noqa: E501
from fireblocks_client.rest import ApiException


class TestFiatAccountsApi(unittest.TestCase):
    """FiatAccountsApi unit test stubs"""

    def setUp(self):
        self.api = fireblocks_client.api.fiat_accounts_api.FiatAccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deposit_funds_from_linked_dda(self):
        """Test case for deposit_funds_from_linked_dda

        Deposit funds from DDA  # noqa: E501
        """
        pass

    def test_get_fiat_account_by_id(self):
        """Test case for get_fiat_account_by_id

        Find a specific fiat account  # noqa: E501
        """
        pass

    def test_get_fiat_accounts(self):
        """Test case for get_fiat_accounts

        List fiat accounts  # noqa: E501
        """
        pass

    def test_redeem_funds_to_linked_dda(self):
        """Test case for redeem_funds_to_linked_dda

        Redeem funds to DDA  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
