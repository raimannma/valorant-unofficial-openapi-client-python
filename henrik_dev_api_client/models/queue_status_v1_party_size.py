from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueueStatusV1PartySize")


@_attrs_define
class QueueStatusV1PartySize:
    """
    Attributes:
        full_party_bypass (bool):
        invalid (list[int]):
        max_ (int):
        min_ (int):
    """

    full_party_bypass: bool
    invalid: list[int]
    max_: int
    min_: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_party_bypass = self.full_party_bypass

        invalid = self.invalid

        max_ = self.max_

        min_ = self.min_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "full_party_bypass": full_party_bypass,
                "invalid": invalid,
                "max": max_,
                "min": min_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        full_party_bypass = d.pop("full_party_bypass")

        invalid = cast(list[int], d.pop("invalid"))

        max_ = d.pop("max")

        min_ = d.pop("min")

        queue_status_v1_party_size = cls(
            full_party_bypass=full_party_bypass,
            invalid=invalid,
            max_=max_,
            min_=min_,
        )

        queue_status_v1_party_size.additional_properties = d
        return queue_status_v1_party_size

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
