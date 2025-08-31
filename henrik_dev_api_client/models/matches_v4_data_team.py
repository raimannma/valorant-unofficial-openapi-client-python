from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v4_data_team_premier_roster import MatchesV4DataTeamPremierRoster
    from ..models.matches_v4_data_team_rounds import MatchesV4DataTeamRounds


T = TypeVar("T", bound="MatchesV4DataTeam")


@_attrs_define
class MatchesV4DataTeam:
    """
    Attributes:
        rounds (MatchesV4DataTeamRounds):
        team_id (str):
        won (bool):
        premier_roster (Union['MatchesV4DataTeamPremierRoster', None, Unset]):
    """

    rounds: "MatchesV4DataTeamRounds"
    team_id: str
    won: bool
    premier_roster: Union["MatchesV4DataTeamPremierRoster", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.matches_v4_data_team_premier_roster import MatchesV4DataTeamPremierRoster

        rounds = self.rounds.to_dict()

        team_id = self.team_id

        won = self.won

        premier_roster: Union[None, Unset, dict[str, Any]]
        if isinstance(self.premier_roster, Unset):
            premier_roster = UNSET
        elif isinstance(self.premier_roster, MatchesV4DataTeamPremierRoster):
            premier_roster = self.premier_roster.to_dict()
        else:
            premier_roster = self.premier_roster

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "rounds": rounds,
                "team_id": team_id,
                "won": won,
            }
        )
        if premier_roster is not UNSET:
            field_dict["premier_roster"] = premier_roster

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_team_premier_roster import MatchesV4DataTeamPremierRoster
        from ..models.matches_v4_data_team_rounds import MatchesV4DataTeamRounds

        d = dict(src_dict)
        rounds = MatchesV4DataTeamRounds.from_dict(d.pop("rounds"))

        team_id = d.pop("team_id")

        won = d.pop("won")

        def _parse_premier_roster(data: object) -> Union["MatchesV4DataTeamPremierRoster", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                premier_roster_type_1 = MatchesV4DataTeamPremierRoster.from_dict(data)

                return premier_roster_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV4DataTeamPremierRoster", None, Unset], data)

        premier_roster = _parse_premier_roster(d.pop("premier_roster", UNSET))

        matches_v4_data_team = cls(
            rounds=rounds,
            team_id=team_id,
            won=won,
            premier_roster=premier_roster,
        )

        matches_v4_data_team.additional_properties = d
        return matches_v4_data_team

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
