from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data_player_stats_damage import MatchesV4DataPlayerStatsDamage


T = TypeVar("T", bound="MatchesV4DataPlayerStats")


@_attrs_define
class MatchesV4DataPlayerStats:
    """
    Attributes:
        assists (int):
        bodyshots (int):
        damage (MatchesV4DataPlayerStatsDamage):
        deaths (int):
        headshots (int):
        kills (int):
        legshots (int):
        score (int):
    """

    assists: int
    bodyshots: int
    damage: "MatchesV4DataPlayerStatsDamage"
    deaths: int
    headshots: int
    kills: int
    legshots: int
    score: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assists = self.assists

        bodyshots = self.bodyshots

        damage = self.damage.to_dict()

        deaths = self.deaths

        headshots = self.headshots

        kills = self.kills

        legshots = self.legshots

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assists": assists,
                "bodyshots": bodyshots,
                "damage": damage,
                "deaths": deaths,
                "headshots": headshots,
                "kills": kills,
                "legshots": legshots,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_player_stats_damage import MatchesV4DataPlayerStatsDamage

        d = dict(src_dict)
        assists = d.pop("assists")

        bodyshots = d.pop("bodyshots")

        damage = MatchesV4DataPlayerStatsDamage.from_dict(d.pop("damage"))

        deaths = d.pop("deaths")

        headshots = d.pop("headshots")

        kills = d.pop("kills")

        legshots = d.pop("legshots")

        score = d.pop("score")

        matches_v4_data_player_stats = cls(
            assists=assists,
            bodyshots=bodyshots,
            damage=damage,
            deaths=deaths,
            headshots=headshots,
            kills=kills,
            legshots=legshots,
            score=score,
        )

        matches_v4_data_player_stats.additional_properties = d
        return matches_v4_data_player_stats

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
