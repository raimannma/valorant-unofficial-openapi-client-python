from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.raw_v1_error_data import RawV1ErrorData


T = TypeVar("T", bound="RawV1Response")


@_attrs_define
class RawV1Response:
    """
    Attributes:
        data (Union['RawV1ErrorData', Any, list[Any]]):
        status (int):
    """

    data: Union["RawV1ErrorData", Any, list[Any]]
    status: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.raw_v1_error_data import RawV1ErrorData

        data: Union[Any, dict[str, Any], list[Any]]
        if isinstance(self.data, list):
            data = self.data

        elif isinstance(self.data, RawV1ErrorData):
            data = self.data.to_dict()
        else:
            data = self.data

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
        from ..models.raw_v1_error_data import RawV1ErrorData

        d = dict(src_dict)

        def _parse_data(data: object) -> Union["RawV1ErrorData", Any, list[Any]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                componentsschemas_raw_v1_response_data_type_1 = cast(list[Any], data)

                return componentsschemas_raw_v1_response_data_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_raw_v1_response_data_type_2 = RawV1ErrorData.from_dict(data)

                return componentsschemas_raw_v1_response_data_type_2
            except:  # noqa: E722
                pass
            return cast(Union["RawV1ErrorData", Any, list[Any]], data)

        data = _parse_data(d.pop("data"))

        status = d.pop("status")

        raw_v1_response = cls(
            data=data,
            status=status,
        )

        raw_v1_response.additional_properties = d
        return raw_v1_response

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
