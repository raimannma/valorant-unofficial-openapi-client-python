from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.matches_v2_data_metadata_premier_info import MatchesV2DataMetadataPremierInfo


T = TypeVar("T", bound="MatchesV2DataMetadata")


@_attrs_define
class MatchesV2DataMetadata:
    """
    Attributes:
        game_length (int):
        game_start (int):
        game_start_patched (str):
        game_version (str):
        matchid (str):
        mode_id (str):
        platform (str):
        premier_info (MatchesV2DataMetadataPremierInfo):
        rounds_played (int):
        season_id (str):
        cluster (Union[None, Unset, str]):
        map_ (Union[None, Unset, str]):
        mode (Union[None, Unset, str]):
        queue (Union[None, Unset, str]):
        region (Union[None, Unset, str]):
    """

    game_length: int
    game_start: int
    game_start_patched: str
    game_version: str
    matchid: str
    mode_id: str
    platform: str
    premier_info: "MatchesV2DataMetadataPremierInfo"
    rounds_played: int
    season_id: str
    cluster: Union[None, Unset, str] = UNSET
    map_: Union[None, Unset, str] = UNSET
    mode: Union[None, Unset, str] = UNSET
    queue: Union[None, Unset, str] = UNSET
    region: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        game_length = self.game_length

        game_start = self.game_start

        game_start_patched = self.game_start_patched

        game_version = self.game_version

        matchid = self.matchid

        mode_id = self.mode_id

        platform = self.platform

        premier_info = self.premier_info.to_dict()

        rounds_played = self.rounds_played

        season_id = self.season_id

        cluster: Union[None, Unset, str]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        else:
            cluster = self.cluster

        map_: Union[None, Unset, str]
        if isinstance(self.map_, Unset):
            map_ = UNSET
        else:
            map_ = self.map_

        mode: Union[None, Unset, str]
        if isinstance(self.mode, Unset):
            mode = UNSET
        else:
            mode = self.mode

        queue: Union[None, Unset, str]
        if isinstance(self.queue, Unset):
            queue = UNSET
        else:
            queue = self.queue

        region: Union[None, Unset, str]
        if isinstance(self.region, Unset):
            region = UNSET
        else:
            region = self.region

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "game_length": game_length,
                "game_start": game_start,
                "game_start_patched": game_start_patched,
                "game_version": game_version,
                "matchid": matchid,
                "mode_id": mode_id,
                "platform": platform,
                "premier_info": premier_info,
                "rounds_played": rounds_played,
                "season_id": season_id,
            }
        )
        if cluster is not UNSET:
            field_dict["cluster"] = cluster
        if map_ is not UNSET:
            field_dict["map"] = map_
        if mode is not UNSET:
            field_dict["mode"] = mode
        if queue is not UNSET:
            field_dict["queue"] = queue
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.matches_v2_data_metadata_premier_info import MatchesV2DataMetadataPremierInfo

        d = dict(src_dict)
        game_length = d.pop("game_length")

        game_start = d.pop("game_start")

        game_start_patched = d.pop("game_start_patched")

        game_version = d.pop("game_version")

        matchid = d.pop("matchid")

        mode_id = d.pop("mode_id")

        platform = d.pop("platform")

        premier_info = MatchesV2DataMetadataPremierInfo.from_dict(d.pop("premier_info"))

        rounds_played = d.pop("rounds_played")

        season_id = d.pop("season_id")

        def _parse_cluster(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        def _parse_map_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        map_ = _parse_map_(d.pop("map", UNSET))

        def _parse_mode(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mode = _parse_mode(d.pop("mode", UNSET))

        def _parse_queue(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        queue = _parse_queue(d.pop("queue", UNSET))

        def _parse_region(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        region = _parse_region(d.pop("region", UNSET))

        matches_v2_data_metadata = cls(
            game_length=game_length,
            game_start=game_start,
            game_start_patched=game_start_patched,
            game_version=game_version,
            matchid=matchid,
            mode_id=mode_id,
            platform=platform,
            premier_info=premier_info,
            rounds_played=rounds_played,
            season_id=season_id,
            cluster=cluster,
            map_=map_,
            mode=mode,
            queue=queue,
            region=region,
        )

        matches_v2_data_metadata.additional_properties = d
        return matches_v2_data_metadata

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
