from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PremierTeamGamesTournament")


@_attrs_define
class PremierTeamGamesTournament:
    """
    Attributes:
        matches (list[str]):
        placement (int):
        placement_league_bonus (int):
        points_after (int):
        points_before (int):
        tournament_id (str):
    """

    matches: list[str]
    placement: int
    placement_league_bonus: int
    points_after: int
    points_before: int
    tournament_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matches = self.matches

        placement = self.placement

        placement_league_bonus = self.placement_league_bonus

        points_after = self.points_after

        points_before = self.points_before

        tournament_id = self.tournament_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "matches": matches,
                "placement": placement,
                "placement_league_bonus": placement_league_bonus,
                "points_after": points_after,
                "points_before": points_before,
                "tournament_id": tournament_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        matches = cast(list[str], d.pop("matches"))

        placement = d.pop("placement")

        placement_league_bonus = d.pop("placement_league_bonus")

        points_after = d.pop("points_after")

        points_before = d.pop("points_before")

        tournament_id = d.pop("tournament_id")

        premier_team_games_tournament = cls(
            matches=matches,
            placement=placement,
            placement_league_bonus=placement_league_bonus,
            points_after=points_after,
            points_before=points_before,
            tournament_id=tournament_id,
        )

        premier_team_games_tournament.additional_properties = d
        return premier_team_games_tournament

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
