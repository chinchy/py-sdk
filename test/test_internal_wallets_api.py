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
from fireblocks_client.api.internal_wallets_api import InternalWalletsApi  # noqa: E501
from fireblocks_client.rest import ApiException


class TestInternalWalletsApi(unittest.TestCase):
    """InternalWalletsApi unit test stubs"""

    def setUp(self):
        self.api = fireblocks_client.api.internal_wallets_api.InternalWalletsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_internal_wallet(self):
        """Test case for create_internal_wallet

        Create an internal wallet  # noqa: E501
        """
        pass

    def test_create_internal_wallet_asset(self):
        """Test case for create_internal_wallet_asset

        Add an asset to an internal wallet  # noqa: E501
        """
        pass

    def test_delete_internal_wallet(self):
        """Test case for delete_internal_wallet

        Delete an internal wallet  # noqa: E501
        """
        pass

    def test_delete_internal_wallet_asset(self):
        """Test case for delete_internal_wallet_asset

        Delete a whitelisted address from an internal wallet  # noqa: E501
        """
        pass

    def test_get_internal_wallet_asset(self):
        """Test case for get_internal_wallet_asset

        Get an asset from an internal wallet  # noqa: E501
        """
        pass

    def test_get_internal_wallet_by_id(self):
        """Test case for get_internal_wallet_by_id

        Get assets for internal wallet  # noqa: E501
        """
        pass

    def test_get_internal_wallets(self):
        """Test case for get_internal_wallets

        List internal wallets  # noqa: E501
        """
        pass

    def test_set_customer_ref_id_for_internal_wallet(self):
        """Test case for set_customer_ref_id_for_internal_wallet

        Set an AML/KYT customer reference ID for an internal wallet  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
