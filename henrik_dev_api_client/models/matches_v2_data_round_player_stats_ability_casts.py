from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchesV2DataRoundPlayerStatsAbilityCasts")


@_attrs_define
class MatchesV2DataRoundPlayerStatsAbilityCasts:
    """
    Attributes:
        c_casts (Union[None, Unset, int]):
        e_casts (Union[None, Unset, int]):
        q_casts (Union[None, Unset, int]):
        x_casts (Union[None, Unset, int]):
    """

    c_casts: Union[None, Unset, int] = UNSET
    e_casts: Union[None, Unset, int] = UNSET
    q_casts: Union[None, Unset, int] = UNSET
    x_casts: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        c_casts: Union[None, Unset, int]
        if isinstance(self.c_casts, Unset):
            c_casts = UNSET
        else:
            c_casts = self.c_casts

        e_casts: Union[None, Unset, int]
        if isinstance(self.e_casts, Unset):
            e_casts = UNSET
        else:
            e_casts = self.e_casts

        q_casts: Union[None, Unset, int]
        if isinstance(self.q_casts, Unset):
            q_casts = UNSET
        else:
            q_casts = self.q_casts

        x_casts: Union[None, Unset, int]
        if isinstance(self.x_casts, Unset):
            x_casts = UNSET
        else:
            x_casts = self.x_casts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if c_casts is not UNSET:
            field_dict["c_casts"] = c_casts
        if e_casts is not UNSET:
            field_dict["e_casts"] = e_casts
        if q_casts is not UNSET:
            field_dict["q_casts"] = q_casts
        if x_casts is not UNSET:
            field_dict["x_casts"] = x_casts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_c_casts(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        c_casts = _parse_c_casts(d.pop("c_casts", UNSET))

        def _parse_e_casts(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        e_casts = _parse_e_casts(d.pop("e_casts", UNSET))

        def _parse_q_casts(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        q_casts = _parse_q_casts(d.pop("q_casts", UNSET))

        def _parse_x_casts(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        x_casts = _parse_x_casts(d.pop("x_casts", UNSET))

        matches_v2_data_round_player_stats_ability_casts = cls(
            c_casts=c_casts,
            e_casts=e_casts,
            q_casts=q_casts,
            x_casts=x_casts,
        )

        matches_v2_data_round_player_stats_ability_casts.additional_properties = d
        return matches_v2_data_round_player_stats_ability_casts

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
