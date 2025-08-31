from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_platform_os import MatchesV2DataPlatformOs


T = TypeVar("T", bound="MatchesV2DataPlatform")


@_attrs_define
class MatchesV2DataPlatform:
    """
    Attributes:
        os (MatchesV2DataPlatformOs):
        type_ (str):
    """

    os: "MatchesV2DataPlatformOs"
    type_: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        os = self.os.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "os": os,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_platform_os import MatchesV2DataPlatformOs

        d = dict(src_dict)
        os = MatchesV2DataPlatformOs.from_dict(d.pop("os"))

        type_ = d.pop("type")

        matches_v2_data_platform = cls(
            os=os,
            type_=type_,
        )

        matches_v2_data_platform.additional_properties = d
        return matches_v2_data_platform

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
