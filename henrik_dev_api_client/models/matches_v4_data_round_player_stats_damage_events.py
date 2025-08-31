from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer


T = TypeVar("T", bound="MatchesV4DataRoundPlayerStatsDamageEvents")


@_attrs_define
class MatchesV4DataRoundPlayerStatsDamageEvents:
    """
    Attributes:
        bodyshots (int):
        damage (int):
        headshots (int):
        legshots (int):
        player (MatchesV4DataRoundPlayer):
    """

    bodyshots: int
    damage: int
    headshots: int
    legshots: int
    player: "MatchesV4DataRoundPlayer"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bodyshots = self.bodyshots

        damage = self.damage

        headshots = self.headshots

        legshots = self.legshots

        player = self.player.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bodyshots": bodyshots,
                "damage": damage,
                "headshots": headshots,
                "legshots": legshots,
                "player": player,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer

        d = dict(src_dict)
        bodyshots = d.pop("bodyshots")

        damage = d.pop("damage")

        headshots = d.pop("headshots")

        legshots = d.pop("legshots")

        player = MatchesV4DataRoundPlayer.from_dict(d.pop("player"))

        matches_v4_data_round_player_stats_damage_events = cls(
            bodyshots=bodyshots,
            damage=damage,
            headshots=headshots,
            legshots=legshots,
            player=player,
        )

        matches_v4_data_round_player_stats_damage_events.additional_properties = d
        return matches_v4_data_round_player_stats_damage_events

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
