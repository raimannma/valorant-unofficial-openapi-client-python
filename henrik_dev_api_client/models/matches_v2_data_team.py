from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v2_data_team_roster import MatchesV2DataTeamRoster


T = TypeVar("T", bound="MatchesV2DataTeam")


@_attrs_define
class MatchesV2DataTeam:
    """
    Attributes:
        has_won (Union[None, Unset, bool]):
        roster (Union['MatchesV2DataTeamRoster', None, Unset]):
        rounds_lost (Union[None, Unset, int]):
        rounds_won (Union[None, Unset, int]):
    """

    has_won: Union[None, Unset, bool] = UNSET
    roster: Union["MatchesV2DataTeamRoster", None, Unset] = UNSET
    rounds_lost: Union[None, Unset, int] = UNSET
    rounds_won: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.matches_v2_data_team_roster import MatchesV2DataTeamRoster

        has_won: Union[None, Unset, bool]
        if isinstance(self.has_won, Unset):
            has_won = UNSET
        else:
            has_won = self.has_won

        roster: Union[None, Unset, dict[str, Any]]
        if isinstance(self.roster, Unset):
            roster = UNSET
        elif isinstance(self.roster, MatchesV2DataTeamRoster):
            roster = self.roster.to_dict()
        else:
            roster = self.roster

        rounds_lost: Union[None, Unset, int]
        if isinstance(self.rounds_lost, Unset):
            rounds_lost = UNSET
        else:
            rounds_lost = self.rounds_lost

        rounds_won: Union[None, Unset, int]
        if isinstance(self.rounds_won, Unset):
            rounds_won = UNSET
        else:
            rounds_won = self.rounds_won

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_won is not UNSET:
            field_dict["has_won"] = has_won
        if roster is not UNSET:
            field_dict["roster"] = roster
        if rounds_lost is not UNSET:
            field_dict["rounds_lost"] = rounds_lost
        if rounds_won is not UNSET:
            field_dict["rounds_won"] = rounds_won

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_team_roster import MatchesV2DataTeamRoster

        d = dict(src_dict)

        def _parse_has_won(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        has_won = _parse_has_won(d.pop("has_won", UNSET))

        def _parse_roster(data: object) -> Union["MatchesV2DataTeamRoster", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                roster_type_1 = MatchesV2DataTeamRoster.from_dict(data)

                return roster_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV2DataTeamRoster", None, Unset], data)

        roster = _parse_roster(d.pop("roster", UNSET))

        def _parse_rounds_lost(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rounds_lost = _parse_rounds_lost(d.pop("rounds_lost", UNSET))

        def _parse_rounds_won(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rounds_won = _parse_rounds_won(d.pop("rounds_won", UNSET))

        matches_v2_data_team = cls(
            has_won=has_won,
            roster=roster,
            rounds_lost=rounds_lost,
            rounds_won=rounds_won,
        )

        matches_v2_data_team.additional_properties = d
        return matches_v2_data_team

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
