from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.esports_v1_data_league import EsportsV1DataLeague
    from ..models.esports_v1_data_match import EsportsV1DataMatch
    from ..models.esports_v1_data_tournament import EsportsV1DataTournament


T = TypeVar("T", bound="EsportsV1Data")


@_attrs_define
class EsportsV1Data:
    """
    Attributes:
        date (str):
        league (EsportsV1DataLeague):
        match (EsportsV1DataMatch):
        state (str):
        tournament (EsportsV1DataTournament):
        type_ (str):
        vod (Union[None, Unset, str]):
    """

    date: str
    league: "EsportsV1DataLeague"
    match: "EsportsV1DataMatch"
    state: str
    tournament: "EsportsV1DataTournament"
    type_: str
    vod: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        league = self.league.to_dict()

        match = self.match.to_dict()

        state = self.state

        tournament = self.tournament.to_dict()

        type_ = self.type_

        vod: Union[None, Unset, str]
        if isinstance(self.vod, Unset):
            vod = UNSET
        else:
            vod = self.vod

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "league": league,
                "match": match,
                "state": state,
                "tournament": tournament,
                "type": type_,
            }
        )
        if vod is not UNSET:
            field_dict["vod"] = vod

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.esports_v1_data_league import EsportsV1DataLeague
        from ..models.esports_v1_data_match import EsportsV1DataMatch
        from ..models.esports_v1_data_tournament import EsportsV1DataTournament

        d = dict(src_dict)
        date = d.pop("date")

        league = EsportsV1DataLeague.from_dict(d.pop("league"))

        match = EsportsV1DataMatch.from_dict(d.pop("match"))

        state = d.pop("state")

        tournament = EsportsV1DataTournament.from_dict(d.pop("tournament"))

        type_ = d.pop("type")

        def _parse_vod(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vod = _parse_vod(d.pop("vod", UNSET))

        esports_v1_data = cls(
            date=date,
            league=league,
            match=match,
            state=state,
            tournament=tournament,
            type_=type_,
            vod=vod,
        )

        esports_v1_data.additional_properties = d
        return esports_v1_data

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
