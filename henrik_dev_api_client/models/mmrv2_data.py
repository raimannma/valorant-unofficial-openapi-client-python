from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mmrv2_current_data import MMRV2CurrentData
    from ..models.mmrv2_highest_rank import MMRV2HighestRank


T = TypeVar("T", bound="MMRV2Data")


@_attrs_define
class MMRV2Data:
    """
    Attributes:
        by_season (Any):
        current_data (MMRV2CurrentData):
        highest_rank (MMRV2HighestRank):
        name (str):
        puuid (str):
        tag (str):
    """

    by_season: Any
    current_data: "MMRV2CurrentData"
    highest_rank: "MMRV2HighestRank"
    name: str
    puuid: str
    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        by_season = self.by_season

        current_data = self.current_data.to_dict()

        highest_rank = self.highest_rank.to_dict()

        name = self.name

        puuid = self.puuid

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "by_season": by_season,
                "current_data": current_data,
                "highest_rank": highest_rank,
                "name": name,
                "puuid": puuid,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mmrv2_current_data import MMRV2CurrentData
        from ..models.mmrv2_highest_rank import MMRV2HighestRank

        d = dict(src_dict)
        by_season = d.pop("by_season")

        current_data = MMRV2CurrentData.from_dict(d.pop("current_data"))

        highest_rank = MMRV2HighestRank.from_dict(d.pop("highest_rank"))

        name = d.pop("name")

        puuid = d.pop("puuid")

        tag = d.pop("tag")

        mmrv2_data = cls(
            by_season=by_season,
            current_data=current_data,
            highest_rank=highest_rank,
            name=name,
            puuid=puuid,
            tag=tag,
        )

        mmrv2_data.additional_properties = d
        return mmrv2_data

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
