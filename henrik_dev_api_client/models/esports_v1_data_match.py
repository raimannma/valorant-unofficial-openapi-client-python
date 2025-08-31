from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.esports_v1_data_match_game_type import EsportsV1DataMatchGameType
    from ..models.esports_v1_data_match_teams import EsportsV1DataMatchTeams


T = TypeVar("T", bound="EsportsV1DataMatch")


@_attrs_define
class EsportsV1DataMatch:
    """
    Attributes:
        game_type (EsportsV1DataMatchGameType):
        teams (list['EsportsV1DataMatchTeams']):
        id (Union[None, Unset, str]):
    """

    game_type: "EsportsV1DataMatchGameType"
    teams: list["EsportsV1DataMatchTeams"]
    id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_type = self.game_type.to_dict()

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "game_type": game_type,
                "teams": teams,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.esports_v1_data_match_game_type import EsportsV1DataMatchGameType
        from ..models.esports_v1_data_match_teams import EsportsV1DataMatchTeams

        d = dict(src_dict)
        game_type = EsportsV1DataMatchGameType.from_dict(d.pop("game_type"))

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = EsportsV1DataMatchTeams.from_dict(teams_item_data)

            teams.append(teams_item)

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        esports_v1_data_match = cls(
            game_type=game_type,
            teams=teams,
            id=id,
        )

        esports_v1_data_match.additional_properties = d
        return esports_v1_data_match

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
