from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.matches_v4_data_coach import MatchesV4DataCoach
    from ..models.matches_v4_data_kill import MatchesV4DataKill
    from ..models.matches_v4_data_metadata import MatchesV4DataMetadata
    from ..models.matches_v4_data_observer import MatchesV4DataObserver
    from ..models.matches_v4_data_player import MatchesV4DataPlayer
    from ..models.matches_v4_data_round import MatchesV4DataRound
    from ..models.matches_v4_data_team import MatchesV4DataTeam


T = TypeVar("T", bound="MatchesV4Data")


@_attrs_define
class MatchesV4Data:
    """
    Attributes:
        coaches (list['MatchesV4DataCoach']):
        kills (list['MatchesV4DataKill']):
        metadata (MatchesV4DataMetadata):
        observers (list['MatchesV4DataObserver']):
        players (list['MatchesV4DataPlayer']):
        rounds (list['MatchesV4DataRound']):
        teams (list['MatchesV4DataTeam']):
    """

    coaches: list["MatchesV4DataCoach"]
    kills: list["MatchesV4DataKill"]
    metadata: "MatchesV4DataMetadata"
    observers: list["MatchesV4DataObserver"]
    players: list["MatchesV4DataPlayer"]
    rounds: list["MatchesV4DataRound"]
    teams: list["MatchesV4DataTeam"]
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

        players = []
        for players_item_data in self.players:
            players_item = players_item_data.to_dict()
            players.append(players_item)

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        teams = []
        for teams_item_data in self.teams:
            teams_item = teams_item_data.to_dict()
            teams.append(teams_item)

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
        from ..models.matches_v4_data_coach import MatchesV4DataCoach
        from ..models.matches_v4_data_kill import MatchesV4DataKill
        from ..models.matches_v4_data_metadata import MatchesV4DataMetadata
        from ..models.matches_v4_data_observer import MatchesV4DataObserver
        from ..models.matches_v4_data_player import MatchesV4DataPlayer
        from ..models.matches_v4_data_round import MatchesV4DataRound
        from ..models.matches_v4_data_team import MatchesV4DataTeam

        d = dict(src_dict)
        coaches = []
        _coaches = d.pop("coaches")
        for coaches_item_data in _coaches:
            coaches_item = MatchesV4DataCoach.from_dict(coaches_item_data)

            coaches.append(coaches_item)

        kills = []
        _kills = d.pop("kills")
        for kills_item_data in _kills:
            kills_item = MatchesV4DataKill.from_dict(kills_item_data)

            kills.append(kills_item)

        metadata = MatchesV4DataMetadata.from_dict(d.pop("metadata"))

        observers = []
        _observers = d.pop("observers")
        for observers_item_data in _observers:
            observers_item = MatchesV4DataObserver.from_dict(observers_item_data)

            observers.append(observers_item)

        players = []
        _players = d.pop("players")
        for players_item_data in _players:
            players_item = MatchesV4DataPlayer.from_dict(players_item_data)

            players.append(players_item)

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = MatchesV4DataRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        teams = []
        _teams = d.pop("teams")
        for teams_item_data in _teams:
            teams_item = MatchesV4DataTeam.from_dict(teams_item_data)

            teams.append(teams_item)

        matches_v4_data = cls(
            coaches=coaches,
            kills=kills,
            metadata=metadata,
            observers=observers,
            players=players,
            rounds=rounds,
            teams=teams,
        )

        matches_v4_data.additional_properties = d
        return matches_v4_data

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
