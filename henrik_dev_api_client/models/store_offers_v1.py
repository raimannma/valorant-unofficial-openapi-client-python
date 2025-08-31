from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.store_offers_v1_offer import StoreOffersV1Offer
    from ..models.store_offers_v1_upgrade_currency import StoreOffersV1UpgradeCurrency


T = TypeVar("T", bound="StoreOffersV1")


@_attrs_define
class StoreOffersV1:
    """
    Attributes:
        offers (list['StoreOffersV1Offer']):
        upgrade_currency_offers (list['StoreOffersV1UpgradeCurrency']):
    """

    offers: list["StoreOffersV1Offer"]
    upgrade_currency_offers: list["StoreOffersV1UpgradeCurrency"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        offers = []
        for offers_item_data in self.offers:
            offers_item = offers_item_data.to_dict()
            offers.append(offers_item)

        upgrade_currency_offers = []
        for upgrade_currency_offers_item_data in self.upgrade_currency_offers:
            upgrade_currency_offers_item = upgrade_currency_offers_item_data.to_dict()
            upgrade_currency_offers.append(upgrade_currency_offers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Offers": offers,
                "UpgradeCurrencyOffers": upgrade_currency_offers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.store_offers_v1_offer import StoreOffersV1Offer
        from ..models.store_offers_v1_upgrade_currency import StoreOffersV1UpgradeCurrency

        d = dict(src_dict)
        offers = []
        _offers = d.pop("Offers")
        for offers_item_data in _offers:
            offers_item = StoreOffersV1Offer.from_dict(offers_item_data)

            offers.append(offers_item)

        upgrade_currency_offers = []
        _upgrade_currency_offers = d.pop("UpgradeCurrencyOffers")
        for upgrade_currency_offers_item_data in _upgrade_currency_offers:
            upgrade_currency_offers_item = StoreOffersV1UpgradeCurrency.from_dict(upgrade_currency_offers_item_data)

            upgrade_currency_offers.append(upgrade_currency_offers_item)

        store_offers_v1 = cls(
            offers=offers,
            upgrade_currency_offers=upgrade_currency_offers,
        )

        store_offers_v1.additional_properties = d
        return store_offers_v1

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
