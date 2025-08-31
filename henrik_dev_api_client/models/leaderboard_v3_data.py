from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leaderboard_v3_data_player import LeaderboardV3DataPlayer
    from ..models.leaderboard_v3_data_threshold import LeaderboardV3DataThreshold


T = TypeVar("T", bound="LeaderboardV3Data")


@_attrs_define
class LeaderboardV3Data:
    """
    Attributes:
        players (list['LeaderboardV3DataPlayer']):
        thresholds (list['LeaderboardV3DataThreshold']):
        updated_at (str):
    """

    players: list["LeaderboardV3DataPlayer"]
    thresholds: list["LeaderboardV3DataThreshold"]
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        thresholds = []
        for thresholds_item_data in self.thresholds:
            thresholds_item = thresholds_item_data.to_dict()
            thresholds.append(thresholds_item)

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "players": players,
                "thresholds": thresholds,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_v3_data_player import LeaderboardV3DataPlayer
        from ..models.leaderboard_v3_data_threshold import LeaderboardV3DataThreshold

        d = dict(src_dict)
        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = LeaderboardV3DataPlayer.from_dict(players_item_data)

            players.append(players_item)

        thresholds = []
        _thresholds = d.pop("thresholds")
        for thresholds_item_data in _thresholds:
            thresholds_item = LeaderboardV3DataThreshold.from_dict(thresholds_item_data)

            thresholds.append(thresholds_item)

        updated_at = d.pop("updated_at")

        leaderboard_v3_data = cls(
            players=players,
            thresholds=thresholds,
            updated_at=updated_at,
        )

        leaderboard_v3_data.additional_properties = d
        return leaderboard_v3_data

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
