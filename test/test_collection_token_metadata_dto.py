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

from fireblocks.models.collection_token_metadata_dto import CollectionTokenMetadataDto


class TestCollectionTokenMetadataDto(unittest.TestCase):
    """CollectionTokenMetadataDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CollectionTokenMetadataDto:
        """Test CollectionTokenMetadataDto
        include_optional is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `CollectionTokenMetadataDto`
        """
        model = CollectionTokenMetadataDto()
        if include_optional:
            return CollectionTokenMetadataDto(
                name = 'DigitalArtTokens',
                description = 'Digital representation of a piece of art',
                image = 'https://some_domain.com/image_filepath',
                animation_url = 'https://some_domain.com/gif_filepath',
                external_url = 'https://some_domain.com/blob_filepath',
                attributes = [
                    fireblocks.models.collection_token_metadata_attribute_dto.CollectionTokenMetadataAttributeDto(
                        trait_type = 'project_start', 
                        value = '30102000', 
                        display_type = 'date', )
                    ]
            )
        else:
            return CollectionTokenMetadataDto(
                name = 'DigitalArtTokens',
                description = 'Digital representation of a piece of art',
        )
        """

    def testCollectionTokenMetadataDto(self):
        """Test CollectionTokenMetadataDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
