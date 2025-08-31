from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.map_id_name_combo import MapIdNameCombo
    from ..models.matches_v4_data_metadata_party_rr_penalty import MatchesV4DataMetadataPartyRRPenalty
    from ..models.matches_v4_data_metadata_queue import MatchesV4DataMetadataQueue
    from ..models.season_id_short_combo import SeasonIdShortCombo


T = TypeVar("T", bound="MatchesV4DataMetadata")


@_attrs_define
class MatchesV4DataMetadata:
    """
    Attributes:
        game_length_in_ms (int):
        game_version (str):
        is_completed (bool):
        map_ (MapIdNameCombo):
        match_id (str):
        party_rr_penaltys (list['MatchesV4DataMetadataPartyRRPenalty']):
        platform (str):
        queue (MatchesV4DataMetadataQueue):
        season (SeasonIdShortCombo):
        started_at (str):
        cluster (Union[None, Unset, str]):
        premier (Union[Unset, Any]):
        region (Union[None, Unset, str]):
    """

    game_length_in_ms: int
    game_version: str
    is_completed: bool
    map_: "MapIdNameCombo"
    match_id: str
    party_rr_penaltys: list["MatchesV4DataMetadataPartyRRPenalty"]
    platform: str
    queue: "MatchesV4DataMetadataQueue"
    season: "SeasonIdShortCombo"
    started_at: str
    cluster: Union[None, Unset, str] = UNSET
    premier: Union[Unset, Any] = UNSET
    region: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_length_in_ms = self.game_length_in_ms

        game_version = self.game_version

        is_completed = self.is_completed

        map_ = self.map_.to_dict()

        match_id = self.match_id

        party_rr_penaltys = []
        for party_rr_penaltys_item_data in self.party_rr_penaltys:
            party_rr_penaltys_item = party_rr_penaltys_item_data.to_dict()
            party_rr_penaltys.append(party_rr_penaltys_item)

        platform = self.platform

        queue = self.queue.to_dict()

        season = self.season.to_dict()

        started_at = self.started_at

        cluster: Union[None, Unset, str]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        else:
            cluster = self.cluster

        premier = self.premier

        region: Union[None, Unset, str]
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "game_length_in_ms": game_length_in_ms,
                "game_version": game_version,
                "is_completed": is_completed,
                "map": map_,
                "match_id": match_id,
                "party_rr_penaltys": party_rr_penaltys,
                "platform": platform,
                "queue": queue,
                "season": season,
                "started_at": started_at,
            }
        )
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if premier is not UNSET:
            field_dict["premier"] = premier
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.map_id_name_combo import MapIdNameCombo
        from ..models.matches_v4_data_metadata_party_rr_penalty import MatchesV4DataMetadataPartyRRPenalty
        from ..models.matches_v4_data_metadata_queue import MatchesV4DataMetadataQueue
        from ..models.season_id_short_combo import SeasonIdShortCombo

        d = dict(src_dict)
        game_length_in_ms = d.pop("game_length_in_ms")

        game_version = d.pop("game_version")

        is_completed = d.pop("is_completed")

        map_ = MapIdNameCombo.from_dict(d.pop("map"))

        match_id = d.pop("match_id")

        party_rr_penaltys = []
        _party_rr_penaltys = d.pop("party_rr_penaltys")
        for party_rr_penaltys_item_data in _party_rr_penaltys:
            party_rr_penaltys_item = MatchesV4DataMetadataPartyRRPenalty.from_dict(party_rr_penaltys_item_data)

            party_rr_penaltys.append(party_rr_penaltys_item)

        platform = d.pop("platform")

        queue = MatchesV4DataMetadataQueue.from_dict(d.pop("queue"))

        season = SeasonIdShortCombo.from_dict(d.pop("season"))

        started_at = d.pop("started_at")

        def _parse_cluster(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        premier = d.pop("premier", UNSET)

        def _parse_region(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        region = _parse_region(d.pop("region", UNSET))

        matches_v4_data_metadata = cls(
            game_length_in_ms=game_length_in_ms,
            game_version=game_version,
            is_completed=is_completed,
            map_=map_,
            match_id=match_id,
            party_rr_penaltys=party_rr_penaltys,
            platform=platform,
            queue=queue,
            season=season,
            started_at=started_at,
            cluster=cluster,
            premier=premier,
            region=region,
        )

        matches_v4_data_metadata.additional_properties = d
        return matches_v4_data_metadata

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
