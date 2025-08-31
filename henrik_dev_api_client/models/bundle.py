from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bundle_item import BundleItem


T = TypeVar("T", bound="Bundle")


@_attrs_define
class Bundle:
    """
    Attributes:
        currency_id (str):
        data_asset_id (str):
        duration_remaining_in_seconds (int):
        id (str):
        items (list['BundleItem']):
        total_discount_percent (float):
        wholesale_only (bool):
    """

    currency_id: str
    data_asset_id: str
    duration_remaining_in_seconds: int
    id: str
    items: list["BundleItem"]
    total_discount_percent: float
    wholesale_only: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_id = self.currency_id

        data_asset_id = self.data_asset_id

        duration_remaining_in_seconds = self.duration_remaining_in_seconds

        id = self.id

        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total_discount_percent = self.total_discount_percent

        wholesale_only = self.wholesale_only

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "CurrencyID": currency_id,
                "DataAssetID": data_asset_id,
                "DurationRemainingInSeconds": duration_remaining_in_seconds,
                "ID": id,
                "Items": items,
                "TotalDiscountPercent": total_discount_percent,
                "WholesaleOnly": wholesale_only,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bundle_item import BundleItem

        d = dict(src_dict)
        currency_id = d.pop("CurrencyID")

        data_asset_id = d.pop("DataAssetID")

        duration_remaining_in_seconds = d.pop("DurationRemainingInSeconds")

        id = d.pop("ID")

        items = []
        _items = d.pop("Items")
        for items_item_data in _items:
            items_item = BundleItem.from_dict(items_item_data)

            items.append(items_item)

        total_discount_percent = d.pop("TotalDiscountPercent")

        wholesale_only = d.pop("WholesaleOnly")

        bundle = cls(
            currency_id=currency_id,
            data_asset_id=data_asset_id,
            duration_remaining_in_seconds=duration_remaining_in_seconds,
            id=id,
            items=items,
            total_discount_percent=total_discount_percent,
            wholesale_only=wholesale_only,
        )

        bundle.additional_properties = d
        return bundle

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
