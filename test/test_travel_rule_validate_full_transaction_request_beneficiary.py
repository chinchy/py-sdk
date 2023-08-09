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

"""
import fireblocks_client
from fireblocks_client.models.travel_rule_validate_full_transaction_request_beneficiary import TravelRuleValidateFullTransactionRequestBeneficiary  # noqa: E501
from fireblocks_client.rest import ApiException
"""
class TestTravelRuleValidateFullTransactionRequestBeneficiary(unittest.TestCase):
    """TravelRuleValidateFullTransactionRequestBeneficiary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """
        Test TravelRuleValidateFullTransactionRequestBeneficiary
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included """
        # uncomment below to create an instance of `TravelRuleValidateFullTransactionRequestBeneficiary`
        """
        model = fireblocks_client.models.travel_rule_validate_full_transaction_request_beneficiary.TravelRuleValidateFullTransactionRequestBeneficiary()  # noqa: E501
        if include_optional :
        return TravelRuleValidateFullTransactionRequestBeneficiary(
            full_name = '', 
            date_of_birth = '', 
            place_of_birth = '', 
            address = '', 
            identification_number = '', 
            nationality = '', 
            country_of_residence = '', 
            tax_identification_number = '', 
            customer_number = ''
        )
        else :
        return TravelRuleValidateFullTransactionRequestBeneficiary(
                full_name = '',
                date_of_birth = '',
                place_of_birth = '',
                address = '',
                identification_number = '',
                nationality = '',
                country_of_residence = '',
                tax_identification_number = '',
                customer_number = '',
        )
        """

    def testTravelRuleValidateFullTransactionRequestBeneficiary(self):
        """Test TravelRuleValidateFullTransactionRequestBeneficiary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()