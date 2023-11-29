# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 
    Contact: support@fireblocks.com
    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import fireblocks_client
from fireblocks_client.paths.fiat_accounts_account_id_redeem_to_linked_dda import post  # noqa: E501
from fireblocks_client import configuration, schemas, api_client

from .. import ApiTestMixin


class TestFiatAccountsAccountIdRedeemToLinkedDda(ApiTestMixin, unittest.TestCase):
    """
    FiatAccountsAccountIdRedeemToLinkedDda unit test stubs
        Redeem funds to DDA  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 201
    response_body = ''


if __name__ == '__main__':
    unittest.main()
