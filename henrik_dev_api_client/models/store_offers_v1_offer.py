from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.store_offers_v1_offer_cost import StoreOffersV1OfferCost
    from ..models.store_offers_v1_reward import StoreOffersV1Reward


T = TypeVar("T", bound="StoreOffersV1Offer")


@_attrs_define
class StoreOffersV1Offer:
    """
    Attributes:
        cost (StoreOffersV1OfferCost):
        is_direct_purchase (bool):
        offer_id (str):
        rewards (list['StoreOffersV1Reward']):
        start_date (str):
    """

    cost: "StoreOffersV1OfferCost"
    is_direct_purchase: bool
    offer_id: str
    rewards: list["StoreOffersV1Reward"]
    start_date: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cost = self.cost.to_dict()

        is_direct_purchase = self.is_direct_purchase

        offer_id = self.offer_id

        rewards = []
        for rewards_item_data in self.rewards:
            rewards_item = rewards_item_data.to_dict()
            rewards.append(rewards_item)

        start_date = self.start_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Cost": cost,
                "IsDirectPurchase": is_direct_purchase,
                "OfferID": offer_id,
                "Rewards": rewards,
                "StartDate": start_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.store_offers_v1_offer_cost import StoreOffersV1OfferCost
        from ..models.store_offers_v1_reward import StoreOffersV1Reward

        d = dict(src_dict)
        cost = StoreOffersV1OfferCost.from_dict(d.pop("Cost"))

        is_direct_purchase = d.pop("IsDirectPurchase")

        offer_id = d.pop("OfferID")

        rewards = []
        _rewards = d.pop("Rewards")
        for rewards_item_data in _rewards:
            rewards_item = StoreOffersV1Reward.from_dict(rewards_item_data)

            rewards.append(rewards_item)

        start_date = d.pop("StartDate")

        store_offers_v1_offer = cls(
            cost=cost,
            is_direct_purchase=is_direct_purchase,
            offer_id=offer_id,
            rewards=rewards,
            start_date=start_date,
        )

        store_offers_v1_offer.additional_properties = d
        return store_offers_v1_offer

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
