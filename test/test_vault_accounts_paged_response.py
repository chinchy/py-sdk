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

"""
import fireblocks_client
from fireblocks_client.models.vault_accounts_paged_response import VaultAccountsPagedResponse  # noqa: E501
from fireblocks_client.rest import ApiException
"""
class TestVaultAccountsPagedResponse(unittest.TestCase):
    """VaultAccountsPagedResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """
        Test VaultAccountsPagedResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
        # uncomment below to create an instance of `VaultAccountsPagedResponse`
        """
        model = fireblocks_client.models.vault_accounts_paged_response.VaultAccountsPagedResponse()  # noqa: E501
        if include_optional :
        return VaultAccountsPagedResponse(
            accounts = [
                    fireblocks_client.models.vault_account.VaultAccount(
                        id = '', 
                        name = '', 
                        assets = [
                            fireblocks_client.models.vault_asset.VaultAsset(
                                id = '', 
                                total = '', 
                                balance = '', 
                                available = '', 
                                pending = '', 
                                frozen = '', 
                                locked_amount = '', 
                                staked = '', 
                                total_staked_cpu = 1.337, 
                                total_staked_network = '', 
                                self_staked_cpu = '', 
                                self_staked_network = '', 
                                pending_refund_cpu = '', 
                                pending_refund_network = '', 
                                block_height = '', 
                                block_hash = '', 
                                rewards_info = fireblocks_client.models.rewards_info.RewardsInfo(
                                    pending_rewards = '', ), )
                            ], 
                        hidden_on_ui = True, 
                        customer_ref_id = '', 
                        auto_fuel = True, )
                    ], 
            paging = fireblocks_client.models.vault_accounts_paged_response_paging.VaultAccountsPagedResponse_paging(
                    before = '', 
                    after = '', ), 
            previous_url = '', 
            next_url = ''
        )
        else :
        return VaultAccountsPagedResponse(
        )
        """

    def testVaultAccountsPagedResponse(self):
        """Test VaultAccountsPagedResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()