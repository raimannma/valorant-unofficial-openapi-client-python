from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leaderboard_pvp_player import LeaderboardPVPPlayer


T = TypeVar("T", bound="LeaderboardV2Response")


@_attrs_define
class LeaderboardV2Response:
    """
    Attributes:
        immortal_1_threshold (int):
        immortal_2_threshold (int):
        immortal_3_threshold (int):
        last_update (int):
        next_update (int):
        players (list['LeaderboardPVPPlayer']):
        radiant_threshold (int):
        total_players (int):
    """

    immortal_1_threshold: int
    immortal_2_threshold: int
    immortal_3_threshold: int
    last_update: int
    next_update: int
    players: list["LeaderboardPVPPlayer"]
    radiant_threshold: int
    total_players: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        immortal_1_threshold = self.immortal_1_threshold

        immortal_2_threshold = self.immortal_2_threshold

        immortal_3_threshold = self.immortal_3_threshold

        last_update = self.last_update

        next_update = self.next_update

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        radiant_threshold = self.radiant_threshold

        total_players = self.total_players

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "immortal_1_threshold": immortal_1_threshold,
                "immortal_2_threshold": immortal_2_threshold,
                "immortal_3_threshold": immortal_3_threshold,
                "last_update": last_update,
                "next_update": next_update,
                "players": players,
                "radiant_threshold": radiant_threshold,
                "total_players": total_players,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_pvp_player import LeaderboardPVPPlayer

        d = dict(src_dict)
        immortal_1_threshold = d.pop("immortal_1_threshold")

        immortal_2_threshold = d.pop("immortal_2_threshold")

        immortal_3_threshold = d.pop("immortal_3_threshold")

        last_update = d.pop("last_update")

        next_update = d.pop("next_update")

        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = LeaderboardPVPPlayer.from_dict(players_item_data)

            players.append(players_item)

        radiant_threshold = d.pop("radiant_threshold")

        total_players = d.pop("total_players")

        leaderboard_v2_response = cls(
            immortal_1_threshold=immortal_1_threshold,
            immortal_2_threshold=immortal_2_threshold,
            immortal_3_threshold=immortal_3_threshold,
            last_update=last_update,
            next_update=next_update,
            players=players,
            radiant_threshold=radiant_threshold,
            total_players=total_players,
        )

        leaderboard_v2_response.additional_properties = d
        return leaderboard_v2_response

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
