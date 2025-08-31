from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.premier_search_response import PremierSearchResponse
from ...models.send_error import SendError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    affinity: str,
    *,
    conference: Union[Unset, str] = UNSET,
    division: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["conference"] = conference

    params["division"] = division

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v1/premier/leaderboard/{affinity}",
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
    affinity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    conference: Union[Unset, str] = UNSET,
    division: Union[Unset, str] = UNSET,
) -> Response[Union[PremierSearchResponse, SendError]]:
    """
    Args:
        affinity (str):
        conference (Union[Unset, str]):
        division (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PremierSearchResponse, SendError]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        conference=conference,
        division=division,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    affinity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    conference: Union[Unset, str] = UNSET,
    division: Union[Unset, str] = UNSET,
) -> Optional[Union[PremierSearchResponse, SendError]]:
    """
    Args:
        affinity (str):
        conference (Union[Unset, str]):
        division (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PremierSearchResponse, SendError]
    """

    return sync_detailed(
        affinity=affinity,
        client=client,
        conference=conference,
        division=division,
    ).parsed


async def asyncio_detailed(
    affinity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    conference: Union[Unset, str] = UNSET,
    division: Union[Unset, str] = UNSET,
) -> Response[Union[PremierSearchResponse, SendError]]:
    """
    Args:
        affinity (str):
        conference (Union[Unset, str]):
        division (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[PremierSearchResponse, SendError]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        conference=conference,
        division=division,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    affinity: str,
    *,
    client: Union[AuthenticatedClient, Client],
    conference: Union[Unset, str] = UNSET,
    division: Union[Unset, str] = UNSET,
) -> Optional[Union[PremierSearchResponse, SendError]]:
    """
    Args:
        affinity (str):
        conference (Union[Unset, str]):
        division (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[PremierSearchResponse, SendError]
    """

    return (
        await asyncio_detailed(
            affinity=affinity,
            client=client,
            conference=conference,
            division=division,
        )
    ).parsed
