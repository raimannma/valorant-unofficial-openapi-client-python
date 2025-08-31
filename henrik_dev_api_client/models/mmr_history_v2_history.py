from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.map_id_name_combo import MapIdNameCombo
    from ..models.season_id_short_combo import SeasonIdShortCombo
    from ..models.tier_id_name_combo import TierIdNameCombo


T = TypeVar("T", bound="MMRHistoryV2History")


@_attrs_define
class MMRHistoryV2History:
    """
    Attributes:
        date (str):
        elo (int):
        last_change (int):
        map_ (MapIdNameCombo):
        match_id (str):
        refunded_rr (int):
        rr (int):
        season (SeasonIdShortCombo):
        tier (TierIdNameCombo):
        was_derank_protected (bool):
    """

    date: str
    elo: int
    last_change: int
    map_: "MapIdNameCombo"
    match_id: str
    refunded_rr: int
    rr: int
    season: "SeasonIdShortCombo"
    tier: "TierIdNameCombo"
    was_derank_protected: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        elo = self.elo

        last_change = self.last_change

        map_ = self.map_.to_dict()

        match_id = self.match_id

        refunded_rr = self.refunded_rr

        rr = self.rr

        season = self.season.to_dict()

        tier = self.tier.to_dict()

        was_derank_protected = self.was_derank_protected

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "elo": elo,
                "last_change": last_change,
                "map": map_,
                "match_id": match_id,
                "refunded_rr": refunded_rr,
                "rr": rr,
                "season": season,
                "tier": tier,
                "was_derank_protected": was_derank_protected,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_id_name_combo import MapIdNameCombo
        from ..models.season_id_short_combo import SeasonIdShortCombo
        from ..models.tier_id_name_combo import TierIdNameCombo

        d = dict(src_dict)
        date = d.pop("date")

        elo = d.pop("elo")

        last_change = d.pop("last_change")

        map_ = MapIdNameCombo.from_dict(d.pop("map"))

        match_id = d.pop("match_id")

        refunded_rr = d.pop("refunded_rr")

        rr = d.pop("rr")

        season = SeasonIdShortCombo.from_dict(d.pop("season"))

        tier = TierIdNameCombo.from_dict(d.pop("tier"))

        was_derank_protected = d.pop("was_derank_protected")

        mmr_history_v2_history = cls(
            date=date,
            elo=elo,
            last_change=last_change,
            map_=map_,
            match_id=match_id,
            refunded_rr=refunded_rr,
            rr=rr,
            season=season,
            tier=tier,
            was_derank_protected=was_derank_protected,
        )

        mmr_history_v2_history.additional_properties = d
        return mmr_history_v2_history

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
