from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data_round_location import MatchesV4DataRoundLocation
    from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer
    from ..models.matches_v4_data_round_player_locations import MatchesV4DataRoundPlayerLocations


T = TypeVar("T", bound="MatchesV4DataRoundPlant")


@_attrs_define
class MatchesV4DataRoundPlant:
    """
    Attributes:
        location (MatchesV4DataRoundLocation):
        player (MatchesV4DataRoundPlayer):
        player_locations (list['MatchesV4DataRoundPlayerLocations']):
        round_time_in_ms (int):
        site (str):
    """

    location: "MatchesV4DataRoundLocation"
    player: "MatchesV4DataRoundPlayer"
    player_locations: list["MatchesV4DataRoundPlayerLocations"]
    round_time_in_ms: int
    site: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location.to_dict()

        player = self.player.to_dict()

        player_locations = []
        for player_locations_item_data in self.player_locations:
            player_locations_item = player_locations_item_data.to_dict()
            player_locations.append(player_locations_item)

        round_time_in_ms = self.round_time_in_ms

        site = self.site

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "player": player,
                "player_locations": player_locations,
                "round_time_in_ms": round_time_in_ms,
                "site": site,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_round_location import MatchesV4DataRoundLocation
        from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer
        from ..models.matches_v4_data_round_player_locations import MatchesV4DataRoundPlayerLocations

        d = dict(src_dict)
        location = MatchesV4DataRoundLocation.from_dict(d.pop("location"))

        player = MatchesV4DataRoundPlayer.from_dict(d.pop("player"))

        player_locations = []
        _player_locations = d.pop("player_locations")
        for player_locations_item_data in _player_locations:
            player_locations_item = MatchesV4DataRoundPlayerLocations.from_dict(player_locations_item_data)

            player_locations.append(player_locations_item)

        round_time_in_ms = d.pop("round_time_in_ms")

        site = d.pop("site")

        matches_v4_data_round_plant = cls(
            location=location,
            player=player,
            player_locations=player_locations,
            round_time_in_ms=round_time_in_ms,
            site=site,
        )

        matches_v4_data_round_plant.additional_properties = d
        return matches_v4_data_round_plant

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
