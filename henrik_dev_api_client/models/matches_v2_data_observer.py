from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_platform import MatchesV2DataPlatform
    from ..models.matches_v2_data_player_session_playtime import MatchesV2DataPlayerSessionPlaytime


T = TypeVar("T", bound="MatchesV2DataObserver")


@_attrs_define
class MatchesV2DataObserver:
    """
    Attributes:
        level (int):
        name (str):
        party_id (str):
        platform (MatchesV2DataPlatform):
        player_card (str):
        player_title (str):
        puuid (str):
        session_playtime (MatchesV2DataPlayerSessionPlaytime):
        tag (str):
        team (str):
    """

    level: int
    name: str
    party_id: str
    platform: "MatchesV2DataPlatform"
    player_card: str
    player_title: str
    puuid: str
    session_playtime: "MatchesV2DataPlayerSessionPlaytime"
    tag: str
    team: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        level = self.level

        name = self.name

        party_id = self.party_id

        platform = self.platform.to_dict()

        player_card = self.player_card

        player_title = self.player_title

        puuid = self.puuid

        session_playtime = self.session_playtime.to_dict()

        tag = self.tag

        team = self.team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "level": level,
                "name": name,
                "party_id": party_id,
                "platform": platform,
                "player_card": player_card,
                "player_title": player_title,
                "puuid": puuid,
                "session_playtime": session_playtime,
                "tag": tag,
                "team": team,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_platform import MatchesV2DataPlatform
        from ..models.matches_v2_data_player_session_playtime import MatchesV2DataPlayerSessionPlaytime

        d = dict(src_dict)
        level = d.pop("level")

        name = d.pop("name")

        party_id = d.pop("party_id")

        platform = MatchesV2DataPlatform.from_dict(d.pop("platform"))

        player_card = d.pop("player_card")

        player_title = d.pop("player_title")

        puuid = d.pop("puuid")

        session_playtime = MatchesV2DataPlayerSessionPlaytime.from_dict(d.pop("session_playtime"))

        tag = d.pop("tag")

        team = d.pop("team")

        matches_v2_data_observer = cls(
            level=level,
            name=name,
            party_id=party_id,
            platform=platform,
            player_card=player_card,
            player_title=player_title,
            puuid=puuid,
            session_playtime=session_playtime,
            tag=tag,
            team=team,
        )

        matches_v2_data_observer.additional_properties = d
        return matches_v2_data_observer

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
