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

from fireblocks.api.off_exchanges_api import OffExchangesApi


class TestOffExchangesApi(unittest.TestCase):
    """OffExchangesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OffExchangesApi()

    def tearDown(self) -> None:
        pass

    def test_add_off_exchange(self) -> None:
        """Test case for add_off_exchange

        add collateral
        """
        pass

    def test_get_off_exchange_collateral_accounts(self) -> None:
        """Test case for get_off_exchange_collateral_accounts

        Find a specific collateral exchange account
        """
        pass

    def test_get_off_exchange_settlement_transactions(self) -> None:
        """Test case for get_off_exchange_settlement_transactions

        get settlements transactions from exchange
        """
        pass

    def test_remove_off_exchange(self) -> None:
        """Test case for remove_off_exchange

        remove collateral
        """
        pass

    def test_settle_off_exchange_trades(self) -> None:
        """Test case for settle_off_exchange_trades

        create settlement for a trader
        """
        pass


if __name__ == "__main__":
    unittest.main()
