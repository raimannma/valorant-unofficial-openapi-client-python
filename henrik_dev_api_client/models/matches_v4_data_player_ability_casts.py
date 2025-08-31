from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchesV4DataPlayerAbilityCasts")


@_attrs_define
class MatchesV4DataPlayerAbilityCasts:
    """
    Attributes:
        ability1 (Union[None, Unset, int]):
        ability2 (Union[None, Unset, int]):
        grenade (Union[None, Unset, int]):
        ultimate (Union[None, Unset, int]):
    """

    ability1: Union[None, Unset, int] = UNSET
    ability2: Union[None, Unset, int] = UNSET
    grenade: Union[None, Unset, int] = UNSET
    ultimate: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ability1: Union[None, Unset, int]
        if isinstance(self.ability1, Unset):
            ability1 = UNSET
        else:
            ability1 = self.ability1

        ability2: Union[None, Unset, int]
        if isinstance(self.ability2, Unset):
            ability2 = UNSET
        else:
            ability2 = self.ability2

        grenade: Union[None, Unset, int]
        if isinstance(self.grenade, Unset):
            grenade = UNSET
        else:
            grenade = self.grenade

        ultimate: Union[None, Unset, int]
        if isinstance(self.ultimate, Unset):
            ultimate = UNSET
        else:
            ultimate = self.ultimate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ability1 is not UNSET:
            field_dict["ability1"] = ability1
        if ability2 is not UNSET:
            field_dict["ability2"] = ability2
        if grenade is not UNSET:
            field_dict["grenade"] = grenade
        if ultimate is not UNSET:
            field_dict["ultimate"] = ultimate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_ability1(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ability1 = _parse_ability1(d.pop("ability1", UNSET))

        def _parse_ability2(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ability2 = _parse_ability2(d.pop("ability2", UNSET))

        def _parse_grenade(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        grenade = _parse_grenade(d.pop("grenade", UNSET))

        def _parse_ultimate(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ultimate = _parse_ultimate(d.pop("ultimate", UNSET))

        matches_v4_data_player_ability_casts = cls(
            ability1=ability1,
            ability2=ability2,
            grenade=grenade,
            ultimate=ultimate,
        )

        matches_v4_data_player_ability_casts.additional_properties = d
        return matches_v4_data_player_ability_casts

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
