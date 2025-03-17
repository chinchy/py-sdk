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

from fireblocks.models.create_transfer_config_operation_request import (
    CreateTransferConfigOperationRequest,
)


class TestCreateTransferConfigOperationRequest(unittest.TestCase):
    """CreateTransferConfigOperationRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateTransferConfigOperationRequest:
        """Test CreateTransferConfigOperationRequest
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateTransferConfigOperationRequest`
        """
        model = CreateTransferConfigOperationRequest()
        if include_optional:
            return CreateTransferConfigOperationRequest(
                type = 'TRANSFER',
                params = fireblocks.models.transfer_operation_config_params.TransferOperationConfigParams(
                    amount = '', 
                    asset_id = '', 
                    source = fireblocks.models.account.Account(
                        account_id = '', 
                        account_type = 'EXCHANGE_ACCOUNT', ), 
                    destination = null, )
            )
        else:
            return CreateTransferConfigOperationRequest(
                type = 'TRANSFER',
                params = fireblocks.models.transfer_operation_config_params.TransferOperationConfigParams(
                    amount = '', 
                    asset_id = '', 
                    source = fireblocks.models.account.Account(
                        account_id = '', 
                        account_type = 'EXCHANGE_ACCOUNT', ), 
                    destination = null, ),
        )
        """

    def testCreateTransferConfigOperationRequest(self):
        """Test CreateTransferConfigOperationRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
