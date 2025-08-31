from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.store_offers_v1_offer import StoreOffersV1Offer


T = TypeVar("T", bound="StoreOffersV1UpgradeCurrency")


@_attrs_define
class StoreOffersV1UpgradeCurrency:
    """
    Attributes:
        discounted_percent (float):
        offer (StoreOffersV1Offer):
        offer_id (str):
        storefront_item_id (str):
    """

    discounted_percent: float
    offer: "StoreOffersV1Offer"
    offer_id: str
    storefront_item_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        discounted_percent = self.discounted_percent

        offer = self.offer.to_dict()

        offer_id = self.offer_id

        storefront_item_id = self.storefront_item_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "DiscountedPercent": discounted_percent,
                "Offer": offer,
                "OfferID": offer_id,
                "StorefrontItemID": storefront_item_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.store_offers_v1_offer import StoreOffersV1Offer

        d = dict(src_dict)
        discounted_percent = d.pop("DiscountedPercent")

        offer = StoreOffersV1Offer.from_dict(d.pop("Offer"))

        offer_id = d.pop("OfferID")

        storefront_item_id = d.pop("StorefrontItemID")

        store_offers_v1_upgrade_currency = cls(
            discounted_percent=discounted_percent,
            offer=offer,
            offer_id=offer_id,
            storefront_item_id=storefront_item_id,
        )

        store_offers_v1_upgrade_currency.additional_properties = d
        return store_offers_v1_upgrade_currency

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
