from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v2_data_coach import MatchesV2DataCoach
    from ..models.matches_v2_data_kill import MatchesV2DataKill
    from ..models.matches_v2_data_metadata import MatchesV2DataMetadata
    from ..models.matches_v2_data_observer import MatchesV2DataObserver
    from ..models.matches_v2_data_players import MatchesV2DataPlayers
    from ..models.matches_v2_data_round import MatchesV2DataRound
    from ..models.matches_v2_data_teams import MatchesV2DataTeams


T = TypeVar("T", bound="MatchesV2Data")


@_attrs_define
class MatchesV2Data:
    """
    Attributes:
        coaches (list['MatchesV2DataCoach']):
        kills (list['MatchesV2DataKill']):
        metadata (MatchesV2DataMetadata):
        observers (list['MatchesV2DataObserver']):
        players (MatchesV2DataPlayers):
        rounds (list['MatchesV2DataRound']):
        teams (MatchesV2DataTeams):
    """

    coaches: list["MatchesV2DataCoach"]
    kills: list["MatchesV2DataKill"]
    metadata: "MatchesV2DataMetadata"
    observers: list["MatchesV2DataObserver"]
    players: "MatchesV2DataPlayers"
    rounds: list["MatchesV2DataRound"]
    teams: "MatchesV2DataTeams"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        coaches = []
        for coaches_item_data in self.coaches:
            coaches_item = coaches_item_data.to_dict()
            coaches.append(coaches_item)

        kills = []
        for kills_item_data in self.kills:
            kills_item = kills_item_data.to_dict()
            kills.append(kills_item)

        metadata = self.metadata.to_dict()

        observers = []
        for observers_item_data in self.observers:
            observers_item = observers_item_data.to_dict()
            observers.append(observers_item)

        players = self.players.to_dict()

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        teams = self.teams.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coaches": coaches,
                "kills": kills,
                "metadata": metadata,
                "observers": observers,
                "players": players,
                "rounds": rounds,
                "teams": teams,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_coach import MatchesV2DataCoach
        from ..models.matches_v2_data_kill import MatchesV2DataKill
        from ..models.matches_v2_data_metadata import MatchesV2DataMetadata
        from ..models.matches_v2_data_observer import MatchesV2DataObserver
        from ..models.matches_v2_data_players import MatchesV2DataPlayers
        from ..models.matches_v2_data_round import MatchesV2DataRound
        from ..models.matches_v2_data_teams import MatchesV2DataTeams

        d = dict(src_dict)
        coaches = []
        _coaches = d.pop("coaches")
        for coaches_item_data in _coaches:
            coaches_item = MatchesV2DataCoach.from_dict(coaches_item_data)

            coaches.append(coaches_item)

        kills = []
        _kills = d.pop("kills")
        for kills_item_data in _kills:
            kills_item = MatchesV2DataKill.from_dict(kills_item_data)

            kills.append(kills_item)

        metadata = MatchesV2DataMetadata.from_dict(d.pop("metadata"))

        observers = []
        _observers = d.pop("observers")
        for observers_item_data in _observers:
            observers_item = MatchesV2DataObserver.from_dict(observers_item_data)

            observers.append(observers_item)

        players = MatchesV2DataPlayers.from_dict(d.pop("players"))

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = MatchesV2DataRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        teams = MatchesV2DataTeams.from_dict(d.pop("teams"))

        matches_v2_data = cls(
            coaches=coaches,
            kills=kills,
            metadata=metadata,
            observers=observers,
            players=players,
            rounds=rounds,
            teams=teams,
        )

        matches_v2_data.additional_properties = d
        return matches_v2_data

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
