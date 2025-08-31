from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.matches_v4_history_response import MatchesV4HistoryResponse
from ...models.send_error import SendError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    affinity: str,
    platform: str,
    puuid: str,
    *,
    mode: Union[Unset, str] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mode"] = mode

    params["map"] = map_

    params["size"] = size

    params["start"] = start

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v4/by-puuid/matches/{affinity}/{platform}/{puuid}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[MatchesV4HistoryResponse, SendError]]:
    if response.status_code == 200:
        response_200 = MatchesV4HistoryResponse.from_dict(response.json())

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
) -> Response[Union[MatchesV4HistoryResponse, SendError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    affinity: str,
    platform: str,
    puuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    mode: Union[Unset, str] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = UNSET,
) -> Response[Union[MatchesV4HistoryResponse, SendError]]:
    """
    Args:
        affinity (str):
        platform (str):
        puuid (str):
        mode (Union[Unset, str]):
        map_ (Union[Unset, str]):
        size (Union[Unset, int]):
        start (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MatchesV4HistoryResponse, SendError]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        platform=platform,
        puuid=puuid,
        mode=mode,
        map_=map_,
        size=size,
        start=start,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    affinity: str,
    platform: str,
    puuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    mode: Union[Unset, str] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = UNSET,
) -> Optional[Union[MatchesV4HistoryResponse, SendError]]:
    """
    Args:
        affinity (str):
        platform (str):
        puuid (str):
        mode (Union[Unset, str]):
        map_ (Union[Unset, str]):
        size (Union[Unset, int]):
        start (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MatchesV4HistoryResponse, SendError]
    """

    return sync_detailed(
        affinity=affinity,
        platform=platform,
        puuid=puuid,
        client=client,
        mode=mode,
        map_=map_,
        size=size,
        start=start,
    ).parsed


async def asyncio_detailed(
    affinity: str,
    platform: str,
    puuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    mode: Union[Unset, str] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = UNSET,
) -> Response[Union[MatchesV4HistoryResponse, SendError]]:
    """
    Args:
        affinity (str):
        platform (str):
        puuid (str):
        mode (Union[Unset, str]):
        map_ (Union[Unset, str]):
        size (Union[Unset, int]):
        start (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MatchesV4HistoryResponse, SendError]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        platform=platform,
        puuid=puuid,
        mode=mode,
        map_=map_,
        size=size,
        start=start,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    affinity: str,
    platform: str,
    puuid: str,
    *,
    client: Union[AuthenticatedClient, Client],
    mode: Union[Unset, str] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    start: Union[Unset, int] = UNSET,
) -> Optional[Union[MatchesV4HistoryResponse, SendError]]:
    """
    Args:
        affinity (str):
        platform (str):
        puuid (str):
        mode (Union[Unset, str]):
        map_ (Union[Unset, str]):
        size (Union[Unset, int]):
        start (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MatchesV4HistoryResponse, SendError]
    """

    return (
        await asyncio_detailed(
            affinity=affinity,
            platform=platform,
            puuid=puuid,
            client=client,
            mode=mode,
            map_=map_,
            size=size,
            start=start,
        )
    ).parsed
