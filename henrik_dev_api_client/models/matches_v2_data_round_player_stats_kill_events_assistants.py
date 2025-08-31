from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV2DataRoundPlayerStatsKillEventsAssistants")


@_attrs_define
class MatchesV2DataRoundPlayerStatsKillEventsAssistants:
    """
    Attributes:
        assistant_display_name (str):
        assistant_puuid (str):
        assistant_team (str):
    """

    assistant_display_name: str
    assistant_puuid: str
    assistant_team: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistant_display_name = self.assistant_display_name

        assistant_puuid = self.assistant_puuid

        assistant_team = self.assistant_team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistant_display_name": assistant_display_name,
                "assistant_puuid": assistant_puuid,
                "assistant_team": assistant_team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        assistant_display_name = d.pop("assistant_display_name")

        assistant_puuid = d.pop("assistant_puuid")

        assistant_team = d.pop("assistant_team")

        matches_v2_data_round_player_stats_kill_events_assistants = cls(
            assistant_display_name=assistant_display_name,
            assistant_puuid=assistant_puuid,
            assistant_team=assistant_team,
        )

        matches_v2_data_round_player_stats_kill_events_assistants.additional_properties = d
        return matches_v2_data_round_player_stats_kill_events_assistants

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
