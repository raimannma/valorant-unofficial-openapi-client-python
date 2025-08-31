from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.queue_status_v1id_name_pair import QueueStatusV1IDNamePair


T = TypeVar("T", bound="QueueStatusV1SkillDisparity")


@_attrs_define
class QueueStatusV1SkillDisparity:
    """
    Attributes:
        max_tier (QueueStatusV1IDNamePair):
        name (str):
        tier (int):
    """

    max_tier: "QueueStatusV1IDNamePair"
    name: str
    tier: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_tier = self.max_tier.to_dict()

        name = self.name

        tier = self.tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "max_tier": max_tier,
                "name": name,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queue_status_v1id_name_pair import QueueStatusV1IDNamePair

        d = dict(src_dict)
        max_tier = QueueStatusV1IDNamePair.from_dict(d.pop("max_tier"))

        name = d.pop("name")

        tier = d.pop("tier")

        queue_status_v1_skill_disparity = cls(
            max_tier=max_tier,
            name=name,
            tier=tier,
        )

        queue_status_v1_skill_disparity.additional_properties = d
        return queue_status_v1_skill_disparity

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
