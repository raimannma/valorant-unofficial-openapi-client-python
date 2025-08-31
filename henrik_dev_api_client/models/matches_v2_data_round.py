from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_round_defuse_events import MatchesV2DataRoundDefuseEvents
    from ..models.matches_v2_data_round_plant_events import MatchesV2DataRoundPlantEvents
    from ..models.matches_v2_data_round_player_stats import MatchesV2DataRoundPlayerStats


T = TypeVar("T", bound="MatchesV2DataRound")


@_attrs_define
class MatchesV2DataRound:
    """
    Attributes:
        bomb_defused (bool):
        bomb_planted (bool):
        defuse_events (MatchesV2DataRoundDefuseEvents):
        end_type (str):
        plant_events (MatchesV2DataRoundPlantEvents):
        player_stats (list['MatchesV2DataRoundPlayerStats']):
        winning_team (str):
    """

    bomb_defused: bool
    bomb_planted: bool
    defuse_events: "MatchesV2DataRoundDefuseEvents"
    end_type: str
    plant_events: "MatchesV2DataRoundPlantEvents"
    player_stats: list["MatchesV2DataRoundPlayerStats"]
    winning_team: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bomb_defused = self.bomb_defused

        bomb_planted = self.bomb_planted

        defuse_events = self.defuse_events.to_dict()

        end_type = self.end_type

        plant_events = self.plant_events.to_dict()

        player_stats = []
        for player_stats_item_data in self.player_stats:
            player_stats_item = player_stats_item_data.to_dict()
            player_stats.append(player_stats_item)

        winning_team = self.winning_team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bomb_defused": bomb_defused,
                "bomb_planted": bomb_planted,
                "defuse_events": defuse_events,
                "end_type": end_type,
                "plant_events": plant_events,
                "player_stats": player_stats,
                "winning_team": winning_team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_round_defuse_events import MatchesV2DataRoundDefuseEvents
        from ..models.matches_v2_data_round_plant_events import MatchesV2DataRoundPlantEvents
        from ..models.matches_v2_data_round_player_stats import MatchesV2DataRoundPlayerStats

        d = dict(src_dict)
        bomb_defused = d.pop("bomb_defused")

        bomb_planted = d.pop("bomb_planted")

        defuse_events = MatchesV2DataRoundDefuseEvents.from_dict(d.pop("defuse_events"))

        end_type = d.pop("end_type")

        plant_events = MatchesV2DataRoundPlantEvents.from_dict(d.pop("plant_events"))

        player_stats = []
        _player_stats = d.pop("player_stats")
        for player_stats_item_data in _player_stats:
            player_stats_item = MatchesV2DataRoundPlayerStats.from_dict(player_stats_item_data)

            player_stats.append(player_stats_item)

        winning_team = d.pop("winning_team")

        matches_v2_data_round = cls(
            bomb_defused=bomb_defused,
            bomb_planted=bomb_planted,
            defuse_events=defuse_events,
            end_type=end_type,
            plant_events=plant_events,
            player_stats=player_stats,
            winning_team=winning_team,
        )

        matches_v2_data_round.additional_properties = d
        return matches_v2_data_round

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
