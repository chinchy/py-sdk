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
from fireblocks_client.models.get_connections_response import GetConnectionsResponse  # noqa: E501
from fireblocks_client.rest import ApiException
"""
class TestGetConnectionsResponse(unittest.TestCase):
    """GetConnectionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """
        Test GetConnectionsResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
        # uncomment below to create an instance of `GetConnectionsResponse`
        """
        model = fireblocks_client.models.get_connections_response.GetConnectionsResponse()  # noqa: E501
        if include_optional :
        return GetConnectionsResponse(
            data = [
                    fireblocks_client.models.session_dto.SessionDTO(
                        id = '4e9e7051-f3b2-48e9-8ee6-b12492552657', 
                        user_id = '', 
                        session_metadata = null, 
                        vault_account_id = 1, 
                        fee_level = 'MEDIUM', 
                        chain_ids = ["ETH","ETH_TEST","SOL"], 
                        connection_type = 'WalletConnect', 
                        connection_method = 'API', 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ], 
            paging = fireblocks_client.models.paging.Paging(
                    next = '', )
        )
        else :
        return GetConnectionsResponse(
                data = [
                    fireblocks_client.models.session_dto.SessionDTO(
                        id = '4e9e7051-f3b2-48e9-8ee6-b12492552657', 
                        user_id = '', 
                        session_metadata = null, 
                        vault_account_id = 1, 
                        fee_level = 'MEDIUM', 
                        chain_ids = ["ETH","ETH_TEST","SOL"], 
                        connection_type = 'WalletConnect', 
                        connection_method = 'API', 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
        )
        """

    def testGetConnectionsResponse(self):
        """Test GetConnectionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()