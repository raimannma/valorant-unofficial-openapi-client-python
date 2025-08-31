from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="VersionV1Data")


@_attrs_define
class VersionV1Data:
    """
    Attributes:
        branch (str):
        build_date (str):
        build_ver (str):
        last_checked (str):
        region (str):
        version (int):
        version_for_api (str):
    """

    branch: str
    build_date: str
    build_ver: str
    last_checked: str
    region: str
    version: int
    version_for_api: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        branch = self.branch

        build_date = self.build_date

        build_ver = self.build_ver

        last_checked = self.last_checked

        region = self.region

        version = self.version

        version_for_api = self.version_for_api

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "branch": branch,
                "build_date": build_date,
                "build_ver": build_ver,
                "last_checked": last_checked,
                "region": region,
                "version": version,
                "version_for_api": version_for_api,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        branch = d.pop("branch")

        build_date = d.pop("build_date")

        build_ver = d.pop("build_ver")

        last_checked = d.pop("last_checked")

        region = d.pop("region")

        version = d.pop("version")

        version_for_api = d.pop("version_for_api")

        version_v1_data = cls(
            branch=branch,
            build_date=build_date,
            build_ver=build_ver,
            last_checked=last_checked,
            region=region,
            version=version,
            version_for_api=version_for_api,
        )

        version_v1_data.additional_properties = d
        return version_v1_data

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
