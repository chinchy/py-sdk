# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fireblocks.api.exchange_accounts_api import ExchangeAccountsApi


class TestExchangeAccountsApi(unittest.TestCase):
    """ExchangeAccountsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExchangeAccountsApi()

    def tearDown(self) -> None:
        pass

    def test_add_exchange_account(self) -> None:
        """Test case for add_exchange_account

        Add an exchange account
        """
        pass

    def test_convert_assets(self) -> None:
        """Test case for convert_assets

        Convert exchange account funds from the source asset to the destination asset.
        """
        pass

    def test_get_exchange_account(self) -> None:
        """Test case for get_exchange_account

        Find a specific exchange account
        """
        pass

    def test_get_exchange_account_asset(self) -> None:
        """Test case for get_exchange_account_asset

        Find an asset for an exchange account
        """
        pass

    def test_get_exchange_accounts_credentials_public_key(self) -> None:
        """Test case for get_exchange_accounts_credentials_public_key

        Get public key to encrypt exchange credentials
        """
        pass

    def test_get_paged_exchange_accounts(self) -> None:
        """Test case for get_paged_exchange_accounts

        Pagination list exchange accounts
        """
        pass

    def test_internal_transfer(self) -> None:
        """Test case for internal_transfer

        Internal transfer for exchange accounts
        """
        pass


if __name__ == "__main__":
    unittest.main()
