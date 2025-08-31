from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LeaderboardPVPPlayer")


@_attrs_define
class LeaderboardPVPPlayer:
    """
    Attributes:
        is_anonymized (bool):
        is_banned (bool):
        player_card_id (str):
        title_id (str):
        competitive_tier (int):
        game_name (str):
        leaderboard_rank (int):
        number_of_wins (int):
        ranked_rating (int):
        tag_line (str):
        puuid (Union[None, Unset, str]):
    """

    is_anonymized: bool
    is_banned: bool
    player_card_id: str
    title_id: str
    competitive_tier: int
    game_name: str
    leaderboard_rank: int
    number_of_wins: int
    ranked_rating: int
    tag_line: str
    puuid: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_anonymized = self.is_anonymized

        is_banned = self.is_banned

        player_card_id = self.player_card_id

        title_id = self.title_id

        competitive_tier = self.competitive_tier

        game_name = self.game_name

        leaderboard_rank = self.leaderboard_rank

        number_of_wins = self.number_of_wins

        ranked_rating = self.ranked_rating

        tag_line = self.tag_line

        puuid: Union[None, Unset, str]
        if isinstance(self.puuid, Unset):
            puuid = UNSET
        else:
            puuid = self.puuid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "IsAnonymized": is_anonymized,
                "IsBanned": is_banned,
                "PlayerCardID": player_card_id,
                "TitleID": title_id,
                "competitiveTier": competitive_tier,
                "gameName": game_name,
                "leaderboardRank": leaderboard_rank,
                "numberOfWins": number_of_wins,
                "rankedRating": ranked_rating,
                "tagLine": tag_line,
            }
        )
        if puuid is not UNSET:
            field_dict["puuid"] = puuid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_anonymized = d.pop("IsAnonymized")

        is_banned = d.pop("IsBanned")

        player_card_id = d.pop("PlayerCardID")

        title_id = d.pop("TitleID")

        competitive_tier = d.pop("competitiveTier")

        game_name = d.pop("gameName")

        leaderboard_rank = d.pop("leaderboardRank")

        number_of_wins = d.pop("numberOfWins")

        ranked_rating = d.pop("rankedRating")

        tag_line = d.pop("tagLine")

        def _parse_puuid(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        puuid = _parse_puuid(d.pop("puuid", UNSET))

        leaderboard_pvp_player = cls(
            is_anonymized=is_anonymized,
            is_banned=is_banned,
            player_card_id=player_card_id,
            title_id=title_id,
            competitive_tier=competitive_tier,
            game_name=game_name,
            leaderboard_rank=leaderboard_rank,
            number_of_wins=number_of_wins,
            ranked_rating=ranked_rating,
            tag_line=tag_line,
            puuid=puuid,
        )

        leaderboard_pvp_player.additional_properties = d
        return leaderboard_pvp_player

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
