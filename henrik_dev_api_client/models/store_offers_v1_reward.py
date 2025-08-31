from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StoreOffersV1Reward")


@_attrs_define
class StoreOffersV1Reward:
    """
    Attributes:
        item_id (str):
        item_type_id (str):
        quantity (int):
    """

    item_id: str
    item_type_id: str
    quantity: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        item_id = self.item_id

        item_type_id = self.item_type_id

        quantity = self.quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ItemID": item_id,
                "ItemTypeID": item_type_id,
                "Quantity": quantity,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        item_id = d.pop("ItemID")

        item_type_id = d.pop("ItemTypeID")

        quantity = d.pop("Quantity")

        store_offers_v1_reward = cls(
            item_id=item_id,
            item_type_id=item_type_id,
            quantity=quantity,
        )

        store_offers_v1_reward.additional_properties = d
        return store_offers_v1_reward

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
