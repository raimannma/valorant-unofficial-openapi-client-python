from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="MatchesV4DataObserver")


@_attrs_define
class MatchesV4DataObserver:
    """
    Attributes:
        account_level (int):
        card_id (str):
        name (str):
        party_id (str):
        puuid (str):
        session_playtime_in_ms (int):
        tag (str):
        title_id (str):
    """

    account_level: int
    card_id: str
    name: str
    party_id: str
    puuid: str
    session_playtime_in_ms: int
    tag: str
    title_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_level = self.account_level

        card_id = self.card_id

        name = self.name

        party_id = self.party_id

        puuid = self.puuid

        session_playtime_in_ms = self.session_playtime_in_ms

        tag = self.tag

        title_id = self.title_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_level": account_level,
                "card_id": card_id,
                "name": name,
                "party_id": party_id,
                "puuid": puuid,
                "session_playtime_in_ms": session_playtime_in_ms,
                "tag": tag,
                "title_id": title_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_level = d.pop("account_level")

        card_id = d.pop("card_id")

        name = d.pop("name")

        party_id = d.pop("party_id")

        puuid = d.pop("puuid")

        session_playtime_in_ms = d.pop("session_playtime_in_ms")

        tag = d.pop("tag")

        title_id = d.pop("title_id")

        matches_v4_data_observer = cls(
            account_level=account_level,
            card_id=card_id,
            name=name,
            party_id=party_id,
            puuid=puuid,
            session_playtime_in_ms=session_playtime_in_ms,
            tag=tag,
            title_id=title_id,
        )

        matches_v4_data_observer.additional_properties = d
        return matches_v4_data_observer

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
