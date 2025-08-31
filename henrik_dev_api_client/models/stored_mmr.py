from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stored_mmr_map import StoredMMRMap
    from ..models.stored_mmr_season import StoredMMRSeason
    from ..models.stored_mmr_tier import StoredMMRTier


T = TypeVar("T", bound="StoredMMR")


@_attrs_define
class StoredMMR:
    """
    Attributes:
        date (str):
        elo (int):
        last_mmr_change (int):
        map_ (StoredMMRMap):
        match_id (str):
        ranking_in_tier (int):
        season (StoredMMRSeason):
        tier (StoredMMRTier):
    """

    date: str
    elo: int
    last_mmr_change: int
    map_: "StoredMMRMap"
    match_id: str
    ranking_in_tier: int
    season: "StoredMMRSeason"
    tier: "StoredMMRTier"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        elo = self.elo

        last_mmr_change = self.last_mmr_change

        map_ = self.map_.to_dict()

        match_id = self.match_id

        ranking_in_tier = self.ranking_in_tier

        season = self.season.to_dict()

        tier = self.tier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "elo": elo,
                "last_mmr_change": last_mmr_change,
                "map": map_,
                "match_id": match_id,
                "ranking_in_tier": ranking_in_tier,
                "season": season,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stored_mmr_map import StoredMMRMap
        from ..models.stored_mmr_season import StoredMMRSeason
        from ..models.stored_mmr_tier import StoredMMRTier

        d = dict(src_dict)
        date = d.pop("date")

        elo = d.pop("elo")

        last_mmr_change = d.pop("last_mmr_change")

        map_ = StoredMMRMap.from_dict(d.pop("map"))

        match_id = d.pop("match_id")

        ranking_in_tier = d.pop("ranking_in_tier")

        season = StoredMMRSeason.from_dict(d.pop("season"))

        tier = StoredMMRTier.from_dict(d.pop("tier"))

        stored_mmr = cls(
            date=date,
            elo=elo,
            last_mmr_change=last_mmr_change,
            map_=map_,
            match_id=match_id,
            ranking_in_tier=ranking_in_tier,
            season=season,
            tier=tier,
        )

        stored_mmr.additional_properties = d
        return stored_mmr

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
