from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchesV4DataPlayerCustomization")


@_attrs_define
class MatchesV4DataPlayerCustomization:
    """
    Attributes:
        card (str):
        title (str):
        preferred_level_border (Union[None, Unset, str]):
    """

    card: str
    title: str
    preferred_level_border: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card = self.card

        title = self.title

        preferred_level_border: Union[None, Unset, str]
        if isinstance(self.preferred_level_border, Unset):
            preferred_level_border = UNSET
        else:
            preferred_level_border = self.preferred_level_border

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card": card,
                "title": title,
            }
        )
        if preferred_level_border is not UNSET:
            field_dict["preferred_level_border"] = preferred_level_border

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        card = d.pop("card")

        title = d.pop("title")

        def _parse_preferred_level_border(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        preferred_level_border = _parse_preferred_level_border(d.pop("preferred_level_border", UNSET))

        matches_v4_data_player_customization = cls(
            card=card,
            title=title,
            preferred_level_border=preferred_level_border,
        )

        matches_v4_data_player_customization.additional_properties = d
        return matches_v4_data_player_customization

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
