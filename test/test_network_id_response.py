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

from fireblocks.models.network_id_response import NetworkIdResponse


class TestNetworkIdResponse(unittest.TestCase):
    """NetworkIdResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkIdResponse:
        """Test NetworkIdResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `NetworkIdResponse`
        """
        model = NetworkIdResponse()
        if include_optional:
            return NetworkIdResponse(
                routing_policy = {
                    'key' : null
                    },
                is_discoverable = True,
                id = '',
                name = ''
            )
        else:
            return NetworkIdResponse(
        )
        """

    def testNetworkIdResponse(self):
        """Test NetworkIdResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
