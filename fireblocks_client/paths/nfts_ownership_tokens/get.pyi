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

from fireblocks_client.model.paging import Paging
from fireblocks_client.model.token_ownership_response import TokenOwnershipResponse

# Query params


class BlockchainDescriptorSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def ETH(cls):
        return cls("ETH")
    
    @schemas.classproperty
    def ETH_TEST3(cls):
        return cls("ETH_TEST3")
    
    @schemas.classproperty
    def POLYGON(cls):
        return cls("POLYGON")
    
    @schemas.classproperty
    def POLYGON_TEST_MUMBAI(cls):
        return cls("POLYGON_TEST_MUMBAI")
VaultAccountIdsSchema = schemas.StrSchema
IdsSchema = schemas.StrSchema
CollectionIdsSchema = schemas.StrSchema
PageCursorSchema = schemas.StrSchema


class PageSizeSchema(
    schemas.NumberSchema
):
    pass


class SortSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
            
            @schemas.classproperty
            def OWNERSHIP_LAST_UPDATE_TIME(cls):
                return cls("ownershipLastUpdateTime")
            
            @schemas.classproperty
            def NAME(cls):
                return cls("name")
            
            @schemas.classproperty
            def COLLECTION_NAME(cls):
                return cls("collection.name")
            
            @schemas.classproperty
            def BLOCKCHAIN_DESCRIPTOR(cls):
                return cls("blockchainDescriptor")

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SortSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)


class OrderSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DESC(cls):
        return cls("DESC")
    
    @schemas.classproperty
    def ASC(cls):
        return cls("ASC")


class StatusSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def LISTED(cls):
        return cls("LISTED")
    
    @schemas.classproperty
    def ARCHIVED(cls):
        return cls("ARCHIVED")


class SearchSchema(
    schemas.StrSchema
):
    pass
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'blockchainDescriptor': typing.Union[BlockchainDescriptorSchema, str, ],
        'vaultAccountIds': typing.Union[VaultAccountIdsSchema, str, ],
        'ids': typing.Union[IdsSchema, str, ],
        'collectionIds': typing.Union[CollectionIdsSchema, str, ],
        'pageCursor': typing.Union[PageCursorSchema, str, ],
        'pageSize': typing.Union[PageSizeSchema, decimal.Decimal, int, float, ],
        'sort': typing.Union[SortSchema, list, tuple, ],
        'order': typing.Union[OrderSchema, str, ],
        'status': typing.Union[StatusSchema, str, ],
        'search': typing.Union[SearchSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_blockchain_descriptor = api_client.QueryParameter(
    name="blockchainDescriptor",
    style=api_client.ParameterStyle.FORM,
    schema=BlockchainDescriptorSchema,
    explode=True,
)
request_query_vault_account_ids = api_client.QueryParameter(
    name="vaultAccountIds",
    style=api_client.ParameterStyle.FORM,
    schema=VaultAccountIdsSchema,
    explode=True,
)
request_query_ids = api_client.QueryParameter(
    name="ids",
    style=api_client.ParameterStyle.FORM,
    schema=IdsSchema,
    explode=True,
)
request_query_collection_ids = api_client.QueryParameter(
    name="collectionIds",
    style=api_client.ParameterStyle.FORM,
    schema=CollectionIdsSchema,
    explode=True,
)
request_query_page_cursor = api_client.QueryParameter(
    name="pageCursor",
    style=api_client.ParameterStyle.FORM,
    schema=PageCursorSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="pageSize",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_sort = api_client.QueryParameter(
    name="sort",
    style=api_client.ParameterStyle.FORM,
    schema=SortSchema,
    explode=True,
)
request_query_order = api_client.QueryParameter(
    name="order",
    style=api_client.ParameterStyle.FORM,
    schema=OrderSchema,
    explode=True,
)
request_query_status = api_client.QueryParameter(
    name="status",
    style=api_client.ParameterStyle.FORM,
    schema=StatusSchema,
    explode=True,
)
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
XRequestIDSchema = schemas.StrSchema


class SchemaFor200ResponseBodyApplicationJson(
    schemas.AnyTypeSchema,
):


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def paging() -> typing.Type['Paging']:
                return Paging
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TokenOwnershipResponse']:
                        return TokenOwnershipResponse
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TokenOwnershipResponse'], typing.List['TokenOwnershipResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TokenOwnershipResponse':
                    return super().__getitem__(i)
            __annotations__ = {
                "paging": paging,
                "data": data,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paging"]) -> 'Paging': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["paging", "data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paging"]) -> typing.Union['Paging', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["paging", "data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        paging: typing.Union['Paging', schemas.Unset] = schemas.unset,
        data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            paging=paging,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )
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
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: ResponseHeadersFor200


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
    headers=[
        x_request_id_parameter,
    ]
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_ownership_tokens_oapg(self, params: typing.Union[RequestQueryParams,] = None, request_options: RequestOptions = None):
        """
        List all owned tokens (paginated)
        """
        query_params = {}
        query_params["blockchain_descriptor"] = params.get("blockchain_descriptor")
        query_params["vault_account_ids"] = params.get("vault_account_ids")
        query_params["ids"] = params.get("ids")
        query_params["collection_ids"] = params.get("collection_ids")
        query_params["page_cursor"] = params.get("page_cursor")
        query_params["page_size"] = params.get("page_size")
        query_params["sort"] = params.get("sort")
        query_params["order"] = params.get("order")
        query_params["status"] = params.get("status")
        query_params["search"] = params.get("search")
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_blockchain_descriptor,
            request_query_vault_account_ids,
            request_query_ids,
            request_query_collection_ids,
            request_query_page_cursor,
            request_query_page_size,
            request_query_sort,
            request_query_order,
            request_query_status,
            request_query_search,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()

        idempotency_key = request_options.get("idempotency_key")
        if idempotency_key:
            _headers.add("Idempotency-Key", idempotency_key)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            timeout=10000,
        )

        response_for_status = _status_code_to_response.get(str(response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(response, self.api_client.configuration)
        else:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GetOwnershipTokens(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    def get_ownership_tokens(self ,params: typing.Union[RequestQueryParams,] = None, request_options: RequestOptions = None):
        return self._get_ownership_tokens_oapg(params, request_options)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_ownership_tokens_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


