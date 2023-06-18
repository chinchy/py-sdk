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

import fireblocks_client
from fireblocks_client.api.network_connections_api import NetworkConnectionsApi  # noqa: E501
from fireblocks_client.rest import ApiException


class TestNetworkConnectionsApi(unittest.TestCase):
    """NetworkConnectionsApi unit test stubs"""

    def setUp(self):
        self.api = fireblocks_client.api.network_connections_api.NetworkConnectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_check_third_party_routing_for_network_connection(self):
        """Test case for check_third_party_routing_for_network_connection

        Retrieve third-party network routing validation by asset type.  # noqa: E501
        """
        pass

    def test_create_network_connection(self):
        """Test case for create_network_connection

        Creates a new network connection  # noqa: E501
        """
        pass

    def test_create_network_id(self):
        """Test case for create_network_id

        Creates a new Network ID  # noqa: E501
        """
        pass

    def test_delete_network_connection(self):
        """Test case for delete_network_connection

        Deletes a network connection by ID  # noqa: E501
        """
        pass

    def test_delete_network_id(self):
        """Test case for delete_network_id

        Deletes specific network ID.  # noqa: E501
        """
        pass

    def test_get_network_connection_by_id(self):
        """Test case for get_network_connection_by_id

        Get a network connection  # noqa: E501
        """
        pass

    def test_get_network_connections(self):
        """Test case for get_network_connections

        List network connections  # noqa: E501
        """
        pass

    def test_get_network_id_by_id(self):
        """Test case for get_network_id_by_id

        Returns specific network ID.  # noqa: E501
        """
        pass

    def test_get_network_ids(self):
        """Test case for get_network_ids

        Returns all network IDs, both local IDs and discoverable remote IDs  # noqa: E501
        """
        pass

    def test_set_discoverability_for_network_id(self):
        """Test case for set_discoverability_for_network_id

        Update network ID's discoverability.  # noqa: E501
        """
        pass

    def test_set_network_id_name(self):
        """Test case for set_network_id_name

        Update network ID's name.  # noqa: E501
        """
        pass

    def test_set_routing_policy_for_network_connection(self):
        """Test case for set_routing_policy_for_network_connection

        Update network connection routing policy.  # noqa: E501
        """
        pass

    def test_set_routing_policy_for_network_id(self):
        """Test case for set_routing_policy_for_network_id

        Update network id routing policy.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
