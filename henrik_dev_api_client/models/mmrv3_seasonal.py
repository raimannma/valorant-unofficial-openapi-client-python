from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mmrv3_leaderboard_placement import MMRV3LeaderboardPlacement
    from ..models.season_id_short_combo import SeasonIdShortCombo
    from ..models.tier_id_name_combo import TierIdNameCombo


T = TypeVar("T", bound="MMRV3Seasonal")


@_attrs_define
class MMRV3Seasonal:
    """
    Attributes:
        act_wins (list['TierIdNameCombo']):
        end_rr (int):
        end_tier (TierIdNameCombo):
        games (int):
        ranking_schema (str):
        season (SeasonIdShortCombo):
        wins (int):
        leaderboard_placement (Union['MMRV3LeaderboardPlacement', None, Unset]):
    """

    act_wins: list["TierIdNameCombo"]
    end_rr: int
    end_tier: "TierIdNameCombo"
    games: int
    ranking_schema: str
    season: "SeasonIdShortCombo"
    wins: int
    leaderboard_placement: Union["MMRV3LeaderboardPlacement", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mmrv3_leaderboard_placement import MMRV3LeaderboardPlacement

        act_wins = []
        for act_wins_item_data in self.act_wins:
            act_wins_item = act_wins_item_data.to_dict()
            act_wins.append(act_wins_item)

        end_rr = self.end_rr

        end_tier = self.end_tier.to_dict()

        games = self.games

        ranking_schema = self.ranking_schema

        season = self.season.to_dict()

        wins = self.wins

        leaderboard_placement: Union[None, Unset, dict[str, Any]]
        if isinstance(self.leaderboard_placement, Unset):
            leaderboard_placement = UNSET
        elif isinstance(self.leaderboard_placement, MMRV3LeaderboardPlacement):
            leaderboard_placement = self.leaderboard_placement.to_dict()
        else:
            leaderboard_placement = self.leaderboard_placement

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "act_wins": act_wins,
                "end_rr": end_rr,
                "end_tier": end_tier,
                "games": games,
                "ranking_schema": ranking_schema,
                "season": season,
                "wins": wins,
            }
        )
        if leaderboard_placement is not UNSET:
            field_dict["leaderboard_placement"] = leaderboard_placement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mmrv3_leaderboard_placement import MMRV3LeaderboardPlacement
        from ..models.season_id_short_combo import SeasonIdShortCombo
        from ..models.tier_id_name_combo import TierIdNameCombo

        d = dict(src_dict)
        act_wins = []
        _act_wins = d.pop("act_wins")
        for act_wins_item_data in _act_wins:
            act_wins_item = TierIdNameCombo.from_dict(act_wins_item_data)

            act_wins.append(act_wins_item)

        end_rr = d.pop("end_rr")

        end_tier = TierIdNameCombo.from_dict(d.pop("end_tier"))

        games = d.pop("games")

        ranking_schema = d.pop("ranking_schema")

        season = SeasonIdShortCombo.from_dict(d.pop("season"))

        wins = d.pop("wins")

        def _parse_leaderboard_placement(data: object) -> Union["MMRV3LeaderboardPlacement", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                leaderboard_placement_type_1 = MMRV3LeaderboardPlacement.from_dict(data)

                return leaderboard_placement_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MMRV3LeaderboardPlacement", None, Unset], data)

        leaderboard_placement = _parse_leaderboard_placement(d.pop("leaderboard_placement", UNSET))

        mmrv3_seasonal = cls(
            act_wins=act_wins,
            end_rr=end_rr,
            end_tier=end_tier,
            games=games,
            ranking_schema=ranking_schema,
            season=season,
            wins=wins,
            leaderboard_placement=leaderboard_placement,
        )

        mmrv3_seasonal.additional_properties = d
        return mmrv3_seasonal

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
