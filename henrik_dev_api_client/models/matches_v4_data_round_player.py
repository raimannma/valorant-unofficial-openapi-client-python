from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV4DataRoundPlayer")


@_attrs_define
class MatchesV4DataRoundPlayer:
    """
    Attributes:
        name (str):
        puuid (str):
        tag (str):
        team (str):
    """

    name: str
    puuid: str
    tag: str
    team: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        puuid = self.puuid

        tag = self.tag

        team = self.team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "puuid": puuid,
                "tag": tag,
                "team": team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        puuid = d.pop("puuid")

        tag = d.pop("tag")

        team = d.pop("team")

        matches_v4_data_round_player = cls(
            name=name,
            puuid=puuid,
            tag=tag,
            team=team,
        )

        matches_v4_data_round_player.additional_properties = d
        return matches_v4_data_round_player

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
