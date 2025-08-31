from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.premier_team_games_league_string import PremierTeamGamesLeagueString
    from ..models.premier_team_games_tournament import PremierTeamGamesTournament


T = TypeVar("T", bound="PremierTeamHistoryV1ResponseData")


@_attrs_define
class PremierTeamHistoryV1ResponseData:
    """
    Attributes:
        league_matches (list['PremierTeamGamesLeagueString']):
        tournament_matches (list['PremierTeamGamesTournament']):
    """

    league_matches: list["PremierTeamGamesLeagueString"]
    tournament_matches: list["PremierTeamGamesTournament"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        league_matches = []
        for league_matches_item_data in self.league_matches:
            league_matches_item = league_matches_item_data.to_dict()
            league_matches.append(league_matches_item)

        tournament_matches = []
        for tournament_matches_item_data in self.tournament_matches:
            tournament_matches_item = tournament_matches_item_data.to_dict()
            tournament_matches.append(tournament_matches_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "league_matches": league_matches,
                "tournament_matches": tournament_matches,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.premier_team_games_league_string import PremierTeamGamesLeagueString
        from ..models.premier_team_games_tournament import PremierTeamGamesTournament

        d = dict(src_dict)
        league_matches = []
        _league_matches = d.pop("league_matches")
        for league_matches_item_data in _league_matches:
            league_matches_item = PremierTeamGamesLeagueString.from_dict(league_matches_item_data)

            league_matches.append(league_matches_item)

        tournament_matches = []
        _tournament_matches = d.pop("tournament_matches")
        for tournament_matches_item_data in _tournament_matches:
            tournament_matches_item = PremierTeamGamesTournament.from_dict(tournament_matches_item_data)

            tournament_matches.append(tournament_matches_item)

        premier_team_history_v1_response_data = cls(
            league_matches=league_matches,
            tournament_matches=tournament_matches,
        )

        premier_team_history_v1_response_data.additional_properties = d
        return premier_team_history_v1_response_data

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
