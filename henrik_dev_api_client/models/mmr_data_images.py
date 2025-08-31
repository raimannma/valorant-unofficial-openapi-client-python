from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MMRDataImages")


@_attrs_define
class MMRDataImages:
    """
    Attributes:
        large (str):
        small (str):
        triangle_down (str):
        triangle_up (str):
    """

    large: str
    small: str
    triangle_down: str
    triangle_up: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        large = self.large

        small = self.small

        triangle_down = self.triangle_down

        triangle_up = self.triangle_up

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "large": large,
                "small": small,
                "triangle_down": triangle_down,
                "triangle_up": triangle_up,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        large = d.pop("large")

        small = d.pop("small")

        triangle_down = d.pop("triangle_down")

        triangle_up = d.pop("triangle_up")

        mmr_data_images = cls(
            large=large,
            small=small,
            triangle_down=triangle_down,
            triangle_up=triangle_up,
        )

        mmr_data_images.additional_properties = d
        return mmr_data_images

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
