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

from fireblocks.models.get_signing_key_response_dto import GetSigningKeyResponseDto


class TestGetSigningKeyResponseDto(unittest.TestCase):
    """GetSigningKeyResponseDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSigningKeyResponseDto:
        """Test GetSigningKeyResponseDto
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetSigningKeyResponseDto`
        """
        model = GetSigningKeyResponseDto()
        if include_optional:
            return GetSigningKeyResponseDto(
                data = [
                    fireblocks.models.signing_key_dto.SigningKeyDto(
                        key_id = '46a92767-5f93-4a46-9eed-f012196bb4fc', 
                        signing_device_key_id = 'MyKey1', 
                        public_key_pem = '-----BEGIN PUBLIC KEY ... END PUBLIC KEY-----', 
                        algorithm = 'ECDSA_SECP256K1', 
                        enabled = True, 
                        vault_account_id = 10, 
                        agent_user_id = 'd18847b5-1df6-4c46-8f99-5cce47284529', 
                        created_at = 124757537, )
                    ],
                next = ''
            )
        else:
            return GetSigningKeyResponseDto(
                data = [
                    fireblocks.models.signing_key_dto.SigningKeyDto(
                        key_id = '46a92767-5f93-4a46-9eed-f012196bb4fc', 
                        signing_device_key_id = 'MyKey1', 
                        public_key_pem = '-----BEGIN PUBLIC KEY ... END PUBLIC KEY-----', 
                        algorithm = 'ECDSA_SECP256K1', 
                        enabled = True, 
                        vault_account_id = 10, 
                        agent_user_id = 'd18847b5-1df6-4c46-8f99-5cce47284529', 
                        created_at = 124757537, )
                    ],
        )
        """

    def testGetSigningKeyResponseDto(self):
        """Test GetSigningKeyResponseDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
