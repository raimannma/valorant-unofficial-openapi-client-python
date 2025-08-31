from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchesV2DataRoundPlayerStatsKillEventsAssets")


@_attrs_define
class MatchesV2DataRoundPlayerStatsKillEventsAssets:
    """
    Attributes:
        display_icon (Union[None, Unset, str]):
        killfeed_icon (Union[None, Unset, str]):
    """

    display_icon: Union[None, Unset, str] = UNSET
    killfeed_icon: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        display_icon: Union[None, Unset, str]
        if isinstance(self.display_icon, Unset):
            display_icon = UNSET
        else:
            display_icon = self.display_icon

        killfeed_icon: Union[None, Unset, str]
        if isinstance(self.killfeed_icon, Unset):
            killfeed_icon = UNSET
        else:
            killfeed_icon = self.killfeed_icon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_icon is not UNSET:
            field_dict["display_icon"] = display_icon
        if killfeed_icon is not UNSET:
            field_dict["killfeed_icon"] = killfeed_icon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_display_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        display_icon = _parse_display_icon(d.pop("display_icon", UNSET))

        def _parse_killfeed_icon(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        killfeed_icon = _parse_killfeed_icon(d.pop("killfeed_icon", UNSET))

        matches_v2_data_round_player_stats_kill_events_assets = cls(
            display_icon=display_icon,
            killfeed_icon=killfeed_icon,
        )

        matches_v2_data_round_player_stats_kill_events_assets.additional_properties = d
        return matches_v2_data_round_player_stats_kill_events_assets

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
