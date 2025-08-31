from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PremierTeamV1ResponseDataCustomization")


@_attrs_define
class PremierTeamV1ResponseDataCustomization:
    """
    Attributes:
        icon (str):
        image (str):
        primary (str):
        secondary (str):
        tertiary (str):
    """

    icon: str
    image: str
    primary: str
    secondary: str
    tertiary: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icon = self.icon

        image = self.image

        primary = self.primary

        secondary = self.secondary

        tertiary = self.tertiary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icon": icon,
                "image": image,
                "primary": primary,
                "secondary": secondary,
                "tertiary": tertiary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        icon = d.pop("icon")

        image = d.pop("image")

        primary = d.pop("primary")

        secondary = d.pop("secondary")

        tertiary = d.pop("tertiary")

        premier_team_v1_response_data_customization = cls(
            icon=icon,
            image=image,
            primary=primary,
            secondary=secondary,
            tertiary=tertiary,
        )

        premier_team_v1_response_data_customization.additional_properties = d
        return premier_team_v1_response_data_customization

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
