from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation


T = TypeVar("T", bound="MatchesV2DataRoundPlayerLocationsOnEvent")


@_attrs_define
class MatchesV2DataRoundPlayerLocationsOnEvent:
    """
    Attributes:
        location (MatchesV2DataRoundEventLocation):
        player_display_name (str):
        player_puuid (str):
        player_team (str):
        view_radians (float):
    """

    location: "MatchesV2DataRoundEventLocation"
    player_display_name: str
    player_puuid: str
    player_team: str
    view_radians: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location.to_dict()

        player_display_name = self.player_display_name

        player_puuid = self.player_puuid

        player_team = self.player_team

        view_radians = self.view_radians

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "player_display_name": player_display_name,
                "player_puuid": player_puuid,
                "player_team": player_team,
                "view_radians": view_radians,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation

        d = dict(src_dict)
        location = MatchesV2DataRoundEventLocation.from_dict(d.pop("location"))

        player_display_name = d.pop("player_display_name")

        player_puuid = d.pop("player_puuid")

        player_team = d.pop("player_team")

        view_radians = d.pop("view_radians")

        matches_v2_data_round_player_locations_on_event = cls(
            location=location,
            player_display_name=player_display_name,
            player_puuid=player_puuid,
            player_team=player_team,
            view_radians=view_radians,
        )

        matches_v2_data_round_player_locations_on_event.additional_properties = d
        return matches_v2_data_round_player_locations_on_event

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
