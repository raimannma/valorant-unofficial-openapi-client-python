from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_team import MatchesV2DataTeam


T = TypeVar("T", bound="MatchesV2DataTeams")


@_attrs_define
class MatchesV2DataTeams:
    """
    Attributes:
        blue (MatchesV2DataTeam):
        red (MatchesV2DataTeam):
    """

    blue: "MatchesV2DataTeam"
    red: "MatchesV2DataTeam"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        blue = self.blue.to_dict()

        red = self.red.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blue": blue,
                "red": red,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_team import MatchesV2DataTeam

        d = dict(src_dict)
        blue = MatchesV2DataTeam.from_dict(d.pop("blue"))

        red = MatchesV2DataTeam.from_dict(d.pop("red"))

        matches_v2_data_teams = cls(
            blue=blue,
            red=red,
        )

        matches_v2_data_teams.additional_properties = d
        return matches_v2_data_teams

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
