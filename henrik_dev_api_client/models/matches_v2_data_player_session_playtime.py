from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV2DataPlayerSessionPlaytime")


@_attrs_define
class MatchesV2DataPlayerSessionPlaytime:
    """
    Attributes:
        milliseconds (int):
        minutes (int):
        seconds (int):
    """

    milliseconds: int
    minutes: int
    seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        milliseconds = self.milliseconds

        minutes = self.minutes

        seconds = self.seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "milliseconds": milliseconds,
                "minutes": minutes,
                "seconds": seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        milliseconds = d.pop("milliseconds")

        minutes = d.pop("minutes")

        seconds = d.pop("seconds")

        matches_v2_data_player_session_playtime = cls(
            milliseconds=milliseconds,
            minutes=minutes,
            seconds=seconds,
        )

        matches_v2_data_player_session_playtime.additional_properties = d
        return matches_v2_data_player_session_playtime

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
