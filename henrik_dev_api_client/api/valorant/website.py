from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.send_error import SendError
from ...models.website_v1_response import WebsiteV1Response
from ...types import UNSET, Response, Unset


def _get_kwargs(
    country_code: str,
    *,
    category: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["category"] = category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v1/website/{country_code}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[SendError, WebsiteV1Response]]:
    if response.status_code == 200:
        response_200 = WebsiteV1Response.from_dict(response.json())

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
) -> Response[Union[SendError, WebsiteV1Response]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    country_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
) -> Response[Union[SendError, WebsiteV1Response]]:
    """
    Args:
        country_code (str):
        category (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendError, WebsiteV1Response]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
        category=category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    country_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
) -> Optional[Union[SendError, WebsiteV1Response]]:
    """
    Args:
        country_code (str):
        category (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendError, WebsiteV1Response]
    """

    return sync_detailed(
        country_code=country_code,
        client=client,
        category=category,
    ).parsed


async def asyncio_detailed(
    country_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
) -> Response[Union[SendError, WebsiteV1Response]]:
    """
    Args:
        country_code (str):
        category (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[SendError, WebsiteV1Response]]
    """

    kwargs = _get_kwargs(
        country_code=country_code,
        category=category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    country_code: str,
    *,
    client: Union[AuthenticatedClient, Client],
    category: Union[Unset, str] = UNSET,
) -> Optional[Union[SendError, WebsiteV1Response]]:
    """
    Args:
        country_code (str):
        category (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[SendError, WebsiteV1Response]
    """

    return (
        await asyncio_detailed(
            country_code=country_code,
            client=client,
            category=category,
        )
    ).parsed
