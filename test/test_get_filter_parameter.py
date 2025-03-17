# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fireblocks.models.get_filter_parameter import GetFilterParameter


class TestGetFilterParameter(unittest.TestCase):
    """GetFilterParameter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFilterParameter:
        """Test GetFilterParameter
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetFilterParameter`
        """
        model = GetFilterParameter()
        if include_optional:
            return GetFilterParameter(
                id = '',
                user_id = '',
                vault_account_id = 1.337,
                connection_method = '',
                fee_level = '',
                app_url = '',
                app_name = ''
            )
        else:
            return GetFilterParameter(
        )
        """

    def testGetFilterParameter(self):
        """Test GetFilterParameter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
