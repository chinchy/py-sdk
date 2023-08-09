# coding: utf-8

"""
    Fireblocks API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.6.2
    Contact: support@fireblocks.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
from typing_extensions import Annotated
from pydantic import Field, StrictStr

from fireblocks_client.models.gas_station_configuration import GasStationConfiguration
from fireblocks_client.models.gas_station_properties_response import GasStationPropertiesResponse
from fireblocks_client.api_client import ApiClient
from fireblocks_client.api_client import Configuration
from fireblocks_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from pydantic import validate_arguments,validate_call

class GasStationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, configuration:Configuration = None):
        if configuration is None:
            api_client = ApiClient()
        else:
            api_client = ApiClient(configuration)
        self.api_client = api_client

    @validate_call
    def get_gas_station(self, **kwargs) -> GasStationPropertiesResponse:  # noqa: E501
        """Get gas station settings  # noqa: E501

        Returns gas station settings and ETH balance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gas_station(async_req = True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GasStationPropertiesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_gas_station_with_http_info(**kwargs)  # noqa: E501

    @validate_call
    def get_gas_station_with_http_info(self, **kwargs):  # noqa: E501
        """Get gas station settings  # noqa: E501

        Returns gas station settings and ETH balance.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req = True

        >>> thread = api.get_gas_station_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GasStationPropertiesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gas_station" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "GasStationPropertiesResponse",
        }

        return self.api_client.call_api(
            '/gas_station', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body = _body_params,
            post_params=_form_params,
            files = _files,
            response_types_map = _response_types_map,
            auth_settings = _auth_settings,
            async_req = _params.get('async_req'),
            _return_http_data_only = _params.get('_return_http_data_only'),  # noqa: E501
            _preload_content = _params.get('_preload_content', True),
            _request_timeout = _params.get('_request_timeout'),
            collection_formats = _collection_formats,
            _request_auth = _params.get('_request_auth'))

    @validate_call
    def get_gas_station_by_asset_id(self, asset_id : Annotated[StrictStr, Field(..., description="The ID of the asset")], **kwargs) -> GasStationPropertiesResponse:  # noqa: E501
        """Get gas station settings by asset  # noqa: E501

        Returns gas station settings and balances for a requested asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_gas_station_by_asset_id(asset_id, async_req = True)
        >>> result = thread.get()

        :param asset_id: The ID of the asset (required)
        :type asset_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GasStationPropertiesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_gas_station_by_asset_id_with_http_info(asset_id, **kwargs)  # noqa: E501

    @validate_call
    def get_gas_station_by_asset_id_with_http_info(self, asset_id : Annotated[StrictStr, Field(..., description="The ID of the asset")], **kwargs):  # noqa: E501
        """Get gas station settings by asset  # noqa: E501

        Returns gas station settings and balances for a requested asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req = True

        >>> thread = api.get_gas_station_by_asset_id_with_http_info(asset_id, async_req=True)
        >>> result = thread.get()

        :param asset_id: The ID of the asset (required)
        :type asset_id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GasStationPropertiesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'asset_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_gas_station_by_asset_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['asset_id']:
            _path_params['assetId'] = _params['asset_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "GasStationPropertiesResponse",
        }

        return self.api_client.call_api(
            '/gas_station/{assetId}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body = _body_params,
            post_params=_form_params,
            files = _files,
            response_types_map = _response_types_map,
            auth_settings = _auth_settings,
            async_req = _params.get('async_req'),
            _return_http_data_only = _params.get('_return_http_data_only'),  # noqa: E501
            _preload_content = _params.get('_preload_content', True),
            _request_timeout = _params.get('_request_timeout'),
            collection_formats = _collection_formats,
            _request_auth = _params.get('_request_auth'))

    @validate_call
    def update_gas_station_configuration(self, gas_station_configuration : GasStationConfiguration, **kwargs) -> None:  # noqa: E501
        """Edit gas station settings  # noqa: E501

        Configures gas station settings for ETH.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_gas_station_configuration(gas_station_configuration, async_req = True)
        >>> result = thread.get()

        :param gas_station_configuration: (required)
        :type gas_station_configuration: GasStationConfiguration
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.update_gas_station_configuration_with_http_info(gas_station_configuration, **kwargs)  # noqa: E501

    @validate_call
    def update_gas_station_configuration_with_http_info(self, gas_station_configuration : GasStationConfiguration, **kwargs):  # noqa: E501
        """Edit gas station settings  # noqa: E501

        Configures gas station settings for ETH.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req = True

        >>> thread = api.update_gas_station_configuration_with_http_info(gas_station_configuration, async_req=True)
        >>> result = thread.get()

        :param gas_station_configuration: (required)
        :type gas_station_configuration: GasStationConfiguration
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'gas_station_configuration'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_gas_station_configuration" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['gas_station_configuration']:
            _body_params = _params['gas_station_configuration']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/gas_station/configuration', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body = _body_params,
            post_params=_form_params,
            files = _files,
            response_types_map = _response_types_map,
            auth_settings = _auth_settings,
            async_req = _params.get('async_req'),
            _return_http_data_only = _params.get('_return_http_data_only'),  # noqa: E501
            _preload_content = _params.get('_preload_content', True),
            _request_timeout = _params.get('_request_timeout'),
            collection_formats = _collection_formats,
            _request_auth = _params.get('_request_auth'))

    @validate_call
    def update_gas_station_configuration_by_asset_id(self, asset_id : Annotated[StrictStr, Field(..., description="The ID of the asset")], gas_station_configuration : GasStationConfiguration, **kwargs) -> None:  # noqa: E501
        """Edit gas station settings for an asset  # noqa: E501

        Configures gas station settings for a requested asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_gas_station_configuration_by_asset_id(asset_id, gas_station_configuration, async_req = True)
        >>> result = thread.get()

        :param asset_id: The ID of the asset (required)
        :type asset_id: str
        :param gas_station_configuration: (required)
        :type gas_station_configuration: GasStationConfiguration
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.update_gas_station_configuration_by_asset_id_with_http_info(asset_id, gas_station_configuration, **kwargs)  # noqa: E501

    @validate_call
    def update_gas_station_configuration_by_asset_id_with_http_info(self, asset_id : Annotated[StrictStr, Field(..., description="The ID of the asset")], gas_station_configuration : GasStationConfiguration, **kwargs):  # noqa: E501
        """Edit gas station settings for an asset  # noqa: E501

        Configures gas station settings for a requested asset.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req = True

        >>> thread = api.update_gas_station_configuration_by_asset_id_with_http_info(asset_id, gas_station_configuration, async_req=True)
        >>> result = thread.get()

        :param asset_id: The ID of the asset (required)
        :type asset_id: str
        :param gas_station_configuration: (required)
        :type gas_station_configuration: GasStationConfiguration
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'asset_id',
            'gas_station_configuration'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_gas_station_configuration_by_asset_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['asset_id']:
            _path_params['assetId'] = _params['asset_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['gas_station_configuration']:
            _body_params = _params['gas_station_configuration']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/gas_station/configuration/{assetId}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body = _body_params,
            post_params=_form_params,
            files = _files,
            response_types_map = _response_types_map,
            auth_settings = _auth_settings,
            async_req = _params.get('async_req'),
            _return_http_data_only = _params.get('_return_http_data_only'),  # noqa: E501
            _preload_content = _params.get('_preload_content', True),
            _request_timeout = _params.get('_request_timeout'),
            collection_formats = _collection_formats,
            _request_auth = _params.get('_request_auth'))
