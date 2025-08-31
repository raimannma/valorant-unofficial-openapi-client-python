from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data import MatchesV4Data


T = TypeVar("T", bound="MatchesV4Response")


@_attrs_define
class MatchesV4Response:
    """
    Attributes:
        data (MatchesV4Data):
        status (int):
    """

    data: "MatchesV4Data"
    status: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data import MatchesV4Data

        d = dict(src_dict)
        data = MatchesV4Data.from_dict(d.pop("data"))

        status = d.pop("status")

        matches_v4_response = cls(
            data=data,
            status=status,
        )

        matches_v4_response.additional_properties = d
        return matches_v4_response

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
