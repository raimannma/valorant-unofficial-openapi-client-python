from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.premier_search_response import PremierSearchResponse
from ...models.send_error import SendError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["name"] = name

    params["tag"] = tag

    params["id"] = id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/valorant/v1/premier/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[PremierSearchResponse, SendError]]:
    if response.status_code == 200:
        response_200 = PremierSearchResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SendError.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = SendError.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = SendError.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[PremierSearchResponse, SendError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
) -> Response[Union[PremierSearchResponse, SendError]]:
    """
    Args:
        name (Union[Unset, str]):
        tag (Union[Unset, str]):
        id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PremierSearchResponse, SendError]]
    """

    kwargs = _get_kwargs(
        name=name,
        tag=tag,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
) -> Optional[Union[PremierSearchResponse, SendError]]:
    """
    Args:
        name (Union[Unset, str]):
        tag (Union[Unset, str]):
        id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PremierSearchResponse, SendError]
    """

    return sync_detailed(
        client=client,
        name=name,
        tag=tag,
        id=id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
) -> Response[Union[PremierSearchResponse, SendError]]:
    """
    Args:
        name (Union[Unset, str]):
        tag (Union[Unset, str]):
        id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PremierSearchResponse, SendError]]
    """

    kwargs = _get_kwargs(
        name=name,
        tag=tag,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
    id: Union[Unset, str] = UNSET,
) -> Optional[Union[PremierSearchResponse, SendError]]:
    """
    Args:
        name (Union[Unset, str]):
        tag (Union[Unset, str]):
        id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PremierSearchResponse, SendError]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            tag=tag,
            id=id,
        )
    ).parsed
