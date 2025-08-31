from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.agent_id_name_combo import AgentIdNameCombo
    from ..models.matches_v4_data_player_ability_casts import MatchesV4DataPlayerAbilityCasts
    from ..models.matches_v4_data_player_behavior import MatchesV4DataPlayerBehavior
    from ..models.matches_v4_data_player_customization import MatchesV4DataPlayerCustomization
    from ..models.matches_v4_data_player_economy import MatchesV4DataPlayerEconomy
    from ..models.matches_v4_data_player_stats import MatchesV4DataPlayerStats
    from ..models.tier_id_name_combo import TierIdNameCombo


T = TypeVar("T", bound="MatchesV4DataPlayer")


@_attrs_define
class MatchesV4DataPlayer:
    """
    Attributes:
        ability_casts (MatchesV4DataPlayerAbilityCasts):
        account_level (int):
        agent (AgentIdNameCombo):
        behavior (MatchesV4DataPlayerBehavior):
        customization (MatchesV4DataPlayerCustomization):
        economy (MatchesV4DataPlayerEconomy):
        name (str):
        party_id (str):
        platform (str):
        puuid (str):
        session_playtime_in_ms (int):
        stats (MatchesV4DataPlayerStats):
        tag (str):
        team_id (str):
        tier (TierIdNameCombo):
    """

    ability_casts: "MatchesV4DataPlayerAbilityCasts"
    account_level: int
    agent: "AgentIdNameCombo"
    behavior: "MatchesV4DataPlayerBehavior"
    customization: "MatchesV4DataPlayerCustomization"
    economy: "MatchesV4DataPlayerEconomy"
    name: str
    party_id: str
    platform: str
    puuid: str
    session_playtime_in_ms: int
    stats: "MatchesV4DataPlayerStats"
    tag: str
    team_id: str
    tier: "TierIdNameCombo"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ability_casts = self.ability_casts.to_dict()

        account_level = self.account_level

        agent = self.agent.to_dict()

        behavior = self.behavior.to_dict()

        customization = self.customization.to_dict()

        economy = self.economy.to_dict()

        name = self.name

        party_id = self.party_id

        platform = self.platform

        puuid = self.puuid

        session_playtime_in_ms = self.session_playtime_in_ms

        stats = self.stats.to_dict()

        tag = self.tag

        team_id = self.team_id

        tier = self.tier.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ability_casts": ability_casts,
                "account_level": account_level,
                "agent": agent,
                "behavior": behavior,
                "customization": customization,
                "economy": economy,
                "name": name,
                "party_id": party_id,
                "platform": platform,
                "puuid": puuid,
                "session_playtime_in_ms": session_playtime_in_ms,
                "stats": stats,
                "tag": tag,
                "team_id": team_id,
                "tier": tier,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_id_name_combo import AgentIdNameCombo
        from ..models.matches_v4_data_player_ability_casts import MatchesV4DataPlayerAbilityCasts
        from ..models.matches_v4_data_player_behavior import MatchesV4DataPlayerBehavior
        from ..models.matches_v4_data_player_customization import MatchesV4DataPlayerCustomization
        from ..models.matches_v4_data_player_economy import MatchesV4DataPlayerEconomy
        from ..models.matches_v4_data_player_stats import MatchesV4DataPlayerStats
        from ..models.tier_id_name_combo import TierIdNameCombo

        d = dict(src_dict)
        ability_casts = MatchesV4DataPlayerAbilityCasts.from_dict(d.pop("ability_casts"))

        account_level = d.pop("account_level")

        agent = AgentIdNameCombo.from_dict(d.pop("agent"))

        behavior = MatchesV4DataPlayerBehavior.from_dict(d.pop("behavior"))

        customization = MatchesV4DataPlayerCustomization.from_dict(d.pop("customization"))

        economy = MatchesV4DataPlayerEconomy.from_dict(d.pop("economy"))

        name = d.pop("name")

        party_id = d.pop("party_id")

        platform = d.pop("platform")

        puuid = d.pop("puuid")

        session_playtime_in_ms = d.pop("session_playtime_in_ms")

        stats = MatchesV4DataPlayerStats.from_dict(d.pop("stats"))

        tag = d.pop("tag")

        team_id = d.pop("team_id")

        tier = TierIdNameCombo.from_dict(d.pop("tier"))

        matches_v4_data_player = cls(
            ability_casts=ability_casts,
            account_level=account_level,
            agent=agent,
            behavior=behavior,
            customization=customization,
            economy=economy,
            name=name,
            party_id=party_id,
            platform=platform,
            puuid=puuid,
            session_playtime_in_ms=session_playtime_in_ms,
            stats=stats,
            tag=tag,
            team_id=team_id,
            tier=tier,
        )

        matches_v4_data_player.additional_properties = d
        return matches_v4_data_player

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
