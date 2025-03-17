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

from fireblocks.models.travel_rule_legal_person_name_identifier import (
    TravelRuleLegalPersonNameIdentifier,
)


class TestTravelRuleLegalPersonNameIdentifier(unittest.TestCase):
    """TravelRuleLegalPersonNameIdentifier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRuleLegalPersonNameIdentifier:
        """Test TravelRuleLegalPersonNameIdentifier
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRuleLegalPersonNameIdentifier`
        """
        model = TravelRuleLegalPersonNameIdentifier()
        if include_optional:
            return TravelRuleLegalPersonNameIdentifier(
                legal_person_name = 'QmVXXj5BJchhqQTU27uEkeghYMnxR6aVjZxJP9jS6uCg9Q',
                legal_person_name_identifier_type = 'QmPevsa5xdkxf6Lgt7f9YweRBdgseeAkWVaYyssKF3Q86e'
            )
        else:
            return TravelRuleLegalPersonNameIdentifier(
        )
        """

    def testTravelRuleLegalPersonNameIdentifier(self):
        """Test TravelRuleLegalPersonNameIdentifier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
