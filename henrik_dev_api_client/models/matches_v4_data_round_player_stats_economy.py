from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v4_data_round_player_stats_economy_armor import MatchesV4DataRoundPlayerStatsEconomyArmor
    from ..models.matches_v4_data_round_player_stats_economy_weapon import MatchesV4DataRoundPlayerStatsEconomyWeapon


T = TypeVar("T", bound="MatchesV4DataRoundPlayerStatsEconomy")


@_attrs_define
class MatchesV4DataRoundPlayerStatsEconomy:
    """
    Attributes:
        loadout_value (int):
        remaining (int):
        armor (Union['MatchesV4DataRoundPlayerStatsEconomyArmor', None, Unset]):
        weapon (Union['MatchesV4DataRoundPlayerStatsEconomyWeapon', None, Unset]):
    """

    loadout_value: int
    remaining: int
    armor: Union["MatchesV4DataRoundPlayerStatsEconomyArmor", None, Unset] = UNSET
    weapon: Union["MatchesV4DataRoundPlayerStatsEconomyWeapon", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.matches_v4_data_round_player_stats_economy_armor import MatchesV4DataRoundPlayerStatsEconomyArmor
        from ..models.matches_v4_data_round_player_stats_economy_weapon import (
            MatchesV4DataRoundPlayerStatsEconomyWeapon,
        )

        loadout_value = self.loadout_value

        remaining = self.remaining

        armor: Union[None, Unset, dict[str, Any]]
        if isinstance(self.armor, Unset):
            armor = UNSET
        elif isinstance(self.armor, MatchesV4DataRoundPlayerStatsEconomyArmor):
            armor = self.armor.to_dict()
        else:
            armor = self.armor

        weapon: Union[None, Unset, dict[str, Any]]
        if isinstance(self.weapon, Unset):
            weapon = UNSET
        elif isinstance(self.weapon, MatchesV4DataRoundPlayerStatsEconomyWeapon):
            weapon = self.weapon.to_dict()
        else:
            weapon = self.weapon

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "loadout_value": loadout_value,
                "remaining": remaining,
            }
        )
        if armor is not UNSET:
            field_dict["armor"] = armor
        if weapon is not UNSET:
            field_dict["weapon"] = weapon

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v4_data_round_player_stats_economy_armor import MatchesV4DataRoundPlayerStatsEconomyArmor
        from ..models.matches_v4_data_round_player_stats_economy_weapon import (
            MatchesV4DataRoundPlayerStatsEconomyWeapon,
        )

        d = dict(src_dict)
        loadout_value = d.pop("loadout_value")

        remaining = d.pop("remaining")

        def _parse_armor(data: object) -> Union["MatchesV4DataRoundPlayerStatsEconomyArmor", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                armor_type_1 = MatchesV4DataRoundPlayerStatsEconomyArmor.from_dict(data)

                return armor_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV4DataRoundPlayerStatsEconomyArmor", None, Unset], data)

        armor = _parse_armor(d.pop("armor", UNSET))

        def _parse_weapon(data: object) -> Union["MatchesV4DataRoundPlayerStatsEconomyWeapon", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                weapon_type_1 = MatchesV4DataRoundPlayerStatsEconomyWeapon.from_dict(data)

                return weapon_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV4DataRoundPlayerStatsEconomyWeapon", None, Unset], data)

        weapon = _parse_weapon(d.pop("weapon", UNSET))

        matches_v4_data_round_player_stats_economy = cls(
            loadout_value=loadout_value,
            remaining=remaining,
            armor=armor,
            weapon=weapon,
        )

        matches_v4_data_round_player_stats_economy.additional_properties = d
        return matches_v4_data_round_player_stats_economy

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
