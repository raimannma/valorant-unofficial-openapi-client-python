from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AccountV2Data")


@_attrs_define
class AccountV2Data:
    """
    Attributes:
        account_level (int):
        card (str):
        name (str):
        platforms (list[str]):
        puuid (str):
        region (str):
        tag (str):
        title (str):
        updated_at (str):
    """

    account_level: int
    card: str
    name: str
    platforms: list[str]
    puuid: str
    region: str
    tag: str
    title: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_level = self.account_level

        card = self.card

        name = self.name

        platforms = self.platforms

        puuid = self.puuid

        region = self.region

        tag = self.tag

        title = self.title

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_level": account_level,
                "card": card,
                "name": name,
                "platforms": platforms,
                "puuid": puuid,
                "region": region,
                "tag": tag,
                "title": title,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_level = d.pop("account_level")

        card = d.pop("card")

        name = d.pop("name")

        platforms = cast(list[str], d.pop("platforms"))

        puuid = d.pop("puuid")

        region = d.pop("region")

        tag = d.pop("tag")

        title = d.pop("title")

        updated_at = d.pop("updated_at")

        account_v2_data = cls(
            account_level=account_level,
            card=card,
            name=name,
            platforms=platforms,
            puuid=puuid,
            region=region,
            tag=tag,
            title=title,
            updated_at=updated_at,
        )

        account_v2_data.additional_properties = d
        return account_v2_data

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
