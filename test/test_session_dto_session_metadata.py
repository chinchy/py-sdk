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
from fireblocks_client.models.session_dto_session_metadata import SessionDTOSessionMetadata  # noqa: E501
from fireblocks_client.rest import ApiException
"""
class TestSessionDTOSessionMetadata(unittest.TestCase):
    """SessionDTOSessionMetadata unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """
        Test SessionDTOSessionMetadata
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
        # uncomment below to create an instance of `SessionDTOSessionMetadata`
        """
        model = fireblocks_client.models.session_dto_session_metadata.SessionDTOSessionMetadata()  # noqa: E501
        if include_optional :
        return SessionDTOSessionMetadata(
            app_url = '', 
            app_name = '', 
            app_description = '', 
            app_icon = ''
        )
        else :
        return SessionDTOSessionMetadata(
                app_url = '',
        )
        """

    def testSessionDTOSessionMetadata(self):
        """Test SessionDTOSessionMetadata"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()