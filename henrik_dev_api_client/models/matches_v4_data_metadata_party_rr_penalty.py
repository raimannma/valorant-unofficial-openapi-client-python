from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV4DataMetadataPartyRRPenalty")


@_attrs_define
class MatchesV4DataMetadataPartyRRPenalty:
    """
    Attributes:
        party_id (str):
        penalty (float):
    """

    party_id: str
    penalty: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        party_id = self.party_id

        penalty = self.penalty

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "party_id": party_id,
                "penalty": penalty,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        party_id = d.pop("party_id")

        penalty = d.pop("penalty")

        matches_v4_data_metadata_party_rr_penalty = cls(
            party_id=party_id,
            penalty=penalty,
        )

        matches_v4_data_metadata_party_rr_penalty.additional_properties = d
        return matches_v4_data_metadata_party_rr_penalty

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
