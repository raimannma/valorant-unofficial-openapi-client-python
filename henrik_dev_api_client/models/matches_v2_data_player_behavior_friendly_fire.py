from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MatchesV2DataPlayerBehaviorFriendlyFire")


@_attrs_define
class MatchesV2DataPlayerBehaviorFriendlyFire:
    """
    Attributes:
        incoming (Union[None, Unset, float]):
        outgoing (Union[None, Unset, float]):
    """

    incoming: Union[None, Unset, float] = UNSET
    outgoing: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incoming: Union[None, Unset, float]
        if isinstance(self.incoming, Unset):
            incoming = UNSET
        else:
            incoming = self.incoming

        outgoing: Union[None, Unset, float]
        if isinstance(self.outgoing, Unset):
            outgoing = UNSET
        else:
            outgoing = self.outgoing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if incoming is not UNSET:
            field_dict["incoming"] = incoming
        if outgoing is not UNSET:
            field_dict["outgoing"] = outgoing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_incoming(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        incoming = _parse_incoming(d.pop("incoming", UNSET))

        def _parse_outgoing(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        outgoing = _parse_outgoing(d.pop("outgoing", UNSET))

        matches_v2_data_player_behavior_friendly_fire = cls(
            incoming=incoming,
            outgoing=outgoing,
        )

        matches_v2_data_player_behavior_friendly_fire.additional_properties = d
        return matches_v2_data_player_behavior_friendly_fire

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
