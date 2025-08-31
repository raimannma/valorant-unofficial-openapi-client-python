from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.season_id_short_combo import SeasonIdShortCombo
    from ..models.tier_id_name_combo import TierIdNameCombo


T = TypeVar("T", bound="MMRV3Peak")


@_attrs_define
class MMRV3Peak:
    """
    Attributes:
        ranking_schema (str):
        rr (int):
        season (SeasonIdShortCombo):
        tier (TierIdNameCombo):
    """

    ranking_schema: str
    rr: int
    season: "SeasonIdShortCombo"
    tier: "TierIdNameCombo"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ranking_schema = self.ranking_schema

        rr = self.rr

        season = self.season.to_dict()

        tier = self.tier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ranking_schema": ranking_schema,
                "rr": rr,
                "season": season,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.season_id_short_combo import SeasonIdShortCombo
        from ..models.tier_id_name_combo import TierIdNameCombo

        d = dict(src_dict)
        ranking_schema = d.pop("ranking_schema")

        rr = d.pop("rr")

        season = SeasonIdShortCombo.from_dict(d.pop("season"))

        tier = TierIdNameCombo.from_dict(d.pop("tier"))

        mmrv3_peak = cls(
            ranking_schema=ranking_schema,
            rr=rr,
            season=season,
            tier=tier,
        )

        mmrv3_peak.additional_properties = d
        return mmrv3_peak

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
