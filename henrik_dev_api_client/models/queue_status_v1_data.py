from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.queue_status_v1_game_rules import QueueStatusV1GameRules
    from ..models.queue_status_v1_high_skill import QueueStatusV1HighSkill
    from ..models.queue_status_v1_maps import QueueStatusV1Maps
    from ..models.queue_status_v1_party_size import QueueStatusV1PartySize
    from ..models.queue_status_v1_skill_disparity import QueueStatusV1SkillDisparity


T = TypeVar("T", bound="QueueStatusV1Data")


@_attrs_define
class QueueStatusV1Data:
    """
    Attributes:
        enabled (bool):
        game_rules (QueueStatusV1GameRules):
        high_skill (QueueStatusV1HighSkill):
        maps (list['QueueStatusV1Maps']):
        mode (str):
        mode_id (str):
        number_of_teams (int):
        party_size (QueueStatusV1PartySize):
        platforms (list[str]):
        ranked (bool):
        required_account_level (int):
        skill_disparity (list['QueueStatusV1SkillDisparity']):
        team_size (int):
        tournament (bool):
    """

    enabled: bool
    game_rules: "QueueStatusV1GameRules"
    high_skill: "QueueStatusV1HighSkill"
    maps: list["QueueStatusV1Maps"]
    mode: str
    mode_id: str
    number_of_teams: int
    party_size: "QueueStatusV1PartySize"
    platforms: list[str]
    ranked: bool
    required_account_level: int
    skill_disparity: list["QueueStatusV1SkillDisparity"]
    team_size: int
    tournament: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        game_rules = self.game_rules.to_dict()

        high_skill = self.high_skill.to_dict()

        maps = []
        for maps_item_data in self.maps:
            maps_item = maps_item_data.to_dict()
            maps.append(maps_item)

        mode = self.mode

        mode_id = self.mode_id

        number_of_teams = self.number_of_teams

        party_size = self.party_size.to_dict()

        platforms = self.platforms

        ranked = self.ranked

        required_account_level = self.required_account_level

        skill_disparity = []
        for skill_disparity_item_data in self.skill_disparity:
            skill_disparity_item = skill_disparity_item_data.to_dict()
            skill_disparity.append(skill_disparity_item)

        team_size = self.team_size

        tournament = self.tournament

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "enabled": enabled,
                "game_rules": game_rules,
                "high_skill": high_skill,
                "maps": maps,
                "mode": mode,
                "mode_id": mode_id,
                "number_of_teams": number_of_teams,
                "party_size": party_size,
                "platforms": platforms,
                "ranked": ranked,
                "required_account_level": required_account_level,
                "skill_disparity": skill_disparity,
                "team_size": team_size,
                "tournament": tournament,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.queue_status_v1_game_rules import QueueStatusV1GameRules
        from ..models.queue_status_v1_high_skill import QueueStatusV1HighSkill
        from ..models.queue_status_v1_maps import QueueStatusV1Maps
        from ..models.queue_status_v1_party_size import QueueStatusV1PartySize
        from ..models.queue_status_v1_skill_disparity import QueueStatusV1SkillDisparity

        d = dict(src_dict)
        enabled = d.pop("enabled")

        game_rules = QueueStatusV1GameRules.from_dict(d.pop("game_rules"))

        high_skill = QueueStatusV1HighSkill.from_dict(d.pop("high_skill"))

        maps = []
        _maps = d.pop("maps")
        for maps_item_data in _maps:
            maps_item = QueueStatusV1Maps.from_dict(maps_item_data)

            maps.append(maps_item)

        mode = d.pop("mode")

        mode_id = d.pop("mode_id")

        number_of_teams = d.pop("number_of_teams")

        party_size = QueueStatusV1PartySize.from_dict(d.pop("party_size"))

        platforms = cast(list[str], d.pop("platforms"))

        ranked = d.pop("ranked")

        required_account_level = d.pop("required_account_level")

        skill_disparity = []
        _skill_disparity = d.pop("skill_disparity")
        for skill_disparity_item_data in _skill_disparity:
            skill_disparity_item = QueueStatusV1SkillDisparity.from_dict(skill_disparity_item_data)

            skill_disparity.append(skill_disparity_item)

        team_size = d.pop("team_size")

        tournament = d.pop("tournament")

        queue_status_v1_data = cls(
            enabled=enabled,
            game_rules=game_rules,
            high_skill=high_skill,
            maps=maps,
            mode=mode,
            mode_id=mode_id,
            number_of_teams=number_of_teams,
            party_size=party_size,
            platforms=platforms,
            ranked=ranked,
            required_account_level=required_account_level,
            skill_disparity=skill_disparity,
            team_size=team_size,
            tournament=tournament,
        )

        queue_status_v1_data.additional_properties = d
        return queue_status_v1_data

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
