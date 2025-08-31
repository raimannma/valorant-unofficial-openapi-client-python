from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="QueueStatusV1GameRules")


@_attrs_define
class QueueStatusV1GameRules:
    """
    Attributes:
        allow_drop_out (bool):
        allow_lenient_surrender (bool):
        allow_overtime_draw_vote (bool):
        assign_random_agents (bool):
        overtime_win_by_two (bool):
        overtime_win_by_two_capped (bool):
        premier_mode (bool):
        skip_pregame (bool):
    """

    allow_drop_out: bool
    allow_lenient_surrender: bool
    allow_overtime_draw_vote: bool
    assign_random_agents: bool
    overtime_win_by_two: bool
    overtime_win_by_two_capped: bool
    premier_mode: bool
    skip_pregame: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        allow_drop_out = self.allow_drop_out

        allow_lenient_surrender = self.allow_lenient_surrender

        allow_overtime_draw_vote = self.allow_overtime_draw_vote

        assign_random_agents = self.assign_random_agents

        overtime_win_by_two = self.overtime_win_by_two

        overtime_win_by_two_capped = self.overtime_win_by_two_capped

        premier_mode = self.premier_mode

        skip_pregame = self.skip_pregame

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "allow_drop_out": allow_drop_out,
                "allow_lenient_surrender": allow_lenient_surrender,
                "allow_overtime_draw_vote": allow_overtime_draw_vote,
                "assign_random_agents": assign_random_agents,
                "overtime_win_by_two": overtime_win_by_two,
                "overtime_win_by_two_capped": overtime_win_by_two_capped,
                "premier_mode": premier_mode,
                "skip_pregame": skip_pregame,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_drop_out = d.pop("allow_drop_out")

        allow_lenient_surrender = d.pop("allow_lenient_surrender")

        allow_overtime_draw_vote = d.pop("allow_overtime_draw_vote")

        assign_random_agents = d.pop("assign_random_agents")

        overtime_win_by_two = d.pop("overtime_win_by_two")

        overtime_win_by_two_capped = d.pop("overtime_win_by_two_capped")

        premier_mode = d.pop("premier_mode")

        skip_pregame = d.pop("skip_pregame")

        queue_status_v1_game_rules = cls(
            allow_drop_out=allow_drop_out,
            allow_lenient_surrender=allow_lenient_surrender,
            allow_overtime_draw_vote=allow_overtime_draw_vote,
            assign_random_agents=assign_random_agents,
            overtime_win_by_two=overtime_win_by_two,
            overtime_win_by_two_capped=overtime_win_by_two_capped,
            premier_mode=premier_mode,
            skip_pregame=skip_pregame,
        )

        queue_status_v1_game_rules.additional_properties = d
        return queue_status_v1_game_rules

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
