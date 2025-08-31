from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="EsportsV1DataLeague")


@_attrs_define
class EsportsV1DataLeague:
    """
    Attributes:
        icon (str):
        identifier (str):
        name (str):
        region (str):
    """

    icon: str
    identifier: str
    name: str
    region: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        icon = self.icon

        identifier = self.identifier

        name = self.name

        region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "icon": icon,
                "identifier": identifier,
                "name": name,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        icon = d.pop("icon")

        identifier = d.pop("identifier")

        name = d.pop("name")

        region = d.pop("region")

        esports_v1_data_league = cls(
            icon=icon,
            identifier=identifier,
            name=name,
            region=region,
        )

        esports_v1_data_league.additional_properties = d
        return esports_v1_data_league

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
