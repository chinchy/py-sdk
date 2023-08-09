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
from fireblocks_client.models.payout_instruction_response import PayoutInstructionResponse  # noqa: E501
from fireblocks_client.rest import ApiException
"""
class TestPayoutInstructionResponse(unittest.TestCase):
    """PayoutInstructionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """
        Test PayoutInstructionResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
        # uncomment below to create an instance of `PayoutInstructionResponse`
        """
        model = fireblocks_client.models.payout_instruction_response.PayoutInstructionResponse()  # noqa: E501
        if include_optional :
        return PayoutInstructionResponse(
            id = '', 
            payee_account = fireblocks_client.models.payee_account_response.PayeeAccountResponse(
                    id = '', 
                    type = 'VAULT_ACCOUNT', ), 
            amount = fireblocks_client.models.instruction_amount.InstructionAmount(
                    amount = '', 
                    asset_id = '', ), 
            state = 'NOT_STARTED', 
            transactions = [
                    fireblocks_client.models.transaction.Transaction(
                        id = '', 
                        state = 'SUBMITTED', 
                        timestamp = 1.337, 
                        instruction_id = '', )
                    ]
        )
        else :
        return PayoutInstructionResponse(
                payee_account = fireblocks_client.models.payee_account_response.PayeeAccountResponse(
                    id = '', 
                    type = 'VAULT_ACCOUNT', ),
                amount = fireblocks_client.models.instruction_amount.InstructionAmount(
                    amount = '', 
                    asset_id = '', ),
                state = 'NOT_STARTED',
                transactions = [
                    fireblocks_client.models.transaction.Transaction(
                        id = '', 
                        state = 'SUBMITTED', 
                        timestamp = 1.337, 
                        instruction_id = '', )
                    ],
        )
        """

    def testPayoutInstructionResponse(self):
        """Test PayoutInstructionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()