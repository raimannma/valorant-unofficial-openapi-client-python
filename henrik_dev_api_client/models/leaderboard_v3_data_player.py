from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderboardV3DataPlayer")


@_attrs_define
class LeaderboardV3DataPlayer:
    """
    Attributes:
        card (str):
        is_anonymized (bool):
        is_banned (bool):
        leaderboard_rank (int):
        name (str):
        rr (int):
        tag (str):
        tier (int):
        title (str):
        updated_at (str):
        wins (int):
        puuid (Union[None, Unset, str]):
    """

    card: str
    is_anonymized: bool
    is_banned: bool
    leaderboard_rank: int
    name: str
    rr: int
    tag: str
    tier: int
    title: str
    updated_at: str
    wins: int
    puuid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card = self.card

        is_anonymized = self.is_anonymized

        is_banned = self.is_banned

        leaderboard_rank = self.leaderboard_rank

        name = self.name

        rr = self.rr

        tag = self.tag

        tier = self.tier

        title = self.title

        updated_at = self.updated_at

        wins = self.wins

        puuid: Union[None, Unset, str]
        if isinstance(self.puuid, Unset):
            puuid = UNSET
        else:
            puuid = self.puuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card": card,
                "is_anonymized": is_anonymized,
                "is_banned": is_banned,
                "leaderboard_rank": leaderboard_rank,
                "name": name,
                "rr": rr,
                "tag": tag,
                "tier": tier,
                "title": title,
                "updated_at": updated_at,
                "wins": wins,
            }
        )
        if puuid is not UNSET:
            field_dict["puuid"] = puuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card = d.pop("card")

        is_anonymized = d.pop("is_anonymized")

        is_banned = d.pop("is_banned")

        leaderboard_rank = d.pop("leaderboard_rank")

        name = d.pop("name")

        rr = d.pop("rr")

        tag = d.pop("tag")

        tier = d.pop("tier")

        title = d.pop("title")

        updated_at = d.pop("updated_at")

        wins = d.pop("wins")

        def _parse_puuid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        puuid = _parse_puuid(d.pop("puuid", UNSET))

        leaderboard_v3_data_player = cls(
            card=card,
            is_anonymized=is_anonymized,
            is_banned=is_banned,
            leaderboard_rank=leaderboard_rank,
            name=name,
            rr=rr,
            tag=tag,
            tier=tier,
            title=title,
            updated_at=updated_at,
            wins=wins,
            puuid=puuid,
        )

        leaderboard_v3_data_player.additional_properties = d
        return leaderboard_v3_data_player

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
