from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV4DataPlayerBehaviorFriendlyFire")


@_attrs_define
class MatchesV4DataPlayerBehaviorFriendlyFire:
    """
    Attributes:
        incoming (float):
        outgoing (float):
    """

    incoming: float
    outgoing: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incoming = self.incoming

        outgoing = self.outgoing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incoming": incoming,
                "outgoing": outgoing,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        incoming = d.pop("incoming")

        outgoing = d.pop("outgoing")

        matches_v4_data_player_behavior_friendly_fire = cls(
            incoming=incoming,
            outgoing=outgoing,
        )

        matches_v4_data_player_behavior_friendly_fire.additional_properties = d
        return matches_v4_data_player_behavior_friendly_fire

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
