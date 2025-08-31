from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_player import MatchesV2DataPlayer


T = TypeVar("T", bound="MatchesV2DataPlayers")


@_attrs_define
class MatchesV2DataPlayers:
    """
    Attributes:
        all_players (list['MatchesV2DataPlayer']):
        blue (list['MatchesV2DataPlayer']):
        red (list['MatchesV2DataPlayer']):
    """

    all_players: list["MatchesV2DataPlayer"]
    blue: list["MatchesV2DataPlayer"]
    red: list["MatchesV2DataPlayer"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        all_players = []
        for all_players_item_data in self.all_players:
            all_players_item = all_players_item_data.to_dict()
            all_players.append(all_players_item)

        blue = []
        for blue_item_data in self.blue:
            blue_item = blue_item_data.to_dict()
            blue.append(blue_item)

        red = []
        for red_item_data in self.red:
            red_item = red_item_data.to_dict()
            red.append(red_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "all_players": all_players,
                "blue": blue,
                "red": red,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_player import MatchesV2DataPlayer

        d = dict(src_dict)
        all_players = []
        _all_players = d.pop("all_players")
        for all_players_item_data in _all_players:
            all_players_item = MatchesV2DataPlayer.from_dict(all_players_item_data)

            all_players.append(all_players_item)

        blue = []
        _blue = d.pop("blue")
        for blue_item_data in _blue:
            blue_item = MatchesV2DataPlayer.from_dict(blue_item_data)

            blue.append(blue_item)

        red = []
        _red = d.pop("red")
        for red_item_data in _red:
            red_item = MatchesV2DataPlayer.from_dict(red_item_data)

            red.append(red_item)

        matches_v2_data_players = cls(
            all_players=all_players,
            blue=blue,
            red=red,
        )

        matches_v2_data_players.additional_properties = d
        return matches_v2_data_players

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
