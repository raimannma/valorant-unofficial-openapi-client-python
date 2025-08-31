from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.account_v1_data_card import AccountV1DataCard


T = TypeVar("T", bound="AccountV1Data")


@_attrs_define
class AccountV1Data:
    """
    Attributes:
        account_level (int):
        card (AccountV1DataCard):
        last_update (str):
        last_update_raw (int):
        name (str):
        puuid (str):
        region (str):
        tag (str):
    """

    account_level: int
    card: "AccountV1DataCard"
    last_update: str
    last_update_raw: int
    name: str
    puuid: str
    region: str
    tag: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_level = self.account_level

        card = self.card.to_dict()

        last_update = self.last_update

        last_update_raw = self.last_update_raw

        name = self.name

        puuid = self.puuid

        region = self.region

        tag = self.tag

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_level": account_level,
                "card": card,
                "last_update": last_update,
                "last_update_raw": last_update_raw,
                "name": name,
                "puuid": puuid,
                "region": region,
                "tag": tag,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account_v1_data_card import AccountV1DataCard

        d = dict(src_dict)
        account_level = d.pop("account_level")

        card = AccountV1DataCard.from_dict(d.pop("card"))

        last_update = d.pop("last_update")

        last_update_raw = d.pop("last_update_raw")

        name = d.pop("name")

        puuid = d.pop("puuid")

        region = d.pop("region")

        tag = d.pop("tag")

        account_v1_data = cls(
            account_level=account_level,
            card=card,
            last_update=last_update,
            last_update_raw=last_update_raw,
            name=name,
            puuid=puuid,
            region=region,
            tag=tag,
        )

        account_v1_data.additional_properties = d
        return account_v1_data

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
