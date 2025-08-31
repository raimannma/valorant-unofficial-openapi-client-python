from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.premier_team_member import PremierTeamMember
    from ..models.premier_team_v1_response_data_customization import PremierTeamV1ResponseDataCustomization
    from ..models.premier_team_v1_response_data_placement import PremierTeamV1ResponseDataPlacement
    from ..models.premier_team_v1_response_data_stats import PremierTeamV1ResponseDataStats


T = TypeVar("T", bound="PremierTeamV1ResponseData")


@_attrs_define
class PremierTeamV1ResponseData:
    """
    Attributes:
        customization (PremierTeamV1ResponseDataCustomization):
        enrolled (bool):
        id (str):
        member (list['PremierTeamMember']):
        name (str):
        placement (PremierTeamV1ResponseDataPlacement):
        stats (PremierTeamV1ResponseDataStats):
        tag (str):
    """

    customization: "PremierTeamV1ResponseDataCustomization"
    enrolled: bool
    id: str
    member: list["PremierTeamMember"]
    name: str
    placement: "PremierTeamV1ResponseDataPlacement"
    stats: "PremierTeamV1ResponseDataStats"
    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customization = self.customization.to_dict()

        enrolled = self.enrolled

        id = self.id

        member = []
        for member_item_data in self.member:
            member_item = member_item_data.to_dict()
            member.append(member_item)

        name = self.name

        placement = self.placement.to_dict()

        stats = self.stats.to_dict()

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customization": customization,
                "enrolled": enrolled,
                "id": id,
                "member": member,
                "name": name,
                "placement": placement,
                "stats": stats,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.premier_team_member import PremierTeamMember
        from ..models.premier_team_v1_response_data_customization import PremierTeamV1ResponseDataCustomization
        from ..models.premier_team_v1_response_data_placement import PremierTeamV1ResponseDataPlacement
        from ..models.premier_team_v1_response_data_stats import PremierTeamV1ResponseDataStats

        d = dict(src_dict)
        customization = PremierTeamV1ResponseDataCustomization.from_dict(d.pop("customization"))

        enrolled = d.pop("enrolled")

        id = d.pop("id")

        member = []
        _member = d.pop("member")
        for member_item_data in _member:
            member_item = PremierTeamMember.from_dict(member_item_data)

            member.append(member_item)

        name = d.pop("name")

        placement = PremierTeamV1ResponseDataPlacement.from_dict(d.pop("placement"))

        stats = PremierTeamV1ResponseDataStats.from_dict(d.pop("stats"))

        tag = d.pop("tag")

        premier_team_v1_response_data = cls(
            customization=customization,
            enrolled=enrolled,
            id=id,
            member=member,
            name=name,
            placement=placement,
            stats=stats,
            tag=tag,
        )

        premier_team_v1_response_data.additional_properties = d
        return premier_team_v1_response_data

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
