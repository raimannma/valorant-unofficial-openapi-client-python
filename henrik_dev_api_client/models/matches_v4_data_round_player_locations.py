from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data_round_location import MatchesV4DataRoundLocation
    from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer


T = TypeVar("T", bound="MatchesV4DataRoundPlayerLocations")


@_attrs_define
class MatchesV4DataRoundPlayerLocations:
    """
    Attributes:
        location (MatchesV4DataRoundLocation):
        player (MatchesV4DataRoundPlayer):
        view_radians (float):
    """

    location: "MatchesV4DataRoundLocation"
    player: "MatchesV4DataRoundPlayer"
    view_radians: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location = self.location.to_dict()

        player = self.player.to_dict()

        view_radians = self.view_radians

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "location": location,
                "player": player,
                "view_radians": view_radians,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_round_location import MatchesV4DataRoundLocation
        from ..models.matches_v4_data_round_player import MatchesV4DataRoundPlayer

        d = dict(src_dict)
        location = MatchesV4DataRoundLocation.from_dict(d.pop("location"))

        player = MatchesV4DataRoundPlayer.from_dict(d.pop("player"))

        view_radians = d.pop("view_radians")

        matches_v4_data_round_player_locations = cls(
            location=location,
            player=player,
            view_radians=view_radians,
        )

        matches_v4_data_round_player_locations.additional_properties = d
        return matches_v4_data_round_player_locations

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
