from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PremierTeamV1ResponseDataPlacement")


@_attrs_define
class PremierTeamV1ResponseDataPlacement:
    """
    Attributes:
        conference (str):
        division (int):
        place (int):
        points (int):
    """

    conference: str
    division: int
    place: int
    points: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conference = self.conference

        division = self.division

        place = self.place

        points = self.points

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "conference": conference,
                "division": division,
                "place": place,
                "points": points,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        conference = d.pop("conference")

        division = d.pop("division")

        place = d.pop("place")

        points = d.pop("points")

        premier_team_v1_response_data_placement = cls(
            conference=conference,
            division=division,
            place=place,
            points=points,
        )

        premier_team_v1_response_data_placement.additional_properties = d
        return premier_team_v1_response_data_placement

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
