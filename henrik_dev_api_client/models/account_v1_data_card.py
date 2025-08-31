from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountV1DataCard")


@_attrs_define
class AccountV1DataCard:
    """
    Attributes:
        id (str):
        large (str):
        small (str):
        wide (str):
    """

    id: str
    large: str
    small: str
    wide: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        large = self.large

        small = self.small

        wide = self.wide

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "large": large,
                "small": small,
                "wide": wide,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        large = d.pop("large")

        small = d.pop("small")

        wide = d.pop("wide")

        account_v1_data_card = cls(
            id=id,
            large=large,
            small=small,
            wide=wide,
        )

        account_v1_data_card.additional_properties = d
        return account_v1_data_card

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
