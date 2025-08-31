from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_round_player_stats_ability_casts import MatchesV2DataRoundPlayerStatsAbilityCasts
    from ..models.matches_v2_data_round_player_stats_damage_events import MatchesV2DataRoundPlayerStatsDamageEvents
    from ..models.matches_v2_data_round_player_stats_economy import MatchesV2DataRoundPlayerStatsEconomy
    from ..models.matches_v2_data_round_player_stats_kill_events import MatchesV2DataRoundPlayerStatsKillEvents


T = TypeVar("T", bound="MatchesV2DataRoundPlayerStats")


@_attrs_define
class MatchesV2DataRoundPlayerStats:
    """
    Attributes:
        ability_casts (MatchesV2DataRoundPlayerStatsAbilityCasts):
        bodyshots (int):
        damage (int):
        damage_events (list['MatchesV2DataRoundPlayerStatsDamageEvents']):
        economy (MatchesV2DataRoundPlayerStatsEconomy):
        headshots (int):
        kill_events (list['MatchesV2DataRoundPlayerStatsKillEvents']):
        kills (int):
        legshots (int):
        player_display_name (str):
        player_puuid (str):
        player_team (str):
        score (int):
        stayed_in_spawn (bool):
        was_afk (bool):
        was_penalized (bool):
    """

    ability_casts: "MatchesV2DataRoundPlayerStatsAbilityCasts"
    bodyshots: int
    damage: int
    damage_events: list["MatchesV2DataRoundPlayerStatsDamageEvents"]
    economy: "MatchesV2DataRoundPlayerStatsEconomy"
    headshots: int
    kill_events: list["MatchesV2DataRoundPlayerStatsKillEvents"]
    kills: int
    legshots: int
    player_display_name: str
    player_puuid: str
    player_team: str
    score: int
    stayed_in_spawn: bool
    was_afk: bool
    was_penalized: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ability_casts = self.ability_casts.to_dict()

        bodyshots = self.bodyshots

        damage = self.damage

        damage_events = []
        for damage_events_item_data in self.damage_events:
            damage_events_item = damage_events_item_data.to_dict()
            damage_events.append(damage_events_item)

        economy = self.economy.to_dict()

        headshots = self.headshots

        kill_events = []
        for kill_events_item_data in self.kill_events:
            kill_events_item = kill_events_item_data.to_dict()
            kill_events.append(kill_events_item)

        kills = self.kills

        legshots = self.legshots

        player_display_name = self.player_display_name

        player_puuid = self.player_puuid

        player_team = self.player_team

        score = self.score

        stayed_in_spawn = self.stayed_in_spawn

        was_afk = self.was_afk

        was_penalized = self.was_penalized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ability_casts": ability_casts,
                "bodyshots": bodyshots,
                "damage": damage,
                "damage_events": damage_events,
                "economy": economy,
                "headshots": headshots,
                "kill_events": kill_events,
                "kills": kills,
                "legshots": legshots,
                "player_display_name": player_display_name,
                "player_puuid": player_puuid,
                "player_team": player_team,
                "score": score,
                "stayed_in_spawn": stayed_in_spawn,
                "was_afk": was_afk,
                "was_penalized": was_penalized,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_round_player_stats_ability_casts import MatchesV2DataRoundPlayerStatsAbilityCasts
        from ..models.matches_v2_data_round_player_stats_damage_events import MatchesV2DataRoundPlayerStatsDamageEvents
        from ..models.matches_v2_data_round_player_stats_economy import MatchesV2DataRoundPlayerStatsEconomy
        from ..models.matches_v2_data_round_player_stats_kill_events import MatchesV2DataRoundPlayerStatsKillEvents

        d = dict(src_dict)
        ability_casts = MatchesV2DataRoundPlayerStatsAbilityCasts.from_dict(d.pop("ability_casts"))

        bodyshots = d.pop("bodyshots")

        damage = d.pop("damage")

        damage_events = []
        _damage_events = d.pop("damage_events")
        for damage_events_item_data in _damage_events:
            damage_events_item = MatchesV2DataRoundPlayerStatsDamageEvents.from_dict(damage_events_item_data)

            damage_events.append(damage_events_item)

        economy = MatchesV2DataRoundPlayerStatsEconomy.from_dict(d.pop("economy"))

        headshots = d.pop("headshots")

        kill_events = []
        _kill_events = d.pop("kill_events")
        for kill_events_item_data in _kill_events:
            kill_events_item = MatchesV2DataRoundPlayerStatsKillEvents.from_dict(kill_events_item_data)

            kill_events.append(kill_events_item)

        kills = d.pop("kills")

        legshots = d.pop("legshots")

        player_display_name = d.pop("player_display_name")

        player_puuid = d.pop("player_puuid")

        player_team = d.pop("player_team")

        score = d.pop("score")

        stayed_in_spawn = d.pop("stayed_in_spawn")

        was_afk = d.pop("was_afk")

        was_penalized = d.pop("was_penalized")

        matches_v2_data_round_player_stats = cls(
            ability_casts=ability_casts,
            bodyshots=bodyshots,
            damage=damage,
            damage_events=damage_events,
            economy=economy,
            headshots=headshots,
            kill_events=kill_events,
            kills=kills,
            legshots=legshots,
            player_display_name=player_display_name,
            player_puuid=player_puuid,
            player_team=player_team,
            score=score,
            stayed_in_spawn=stayed_in_spawn,
            was_afk=was_afk,
            was_penalized=was_penalized,
        )

        matches_v2_data_round_player_stats.additional_properties = d
        return matches_v2_data_round_player_stats

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
