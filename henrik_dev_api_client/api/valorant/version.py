from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_error import SendError
from ...models.version_v1_response import VersionV1Response
from ...types import Response


def _get_kwargs(
    affinity: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v1/version/{affinity}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SendError, VersionV1Response]]:
    if response.status_code == 200:
        response_200 = VersionV1Response.from_dict(response.json())

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
) -> Response[Union[SendError, VersionV1Response]]:
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
) -> Response[Union[SendError, VersionV1Response]]:
    """
    Args:
        affinity (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendError, VersionV1Response]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    affinity: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[SendError, VersionV1Response]]:
    """
    Args:
        affinity (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendError, VersionV1Response]
    """

    return sync_detailed(
        affinity=affinity,
        client=client,
    ).parsed


async def asyncio_detailed(
    affinity: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[SendError, VersionV1Response]]:
    """
    Args:
        affinity (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendError, VersionV1Response]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    affinity: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[SendError, VersionV1Response]]:
    """
    Args:
        affinity (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendError, VersionV1Response]
    """

    return (
        await asyncio_detailed(
            affinity=affinity,
            client=client,
        )
    ).parsed
