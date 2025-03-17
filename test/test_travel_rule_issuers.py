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

from fireblocks.models.travel_rule_issuers import TravelRuleIssuers


class TestTravelRuleIssuers(unittest.TestCase):
    """TravelRuleIssuers unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRuleIssuers:
        """Test TravelRuleIssuers
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRuleIssuers`
        """
        model = TravelRuleIssuers()
        if include_optional:
            return TravelRuleIssuers(
                year_founded = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                is_regulated = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                regulatory_authorities = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                name = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                logo = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                website = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                legal_name = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                legal_structure = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                incorporation_country = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                business_number = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                address_line1 = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                city = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                country = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                description = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', )
            )
        else:
            return TravelRuleIssuers(
                year_founded = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                is_regulated = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                regulatory_authorities = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                name = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                logo = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                website = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                legal_name = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                legal_structure = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                incorporation_country = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                business_number = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                address_line1 = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                city = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                country = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
                description = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                    issuer_did = '', ),
        )
        """

    def testTravelRuleIssuers(self):
        """Test TravelRuleIssuers"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
