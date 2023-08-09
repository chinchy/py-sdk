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
from fireblocks_client.models.set_discoverability_for_network_id_request import SetDiscoverabilityForNetworkIdRequest  # noqa: E501
from fireblocks_client.rest import ApiException
"""
class TestSetDiscoverabilityForNetworkIdRequest(unittest.TestCase):
    """SetDiscoverabilityForNetworkIdRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """
        Test SetDiscoverabilityForNetworkIdRequest
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
        # uncomment below to create an instance of `SetDiscoverabilityForNetworkIdRequest`
        """
        model = fireblocks_client.models.set_discoverability_for_network_id_request.SetDiscoverabilityForNetworkIdRequest()  # noqa: E501
        if include_optional :
        return SetDiscoverabilityForNetworkIdRequest(
            is_discoverable = True
        )
        else :
        return SetDiscoverabilityForNetworkIdRequest(
                is_discoverable = True,
        )
        """

    def testSetDiscoverabilityForNetworkIdRequest(self):
        """Test SetDiscoverabilityForNetworkIdRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()