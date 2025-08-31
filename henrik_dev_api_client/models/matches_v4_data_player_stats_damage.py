from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV4DataPlayerStatsDamage")


@_attrs_define
class MatchesV4DataPlayerStatsDamage:
    """
    Attributes:
        dealt (int):
        received (int):
    """

    dealt: int
    received: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dealt = self.dealt

        received = self.received

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dealt": dealt,
                "received": received,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dealt = d.pop("dealt")

        received = d.pop("received")

        matches_v4_data_player_stats_damage = cls(
            dealt=dealt,
            received=received,
        )

        matches_v4_data_player_stats_damage.additional_properties = d
        return matches_v4_data_player_stats_damage

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
