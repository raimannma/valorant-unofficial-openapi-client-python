from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MMRV2HighestRank")


@_attrs_define
class MMRV2HighestRank:
    """
    Attributes:
        old (bool):
        patched_tier (str):
        season (str):
        tier (int):
    """

    old: bool
    patched_tier: str
    season: str
    tier: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        old = self.old

        patched_tier = self.patched_tier

        season = self.season

        tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "old": old,
                "patched_tier": patched_tier,
                "season": season,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        old = d.pop("old")

        patched_tier = d.pop("patched_tier")

        season = d.pop("season")

        tier = d.pop("tier")

        mmrv2_highest_rank = cls(
            old=old,
            patched_tier=patched_tier,
            season=season,
            tier=tier,
        )

        mmrv2_highest_rank.additional_properties = d
        return mmrv2_highest_rank

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
