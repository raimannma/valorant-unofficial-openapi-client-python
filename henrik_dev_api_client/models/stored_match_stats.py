from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.stored_match_stats_character import StoredMatchStatsCharacter
    from ..models.stored_match_stats_damage import StoredMatchStatsDamage
    from ..models.stored_match_stats_shots import StoredMatchStatsShots


T = TypeVar("T", bound="StoredMatchStats")


@_attrs_define
class StoredMatchStats:
    """
    Attributes:
        assists (int):
        character (StoredMatchStatsCharacter):
        damage (StoredMatchStatsDamage):
        deaths (int):
        kills (int):
        level (int):
        puuid (str):
        score (int):
        shots (StoredMatchStatsShots):
        team (str):
        tier (int):
    """

    assists: int
    character: "StoredMatchStatsCharacter"
    damage: "StoredMatchStatsDamage"
    deaths: int
    kills: int
    level: int
    puuid: str
    score: int
    shots: "StoredMatchStatsShots"
    team: str
    tier: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assists = self.assists

        character = self.character.to_dict()

        damage = self.damage.to_dict()

        deaths = self.deaths

        kills = self.kills

        level = self.level

        puuid = self.puuid

        score = self.score

        shots = self.shots.to_dict()

        team = self.team

        tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assists": assists,
                "character": character,
                "damage": damage,
                "deaths": deaths,
                "kills": kills,
                "level": level,
                "puuid": puuid,
                "score": score,
                "shots": shots,
                "team": team,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stored_match_stats_character import StoredMatchStatsCharacter
        from ..models.stored_match_stats_damage import StoredMatchStatsDamage
        from ..models.stored_match_stats_shots import StoredMatchStatsShots

        d = dict(src_dict)
        assists = d.pop("assists")

        character = StoredMatchStatsCharacter.from_dict(d.pop("character"))

        damage = StoredMatchStatsDamage.from_dict(d.pop("damage"))

        deaths = d.pop("deaths")

        kills = d.pop("kills")

        level = d.pop("level")

        puuid = d.pop("puuid")

        score = d.pop("score")

        shots = StoredMatchStatsShots.from_dict(d.pop("shots"))

        team = d.pop("team")

        tier = d.pop("tier")

        stored_match_stats = cls(
            assists=assists,
            character=character,
            damage=damage,
            deaths=deaths,
            kills=kills,
            level=level,
            puuid=puuid,
            score=score,
            shots=shots,
            team=team,
            tier=tier,
        )

        stored_match_stats.additional_properties = d
        return stored_match_stats

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
