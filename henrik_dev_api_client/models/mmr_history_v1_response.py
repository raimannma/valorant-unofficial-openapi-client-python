from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mmr_history_v1_data import MMRHistoryV1Data


T = TypeVar("T", bound="MMRHistoryV1Response")


@_attrs_define
class MMRHistoryV1Response:
    """
    Attributes:
        data (list['MMRHistoryV1Data']):
        name (str):
        status (int):
        tag (str):
    """

    data: list["MMRHistoryV1Data"]
    name: str
    status: int
    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        name = self.name

        status = self.status

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "name": name,
                "status": status,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mmr_history_v1_data import MMRHistoryV1Data

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = MMRHistoryV1Data.from_dict(data_item_data)

            data.append(data_item)

        name = d.pop("name")

        status = d.pop("status")

        tag = d.pop("tag")

        mmr_history_v1_response = cls(
            data=data,
            name=name,
            status=status,
            tag=tag,
        )

        mmr_history_v1_response.additional_properties = d
        return mmr_history_v1_response

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
