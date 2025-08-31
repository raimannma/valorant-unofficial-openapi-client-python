from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.item import Item


T = TypeVar("T", bound="BundleItem")


@_attrs_define
class BundleItem:
    """
    Attributes:
        base_price (int):
        currency_id (str):
        discount_percent (float):
        discounted_price (float):
        is_promo_item (bool):
        item (Item):
    """

    base_price: int
    currency_id: str
    discount_percent: float
    discounted_price: float
    is_promo_item: bool
    item: "Item"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_price = self.base_price

        currency_id = self.currency_id

        discount_percent = self.discount_percent

        discounted_price = self.discounted_price

        is_promo_item = self.is_promo_item

        item = self.item.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "BasePrice": base_price,
                "CurrencyID": currency_id,
                "DiscountPercent": discount_percent,
                "DiscountedPrice": discounted_price,
                "IsPromoItem": is_promo_item,
                "Item": item,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item import Item

        d = dict(src_dict)
        base_price = d.pop("BasePrice")

        currency_id = d.pop("CurrencyID")

        discount_percent = d.pop("DiscountPercent")

        discounted_price = d.pop("DiscountedPrice")

        is_promo_item = d.pop("IsPromoItem")

        item = Item.from_dict(d.pop("Item"))

        bundle_item = cls(
            base_price=base_price,
            currency_id=currency_id,
            discount_percent=discount_percent,
            discounted_price=discounted_price,
            is_promo_item=is_promo_item,
            item=item,
        )

        bundle_item.additional_properties = d
        return bundle_item

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
