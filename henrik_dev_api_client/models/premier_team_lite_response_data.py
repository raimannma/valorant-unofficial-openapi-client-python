from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.premier_team_v1_response_data_customization import PremierTeamV1ResponseDataCustomization


T = TypeVar("T", bound="PremierTeamLiteResponseData")


@_attrs_define
class PremierTeamLiteResponseData:
    """
    Attributes:
        affinity (str):
        conference (str):
        customization (PremierTeamV1ResponseDataCustomization):
        division (int):
        id (str):
        losses (int):
        name (str):
        ranking (int):
        region (str):
        score (int):
        tag (str):
        updated_at (str):
        wins (int):
    """

    affinity: str
    conference: str
    customization: "PremierTeamV1ResponseDataCustomization"
    division: int
    id: str
    losses: int
    name: str
    ranking: int
    region: str
    score: int
    tag: str
    updated_at: str
    wins: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        affinity = self.affinity

        conference = self.conference

        customization = self.customization.to_dict()

        division = self.division

        id = self.id

        losses = self.losses

        name = self.name

        ranking = self.ranking

        region = self.region

        score = self.score

        tag = self.tag

        updated_at = self.updated_at

        wins = self.wins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "affinity": affinity,
                "conference": conference,
                "customization": customization,
                "division": division,
                "id": id,
                "losses": losses,
                "name": name,
                "ranking": ranking,
                "region": region,
                "score": score,
                "tag": tag,
                "updated_at": updated_at,
                "wins": wins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.premier_team_v1_response_data_customization import PremierTeamV1ResponseDataCustomization

        d = dict(src_dict)
        affinity = d.pop("affinity")

        conference = d.pop("conference")

        customization = PremierTeamV1ResponseDataCustomization.from_dict(d.pop("customization"))

        division = d.pop("division")

        id = d.pop("id")

        losses = d.pop("losses")

        name = d.pop("name")

        ranking = d.pop("ranking")

        region = d.pop("region")

        score = d.pop("score")

        tag = d.pop("tag")

        updated_at = d.pop("updated_at")

        wins = d.pop("wins")

        premier_team_lite_response_data = cls(
            affinity=affinity,
            conference=conference,
            customization=customization,
            division=division,
            id=id,
            losses=losses,
            name=name,
            ranking=ranking,
            region=region,
            score=score,
            tag=tag,
            updated_at=updated_at,
            wins=wins,
        )

        premier_team_lite_response_data.additional_properties = d
        return premier_team_lite_response_data

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
