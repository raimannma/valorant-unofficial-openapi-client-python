from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data_player_behavior_friendly_fire import MatchesV4DataPlayerBehaviorFriendlyFire


T = TypeVar("T", bound="MatchesV4DataPlayerBehavior")


@_attrs_define
class MatchesV4DataPlayerBehavior:
    """
    Attributes:
        afk_rounds (float):
        friendly_fire (MatchesV4DataPlayerBehaviorFriendlyFire):
        rounds_in_spawn (float):
    """

    afk_rounds: float
    friendly_fire: "MatchesV4DataPlayerBehaviorFriendlyFire"
    rounds_in_spawn: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        afk_rounds = self.afk_rounds

        friendly_fire = self.friendly_fire.to_dict()

        rounds_in_spawn = self.rounds_in_spawn

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "afk_rounds": afk_rounds,
                "friendly_fire": friendly_fire,
                "rounds_in_spawn": rounds_in_spawn,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_player_behavior_friendly_fire import MatchesV4DataPlayerBehaviorFriendlyFire

        d = dict(src_dict)
        afk_rounds = d.pop("afk_rounds")

        friendly_fire = MatchesV4DataPlayerBehaviorFriendlyFire.from_dict(d.pop("friendly_fire"))

        rounds_in_spawn = d.pop("rounds_in_spawn")

        matches_v4_data_player_behavior = cls(
            afk_rounds=afk_rounds,
            friendly_fire=friendly_fire,
            rounds_in_spawn=rounds_in_spawn,
        )

        matches_v4_data_player_behavior.additional_properties = d
        return matches_v4_data_player_behavior

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
