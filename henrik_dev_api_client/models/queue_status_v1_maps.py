from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.queue_status_v1_map import QueueStatusV1Map


T = TypeVar("T", bound="QueueStatusV1Maps")


@_attrs_define
class QueueStatusV1Maps:
    """
    Attributes:
        enabled (bool):
        map_ (QueueStatusV1Map):
    """

    enabled: bool
    map_: "QueueStatusV1Map"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        map_ = self.map_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "map": map_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queue_status_v1_map import QueueStatusV1Map

        d = dict(src_dict)
        enabled = d.pop("enabled")

        map_ = QueueStatusV1Map.from_dict(d.pop("map"))

        queue_status_v1_maps = cls(
            enabled=enabled,
            map_=map_,
        )

        queue_status_v1_maps.additional_properties = d
        return queue_status_v1_maps

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
