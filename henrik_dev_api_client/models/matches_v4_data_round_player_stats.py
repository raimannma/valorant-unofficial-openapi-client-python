from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer
    from ..models.matches_v4_data_round_player_stats_ability_casts import MatchesV4DataRoundPlayerStatsAbilityCasts
    from ..models.matches_v4_data_round_player_stats_damage_events import MatchesV4DataRoundPlayerStatsDamageEvents
    from ..models.matches_v4_data_round_player_stats_economy import MatchesV4DataRoundPlayerStatsEconomy
    from ..models.matches_v4_data_round_player_stats_stats import MatchesV4DataRoundPlayerStatsStats


T = TypeVar("T", bound="MatchesV4DataRoundPlayerStats")


@_attrs_define
class MatchesV4DataRoundPlayerStats:
    """
    Attributes:
        ability_casts (MatchesV4DataRoundPlayerStatsAbilityCasts):
        damage_events (list['MatchesV4DataRoundPlayerStatsDamageEvents']):
        economy (MatchesV4DataRoundPlayerStatsEconomy):
        player (MatchesV4DataRoundPlayer):
        received_penalty (bool):
        stats (MatchesV4DataRoundPlayerStatsStats):
        stayed_in_spawn (bool):
        was_afk (bool):
    """

    ability_casts: "MatchesV4DataRoundPlayerStatsAbilityCasts"
    damage_events: list["MatchesV4DataRoundPlayerStatsDamageEvents"]
    economy: "MatchesV4DataRoundPlayerStatsEconomy"
    player: "MatchesV4DataRoundPlayer"
    received_penalty: bool
    stats: "MatchesV4DataRoundPlayerStatsStats"
    stayed_in_spawn: bool
    was_afk: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ability_casts = self.ability_casts.to_dict()

        damage_events = []
        for damage_events_item_data in self.damage_events:
            damage_events_item = damage_events_item_data.to_dict()
            damage_events.append(damage_events_item)

        economy = self.economy.to_dict()

        player = self.player.to_dict()

        received_penalty = self.received_penalty

        stats = self.stats.to_dict()

        stayed_in_spawn = self.stayed_in_spawn

        was_afk = self.was_afk

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ability_casts": ability_casts,
                "damage_events": damage_events,
                "economy": economy,
                "player": player,
                "received_penalty": received_penalty,
                "stats": stats,
                "stayed_in_spawn": stayed_in_spawn,
                "was_afk": was_afk,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer
        from ..models.matches_v4_data_round_player_stats_ability_casts import MatchesV4DataRoundPlayerStatsAbilityCasts
        from ..models.matches_v4_data_round_player_stats_damage_events import MatchesV4DataRoundPlayerStatsDamageEvents
        from ..models.matches_v4_data_round_player_stats_economy import MatchesV4DataRoundPlayerStatsEconomy
        from ..models.matches_v4_data_round_player_stats_stats import MatchesV4DataRoundPlayerStatsStats

        d = dict(src_dict)
        ability_casts = MatchesV4DataRoundPlayerStatsAbilityCasts.from_dict(d.pop("ability_casts"))

        damage_events = []
        _damage_events = d.pop("damage_events")
        for damage_events_item_data in _damage_events:
            damage_events_item = MatchesV4DataRoundPlayerStatsDamageEvents.from_dict(damage_events_item_data)

            damage_events.append(damage_events_item)

        economy = MatchesV4DataRoundPlayerStatsEconomy.from_dict(d.pop("economy"))

        player = MatchesV4DataRoundPlayer.from_dict(d.pop("player"))

        received_penalty = d.pop("received_penalty")

        stats = MatchesV4DataRoundPlayerStatsStats.from_dict(d.pop("stats"))

        stayed_in_spawn = d.pop("stayed_in_spawn")

        was_afk = d.pop("was_afk")

        matches_v4_data_round_player_stats = cls(
            ability_casts=ability_casts,
            damage_events=damage_events,
            economy=economy,
            player=player,
            received_penalty=received_penalty,
            stats=stats,
            stayed_in_spawn=stayed_in_spawn,
            was_afk=was_afk,
        )

        matches_v4_data_round_player_stats.additional_properties = d
        return matches_v4_data_round_player_stats

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
