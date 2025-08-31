from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mmr_data_images import MMRDataImages
    from ..models.mmr_history_v1_data_map import MMRHistoryV1DataMap


T = TypeVar("T", bound="MMRHistoryV1Data")


@_attrs_define
class MMRHistoryV1Data:
    """
    Attributes:
        currenttier (int):
        currenttierpatched (str):
        date (str):
        date_raw (int):
        elo (int):
        images (MMRDataImages):
        map_ (MMRHistoryV1DataMap):
        match_id (str):
        mmr_change_to_last_game (int):
        ranking_in_tier (int):
        season_id (str):
    """

    currenttier: int
    currenttierpatched: str
    date: str
    date_raw: int
    elo: int
    images: "MMRDataImages"
    map_: "MMRHistoryV1DataMap"
    match_id: str
    mmr_change_to_last_game: int
    ranking_in_tier: int
    season_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currenttier = self.currenttier

        currenttierpatched = self.currenttierpatched

        date = self.date

        date_raw = self.date_raw

        elo = self.elo

        images = self.images.to_dict()

        map_ = self.map_.to_dict()

        match_id = self.match_id

        mmr_change_to_last_game = self.mmr_change_to_last_game

        ranking_in_tier = self.ranking_in_tier

        season_id = self.season_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currenttier": currenttier,
                "currenttierpatched": currenttierpatched,
                "date": date,
                "date_raw": date_raw,
                "elo": elo,
                "images": images,
                "map": map_,
                "match_id": match_id,
                "mmr_change_to_last_game": mmr_change_to_last_game,
                "ranking_in_tier": ranking_in_tier,
                "season_id": season_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mmr_data_images import MMRDataImages
        from ..models.mmr_history_v1_data_map import MMRHistoryV1DataMap

        d = dict(src_dict)
        currenttier = d.pop("currenttier")

        currenttierpatched = d.pop("currenttierpatched")

        date = d.pop("date")

        date_raw = d.pop("date_raw")

        elo = d.pop("elo")

        images = MMRDataImages.from_dict(d.pop("images"))

        map_ = MMRHistoryV1DataMap.from_dict(d.pop("map"))

        match_id = d.pop("match_id")

        mmr_change_to_last_game = d.pop("mmr_change_to_last_game")

        ranking_in_tier = d.pop("ranking_in_tier")

        season_id = d.pop("season_id")

        mmr_history_v1_data = cls(
            currenttier=currenttier,
            currenttierpatched=currenttierpatched,
            date=date,
            date_raw=date_raw,
            elo=elo,
            images=images,
            map_=map_,
            match_id=match_id,
            mmr_change_to_last_game=mmr_change_to_last_game,
            ranking_in_tier=ranking_in_tier,
            season_id=season_id,
        )

        mmr_history_v1_data.additional_properties = d
        return mmr_history_v1_data

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
