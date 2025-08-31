from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_player_assets_agent import MatchesV2DataPlayerAssetsAgent
    from ..models.matches_v2_data_player_assets_card import MatchesV2DataPlayerAssetsCard


T = TypeVar("T", bound="MatchesV2DataPlayerAssets")


@_attrs_define
class MatchesV2DataPlayerAssets:
    """
    Attributes:
        agent (MatchesV2DataPlayerAssetsAgent):
        card (MatchesV2DataPlayerAssetsCard):
    """

    agent: "MatchesV2DataPlayerAssetsAgent"
    card: "MatchesV2DataPlayerAssetsCard"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        agent = self.agent.to_dict()

        card = self.card.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "agent": agent,
                "card": card,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_player_assets_agent import MatchesV2DataPlayerAssetsAgent
        from ..models.matches_v2_data_player_assets_card import MatchesV2DataPlayerAssetsCard

        d = dict(src_dict)
        agent = MatchesV2DataPlayerAssetsAgent.from_dict(d.pop("agent"))

        card = MatchesV2DataPlayerAssetsCard.from_dict(d.pop("card"))

        matches_v2_data_player_assets = cls(
            agent=agent,
            card=card,
        )

        matches_v2_data_player_assets.additional_properties = d
        return matches_v2_data_player_assets

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
