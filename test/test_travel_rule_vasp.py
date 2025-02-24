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

from fireblocks.models.travel_rule_vasp import TravelRuleVASP


class TestTravelRuleVASP(unittest.TestCase):
    """TravelRuleVASP unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TravelRuleVASP:
        """Test TravelRuleVASP
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `TravelRuleVASP`
        """
        model = TravelRuleVASP()
        if include_optional:
            return TravelRuleVASP(
                did = 'did:ethr:0x17fe2dd11a2daa7f6c1fdf22532a4763f963aea6',
                name = 'Fireblocks TST',
                verification_status = 'VERIFIED',
                address_line1 = '657 Campfire Street',
                address_line2 = 'Suite 10',
                city = 'New York',
                country = 'US',
                email_domains = 'fireblocks.com,example.com',
                website = 'https://fireblocks.com',
                logo = 'https://fireblocks.com/logo.png',
                legal_structure = 'CORPORATION',
                legal_name = 'Fireblocks Inc.',
                year_founded = '2019',
                incorporation_country = 'US',
                is_regulated = 'YES',
                other_names = 'Fireblocks Test VASP',
                identification_type = 'Business License',
                identification_country = 'US',
                business_number = '123456789',
                regulatory_authorities = 'SEC, FINCEN',
                jurisdictions = 'US, EU',
                street = 'Wall Street',
                number = '10',
                unit = 'Apt 2B',
                post_code = '10005',
                state = 'NY',
                certificates = 'ISO 27001',
                description = 'A leading provider of crypto security solutions.',
                travel_rule_openvasp = 'active',
                travel_rule_sygna = 'inactive',
                travel_rule_trisa = 'pending',
                travel_rule_trlight = 'active',
                travel_rule_email = 'inactive',
                travel_rule_trp = 'active',
                travel_rule_shyft = 'inactive',
                travel_rule_ustravelrulewg = 'pending',
                created_at = '2023-09-19T12:23:59.711Z',
                created_by = 'admin',
                updated_at = '2024-08-29T08:23:51.416Z',
                updated_by = 'system',
                last_sent_date = '2024-03-18T09:26:07.988Z',
                last_received_date = '2024-03-20T11:45:30.212Z',
                documents = '['license.pdf', 'compliance.pdf']',
                has_admin = True,
                is_notifiable = True,
                issuers = fireblocks.models.travel_rule_issuers.TravelRuleIssuers(
                    year_founded = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                        issuer_did = '', ), 
                    is_regulated = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                        issuer_did = '', ), 
                    regulatory_authorities = , 
                    name = , 
                    logo = , 
                    website = , 
                    legal_name = , 
                    legal_structure = , 
                    incorporation_country = , 
                    business_number = , 
                    address_line1 = , 
                    city = , 
                    country = , 
                    description = , )
            )
        else:
            return TravelRuleVASP(
                did = 'did:ethr:0x17fe2dd11a2daa7f6c1fdf22532a4763f963aea6',
                name = 'Fireblocks TST',
                verification_status = 'VERIFIED',
                address_line1 = '657 Campfire Street',
                city = 'New York',
                country = 'US',
                email_domains = 'fireblocks.com,example.com',
                website = 'https://fireblocks.com',
                legal_structure = 'CORPORATION',
                legal_name = 'Fireblocks Inc.',
                year_founded = '2019',
                incorporation_country = 'US',
                is_regulated = 'YES',
                jurisdictions = 'US, EU',
                travel_rule_trlight = 'active',
                created_at = '2023-09-19T12:23:59.711Z',
                has_admin = True,
                is_notifiable = True,
                issuers = fireblocks.models.travel_rule_issuers.TravelRuleIssuers(
                    year_founded = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                        issuer_did = '', ), 
                    is_regulated = fireblocks.models.travel_rule_issuer.TravelRuleIssuer(
                        issuer_did = '', ), 
                    regulatory_authorities = , 
                    name = , 
                    logo = , 
                    website = , 
                    legal_name = , 
                    legal_structure = , 
                    incorporation_country = , 
                    business_number = , 
                    address_line1 = , 
                    city = , 
                    country = , 
                    description = , ),
        )
        """

    def testTravelRuleVASP(self):
        """Test TravelRuleVASP"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
