from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data_round_location import MatchesV4DataRoundLocation
    from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer
    from ..models.matches_v4_data_round_player_locations import MatchesV4DataRoundPlayerLocations
    from ..models.matches_v4_data_round_player_stats_economy_weapon import MatchesV4DataRoundPlayerStatsEconomyWeapon


T = TypeVar("T", bound="MatchesV4DataKill")


@_attrs_define
class MatchesV4DataKill:
    """
    Attributes:
        assistants (list['MatchesV4DataRoundPlayer']):
        killer (MatchesV4DataRoundPlayer):
        location (MatchesV4DataRoundLocation):
        player_locations (list['MatchesV4DataRoundPlayerLocations']):
        round_ (int):
        secondary_fire_mode (bool):
        time_in_match_in_ms (int):
        time_in_round_in_ms (int):
        victim (MatchesV4DataRoundPlayer):
        weapon (MatchesV4DataRoundPlayerStatsEconomyWeapon):
    """

    assistants: list["MatchesV4DataRoundPlayer"]
    killer: "MatchesV4DataRoundPlayer"
    location: "MatchesV4DataRoundLocation"
    player_locations: list["MatchesV4DataRoundPlayerLocations"]
    round_: int
    secondary_fire_mode: bool
    time_in_match_in_ms: int
    time_in_round_in_ms: int
    victim: "MatchesV4DataRoundPlayer"
    weapon: "MatchesV4DataRoundPlayerStatsEconomyWeapon"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        assistants = []
        for assistants_item_data in self.assistants:
            assistants_item = assistants_item_data.to_dict()
            assistants.append(assistants_item)

        killer = self.killer.to_dict()

        location = self.location.to_dict()

        player_locations = []
        for player_locations_item_data in self.player_locations:
            player_locations_item = player_locations_item_data.to_dict()
            player_locations.append(player_locations_item)

        round_ = self.round_

        secondary_fire_mode = self.secondary_fire_mode

        time_in_match_in_ms = self.time_in_match_in_ms

        time_in_round_in_ms = self.time_in_round_in_ms

        victim = self.victim.to_dict()

        weapon = self.weapon.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assistants": assistants,
                "killer": killer,
                "location": location,
                "player_locations": player_locations,
                "round": round_,
                "secondary_fire_mode": secondary_fire_mode,
                "time_in_match_in_ms": time_in_match_in_ms,
                "time_in_round_in_ms": time_in_round_in_ms,
                "victim": victim,
                "weapon": weapon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_round_location import MatchesV4DataRoundLocation
        from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer
        from ..models.matches_v4_data_round_player_locations import MatchesV4DataRoundPlayerLocations
        from ..models.matches_v4_data_round_player_stats_economy_weapon import (
            MatchesV4DataRoundPlayerStatsEconomyWeapon,
        )

        d = dict(src_dict)
        assistants = []
        _assistants = d.pop("assistants")
        for assistants_item_data in _assistants:
            assistants_item = MatchesV4DataRoundPlayer.from_dict(assistants_item_data)

            assistants.append(assistants_item)

        killer = MatchesV4DataRoundPlayer.from_dict(d.pop("killer"))

        location = MatchesV4DataRoundLocation.from_dict(d.pop("location"))

        player_locations = []
        _player_locations = d.pop("player_locations")
        for player_locations_item_data in _player_locations:
            player_locations_item = MatchesV4DataRoundPlayerLocations.from_dict(player_locations_item_data)

            player_locations.append(player_locations_item)

        round_ = d.pop("round")

        secondary_fire_mode = d.pop("secondary_fire_mode")

        time_in_match_in_ms = d.pop("time_in_match_in_ms")

        time_in_round_in_ms = d.pop("time_in_round_in_ms")

        victim = MatchesV4DataRoundPlayer.from_dict(d.pop("victim"))

        weapon = MatchesV4DataRoundPlayerStatsEconomyWeapon.from_dict(d.pop("weapon"))

        matches_v4_data_kill = cls(
            assistants=assistants,
            killer=killer,
            location=location,
            player_locations=player_locations,
            round_=round_,
            secondary_fire_mode=secondary_fire_mode,
            time_in_match_in_ms=time_in_match_in_ms,
            time_in_round_in_ms=time_in_round_in_ms,
            victim=victim,
            weapon=weapon,
        )

        matches_v4_data_kill.additional_properties = d
        return matches_v4_data_kill

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
