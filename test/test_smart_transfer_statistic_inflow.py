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

from fireblocks.models.smart_transfer_statistic_inflow import (
    SmartTransferStatisticInflow,
)


class TestSmartTransferStatisticInflow(unittest.TestCase):
    """SmartTransferStatisticInflow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SmartTransferStatisticInflow:
        """Test SmartTransferStatisticInflow
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SmartTransferStatisticInflow`
        """
        model = SmartTransferStatisticInflow()
        if include_optional:
            return SmartTransferStatisticInflow(
                coins = [
                    fireblocks.models.smart_transfer_coin_statistic.SmartTransferCoinStatistic(
                        asset = 'BTC', 
                        amount = '15', )
                    ],
                ticket_count = 4
            )
        else:
            return SmartTransferStatisticInflow(
        )
        """

    def testSmartTransferStatisticInflow(self):
        """Test SmartTransferStatisticInflow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
