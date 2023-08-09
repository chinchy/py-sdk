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
from fireblocks_client.models.destination_transfer_peer_path_all_of import DestinationTransferPeerPathAllOf  # noqa: E501
from fireblocks_client.rest import ApiException
"""
class TestDestinationTransferPeerPathAllOf(unittest.TestCase):
    """DestinationTransferPeerPathAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """
        Test DestinationTransferPeerPathAllOf
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
        # uncomment below to create an instance of `DestinationTransferPeerPathAllOf`
        """
        model = fireblocks_client.models.destination_transfer_peer_path_all_of.DestinationTransferPeerPathAllOf()  # noqa: E501
        if include_optional :
        return DestinationTransferPeerPathAllOf(
            one_time_address = fireblocks_client.models.one_time_address.OneTimeAddress(
                    address = '', 
                    tag = '', )
        )
        else :
        return DestinationTransferPeerPathAllOf(
        )
        """

    def testDestinationTransferPeerPathAllOf(self):
        """Test DestinationTransferPeerPathAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()