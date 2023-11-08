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

from fireblocks_client.model.create_address_response import CreateAddressResponse
from fireblocks_client.model.error import Error

from . import path

# Path params
VaultAccountIdSchema = schemas.StrSchema
AssetIdSchema = schemas.StrSchema
AddressIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'vaultAccountId': typing.Union[VaultAccountIdSchema, str, ],
        'assetId': typing.Union[AssetIdSchema, str, ],
        'addressId': typing.Union[AddressIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_vault_account_id = api_client.PathParameter(
    name="vaultAccountId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VaultAccountIdSchema,
    required=True,
)
request_path_asset_id = api_client.PathParameter(
    name="assetId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AssetIdSchema,
    required=True,
)
request_path_address_id = api_client.PathParameter(
    name="addressId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=AddressIdSchema,
    required=True,
)
XRequestIDSchema = schemas.StrSchema
x_request_id_parameter = api_client.HeaderParameter(
name="X-Request-ID",
    style=api_client.ParameterStyle.SIMPLE,
        schema=XRequestIDSchema,
)
SchemaFor200ResponseBody = CreateAddressResponse
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'X-Request-ID': XRequestIDSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
                SchemaFor200ResponseBody,
        ]
    headers: ResponseHeadersFor200


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
    '*/*': api_client.MediaType(
    schema=SchemaFor200ResponseBody),
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
    '200': _response_for_200,
    'default': _response_for_default,
}
_all_accept_content_types = (
    '*/*',
    'application/json',
        )


class BaseApi(api_client.Api):

    def _create_legacy_address_for_vault_account_asset_oapg(self, params: typing.Union[RequestPathParams] = None, request_options: RequestOptions = None):
        """
        Convert a segwit address to legacy format
        """
        path_params = {}
        for parameter in (
            request_path_vault_account_id,
            request_path_asset_id,
            request_path_address_id,
        ):
            path_params[parameter.name] =  params.get(parameter.name,None)

        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)

        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_vault_account_id,
            request_path_asset_id,
            request_path_address_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
        _headers = HTTPHeaderDict()

        idempotency_key = request_options.get("idempotency_key")
        if idempotency_key:
            _headers.add("Idempotency-Key", idempotency_key)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
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


class CreateLegacyAddressForVaultAccountAsset(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def create_legacy_address_for_vault_account_asset(self ,params: typing.Union[RequestPathParams] = None, request_options: RequestOptions = None):
        return self._create_legacy_address_for_vault_account_asset_oapg(params, request_options)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
    ]: ...

    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._create_legacy_address_for_vault_account_asset_oapg(
        path_params=path_params,
        accept_content_types=accept_content_types,
        stream=stream,
        timeout=timeout,
        skip_deserialization=skip_deserialization
    )


