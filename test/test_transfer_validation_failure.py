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

from fireblocks.models.transfer_validation_failure import TransferValidationFailure


class TestTransferValidationFailure(unittest.TestCase):
    """TransferValidationFailure unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TransferValidationFailure:
        """Test TransferValidationFailure
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TransferValidationFailure`
        """
        model = TransferValidationFailure()
        if include_optional:
            return TransferValidationFailure(
                reason = 'ACCOUNT_NOT_FOUND',
                data = { }
            )
        else:
            return TransferValidationFailure(
                reason = 'ACCOUNT_NOT_FOUND',
        )
        """

    def testTransferValidationFailure(self):
        """Test TransferValidationFailure"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
