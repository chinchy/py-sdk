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

from fireblocks.models.create_signing_key_dto_proof_of_ownership import (
    CreateSigningKeyDtoProofOfOwnership,
)


class TestCreateSigningKeyDtoProofOfOwnership(unittest.TestCase):
    """CreateSigningKeyDtoProofOfOwnership unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateSigningKeyDtoProofOfOwnership:
        """Test CreateSigningKeyDtoProofOfOwnership
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CreateSigningKeyDtoProofOfOwnership`
        """
        model = CreateSigningKeyDtoProofOfOwnership()
        if include_optional:
            return CreateSigningKeyDtoProofOfOwnership(
                message = '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263',
                signature = '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263'
            )
        else:
            return CreateSigningKeyDtoProofOfOwnership(
                message = '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263',
                signature = '0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263',
        )
        """

    def testCreateSigningKeyDtoProofOfOwnership(self):
        """Test CreateSigningKeyDtoProofOfOwnership"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
