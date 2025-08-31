from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_player_economy_value import MatchesV2DataPlayerEconomyValue


T = TypeVar("T", bound="MatchesV2DataPlayerEconomy")


@_attrs_define
class MatchesV2DataPlayerEconomy:
    """
    Attributes:
        loadout_value (MatchesV2DataPlayerEconomyValue):
        spent (MatchesV2DataPlayerEconomyValue):
    """

    loadout_value: "MatchesV2DataPlayerEconomyValue"
    spent: "MatchesV2DataPlayerEconomyValue"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        loadout_value = self.loadout_value.to_dict()

        spent = self.spent.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "loadout_value": loadout_value,
                "spent": spent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_player_economy_value import MatchesV2DataPlayerEconomyValue

        d = dict(src_dict)
        loadout_value = MatchesV2DataPlayerEconomyValue.from_dict(d.pop("loadout_value"))

        spent = MatchesV2DataPlayerEconomyValue.from_dict(d.pop("spent"))

        matches_v2_data_player_economy = cls(
            loadout_value=loadout_value,
            spent=spent,
        )

        matches_v2_data_player_economy.additional_properties = d
        return matches_v2_data_player_economy

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
