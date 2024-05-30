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

from fireblocks.models.transaction_fee import TransactionFee


class TestTransactionFee(unittest.TestCase):
    """TransactionFee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransactionFee:
        """Test TransactionFee
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransactionFee`
        """
        model = TransactionFee()
        if include_optional:
            return TransactionFee(
                fee_per_byte = '',
                gas_price = 1.337,
                gas_limit = '',
                network_fee = '',
                base_fee = 1.337,
                priority_fee = 1.337,
                max_fee_per_gas_delta = '',
                l1_fee = ''
            )
        else:
            return TransactionFee(
        )
        """

    def testTransactionFee(self):
        """Test TransactionFee"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
