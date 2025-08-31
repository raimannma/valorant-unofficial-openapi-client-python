from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.matches_v2_response import MatchesV2Response
from ...models.send_error import SendError
from ...types import Response


def _get_kwargs(
    match_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v2/match/{match_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[MatchesV2Response, SendError]]:
    if response.status_code == 200:
        response_200 = MatchesV2Response.from_dict(response.json())

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
) -> Response[Union[MatchesV2Response, SendError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    match_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[MatchesV2Response, SendError]]:
    """
    Args:
        match_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MatchesV2Response, SendError]]
    """

    kwargs = _get_kwargs(
        match_id=match_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    match_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[MatchesV2Response, SendError]]:
    """
    Args:
        match_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MatchesV2Response, SendError]
    """

    return sync_detailed(
        match_id=match_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    match_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[MatchesV2Response, SendError]]:
    """
    Args:
        match_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MatchesV2Response, SendError]]
    """

    kwargs = _get_kwargs(
        match_id=match_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    match_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[MatchesV2Response, SendError]]:
    """
    Args:
        match_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MatchesV2Response, SendError]
    """

    return (
        await asyncio_detailed(
            match_id=match_id,
            client=client,
        )
    ).parsed
