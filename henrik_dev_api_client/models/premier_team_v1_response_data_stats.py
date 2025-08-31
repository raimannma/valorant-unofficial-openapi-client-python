from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PremierTeamV1ResponseDataStats")


@_attrs_define
class PremierTeamV1ResponseDataStats:
    """
    Attributes:
        losses (int):
        matches (int):
        rounds_lost (int):
        rounds_won (int):
        wins (int):
    """

    losses: int
    matches: int
    rounds_lost: int
    rounds_won: int
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        losses = self.losses

        matches = self.matches

        rounds_lost = self.rounds_lost

        rounds_won = self.rounds_won

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "losses": losses,
                "matches": matches,
                "rounds_lost": rounds_lost,
                "rounds_won": rounds_won,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        losses = d.pop("losses")

        matches = d.pop("matches")

        rounds_lost = d.pop("rounds_lost")

        rounds_won = d.pop("rounds_won")

        wins = d.pop("wins")

        premier_team_v1_response_data_stats = cls(
            losses=losses,
            matches=matches,
            rounds_lost=rounds_lost,
            rounds_won=rounds_won,
            wins=wins,
        )

        premier_team_v1_response_data_stats.additional_properties = d
        return premier_team_v1_response_data_stats

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
