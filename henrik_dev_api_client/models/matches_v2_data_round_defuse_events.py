from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
    from ..models.matches_v2_data_round_player import MatchesV2DataRoundPlayer
    from ..models.matches_v2_data_round_player_locations_on_event import MatchesV2DataRoundPlayerLocationsOnEvent


T = TypeVar("T", bound="MatchesV2DataRoundDefuseEvents")


@_attrs_define
class MatchesV2DataRoundDefuseEvents:
    """
    Attributes:
        defuse_location (Union['MatchesV2DataRoundEventLocation', None, Unset]):
        defuse_time_in_round (Union[None, Unset, int]):
        defused_by (Union['MatchesV2DataRoundPlayer', None, Unset]):
        player_locations_on_defuse (Union[None, Unset, list['MatchesV2DataRoundPlayerLocationsOnEvent']]):
    """

    defuse_location: Union["MatchesV2DataRoundEventLocation", None, Unset] = UNSET
    defuse_time_in_round: Union[None, Unset, int] = UNSET
    defused_by: Union["MatchesV2DataRoundPlayer", None, Unset] = UNSET
    player_locations_on_defuse: Union[None, Unset, list["MatchesV2DataRoundPlayerLocationsOnEvent"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
        from ..models.matches_v2_data_round_player import MatchesV2DataRoundPlayer

        defuse_location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.defuse_location, Unset):
            defuse_location = UNSET
        elif isinstance(self.defuse_location, MatchesV2DataRoundEventLocation):
            defuse_location = self.defuse_location.to_dict()
        else:
            defuse_location = self.defuse_location

        defuse_time_in_round: Union[None, Unset, int]
        if isinstance(self.defuse_time_in_round, Unset):
            defuse_time_in_round = UNSET
        else:
            defuse_time_in_round = self.defuse_time_in_round

        defused_by: Union[None, Unset, dict[str, Any]]
        if isinstance(self.defused_by, Unset):
            defused_by = UNSET
        elif isinstance(self.defused_by, MatchesV2DataRoundPlayer):
            defused_by = self.defused_by.to_dict()
        else:
            defused_by = self.defused_by

        player_locations_on_defuse: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.player_locations_on_defuse, Unset):
            player_locations_on_defuse = UNSET
        elif isinstance(self.player_locations_on_defuse, list):
            player_locations_on_defuse = []
            for player_locations_on_defuse_type_0_item_data in self.player_locations_on_defuse:
                player_locations_on_defuse_type_0_item = player_locations_on_defuse_type_0_item_data.to_dict()
                player_locations_on_defuse.append(player_locations_on_defuse_type_0_item)

        else:
            player_locations_on_defuse = self.player_locations_on_defuse

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if defuse_location is not UNSET:
            field_dict["defuse_location"] = defuse_location
        if defuse_time_in_round is not UNSET:
            field_dict["defuse_time_in_round"] = defuse_time_in_round
        if defused_by is not UNSET:
            field_dict["defused_by"] = defused_by
        if player_locations_on_defuse is not UNSET:
            field_dict["player_locations_on_defuse"] = player_locations_on_defuse

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
        from ..models.matches_v2_data_round_player import MatchesV2DataRoundPlayer
        from ..models.matches_v2_data_round_player_locations_on_event import MatchesV2DataRoundPlayerLocationsOnEvent

        d = dict(src_dict)

        def _parse_defuse_location(data: object) -> Union["MatchesV2DataRoundEventLocation", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                defuse_location_type_1 = MatchesV2DataRoundEventLocation.from_dict(data)

                return defuse_location_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV2DataRoundEventLocation", None, Unset], data)

        defuse_location = _parse_defuse_location(d.pop("defuse_location", UNSET))

        def _parse_defuse_time_in_round(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        defuse_time_in_round = _parse_defuse_time_in_round(d.pop("defuse_time_in_round", UNSET))

        def _parse_defused_by(data: object) -> Union["MatchesV2DataRoundPlayer", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                defused_by_type_1 = MatchesV2DataRoundPlayer.from_dict(data)

                return defused_by_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV2DataRoundPlayer", None, Unset], data)

        defused_by = _parse_defused_by(d.pop("defused_by", UNSET))

        def _parse_player_locations_on_defuse(
            data: object,
        ) -> Union[None, Unset, list["MatchesV2DataRoundPlayerLocationsOnEvent"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                player_locations_on_defuse_type_0 = []
                _player_locations_on_defuse_type_0 = data
                for player_locations_on_defuse_type_0_item_data in _player_locations_on_defuse_type_0:
                    player_locations_on_defuse_type_0_item = MatchesV2DataRoundPlayerLocationsOnEvent.from_dict(
                        player_locations_on_defuse_type_0_item_data
                    )

                    player_locations_on_defuse_type_0.append(player_locations_on_defuse_type_0_item)

                return player_locations_on_defuse_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MatchesV2DataRoundPlayerLocationsOnEvent"]], data)

        player_locations_on_defuse = _parse_player_locations_on_defuse(d.pop("player_locations_on_defuse", UNSET))

        matches_v2_data_round_defuse_events = cls(
            defuse_location=defuse_location,
            defuse_time_in_round=defuse_time_in_round,
            defused_by=defused_by,
            player_locations_on_defuse=player_locations_on_defuse,
        )

        matches_v2_data_round_defuse_events.additional_properties = d
        return matches_v2_data_round_defuse_events

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
