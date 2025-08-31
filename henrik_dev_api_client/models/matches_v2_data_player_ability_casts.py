from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchesV2DataPlayerAbilityCasts")


@_attrs_define
class MatchesV2DataPlayerAbilityCasts:
    """
    Attributes:
        c_cast (Union[None, Unset, int]):
        e_cast (Union[None, Unset, int]):
        q_cast (Union[None, Unset, int]):
        x_cast (Union[None, Unset, int]):
    """

    c_cast: Union[None, Unset, int] = UNSET
    e_cast: Union[None, Unset, int] = UNSET
    q_cast: Union[None, Unset, int] = UNSET
    x_cast: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        c_cast: Union[None, Unset, int]
        if isinstance(self.c_cast, Unset):
            c_cast = UNSET
        else:
            c_cast = self.c_cast

        e_cast: Union[None, Unset, int]
        if isinstance(self.e_cast, Unset):
            e_cast = UNSET
        else:
            e_cast = self.e_cast

        q_cast: Union[None, Unset, int]
        if isinstance(self.q_cast, Unset):
            q_cast = UNSET
        else:
            q_cast = self.q_cast

        x_cast: Union[None, Unset, int]
        if isinstance(self.x_cast, Unset):
            x_cast = UNSET
        else:
            x_cast = self.x_cast

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if c_cast is not UNSET:
            field_dict["c_cast"] = c_cast
        if e_cast is not UNSET:
            field_dict["e_cast"] = e_cast
        if q_cast is not UNSET:
            field_dict["q_cast"] = q_cast
        if x_cast is not UNSET:
            field_dict["x_cast"] = x_cast

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_c_cast(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        c_cast = _parse_c_cast(d.pop("c_cast", UNSET))

        def _parse_e_cast(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        e_cast = _parse_e_cast(d.pop("e_cast", UNSET))

        def _parse_q_cast(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        q_cast = _parse_q_cast(d.pop("q_cast", UNSET))

        def _parse_x_cast(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        x_cast = _parse_x_cast(d.pop("x_cast", UNSET))

        matches_v2_data_player_ability_casts = cls(
            c_cast=c_cast,
            e_cast=e_cast,
            q_cast=q_cast,
            x_cast=x_cast,
        )

        matches_v2_data_player_ability_casts.additional_properties = d
        return matches_v2_data_player_ability_casts

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
