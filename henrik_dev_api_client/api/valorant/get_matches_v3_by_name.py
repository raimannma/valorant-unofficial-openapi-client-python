from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.match_mode import MatchMode
from ...models.matches_v3_list_response import MatchesV3ListResponse
from ...models.send_error import SendError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    affinity: str,
    name: str,
    tag: str,
    *,
    mode: Union[Unset, MatchMode] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_mode: Union[Unset, str] = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode

    params["mode"] = json_mode

    params["map"] = map_

    params["size"] = size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/valorant/v3/matches/{affinity}/{name}/{tag}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[MatchesV3ListResponse, SendError]]:
    if response.status_code == 200:
        response_200 = MatchesV3ListResponse.from_dict(response.json())

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
) -> Response[Union[MatchesV3ListResponse, SendError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    affinity: str,
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
    mode: Union[Unset, MatchMode] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
) -> Response[Union[MatchesV3ListResponse, SendError]]:
    """
    Args:
        affinity (str):
        name (str):
        tag (str):
        mode (Union[Unset, MatchMode]):
        map_ (Union[Unset, str]):
        size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MatchesV3ListResponse, SendError]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        name=name,
        tag=tag,
        mode=mode,
        map_=map_,
        size=size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    affinity: str,
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
    mode: Union[Unset, MatchMode] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
) -> Optional[Union[MatchesV3ListResponse, SendError]]:
    """
    Args:
        affinity (str):
        name (str):
        tag (str):
        mode (Union[Unset, MatchMode]):
        map_ (Union[Unset, str]):
        size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MatchesV3ListResponse, SendError]
    """

    return sync_detailed(
        affinity=affinity,
        name=name,
        tag=tag,
        client=client,
        mode=mode,
        map_=map_,
        size=size,
    ).parsed


async def asyncio_detailed(
    affinity: str,
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
    mode: Union[Unset, MatchMode] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
) -> Response[Union[MatchesV3ListResponse, SendError]]:
    """
    Args:
        affinity (str):
        name (str):
        tag (str):
        mode (Union[Unset, MatchMode]):
        map_ (Union[Unset, str]):
        size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[MatchesV3ListResponse, SendError]]
    """

    kwargs = _get_kwargs(
        affinity=affinity,
        name=name,
        tag=tag,
        mode=mode,
        map_=map_,
        size=size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    affinity: str,
    name: str,
    tag: str,
    *,
    client: Union[AuthenticatedClient, Client],
    mode: Union[Unset, MatchMode] = UNSET,
    map_: Union[Unset, str] = UNSET,
    size: Union[Unset, int] = UNSET,
) -> Optional[Union[MatchesV3ListResponse, SendError]]:
    """
    Args:
        affinity (str):
        name (str):
        tag (str):
        mode (Union[Unset, MatchMode]):
        map_ (Union[Unset, str]):
        size (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[MatchesV3ListResponse, SendError]
    """

    return (
        await asyncio_detailed(
            affinity=affinity,
            name=name,
            tag=tag,
            client=client,
            mode=mode,
            map_=map_,
            size=size,
        )
    ).parsed
