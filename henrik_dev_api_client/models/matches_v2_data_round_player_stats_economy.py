from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_round_player_stats_economy_equipment_armor import (
        MatchesV2DataRoundPlayerStatsEconomyEquipmentArmor,
    )
    from ..models.matches_v2_data_round_player_stats_economy_equipment_weapon import (
        MatchesV2DataRoundPlayerStatsEconomyEquipmentWeapon,
    )


T = TypeVar("T", bound="MatchesV2DataRoundPlayerStatsEconomy")


@_attrs_define
class MatchesV2DataRoundPlayerStatsEconomy:
    """
    Attributes:
        armor (MatchesV2DataRoundPlayerStatsEconomyEquipmentArmor):
        loadout_value (int):
        remaining (int):
        spent (int):
        weapon (MatchesV2DataRoundPlayerStatsEconomyEquipmentWeapon):
    """

    armor: "MatchesV2DataRoundPlayerStatsEconomyEquipmentArmor"
    loadout_value: int
    remaining: int
    spent: int
    weapon: "MatchesV2DataRoundPlayerStatsEconomyEquipmentWeapon"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        armor = self.armor.to_dict()

        loadout_value = self.loadout_value

        remaining = self.remaining

        spent = self.spent

        weapon = self.weapon.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "armor": armor,
                "loadout_value": loadout_value,
                "remaining": remaining,
                "spent": spent,
                "weapon": weapon,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_round_player_stats_economy_equipment_armor import (
            MatchesV2DataRoundPlayerStatsEconomyEquipmentArmor,
        )
        from ..models.matches_v2_data_round_player_stats_economy_equipment_weapon import (
            MatchesV2DataRoundPlayerStatsEconomyEquipmentWeapon,
        )

        d = dict(src_dict)
        armor = MatchesV2DataRoundPlayerStatsEconomyEquipmentArmor.from_dict(d.pop("armor"))

        loadout_value = d.pop("loadout_value")

        remaining = d.pop("remaining")

        spent = d.pop("spent")

        weapon = MatchesV2DataRoundPlayerStatsEconomyEquipmentWeapon.from_dict(d.pop("weapon"))

        matches_v2_data_round_player_stats_economy = cls(
            armor=armor,
            loadout_value=loadout_value,
            remaining=remaining,
            spent=spent,
            weapon=weapon,
        )

        matches_v2_data_round_player_stats_economy.additional_properties = d
        return matches_v2_data_round_player_stats_economy

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
