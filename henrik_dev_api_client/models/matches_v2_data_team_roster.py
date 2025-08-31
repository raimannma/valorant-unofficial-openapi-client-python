from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_team_roster_customization import MatchesV2DataTeamRosterCustomization


T = TypeVar("T", bound="MatchesV2DataTeamRoster")


@_attrs_define
class MatchesV2DataTeamRoster:
    """
    Attributes:
        customization (MatchesV2DataTeamRosterCustomization):
        id (str):
        members (list[str]):
        name (str):
        tag (str):
    """

    customization: "MatchesV2DataTeamRosterCustomization"
    id: str
    members: list[str]
    name: str
    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customization = self.customization.to_dict()

        id = self.id

        members = self.members

        name = self.name

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customization": customization,
                "id": id,
                "members": members,
                "name": name,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_team_roster_customization import MatchesV2DataTeamRosterCustomization

        d = dict(src_dict)
        customization = MatchesV2DataTeamRosterCustomization.from_dict(d.pop("customization"))

        id = d.pop("id")

        members = cast(list[str], d.pop("members"))

        name = d.pop("name")

        tag = d.pop("tag")

        matches_v2_data_team_roster = cls(
            customization=customization,
            id=id,
            members=members,
            name=name,
            tag=tag,
        )

        matches_v2_data_team_roster.additional_properties = d
        return matches_v2_data_team_roster

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
