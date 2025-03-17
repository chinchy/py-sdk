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

from fireblocks.models.travel_rule_validate_national_identification import (
    TravelRuleValidateNationalIdentification,
)


class TestTravelRuleValidateNationalIdentification(unittest.TestCase):
    """TravelRuleValidateNationalIdentification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> TravelRuleValidateNationalIdentification:
        """Test TravelRuleValidateNationalIdentification
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRuleValidateNationalIdentification`
        """
        model = TravelRuleValidateNationalIdentification()
        if include_optional:
            return TravelRuleValidateNationalIdentification(
                country_of_issue = 'US',
                national_identifier = '123456789',
                national_identifier_type = 'NATIONAL_ID',
                registration_authority = 'RA123456'
            )
        else:
            return TravelRuleValidateNationalIdentification(
        )
        """

    def testTravelRuleValidateNationalIdentification(self):
        """Test TravelRuleValidateNationalIdentification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
