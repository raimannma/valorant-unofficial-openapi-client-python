from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stored_match_meta_map import StoredMatchMetaMap
    from ..models.stored_match_meta_season import StoredMatchMetaSeason


T = TypeVar("T", bound="StoredMatchMeta")


@_attrs_define
class StoredMatchMeta:
    """
    Attributes:
        id (str):
        map_ (StoredMatchMetaMap):
        mode (str):
        region (str):
        season (StoredMatchMetaSeason):
        started_at (str):
        version (str):
        cluster (Union[None, Unset, str]):
    """

    id: str
    map_: "StoredMatchMetaMap"
    mode: str
    region: str
    season: "StoredMatchMetaSeason"
    started_at: str
    version: str
    cluster: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        map_ = self.map_.to_dict()

        mode = self.mode

        region = self.region

        season = self.season.to_dict()

        started_at = self.started_at

        version = self.version

        cluster: Union[None, Unset, str]
        if isinstance(self.cluster, Unset):
            cluster = UNSET
        else:
            cluster = self.cluster

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "map": map_,
                "mode": mode,
                "region": region,
                "season": season,
                "started_at": started_at,
                "version": version,
            }
        )
        if cluster is not UNSET:
            field_dict["cluster"] = cluster

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stored_match_meta_map import StoredMatchMetaMap
        from ..models.stored_match_meta_season import StoredMatchMetaSeason

        d = dict(src_dict)
        id = d.pop("id")

        map_ = StoredMatchMetaMap.from_dict(d.pop("map"))

        mode = d.pop("mode")

        region = d.pop("region")

        season = StoredMatchMetaSeason.from_dict(d.pop("season"))

        started_at = d.pop("started_at")

        version = d.pop("version")

        def _parse_cluster(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cluster = _parse_cluster(d.pop("cluster", UNSET))

        stored_match_meta = cls(
            id=id,
            map_=map_,
            mode=mode,
            region=region,
            season=season,
            started_at=started_at,
            version=version,
            cluster=cluster,
        )

        stored_match_meta.additional_properties = d
        return stored_match_meta

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
