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

from pydantic import Field, StrictStr, confloat

from typing import Any, Dict, Optional

from fireblocks_client.models.create_connection_request import CreateConnectionRequest
from fireblocks_client.models.create_connection_response import CreateConnectionResponse
from fireblocks_client.models.get_connections_response import GetConnectionsResponse
from fireblocks_client.models.respond_to_connection_request import RespondToConnectionRequest

from fireblocks_client.api_client import ApiClient
from fireblocks_client.api_client import Configuration
from fireblocks_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from pydantic import validate_arguments



class Web3ConnectionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, configuration:Configuration=None):
        if configuration is None:
            api_client = ApiClient()
        else:
            api_client = ApiClient(configuration)
        self.api_client = api_client

    @validate_arguments
    def create_wc_connection(self, create_connection_request : CreateConnectionRequest, **kwargs) -> CreateConnectionResponse:  # noqa: E501
        """Create a new Web3 connection.  # noqa: E501

        Initiate a new Web3 connection.  * Note: After this succeeds, make a request to `PUT /v1/connections/wc/{id}` (below) to approve or reject the new Web3 connection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_wc_connection(create_connection_request, async_req=True)
        >>> result = thread.get()

        :param create_connection_request: (required)
        :type create_connection_request: CreateConnectionRequest
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
        :rtype: CreateConnectionResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.create_wc_connection_with_http_info(create_connection_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_wc_connection_with_http_info(self, create_connection_request : CreateConnectionRequest, **kwargs):  # noqa: E501
        """Create a new Web3 connection.  # noqa: E501

        Initiate a new Web3 connection.  * Note: After this succeeds, make a request to `PUT /v1/connections/wc/{id}` (below) to approve or reject the new Web3 connection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_wc_connection_with_http_info(create_connection_request, async_req=True)
        >>> result = thread.get()

        :param create_connection_request: (required)
        :type create_connection_request: CreateConnectionRequest
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
        :rtype: tuple(CreateConnectionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_connection_request'
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
                    " to method create_wc_connection" % _key
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
        if _params['create_connection_request']:
            _body_params = _params['create_connection_request']

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

        _response_types_map = {
            '201': "CreateConnectionResponse",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/connections/wc', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_wc_connection(self, id : Annotated[StrictStr, Field(..., description="The ID of the existing Web3 connection to remove.")], **kwargs) -> None:  # noqa: E501
        """Remove an existing Web3 connection.  # noqa: E501

        Remove a Web3 connection  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_wc_connection(id, async_req=True)
        >>> result = thread.get()

        :param id: The ID of the existing Web3 connection to remove. (required)
        :type id: str
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
        return self.delete_wc_connection_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_wc_connection_with_http_info(self, id : Annotated[StrictStr, Field(..., description="The ID of the existing Web3 connection to remove.")], **kwargs):  # noqa: E501
        """Remove an existing Web3 connection.  # noqa: E501

        Remove a Web3 connection  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_wc_connection_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The ID of the existing Web3 connection to remove. (required)
        :type id: str
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
            'id'
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
                    " to method delete_wc_connection" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/connections/wc/{id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_connections(self, order : Annotated[Optional[StrictStr], Field(description="List order; ascending or descending.")] = None, filter : Annotated[Optional[Dict[str, Any]], Field(description="Parsed filter object")] = None, sort : Annotated[Optional[StrictStr], Field(description="Property to sort Web3 connections by.")] = None, page_size : Annotated[Optional[confloat(ge=50, strict=True)], Field(description="Amount of results to return in the next page.")] = None, next : Annotated[Optional[StrictStr], Field(description="Cursor to the next page")] = None, **kwargs) -> GetConnectionsResponse:  # noqa: E501
        """List all open Web3 connections.  # noqa: E501

        Get open Web3 connections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_connections(order, filter, sort, page_size, next, async_req=True)
        >>> result = thread.get()

        :param order: List order; ascending or descending.
        :type order: str
        :param filter: Parsed filter object
        :type filter: GetConnectionsFilterParameter
        :param sort: Property to sort Web3 connections by.
        :type sort: str
        :param page_size: Amount of results to return in the next page.
        :type page_size: float
        :param next: Cursor to the next page
        :type next: str
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
        :rtype: GetConnectionsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_connections_with_http_info(order, filter, sort, page_size, next, **kwargs)  # noqa: E501

    @validate_arguments
    def get_connections_with_http_info(self, order : Annotated[Optional[StrictStr], Field(description="List order; ascending or descending.")] = None, filter : Annotated[Optional[Dict[str, Any]], Field(description="Parsed filter object")] = None, sort : Annotated[Optional[StrictStr], Field(description="Property to sort Web3 connections by.")] = None, page_size : Annotated[Optional[confloat(ge=50, strict=True)], Field(description="Amount of results to return in the next page.")] = None, next : Annotated[Optional[StrictStr], Field(description="Cursor to the next page")] = None, **kwargs):  # noqa: E501
        """List all open Web3 connections.  # noqa: E501

        Get open Web3 connections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_connections_with_http_info(order, filter, sort, page_size, next, async_req=True)
        >>> result = thread.get()

        :param order: List order; ascending or descending.
        :type order: str
        :param filter: Parsed filter object
        :type filter: GetConnectionsFilterParameter
        :param sort: Property to sort Web3 connections by.
        :type sort: str
        :param page_size: Amount of results to return in the next page.
        :type page_size: float
        :param next: Cursor to the next page
        :type next: str
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
        :rtype: tuple(GetConnectionsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'order',
            'filter',
            'sort',
            'page_size',
            'next'
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
                    " to method get_connections" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('order') is not None:  # noqa: E501
            _query_params.append(('order', _params['order']))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        if _params.get('page_size') is not None:  # noqa: E501
            _query_params.append(('pageSize', _params['page_size']))

        if _params.get('next') is not None:  # noqa: E501
            _query_params.append(('next', _params['next']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "GetConnectionsResponse",
            '400': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/connections', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_wc_connection(self, id : Annotated[StrictStr, Field(..., description="The ID of the initiated Web3 connection to approve.")], respond_to_connection_request : RespondToConnectionRequest, **kwargs) -> None:  # noqa: E501
        """Respond to a pending Web3 connection request.  # noqa: E501

        Submit a response to *approve* or *reject* an initiated Web3 connection. * Note: This call is used to complete your `POST /v1/connections/wc/` request.  After this succeeds, your new Web3 connection is created and functioning.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_wc_connection(id, respond_to_connection_request, async_req=True)
        >>> result = thread.get()

        :param id: The ID of the initiated Web3 connection to approve. (required)
        :type id: str
        :param respond_to_connection_request: (required)
        :type respond_to_connection_request: RespondToConnectionRequest
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
        return self.update_wc_connection_with_http_info(id, respond_to_connection_request, **kwargs)  # noqa: E501

    @validate_arguments
    def update_wc_connection_with_http_info(self, id : Annotated[StrictStr, Field(..., description="The ID of the initiated Web3 connection to approve.")], respond_to_connection_request : RespondToConnectionRequest, **kwargs):  # noqa: E501
        """Respond to a pending Web3 connection request.  # noqa: E501

        Submit a response to *approve* or *reject* an initiated Web3 connection. * Note: This call is used to complete your `POST /v1/connections/wc/` request.  After this succeeds, your new Web3 connection is created and functioning.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_wc_connection_with_http_info(id, respond_to_connection_request, async_req=True)
        >>> result = thread.get()

        :param id: The ID of the initiated Web3 connection to approve. (required)
        :type id: str
        :param respond_to_connection_request: (required)
        :type respond_to_connection_request: RespondToConnectionRequest
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
            'id',
            'respond_to_connection_request'
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
                    " to method update_wc_connection" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['respond_to_connection_request']:
            _body_params = _params['respond_to_connection_request']

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
            '/connections/wc/{id}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
