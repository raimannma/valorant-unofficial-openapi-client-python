from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v2_data_coach import MatchesV2DataCoach
    from ..models.matches_v2_data_kill import MatchesV2DataKill
    from ..models.matches_v2_data_metadata import MatchesV2DataMetadata
    from ..models.matches_v2_data_observer import MatchesV2DataObserver
    from ..models.matches_v2_data_players import MatchesV2DataPlayers
    from ..models.matches_v2_data_round import MatchesV2DataRound
    from ..models.matches_v2_data_teams import MatchesV2DataTeams


T = TypeVar("T", bound="MatchesV3ListResponseData")


@_attrs_define
class MatchesV3ListResponseData:
    """
    Attributes:
        coaches (list['MatchesV2DataCoach']):
        is_available (bool):
        kills (list['MatchesV2DataKill']):
        observers (list['MatchesV2DataObserver']):
        rounds (list['MatchesV2DataRound']):
        metadata (Union['MatchesV2DataMetadata', None, Unset]):
        players (Union['MatchesV2DataPlayers', None, Unset]):
        teams (Union['MatchesV2DataTeams', None, Unset]):
    """

    coaches: list["MatchesV2DataCoach"]
    is_available: bool
    kills: list["MatchesV2DataKill"]
    observers: list["MatchesV2DataObserver"]
    rounds: list["MatchesV2DataRound"]
    metadata: Union["MatchesV2DataMetadata", None, Unset] = UNSET
    players: Union["MatchesV2DataPlayers", None, Unset] = UNSET
    teams: Union["MatchesV2DataTeams", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.matches_v2_data_metadata import MatchesV2DataMetadata
        from ..models.matches_v2_data_players import MatchesV2DataPlayers
        from ..models.matches_v2_data_teams import MatchesV2DataTeams

        coaches = []
        for coaches_item_data in self.coaches:
            coaches_item = coaches_item_data.to_dict()
            coaches.append(coaches_item)

        is_available = self.is_available

        kills = []
        for kills_item_data in self.kills:
            kills_item = kills_item_data.to_dict()
            kills.append(kills_item)

        observers = []
        for observers_item_data in self.observers:
            observers_item = observers_item_data.to_dict()
            observers.append(observers_item)

        rounds = []
        for rounds_item_data in self.rounds:
            rounds_item = rounds_item_data.to_dict()
            rounds.append(rounds_item)

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, MatchesV2DataMetadata):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        players: Union[None, Unset, dict[str, Any]]
        if isinstance(self.players, Unset):
            players = UNSET
        elif isinstance(self.players, MatchesV2DataPlayers):
            players = self.players.to_dict()
        else:
            players = self.players

        teams: Union[None, Unset, dict[str, Any]]
        if isinstance(self.teams, Unset):
            teams = UNSET
        elif isinstance(self.teams, MatchesV2DataTeams):
            teams = self.teams.to_dict()
        else:
            teams = self.teams

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coaches": coaches,
                "is_available": is_available,
                "kills": kills,
                "observers": observers,
                "rounds": rounds,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if players is not UNSET:
            field_dict["players"] = players
        if teams is not UNSET:
            field_dict["teams"] = teams

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

        is_available = d.pop("is_available")

        kills = []
        _kills = d.pop("kills")
        for kills_item_data in _kills:
            kills_item = MatchesV2DataKill.from_dict(kills_item_data)

            kills.append(kills_item)

        observers = []
        _observers = d.pop("observers")
        for observers_item_data in _observers:
            observers_item = MatchesV2DataObserver.from_dict(observers_item_data)

            observers.append(observers_item)

        rounds = []
        _rounds = d.pop("rounds")
        for rounds_item_data in _rounds:
            rounds_item = MatchesV2DataRound.from_dict(rounds_item_data)

            rounds.append(rounds_item)

        def _parse_metadata(data: object) -> Union["MatchesV2DataMetadata", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_1 = MatchesV2DataMetadata.from_dict(data)

                return metadata_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV2DataMetadata", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_players(data: object) -> Union["MatchesV2DataPlayers", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                players_type_1 = MatchesV2DataPlayers.from_dict(data)

                return players_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV2DataPlayers", None, Unset], data)

        players = _parse_players(d.pop("players", UNSET))

        def _parse_teams(data: object) -> Union["MatchesV2DataTeams", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                teams_type_1 = MatchesV2DataTeams.from_dict(data)

                return teams_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MatchesV2DataTeams", None, Unset], data)

        teams = _parse_teams(d.pop("teams", UNSET))

        matches_v3_list_response_data = cls(
            coaches=coaches,
            is_available=is_available,
            kills=kills,
            observers=observers,
            rounds=rounds,
            metadata=metadata,
            players=players,
            teams=teams,
        )

        matches_v3_list_response_data.additional_properties = d
        return matches_v3_list_response_data

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
