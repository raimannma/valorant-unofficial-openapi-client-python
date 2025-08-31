from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueueStatusV1HighSkill")


@_attrs_define
class QueueStatusV1HighSkill:
    """
    Attributes:
        max_party_size (int):
        max_tier (int):
        min_tier (int):
    """

    max_party_size: int
    max_tier: int
    min_tier: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_party_size = self.max_party_size

        max_tier = self.max_tier

        min_tier = self.min_tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_party_size": max_party_size,
                "max_tier": max_tier,
                "min_tier": min_tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_party_size = d.pop("max_party_size")

        max_tier = d.pop("max_tier")

        min_tier = d.pop("min_tier")

        queue_status_v1_high_skill = cls(
            max_party_size=max_party_size,
            max_tier=max_tier,
            min_tier=min_tier,
        )

        queue_status_v1_high_skill.additional_properties = d
        return queue_status_v1_high_skill

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
