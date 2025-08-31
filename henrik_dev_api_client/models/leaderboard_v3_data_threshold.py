from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leaderboard_v3_data_threshold_tier import LeaderboardV3DataThresholdTier


T = TypeVar("T", bound="LeaderboardV3DataThreshold")


@_attrs_define
class LeaderboardV3DataThreshold:
    """
    Attributes:
        start_index (int):
        threshold (int):
        tier (LeaderboardV3DataThresholdTier):
    """

    start_index: int
    threshold: int
    tier: "LeaderboardV3DataThresholdTier"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        start_index = self.start_index

        threshold = self.threshold

        tier = self.tier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "start_index": start_index,
                "threshold": threshold,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_v3_data_threshold_tier import LeaderboardV3DataThresholdTier

        d = dict(src_dict)
        start_index = d.pop("start_index")

        threshold = d.pop("threshold")

        tier = LeaderboardV3DataThresholdTier.from_dict(d.pop("tier"))

        leaderboard_v3_data_threshold = cls(
            start_index=start_index,
            threshold=threshold,
            tier=tier,
        )

        leaderboard_v3_data_threshold.additional_properties = d
        return leaderboard_v3_data_threshold

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
