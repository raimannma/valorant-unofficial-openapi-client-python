from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV4DataTeamRounds")


@_attrs_define
class MatchesV4DataTeamRounds:
    """
    Attributes:
        lost (int):
        won (int):
    """

    lost: int
    won: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lost = self.lost

        won = self.won

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lost": lost,
                "won": won,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        lost = d.pop("lost")

        won = d.pop("won")

        matches_v4_data_team_rounds = cls(
            lost=lost,
            won=won,
        )

        matches_v4_data_team_rounds.additional_properties = d
        return matches_v4_data_team_rounds

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
