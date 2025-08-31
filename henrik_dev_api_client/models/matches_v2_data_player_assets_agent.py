from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV2DataPlayerAssetsAgent")


@_attrs_define
class MatchesV2DataPlayerAssetsAgent:
    """
    Attributes:
        bust (str):
        full (str):
        killfeed (str):
        small (str):
    """

    bust: str
    full: str
    killfeed: str
    small: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bust = self.bust

        full = self.full

        killfeed = self.killfeed

        small = self.small

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bust": bust,
                "full": full,
                "killfeed": killfeed,
                "small": small,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bust = d.pop("bust")

        full = d.pop("full")

        killfeed = d.pop("killfeed")

        small = d.pop("small")

        matches_v2_data_player_assets_agent = cls(
            bust=bust,
            full=full,
            killfeed=killfeed,
            small=small,
        )

        matches_v2_data_player_assets_agent.additional_properties = d
        return matches_v2_data_player_assets_agent

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
