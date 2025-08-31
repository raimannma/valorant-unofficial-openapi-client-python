from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV4DataRoundPlayerStatsStats")


@_attrs_define
class MatchesV4DataRoundPlayerStatsStats:
    """
    Attributes:
        bodyshots (int):
        headshots (int):
        kills (int):
        legshots (int):
        score (int):
    """

    bodyshots: int
    headshots: int
    kills: int
    legshots: int
    score: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bodyshots = self.bodyshots

        headshots = self.headshots

        kills = self.kills

        legshots = self.legshots

        score = self.score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bodyshots": bodyshots,
                "headshots": headshots,
                "kills": kills,
                "legshots": legshots,
                "score": score,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bodyshots = d.pop("bodyshots")

        headshots = d.pop("headshots")

        kills = d.pop("kills")

        legshots = d.pop("legshots")

        score = d.pop("score")

        matches_v4_data_round_player_stats_stats = cls(
            bodyshots=bodyshots,
            headshots=headshots,
            kills=kills,
            legshots=legshots,
            score=score,
        )

        matches_v4_data_round_player_stats_stats.additional_properties = d
        return matches_v4_data_round_player_stats_stats

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
