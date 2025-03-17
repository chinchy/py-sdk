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

from fireblocks.models.asset_metadata_dto import AssetMetadataDto


class TestAssetMetadataDto(unittest.TestCase):
    """AssetMetadataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssetMetadataDto:
        """Test AssetMetadataDto
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AssetMetadataDto`
        """
        model = AssetMetadataDto()
        if include_optional:
            return AssetMetadataDto(
                asset_id = 'BQ5R_MY_TOKEN',
                name = 'MyToken',
                symbol = 'MYT',
                network_protocol = 'ETH',
                total_supply = '1000000000000000',
                holders_count = 6,
                type = 'ERC20',
                contract_address = '0x1234567890abcdef1234567890abcdef12345678',
                issuer_address = 'rGyXjc5d7s17vvt3NtKKascvJrnSxV21kQ',
                testnet = True,
                blockchain = 'ETH_TEST5',
                decimals = 18,
                vault_account_id = '0'
            )
        else:
            return AssetMetadataDto(
                asset_id = 'BQ5R_MY_TOKEN',
        )
        """

    def testAssetMetadataDto(self):
        """Test AssetMetadataDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
