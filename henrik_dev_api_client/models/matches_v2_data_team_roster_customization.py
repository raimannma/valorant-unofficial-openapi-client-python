from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV2DataTeamRosterCustomization")


@_attrs_define
class MatchesV2DataTeamRosterCustomization:
    """
    Attributes:
        icon (str):
        image (str):
        primary_color (str):
        secondary_color (str):
        tertiary_color (str):
    """

    icon: str
    image: str
    primary_color: str
    secondary_color: str
    tertiary_color: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icon = self.icon

        image = self.image

        primary_color = self.primary_color

        secondary_color = self.secondary_color

        tertiary_color = self.tertiary_color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icon": icon,
                "image": image,
                "primary_color": primary_color,
                "secondary_color": secondary_color,
                "tertiary_color": tertiary_color,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        icon = d.pop("icon")

        image = d.pop("image")

        primary_color = d.pop("primary_color")

        secondary_color = d.pop("secondary_color")

        tertiary_color = d.pop("tertiary_color")

        matches_v2_data_team_roster_customization = cls(
            icon=icon,
            image=image,
            primary_color=primary_color,
            secondary_color=secondary_color,
            tertiary_color=tertiary_color,
        )

        matches_v2_data_team_roster_customization.additional_properties = d
        return matches_v2_data_team_roster_customization

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
