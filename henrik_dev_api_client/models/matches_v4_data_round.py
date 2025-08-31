from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v4_data_round_defuse import MatchesV4DataRoundDefuse
    from ..models.matches_v4_data_round_plant import MatchesV4DataRoundPlant
    from ..models.matches_v4_data_round_player_stats import MatchesV4DataRoundPlayerStats


T = TypeVar("T", bound="MatchesV4DataRound")


@_attrs_define
class MatchesV4DataRound:
    """
    Attributes:
        ceremony (str):
        id (int):
        result (str):
        stats (list['MatchesV4DataRoundPlayerStats']):
        winning_team (str):
        defuse (Union['MatchesV4DataRoundDefuse', None, Unset]):
        plant (Union['MatchesV4DataRoundPlant', None, Unset]):
    """

    ceremony: str
    id: int
    result: str
    stats: list["MatchesV4DataRoundPlayerStats"]
    winning_team: str
    defuse: Union["MatchesV4DataRoundDefuse", None, Unset] = UNSET
    plant: Union["MatchesV4DataRoundPlant", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.matches_v4_data_round_defuse import MatchesV4DataRoundDefuse
        from ..models.matches_v4_data_round_plant import MatchesV4DataRoundPlant

        ceremony = self.ceremony

        id = self.id

        result = self.result

        stats = []
        for stats_item_data in self.stats:
            stats_item = stats_item_data.to_dict()
            stats.append(stats_item)

        winning_team = self.winning_team

        defuse: Union[None, Unset, dict[str, Any]]
        if isinstance(self.defuse, Unset):
            defuse = UNSET
        elif isinstance(self.defuse, MatchesV4DataRoundDefuse):
            defuse = self.defuse.to_dict()
        else:
            defuse = self.defuse

        plant: Union[None, Unset, dict[str, Any]]
        if isinstance(self.plant, Unset):
            plant = UNSET
        elif isinstance(self.plant, MatchesV4DataRoundPlant):
            plant = self.plant.to_dict()
        else:
            plant = self.plant

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ceremony": ceremony,
                "id": id,
                "result": result,
                "stats": stats,
                "winning_team": winning_team,
            }
        )
        if defuse is not UNSET:
            field_dict["defuse"] = defuse
        if plant is not UNSET:
            field_dict["plant"] = plant

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_round_defuse import MatchesV4DataRoundDefuse
        from ..models.matches_v4_data_round_plant import MatchesV4DataRoundPlant
        from ..models.matches_v4_data_round_player_stats import MatchesV4DataRoundPlayerStats

        d = dict(src_dict)
        ceremony = d.pop("ceremony")

        id = d.pop("id")

        result = d.pop("result")

        stats = []
        _stats = d.pop("stats")
        for stats_item_data in _stats:
            stats_item = MatchesV4DataRoundPlayerStats.from_dict(stats_item_data)

            stats.append(stats_item)

        winning_team = d.pop("winning_team")

        def _parse_defuse(data: object) -> Union["MatchesV4DataRoundDefuse", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                defuse_type_1 = MatchesV4DataRoundDefuse.from_dict(data)

                return defuse_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV4DataRoundDefuse", None, Unset], data)

        defuse = _parse_defuse(d.pop("defuse", UNSET))

        def _parse_plant(data: object) -> Union["MatchesV4DataRoundPlant", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                plant_type_1 = MatchesV4DataRoundPlant.from_dict(data)

                return plant_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV4DataRoundPlant", None, Unset], data)

        plant = _parse_plant(d.pop("plant", UNSET))

        matches_v4_data_round = cls(
            ceremony=ceremony,
            id=id,
            result=result,
            stats=stats,
            winning_team=winning_team,
            defuse=defuse,
            plant=plant,
        )

        matches_v4_data_round.additional_properties = d
        return matches_v4_data_round

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
