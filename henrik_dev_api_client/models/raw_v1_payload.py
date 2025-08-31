from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawV1Payload")


@_attrs_define
class RawV1Payload:
    """
    Attributes:
        region (str):
        type_ (str):
        value (Union[list[str], str]):
        platform (Union[None, Unset, str]):
        queries (Union[None, Unset, str]):
    """

    region: str
    type_: str
    value: Union[list[str], str]
    platform: Union[None, Unset, str] = UNSET
    queries: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        region = self.region

        type_ = self.type_

        value: Union[list[str], str]
        if isinstance(self.value, list):
            value = self.value

        else:
            value = self.value

        platform: Union[None, Unset, str]
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        queries: Union[None, Unset, str]
        if isinstance(self.queries, Unset):
            queries = UNSET
        else:
            queries = self.queries

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "region": region,
                "type": type_,
                "value": value,
            }
        )
        if platform is not UNSET:
            field_dict["platform"] = platform
        if queries is not UNSET:
            field_dict["queries"] = queries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        region = d.pop("region")

        type_ = d.pop("type")

        def _parse_value(data: object) -> Union[list[str], str]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_raw_v1_payload_values_type_1 = cast(list[str], data)

                return componentsschemas_raw_v1_payload_values_type_1
            except:  # noqa: E722
                pass
            return cast(Union[list[str], str], data)

        value = _parse_value(d.pop("value"))

        def _parse_platform(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        platform = _parse_platform(d.pop("platform", UNSET))

        def _parse_queries(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        queries = _parse_queries(d.pop("queries", UNSET))

        raw_v1_payload = cls(
            region=region,
            type_=type_,
            value=value,
            platform=platform,
            queries=queries,
        )

        raw_v1_payload.additional_properties = d
        return raw_v1_payload

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
