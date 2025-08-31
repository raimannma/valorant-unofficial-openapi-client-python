from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v2_data_platform import MatchesV2DataPlatform
    from ..models.matches_v2_data_player_ability_casts import MatchesV2DataPlayerAbilityCasts
    from ..models.matches_v2_data_player_assets import MatchesV2DataPlayerAssets
    from ..models.matches_v2_data_player_behavior import MatchesV2DataPlayerBehavior
    from ..models.matches_v2_data_player_economy import MatchesV2DataPlayerEconomy
    from ..models.matches_v2_data_player_session_playtime import MatchesV2DataPlayerSessionPlaytime
    from ..models.matches_v2_data_player_stats import MatchesV2DataPlayerStats


T = TypeVar("T", bound="MatchesV2DataPlayer")


@_attrs_define
class MatchesV2DataPlayer:
    """
    Attributes:
        ability_casts (MatchesV2DataPlayerAbilityCasts):
        assets (MatchesV2DataPlayerAssets):
        behavior (MatchesV2DataPlayerBehavior):
        currenttier (int):
        currenttier_patched (str):
        damage_made (int):
        damage_received (int):
        economy (MatchesV2DataPlayerEconomy):
        level (int):
        name (str):
        party_id (str):
        platform (MatchesV2DataPlatform):
        player_card (str):
        player_title (str):
        puuid (str):
        session_playtime (MatchesV2DataPlayerSessionPlaytime):
        stats (MatchesV2DataPlayerStats):
        tag (str):
        team (str):
        character (Union[None, Unset, str]):
    """

    ability_casts: "MatchesV2DataPlayerAbilityCasts"
    assets: "MatchesV2DataPlayerAssets"
    behavior: "MatchesV2DataPlayerBehavior"
    currenttier: int
    currenttier_patched: str
    damage_made: int
    damage_received: int
    economy: "MatchesV2DataPlayerEconomy"
    level: int
    name: str
    party_id: str
    platform: "MatchesV2DataPlatform"
    player_card: str
    player_title: str
    puuid: str
    session_playtime: "MatchesV2DataPlayerSessionPlaytime"
    stats: "MatchesV2DataPlayerStats"
    tag: str
    team: str
    character: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ability_casts = self.ability_casts.to_dict()

        assets = self.assets.to_dict()

        behavior = self.behavior.to_dict()

        currenttier = self.currenttier

        currenttier_patched = self.currenttier_patched

        damage_made = self.damage_made

        damage_received = self.damage_received

        economy = self.economy.to_dict()

        level = self.level

        name = self.name

        party_id = self.party_id

        platform = self.platform.to_dict()

        player_card = self.player_card

        player_title = self.player_title

        puuid = self.puuid

        session_playtime = self.session_playtime.to_dict()

        stats = self.stats.to_dict()

        tag = self.tag

        team = self.team

        character: Union[None, Unset, str]
        if isinstance(self.character, Unset):
            character = UNSET
        else:
            character = self.character

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ability_casts": ability_casts,
                "assets": assets,
                "behavior": behavior,
                "currenttier": currenttier,
                "currenttier_patched": currenttier_patched,
                "damage_made": damage_made,
                "damage_received": damage_received,
                "economy": economy,
                "level": level,
                "name": name,
                "party_id": party_id,
                "platform": platform,
                "player_card": player_card,
                "player_title": player_title,
                "puuid": puuid,
                "session_playtime": session_playtime,
                "stats": stats,
                "tag": tag,
                "team": team,
            }
        )
        if character is not UNSET:
            field_dict["character"] = character

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_platform import MatchesV2DataPlatform
        from ..models.matches_v2_data_player_ability_casts import MatchesV2DataPlayerAbilityCasts
        from ..models.matches_v2_data_player_assets import MatchesV2DataPlayerAssets
        from ..models.matches_v2_data_player_behavior import MatchesV2DataPlayerBehavior
        from ..models.matches_v2_data_player_economy import MatchesV2DataPlayerEconomy
        from ..models.matches_v2_data_player_session_playtime import MatchesV2DataPlayerSessionPlaytime
        from ..models.matches_v2_data_player_stats import MatchesV2DataPlayerStats

        d = dict(src_dict)
        ability_casts = MatchesV2DataPlayerAbilityCasts.from_dict(d.pop("ability_casts"))

        assets = MatchesV2DataPlayerAssets.from_dict(d.pop("assets"))

        behavior = MatchesV2DataPlayerBehavior.from_dict(d.pop("behavior"))

        currenttier = d.pop("currenttier")

        currenttier_patched = d.pop("currenttier_patched")

        damage_made = d.pop("damage_made")

        damage_received = d.pop("damage_received")

        economy = MatchesV2DataPlayerEconomy.from_dict(d.pop("economy"))

        level = d.pop("level")

        name = d.pop("name")

        party_id = d.pop("party_id")

        platform = MatchesV2DataPlatform.from_dict(d.pop("platform"))

        player_card = d.pop("player_card")

        player_title = d.pop("player_title")

        puuid = d.pop("puuid")

        session_playtime = MatchesV2DataPlayerSessionPlaytime.from_dict(d.pop("session_playtime"))

        stats = MatchesV2DataPlayerStats.from_dict(d.pop("stats"))

        tag = d.pop("tag")

        team = d.pop("team")

        def _parse_character(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        character = _parse_character(d.pop("character", UNSET))

        matches_v2_data_player = cls(
            ability_casts=ability_casts,
            assets=assets,
            behavior=behavior,
            currenttier=currenttier,
            currenttier_patched=currenttier_patched,
            damage_made=damage_made,
            damage_received=damage_received,
            economy=economy,
            level=level,
            name=name,
            party_id=party_id,
            platform=platform,
            player_card=player_card,
            player_title=player_title,
            puuid=puuid,
            session_playtime=session_playtime,
            stats=stats,
            tag=tag,
            team=team,
            character=character,
        )

        matches_v2_data_player.additional_properties = d
        return matches_v2_data_player

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
