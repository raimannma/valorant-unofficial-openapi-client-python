from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mmr_data_images import MMRDataImages


T = TypeVar("T", bound="MMRV2CurrentData")


@_attrs_define
class MMRV2CurrentData:
    """
    Attributes:
        currenttier (int):
        currenttierpatched (str):
        elo (int):
        games_needed_for_rating (int):
        images (MMRDataImages):
        mmr_change_to_last_game (int):
        old (bool):
        ranking_in_tier (int):
    """

    currenttier: int
    currenttierpatched: str
    elo: int
    games_needed_for_rating: int
    images: "MMRDataImages"
    mmr_change_to_last_game: int
    old: bool
    ranking_in_tier: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currenttier = self.currenttier

        currenttierpatched = self.currenttierpatched

        elo = self.elo

        games_needed_for_rating = self.games_needed_for_rating

        images = self.images.to_dict()

        mmr_change_to_last_game = self.mmr_change_to_last_game

        old = self.old

        ranking_in_tier = self.ranking_in_tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currenttier": currenttier,
                "currenttierpatched": currenttierpatched,
                "elo": elo,
                "games_needed_for_rating": games_needed_for_rating,
                "images": images,
                "mmr_change_to_last_game": mmr_change_to_last_game,
                "old": old,
                "ranking_in_tier": ranking_in_tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mmr_data_images import MMRDataImages

        d = dict(src_dict)
        currenttier = d.pop("currenttier")

        currenttierpatched = d.pop("currenttierpatched")

        elo = d.pop("elo")

        games_needed_for_rating = d.pop("games_needed_for_rating")

        images = MMRDataImages.from_dict(d.pop("images"))

        mmr_change_to_last_game = d.pop("mmr_change_to_last_game")

        old = d.pop("old")

        ranking_in_tier = d.pop("ranking_in_tier")

        mmrv2_current_data = cls(
            currenttier=currenttier,
            currenttierpatched=currenttierpatched,
            elo=elo,
            games_needed_for_rating=games_needed_for_rating,
            images=images,
            mmr_change_to_last_game=mmr_change_to_last_game,
            old=old,
            ranking_in_tier=ranking_in_tier,
        )

        mmrv2_current_data.additional_properties = d
        return mmrv2_current_data

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
