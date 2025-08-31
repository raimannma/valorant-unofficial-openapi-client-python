from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_error import SendError
from ...models.stored_mmrv2_response import StoredMMRV2Response
from ...types import UNSET, Response, Unset


def _get_kwargs(
    affinity: str,
    platform: str,
    name: str,
    tag: str,
    *,
    size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v2/stored-mmr-history/{affinity}/{platform}/{name}/{tag}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SendError, StoredMMRV2Response]]:
    if response.status_code == 200:
        response_200 = StoredMMRV2Response.from_dict(response.json())

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
) -> Response[Union[SendError, StoredMMRV2Response]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    affinity: str,
    platform: str,
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
    size: Union[Unset, int] = UNSET,
) -> Response[Union[SendError, StoredMMRV2Response]]:
    """
    Args:
        affinity (str):
        platform (str):
        name (str):
        tag (str):
        size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendError, StoredMMRV2Response]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        platform=platform,
        name=name,
        tag=tag,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    affinity: str,
    platform: str,
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
    size: Union[Unset, int] = UNSET,
) -> Optional[Union[SendError, StoredMMRV2Response]]:
    """
    Args:
        affinity (str):
        platform (str):
        name (str):
        tag (str):
        size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendError, StoredMMRV2Response]
    """

    return sync_detailed(
        affinity=affinity,
        platform=platform,
        name=name,
        tag=tag,
        client=client,
        size=size,
    ).parsed


async def asyncio_detailed(
    affinity: str,
    platform: str,
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
    size: Union[Unset, int] = UNSET,
) -> Response[Union[SendError, StoredMMRV2Response]]:
    """
    Args:
        affinity (str):
        platform (str):
        name (str):
        tag (str):
        size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendError, StoredMMRV2Response]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        platform=platform,
        name=name,
        tag=tag,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    affinity: str,
    platform: str,
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
    size: Union[Unset, int] = UNSET,
) -> Optional[Union[SendError, StoredMMRV2Response]]:
    """
    Args:
        affinity (str):
        platform (str):
        name (str):
        tag (str):
        size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendError, StoredMMRV2Response]
    """

    return (
        await asyncio_detailed(
            affinity=affinity,
            platform=platform,
            name=name,
            tag=tag,
            client=client,
            size=size,
        )
    ).parsed
