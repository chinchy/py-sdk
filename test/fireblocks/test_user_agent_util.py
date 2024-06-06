"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import pytest
from fireblocks.user_agent_util import UserAgentUtil

@pytest.fixture
def mock_platform(mocker):
    mocker.patch('platform.system', return_value="Linux")
    mocker.patch('platform.release', return_value="5.4.0-42-generic")
    mocker.patch('platform.machine', return_value="x86_64")

@pytest.mark.parametrize("is_anonymous_platform, user_agent, expected", [
    (False, "customUserAgent", "customUserAgent fireblocks/sdk/python/1.0.3 (Linux 5.4.0-42-generic; x86_64)"),
    (True, "customUserAgent", "customUserAgent fireblocks/sdk/python/1.0.3"),
    (False, None, "fireblocks/sdk/python/1.0.3 (Linux 5.4.0-42-generic; x86_64)"),
    (True, None, "fireblocks/sdk/python/1.0.3")])
def test_get_user_agent(mock_platform, is_anonymous_platform, user_agent, expected):
    # Create an instance of UserAgentUtil
    util = UserAgentUtil()

    # Call the get_user_agent method with test inputs
    result = util.get_user_agent(is_anonymous_platform, user_agent)

    # Assert that the output is as expected
    assert result == expected
