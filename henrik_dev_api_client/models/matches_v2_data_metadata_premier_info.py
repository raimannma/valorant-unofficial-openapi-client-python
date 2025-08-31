from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchesV2DataMetadataPremierInfo")


@_attrs_define
class MatchesV2DataMetadataPremierInfo:
    """
    Attributes:
        matchup_id (Union[None, Unset, str]):
        tournament_id (Union[None, Unset, str]):
    """

    matchup_id: Union[None, Unset, str] = UNSET
    tournament_id: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        matchup_id: Union[None, Unset, str]
        if isinstance(self.matchup_id, Unset):
            matchup_id = UNSET
        else:
            matchup_id = self.matchup_id

        tournament_id: Union[None, Unset, str]
        if isinstance(self.tournament_id, Unset):
            tournament_id = UNSET
        else:
            tournament_id = self.tournament_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if matchup_id is not UNSET:
            field_dict["matchup_id"] = matchup_id
        if tournament_id is not UNSET:
            field_dict["tournament_id"] = tournament_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_matchup_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        matchup_id = _parse_matchup_id(d.pop("matchup_id", UNSET))

        def _parse_tournament_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tournament_id = _parse_tournament_id(d.pop("tournament_id", UNSET))

        matches_v2_data_metadata_premier_info = cls(
            matchup_id=matchup_id,
            tournament_id=tournament_id,
        )

        matches_v2_data_metadata_premier_info.additional_properties = d
        return matches_v2_data_metadata_premier_info

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
