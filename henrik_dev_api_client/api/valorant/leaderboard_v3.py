from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.leaderboard_v3_response import LeaderboardV3Response
from ...models.send_error import SendError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    affinity: str,
    platform: str,
    *,
    season: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["season"] = season

    params["size"] = size

    params["page"] = page

    params["name"] = name

    params["tag"] = tag

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v3/leaderboard/{affinity}/{platform}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[LeaderboardV3Response, SendError]]:
    if response.status_code == 200:
        response_200 = LeaderboardV3Response.from_dict(response.json())

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
) -> Response[Union[LeaderboardV3Response, SendError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    affinity: str,
    platform: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
) -> Response[Union[LeaderboardV3Response, SendError]]:
    """
    Args:
        affinity (str):
        platform (str):
        season (Union[Unset, str]):
        size (Union[Unset, int]):
        page (Union[Unset, int]):
        name (Union[Unset, str]):
        tag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[LeaderboardV3Response, SendError]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        platform=platform,
        season=season,
        size=size,
        page=page,
        name=name,
        tag=tag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    affinity: str,
    platform: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
) -> Optional[Union[LeaderboardV3Response, SendError]]:
    """
    Args:
        affinity (str):
        platform (str):
        season (Union[Unset, str]):
        size (Union[Unset, int]):
        page (Union[Unset, int]):
        name (Union[Unset, str]):
        tag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[LeaderboardV3Response, SendError]
    """

    return sync_detailed(
        affinity=affinity,
        platform=platform,
        client=client,
        season=season,
        size=size,
        page=page,
        name=name,
        tag=tag,
    ).parsed


async def asyncio_detailed(
    affinity: str,
    platform: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
) -> Response[Union[LeaderboardV3Response, SendError]]:
    """
    Args:
        affinity (str):
        platform (str):
        season (Union[Unset, str]):
        size (Union[Unset, int]):
        page (Union[Unset, int]):
        name (Union[Unset, str]):
        tag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[LeaderboardV3Response, SendError]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        platform=platform,
        season=season,
        size=size,
        page=page,
        name=name,
        tag=tag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    affinity: str,
    platform: str,
    *,
    client: Union[AuthenticatedClient, Client],
    season: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    tag: Union[Unset, str] = UNSET,
) -> Optional[Union[LeaderboardV3Response, SendError]]:
    """
    Args:
        affinity (str):
        platform (str):
        season (Union[Unset, str]):
        size (Union[Unset, int]):
        page (Union[Unset, int]):
        name (Union[Unset, str]):
        tag (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[LeaderboardV3Response, SendError]
    """

    return (
        await asyncio_detailed(
            affinity=affinity,
            platform=platform,
            client=client,
            season=season,
            size=size,
            page=page,
            name=name,
            tag=tag,
        )
    ).parsed
