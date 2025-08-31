from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
    from ..models.matches_v2_data_round_player import MatchesV2DataRoundPlayer
    from ..models.matches_v2_data_round_player_locations_on_event import MatchesV2DataRoundPlayerLocationsOnEvent


T = TypeVar("T", bound="MatchesV2DataRoundPlantEvents")


@_attrs_define
class MatchesV2DataRoundPlantEvents:
    """
    Attributes:
        plant_location (Union['MatchesV2DataRoundEventLocation', None, Unset]):
        plant_site (Union[None, Unset, str]):
        plant_time_in_round (Union[None, Unset, int]):
        planted_by (Union['MatchesV2DataRoundPlayer', None, Unset]):
        player_locations_on_plant (Union[None, Unset, list['MatchesV2DataRoundPlayerLocationsOnEvent']]):
    """

    plant_location: Union["MatchesV2DataRoundEventLocation", None, Unset] = UNSET
    plant_site: Union[None, Unset, str] = UNSET
    plant_time_in_round: Union[None, Unset, int] = UNSET
    planted_by: Union["MatchesV2DataRoundPlayer", None, Unset] = UNSET
    player_locations_on_plant: Union[None, Unset, list["MatchesV2DataRoundPlayerLocationsOnEvent"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
        from ..models.matches_v2_data_round_player import MatchesV2DataRoundPlayer

        plant_location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.plant_location, Unset):
            plant_location = UNSET
        elif isinstance(self.plant_location, MatchesV2DataRoundEventLocation):
            plant_location = self.plant_location.to_dict()
        else:
            plant_location = self.plant_location

        plant_site: Union[None, Unset, str]
        if isinstance(self.plant_site, Unset):
            plant_site = UNSET
        else:
            plant_site = self.plant_site

        plant_time_in_round: Union[None, Unset, int]
        if isinstance(self.plant_time_in_round, Unset):
            plant_time_in_round = UNSET
        else:
            plant_time_in_round = self.plant_time_in_round

        planted_by: Union[None, Unset, dict[str, Any]]
        if isinstance(self.planted_by, Unset):
            planted_by = UNSET
        elif isinstance(self.planted_by, MatchesV2DataRoundPlayer):
            planted_by = self.planted_by.to_dict()
        else:
            planted_by = self.planted_by

        player_locations_on_plant: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.player_locations_on_plant, Unset):
            player_locations_on_plant = UNSET
        elif isinstance(self.player_locations_on_plant, list):
            player_locations_on_plant = []
            for player_locations_on_plant_type_0_item_data in self.player_locations_on_plant:
                player_locations_on_plant_type_0_item = player_locations_on_plant_type_0_item_data.to_dict()
                player_locations_on_plant.append(player_locations_on_plant_type_0_item)

        else:
            player_locations_on_plant = self.player_locations_on_plant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if plant_location is not UNSET:
            field_dict["plant_location"] = plant_location
        if plant_site is not UNSET:
            field_dict["plant_site"] = plant_site
        if plant_time_in_round is not UNSET:
            field_dict["plant_time_in_round"] = plant_time_in_round
        if planted_by is not UNSET:
            field_dict["planted_by"] = planted_by
        if player_locations_on_plant is not UNSET:
            field_dict["player_locations_on_plant"] = player_locations_on_plant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_round_event_location import MatchesV2DataRoundEventLocation
        from ..models.matches_v2_data_round_player import MatchesV2DataRoundPlayer
        from ..models.matches_v2_data_round_player_locations_on_event import MatchesV2DataRoundPlayerLocationsOnEvent

        d = dict(src_dict)

        def _parse_plant_location(data: object) -> Union["MatchesV2DataRoundEventLocation", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                plant_location_type_1 = MatchesV2DataRoundEventLocation.from_dict(data)

                return plant_location_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV2DataRoundEventLocation", None, Unset], data)

        plant_location = _parse_plant_location(d.pop("plant_location", UNSET))

        def _parse_plant_site(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        plant_site = _parse_plant_site(d.pop("plant_site", UNSET))

        def _parse_plant_time_in_round(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        plant_time_in_round = _parse_plant_time_in_round(d.pop("plant_time_in_round", UNSET))

        def _parse_planted_by(data: object) -> Union["MatchesV2DataRoundPlayer", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                planted_by_type_1 = MatchesV2DataRoundPlayer.from_dict(data)

                return planted_by_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV2DataRoundPlayer", None, Unset], data)

        planted_by = _parse_planted_by(d.pop("planted_by", UNSET))

        def _parse_player_locations_on_plant(
            data: object,
        ) -> Union[None, Unset, list["MatchesV2DataRoundPlayerLocationsOnEvent"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                player_locations_on_plant_type_0 = []
                _player_locations_on_plant_type_0 = data
                for player_locations_on_plant_type_0_item_data in _player_locations_on_plant_type_0:
                    player_locations_on_plant_type_0_item = MatchesV2DataRoundPlayerLocationsOnEvent.from_dict(
                        player_locations_on_plant_type_0_item_data
                    )

                    player_locations_on_plant_type_0.append(player_locations_on_plant_type_0_item)

                return player_locations_on_plant_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["MatchesV2DataRoundPlayerLocationsOnEvent"]], data)

        player_locations_on_plant = _parse_player_locations_on_plant(d.pop("player_locations_on_plant", UNSET))

        matches_v2_data_round_plant_events = cls(
            plant_location=plant_location,
            plant_site=plant_site,
            plant_time_in_round=plant_time_in_round,
            planted_by=planted_by,
            player_locations_on_plant=player_locations_on_plant,
        )

        matches_v2_data_round_plant_events.additional_properties = d
        return matches_v2_data_round_plant_events

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
