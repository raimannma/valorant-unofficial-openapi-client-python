from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PremierTeamGamesLeagueString")


@_attrs_define
class PremierTeamGamesLeagueString:
    """
    Attributes:
        id (str):
        points_after (int):
        points_before (int):
        started_at (str):
    """

    id: str
    points_after: int
    points_before: int
    started_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        points_after = self.points_after

        points_before = self.points_before

        started_at = self.started_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "points_after": points_after,
                "points_before": points_before,
                "started_at": started_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        points_after = d.pop("points_after")

        points_before = d.pop("points_before")

        started_at = d.pop("started_at")

        premier_team_games_league_string = cls(
            id=id,
            points_after=points_after,
            points_before=points_before,
            started_at=started_at,
        )

        premier_team_games_league_string.additional_properties = d
        return premier_team_games_league_string

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
