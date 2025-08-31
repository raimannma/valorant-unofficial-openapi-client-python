from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
    from ..models.matches_v2_data_round_player_locations_on_event import MatchesV2DataRoundPlayerLocationsOnEvent
    from ..models.matches_v2_data_round_player_stats_kill_events_assets import (
        MatchesV2DataRoundPlayerStatsKillEventsAssets,
    )
    from ..models.matches_v2_data_round_player_stats_kill_events_assistants import (
        MatchesV2DataRoundPlayerStatsKillEventsAssistants,
    )


T = TypeVar("T", bound="MatchesV2DataKill")


@_attrs_define
class MatchesV2DataKill:
    """
    Attributes:
        assistants (list['MatchesV2DataRoundPlayerStatsKillEventsAssistants']):
        damage_weapon_assets (MatchesV2DataRoundPlayerStatsKillEventsAssets):
        damage_weapon_id (str):
        kill_time_in_match (int):
        kill_time_in_round (int):
        killer_display_name (str):
        killer_puuid (str):
        killer_team (str):
        player_locations_on_kill (list['MatchesV2DataRoundPlayerLocationsOnEvent']):
        round_ (int):
        secondary_fire_mode (bool):
        victim_death_location (MatchesV2DataRoundEventLocation):
        victim_display_name (str):
        victim_puuid (str):
        victim_team (str):
        damage_weapon_name (Union[None, Unset, str]):
    """

    assistants: list["MatchesV2DataRoundPlayerStatsKillEventsAssistants"]
    damage_weapon_assets: "MatchesV2DataRoundPlayerStatsKillEventsAssets"
    damage_weapon_id: str
    kill_time_in_match: int
    kill_time_in_round: int
    killer_display_name: str
    killer_puuid: str
    killer_team: str
    player_locations_on_kill: list["MatchesV2DataRoundPlayerLocationsOnEvent"]
    round_: int
    secondary_fire_mode: bool
    victim_death_location: "MatchesV2DataRoundEventLocation"
    victim_display_name: str
    victim_puuid: str
    victim_team: str
    damage_weapon_name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistants = []
        for assistants_item_data in self.assistants:
            assistants_item = assistants_item_data.to_dict()
            assistants.append(assistants_item)

        damage_weapon_assets = self.damage_weapon_assets.to_dict()

        damage_weapon_id = self.damage_weapon_id

        kill_time_in_match = self.kill_time_in_match

        kill_time_in_round = self.kill_time_in_round

        killer_display_name = self.killer_display_name

        killer_puuid = self.killer_puuid

        killer_team = self.killer_team

        player_locations_on_kill = []
        for player_locations_on_kill_item_data in self.player_locations_on_kill:
            player_locations_on_kill_item = player_locations_on_kill_item_data.to_dict()
            player_locations_on_kill.append(player_locations_on_kill_item)

        round_ = self.round_

        secondary_fire_mode = self.secondary_fire_mode

        victim_death_location = self.victim_death_location.to_dict()

        victim_display_name = self.victim_display_name

        victim_puuid = self.victim_puuid

        victim_team = self.victim_team

        damage_weapon_name: Union[None, Unset, str]
        if isinstance(self.damage_weapon_name, Unset):
            damage_weapon_name = UNSET
        else:
            damage_weapon_name = self.damage_weapon_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistants": assistants,
                "damage_weapon_assets": damage_weapon_assets,
                "damage_weapon_id": damage_weapon_id,
                "kill_time_in_match": kill_time_in_match,
                "kill_time_in_round": kill_time_in_round,
                "killer_display_name": killer_display_name,
                "killer_puuid": killer_puuid,
                "killer_team": killer_team,
                "player_locations_on_kill": player_locations_on_kill,
                "round": round_,
                "secondary_fire_mode": secondary_fire_mode,
                "victim_death_location": victim_death_location,
                "victim_display_name": victim_display_name,
                "victim_puuid": victim_puuid,
                "victim_team": victim_team,
            }
        )
        if damage_weapon_name is not UNSET:
            field_dict["damage_weapon_name"] = damage_weapon_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
        from ..models.matches_v2_data_round_player_locations_on_event import MatchesV2DataRoundPlayerLocationsOnEvent
        from ..models.matches_v2_data_round_player_stats_kill_events_assets import (
            MatchesV2DataRoundPlayerStatsKillEventsAssets,
        )
        from ..models.matches_v2_data_round_player_stats_kill_events_assistants import (
            MatchesV2DataRoundPlayerStatsKillEventsAssistants,
        )

        d = dict(src_dict)
        assistants = []
        _assistants = d.pop("assistants")
        for assistants_item_data in _assistants:
            assistants_item = MatchesV2DataRoundPlayerStatsKillEventsAssistants.from_dict(assistants_item_data)

            assistants.append(assistants_item)

        damage_weapon_assets = MatchesV2DataRoundPlayerStatsKillEventsAssets.from_dict(d.pop("damage_weapon_assets"))

        damage_weapon_id = d.pop("damage_weapon_id")

        kill_time_in_match = d.pop("kill_time_in_match")

        kill_time_in_round = d.pop("kill_time_in_round")

        killer_display_name = d.pop("killer_display_name")

        killer_puuid = d.pop("killer_puuid")

        killer_team = d.pop("killer_team")

        player_locations_on_kill = []
        _player_locations_on_kill = d.pop("player_locations_on_kill")
        for player_locations_on_kill_item_data in _player_locations_on_kill:
            player_locations_on_kill_item = MatchesV2DataRoundPlayerLocationsOnEvent.from_dict(
                player_locations_on_kill_item_data
            )

            player_locations_on_kill.append(player_locations_on_kill_item)

        round_ = d.pop("round")

        secondary_fire_mode = d.pop("secondary_fire_mode")

        victim_death_location = MatchesV2DataRoundEventLocation.from_dict(d.pop("victim_death_location"))

        victim_display_name = d.pop("victim_display_name")

        victim_puuid = d.pop("victim_puuid")

        victim_team = d.pop("victim_team")

        def _parse_damage_weapon_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        damage_weapon_name = _parse_damage_weapon_name(d.pop("damage_weapon_name", UNSET))

        matches_v2_data_kill = cls(
            assistants=assistants,
            damage_weapon_assets=damage_weapon_assets,
            damage_weapon_id=damage_weapon_id,
            kill_time_in_match=kill_time_in_match,
            kill_time_in_round=kill_time_in_round,
            killer_display_name=killer_display_name,
            killer_puuid=killer_puuid,
            killer_team=killer_team,
            player_locations_on_kill=player_locations_on_kill,
            round_=round_,
            secondary_fire_mode=secondary_fire_mode,
            victim_death_location=victim_death_location,
            victim_display_name=victim_display_name,
            victim_puuid=victim_puuid,
            victim_team=victim_team,
            damage_weapon_name=damage_weapon_name,
        )

        matches_v2_data_kill.additional_properties = d
        return matches_v2_data_kill

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
