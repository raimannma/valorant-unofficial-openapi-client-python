from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.premier_team_history_v1_response import PremierTeamHistoryV1Response
from ...types import Response


def _get_kwargs(
    name: str,
    tag: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v1/premier/{name}/{tag}/history",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PremierTeamHistoryV1Response]]:
    if response.status_code == 200:
        response_200 = PremierTeamHistoryV1Response.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PremierTeamHistoryV1Response]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, PremierTeamHistoryV1Response]]:
    """
    Args:
        name (str):
        tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PremierTeamHistoryV1Response]]
    """

    kwargs = _get_kwargs(
        name=name,
        tag=tag,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, PremierTeamHistoryV1Response]]:
    """
    Args:
        name (str):
        tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PremierTeamHistoryV1Response]
    """

    return sync_detailed(
        name=name,
        tag=tag,
        client=client,
    ).parsed


async def asyncio_detailed(
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, PremierTeamHistoryV1Response]]:
    """
    Args:
        name (str):
        tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PremierTeamHistoryV1Response]]
    """

    kwargs = _get_kwargs(
        name=name,
        tag=tag,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, PremierTeamHistoryV1Response]]:
    """
    Args:
        name (str):
        tag (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PremierTeamHistoryV1Response]
    """

    return (
        await asyncio_detailed(
            name=name,
            tag=tag,
            client=client,
        )
    ).parsed
