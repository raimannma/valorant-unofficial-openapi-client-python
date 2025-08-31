from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV2DataRoundPlayerStatsDamageEvents")


@_attrs_define
class MatchesV2DataRoundPlayerStatsDamageEvents:
    """
    Attributes:
        bodyshots (int):
        damage (int):
        headshots (int):
        legshots (int):
        receiver_display_name (str):
        receiver_puuid (str):
        receiver_team (str):
    """

    bodyshots: int
    damage: int
    headshots: int
    legshots: int
    receiver_display_name: str
    receiver_puuid: str
    receiver_team: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bodyshots = self.bodyshots

        damage = self.damage

        headshots = self.headshots

        legshots = self.legshots

        receiver_display_name = self.receiver_display_name

        receiver_puuid = self.receiver_puuid

        receiver_team = self.receiver_team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bodyshots": bodyshots,
                "damage": damage,
                "headshots": headshots,
                "legshots": legshots,
                "receiver_display_name": receiver_display_name,
                "receiver_puuid": receiver_puuid,
                "receiver_team": receiver_team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bodyshots = d.pop("bodyshots")

        damage = d.pop("damage")

        headshots = d.pop("headshots")

        legshots = d.pop("legshots")

        receiver_display_name = d.pop("receiver_display_name")

        receiver_puuid = d.pop("receiver_puuid")

        receiver_team = d.pop("receiver_team")

        matches_v2_data_round_player_stats_damage_events = cls(
            bodyshots=bodyshots,
            damage=damage,
            headshots=headshots,
            legshots=legshots,
            receiver_display_name=receiver_display_name,
            receiver_puuid=receiver_puuid,
            receiver_team=receiver_team,
        )

        matches_v2_data_round_player_stats_damage_events.additional_properties = d
        return matches_v2_data_round_player_stats_damage_events

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
