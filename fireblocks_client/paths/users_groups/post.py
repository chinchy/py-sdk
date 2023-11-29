# coding: utf-8
from dataclasses import dataclass
import typing_extensions
from fireblocks_client.model.request_options import RequestOptions
import urllib3
from urllib3._collections import HTTPHeaderDict

from fireblocks_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from fireblocks_client import schemas  # noqa: F401

from fireblocks_client.model.user_group_create_request import UserGroupCreateRequest
from fireblocks_client.model.create_users_group_response import CreateUsersGroupResponse
from fireblocks_client.model.error import Error

from . import path

# body param
SchemaForRequestBodyApplicationJson = UserGroupCreateRequest
request_body_user_group_create_request = api_client.RequestBody(
content={
    'application/json': api_client.MediaType(
        schema=SchemaForRequestBodyApplicationJson),
},
    required=True,
)
XRequestIDSchema = schemas.StrSchema
x_request_id_parameter = api_client.HeaderParameter(
name="X-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
        schema=XRequestIDSchema,
)
SchemaFor201ResponseBody = CreateUsersGroupResponse
ResponseHeadersFor201 = typing_extensions.TypedDict(
    'ResponseHeadersFor201',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
                SchemaFor201ResponseBody,
        ]
    headers: ResponseHeadersFor201


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    content={
    '*/*': api_client.MediaType(
    schema=SchemaFor201ResponseBody),
    },
    headers=[
            x_request_id_parameter,
        ]
    )
XRequestIDSchema = schemas.StrSchema
x_request_id_parameter = api_client.HeaderParameter(
name="X-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
        schema=XRequestIDSchema,
)
SchemaFor0ResponseBodyApplicationJson = Error
ResponseHeadersFor0 = typing_extensions.TypedDict(
    'ResponseHeadersFor0',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
                SchemaFor0ResponseBodyApplicationJson,
        ]
    headers: ResponseHeadersFor0


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
    'application/json': api_client.MediaType(
    schema=SchemaFor0ResponseBodyApplicationJson),
    },
    headers=[
            x_request_id_parameter,
        ]
    )
_status_code_to_response = {
    '201': _response_for_201,
    'default': _response_for_default,
}
_all_accept_content_types = (
    '*/*',
    'application/json',
        )


class BaseApi(api_client.Api):

    def _create_user_group_oapg(self, params: typing.Union[SchemaForRequestBodyApplicationJson,] = None, request_options: RequestOptions = None):
        """
        Create users group
        """

        used_path = path.value
        _headers = HTTPHeaderDict()

        body =  params.get(user_group_create_request, schemas.unset)
        if body is schemas.unset:
            raise exceptions.ApiValueError(
            'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        serialized_data = request_body_user_group_create_request.serialize(params, "application/json")
        _headers.add('Content-Type', "application/json")
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
        idempotency_key = request_options.get("idempotency_key")
        if idempotency_key:
            _headers.add("Idempotency-Key", idempotency_key)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            timeout=10000,
        )

        response_for_status = _status_code_to_response.get(str(response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(response, self.api_client.configuration)
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class CreateUserGroup(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def create_user_group(self ,params: typing.Union[SchemaForRequestBodyApplicationJson,] = None, request_options: RequestOptions = None):
        return self._create_user_group_oapg(params, request_options)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: typing_extensions.Literal["application/json"] = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
    ]: ...


    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = ...,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        body: typing.Union[SchemaForRequestBodyApplicationJson,],
        content_type: str = 'application/json',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._create_user_group_oapg(
        body=body,
        content_type=content_type,
        accept_content_types=accept_content_types,
        stream=stream,
        timeout=timeout,
        skip_deserialization=skip_deserialization
    )


