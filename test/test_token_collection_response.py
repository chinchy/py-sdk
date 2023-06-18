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
import datetime

import fireblocks_client
from fireblocks_client.models.token_collection_response import TokenCollectionResponse  # noqa: E501
from fireblocks_client.rest import ApiException

class TestTokenCollectionResponse(unittest.TestCase):
    """TokenCollectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TokenCollectionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TokenCollectionResponse`
        """
        model = fireblocks_client.models.token_collection_response.TokenCollectionResponse()  # noqa: E501
        if include_optional :
            return TokenCollectionResponse(
                id = '', 
                name = '', 
                symbol = ''
            )
        else :
            return TokenCollectionResponse(
                id = '',
                name = '',
                symbol = '',
        )
        """

    def testTokenCollectionResponse(self):
        """Test TokenCollectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
