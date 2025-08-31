from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.esports_v1_data_match_teams_record import EsportsV1DataMatchTeamsRecord


T = TypeVar("T", bound="EsportsV1DataMatchTeams")


@_attrs_define
class EsportsV1DataMatchTeams:
    """
    Attributes:
        code (str):
        game_wins (int):
        has_won (bool):
        icon (str):
        name (str):
        record (EsportsV1DataMatchTeamsRecord):
    """

    code: str
    game_wins: int
    has_won: bool
    icon: str
    name: str
    record: "EsportsV1DataMatchTeamsRecord"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        game_wins = self.game_wins

        has_won = self.has_won

        icon = self.icon

        name = self.name

        record = self.record.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "game_wins": game_wins,
                "has_won": has_won,
                "icon": icon,
                "name": name,
                "record": record,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.esports_v1_data_match_teams_record import EsportsV1DataMatchTeamsRecord

        d = dict(src_dict)
        code = d.pop("code")

        game_wins = d.pop("game_wins")

        has_won = d.pop("has_won")

        icon = d.pop("icon")

        name = d.pop("name")

        record = EsportsV1DataMatchTeamsRecord.from_dict(d.pop("record"))

        esports_v1_data_match_teams = cls(
            code=code,
            game_wins=game_wins,
            has_won=has_won,
            icon=icon,
            name=name,
            record=record,
        )

        esports_v1_data_match_teams.additional_properties = d
        return esports_v1_data_match_teams

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
