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
from fireblocks_client.models.network_connection_response import NetworkConnectionResponse  # noqa: E501
from fireblocks_client.rest import ApiException
"""
class TestNetworkConnectionResponse(unittest.TestCase):
    """NetworkConnectionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """
        Test NetworkConnectionResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
        # uncomment below to create an instance of `NetworkConnectionResponse`
        """
        model = fireblocks_client.models.network_connection_response.NetworkConnectionResponse()  # noqa: E501
        if include_optional :
        return NetworkConnectionResponse(
            id = '', 
            local_channel = None, 
            remote_channel = None, 
            status = 'WAITING_FOR_APPROVAL', 
            local_network_id = fireblocks_client.models.network_id.NetworkId(
                    id = '', 
                    name = '', ), 
            remote_network_id = fireblocks_client.models.network_id.NetworkId(
                    id = '', 
                    name = '', ), 
            routing_policy = fireblocks_client.models.network_connection_routing_policy.NetworkConnectionRoutingPolicy(
                    crypto = null, 
                    sen = null, 
                    signet = null, 
                    sen_test = null, 
                    signet_test = null, )
        )
        else :
        return NetworkConnectionResponse(
                id = '',
                status = 'WAITING_FOR_APPROVAL',
                local_network_id = fireblocks_client.models.network_id.NetworkId(
                    id = '', 
                    name = '', ),
                remote_network_id = fireblocks_client.models.network_id.NetworkId(
                    id = '', 
                    name = '', ),
                routing_policy = fireblocks_client.models.network_connection_routing_policy.NetworkConnectionRoutingPolicy(
                    crypto = null, 
                    sen = null, 
                    signet = null, 
                    sen_test = null, 
                    signet_test = null, ),
        )
        """

    def testNetworkConnectionResponse(self):
        """Test NetworkConnectionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()