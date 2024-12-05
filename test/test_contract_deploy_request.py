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

from fireblocks.models.contract_deploy_request import ContractDeployRequest


class TestContractDeployRequest(unittest.TestCase):
    """ContractDeployRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContractDeployRequest:
        """Test ContractDeployRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ContractDeployRequest`
        """
        model = ContractDeployRequest()
        if include_optional:
            return ContractDeployRequest(
                asset_id = 'ETH_TEST5',
                vault_account_id = '0',
                constructor_parameters = [{"internalType":"string","name":"name_","type":"string","value":"TokenName"},{"internalType":"string","name":"symbol_","type":"string","value":"TokenSymbol"}],
                use_gasless = False,
                fee = '2000',
                fee_level = 'MEDIUM'
            )
        else:
            return ContractDeployRequest(
                asset_id = 'ETH_TEST5',
                vault_account_id = '0',
        )
        """

    def testContractDeployRequest(self):
        """Test ContractDeployRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
