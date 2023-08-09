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
from fireblocks_client.api.payments_cross_border_settlement_api import PaymentsCrossBorderSettlementApi  # noqa: E501
from fireblocks_client.rest import ApiException
import importlib
import os
import sys

class TestPaymentsCrossBorderSettlementApi(unittest.TestCase):
    """PaymentsCrossBorderSettlementApi unit test stubs"""
    os.environ["FIREBLOCKS_API_KEY"] = ""
    os.environ["FIREBLOCKS_SECRET_KEY"]  = ""
    def setUp(self):
        self.api = fireblocks_client.api.payments_cross_border_settlement_api.PaymentsCrossBorderSettlementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_xb_settlement_config(self):
        """Test case for create_xb_settlement_config

        Create a new cross-border settlement configuration  # noqa: E501
        """
        pass

    def test_create_xb_settlement_flow(self):
        """Test case for create_xb_settlement_flow

        Create a new cross-border settlement flow  # noqa: E501
        """
        pass

    def test_delete_xb_settlement_config(self):
        """Test case for delete_xb_settlement_config

        Delete a cross-border settlement configuration  # noqa: E501
        """
        pass

    def test_execute_xb_settlement_flow_action(self):
        """Test case for execute_xb_settlement_flow_action

        Execute cross-border settlement flow  # noqa: E501
        """
        pass

    def test_get_xb_settlement_config_by_id(self):
        """Test case for get_xb_settlement_config_by_id

        Get a specific cross-border settlement configuration  # noqa: E501
        """
        pass

    def test_get_xb_settlement_configs(self):
        """Test case for get_xb_settlement_configs

        Get all the cross-border settlement configurations  # noqa: E501
        """
        pass

    def test_get_xb_settlement_flow_by_id(self):
        """Test case for get_xb_settlement_flow_by_id

        Get specific cross-border settlement flow details  # noqa: E501
        """
        pass

    def test_update_xb_settlement_config(self):
        """Test case for update_xb_settlement_config

        Edit a cross-border settlement configuration  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()