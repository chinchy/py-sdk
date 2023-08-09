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
from fireblocks_client.api.policy_editor_beta_api import PolicyEditorBetaApi  # noqa: E501
from fireblocks_client.rest import ApiException
import importlib
import os
import sys

class TestPolicyEditorBetaApi(unittest.TestCase):
    """PolicyEditorBetaApi unit test stubs"""
    os.environ["FIREBLOCKS_API_KEY"] = ""
    os.environ["FIREBLOCKS_SECRET_KEY"]  = ""
    def setUp(self):
        self.api = fireblocks_client.api.policy_editor_beta_api.PolicyEditorBetaApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_active_policy(self):
        """Test case for get_active_policy

        Get the active policy and its validation  # noqa: E501
        """
        pass

    def test_get_draft(self):
        """Test case for get_draft

        Get the active draft  # noqa: E501
        """
        pass

    def test_publish_draft(self):
        """Test case for publish_draft

        Send publish request for a certain draft id  # noqa: E501
        """
        pass

    def test_publish_policy_rules(self):
        """Test case for publish_policy_rules

        Send publish request for a set of policy rules  # noqa: E501
        """
        pass

    def test_update_draft(self):
        """Test case for update_draft

        Update the draft with a new set of rules  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()