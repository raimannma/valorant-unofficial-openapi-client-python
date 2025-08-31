from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stored_match_meta import StoredMatchMeta
    from ..models.stored_match_stats import StoredMatchStats
    from ..models.stored_match_team import StoredMatchTeam


T = TypeVar("T", bound="StoredMatch")


@_attrs_define
class StoredMatch:
    """
    Attributes:
        meta (StoredMatchMeta):
        stats (StoredMatchStats):
        teams (StoredMatchTeam):
    """

    meta: "StoredMatchMeta"
    stats: "StoredMatchStats"
    teams: "StoredMatchTeam"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        meta = self.meta.to_dict()

        stats = self.stats.to_dict()

        teams = self.teams.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "meta": meta,
                "stats": stats,
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stored_match_meta import StoredMatchMeta
        from ..models.stored_match_stats import StoredMatchStats
        from ..models.stored_match_team import StoredMatchTeam

        d = dict(src_dict)
        meta = StoredMatchMeta.from_dict(d.pop("meta"))

        stats = StoredMatchStats.from_dict(d.pop("stats"))

        teams = StoredMatchTeam.from_dict(d.pop("teams"))

        stored_match = cls(
            meta=meta,
            stats=stats,
            teams=teams,
        )

        stored_match.additional_properties = d
        return stored_match

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
