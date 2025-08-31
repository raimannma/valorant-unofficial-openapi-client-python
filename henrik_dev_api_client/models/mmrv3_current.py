from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mmrv3_leaderboard_placement import MMRV3LeaderboardPlacement
    from ..models.tier_id_name_combo import TierIdNameCombo


T = TypeVar("T", bound="MMRV3Current")


@_attrs_define
class MMRV3Current:
    """
    Attributes:
        elo (int):
        games_needed_for_rating (int):
        last_change (int):
        rank_protection_shields (int):
        rr (int):
        tier (TierIdNameCombo):
        leaderboard_placement (Union['MMRV3LeaderboardPlacement', None, Unset]):
    """

    elo: int
    games_needed_for_rating: int
    last_change: int
    rank_protection_shields: int
    rr: int
    tier: "TierIdNameCombo"
    leaderboard_placement: Union["MMRV3LeaderboardPlacement", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mmrv3_leaderboard_placement import MMRV3LeaderboardPlacement

        elo = self.elo

        games_needed_for_rating = self.games_needed_for_rating

        last_change = self.last_change

        rank_protection_shields = self.rank_protection_shields

        rr = self.rr

        tier = self.tier.to_dict()

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
                "elo": elo,
                "games_needed_for_rating": games_needed_for_rating,
                "last_change": last_change,
                "rank_protection_shields": rank_protection_shields,
                "rr": rr,
                "tier": tier,
            }
        )
        if leaderboard_placement is not UNSET:
            field_dict["leaderboard_placement"] = leaderboard_placement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mmrv3_leaderboard_placement import MMRV3LeaderboardPlacement
        from ..models.tier_id_name_combo import TierIdNameCombo

        d = dict(src_dict)
        elo = d.pop("elo")

        games_needed_for_rating = d.pop("games_needed_for_rating")

        last_change = d.pop("last_change")

        rank_protection_shields = d.pop("rank_protection_shields")

        rr = d.pop("rr")

        tier = TierIdNameCombo.from_dict(d.pop("tier"))

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

        mmrv3_current = cls(
            elo=elo,
            games_needed_for_rating=games_needed_for_rating,
            last_change=last_change,
            rank_protection_shields=rank_protection_shields,
            rr=rr,
            tier=tier,
            leaderboard_placement=leaderboard_placement,
        )

        mmrv3_current.additional_properties = d
        return mmrv3_current

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
