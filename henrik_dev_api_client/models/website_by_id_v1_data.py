from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebsiteByIdV1Data")


@_attrs_define
class WebsiteByIdV1Data:
    """
    Attributes:
        category (str):
        date (str):
        title (str):
        url (str):
        banner_url (Union[None, Unset, str]):
        content (Union[None, Unset, str]):
        description (Union[None, Unset, str]):
        external_link (Union[None, Unset, str]):
    """

    category: str
    date: str
    title: str
    url: str
    banner_url: Union[None, Unset, str] = UNSET
    content: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    external_link: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category = self.category

        date = self.date

        title = self.title

        url = self.url

        banner_url: Union[None, Unset, str]
        if isinstance(self.banner_url, Unset):
            banner_url = UNSET
        else:
            banner_url = self.banner_url

        content: Union[None, Unset, str]
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        external_link: Union[None, Unset, str]
        if isinstance(self.external_link, Unset):
            external_link = UNSET
        else:
            external_link = self.external_link

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "date": date,
                "title": title,
                "url": url,
            }
        )
        if banner_url is not UNSET:
            field_dict["banner_url"] = banner_url
        if content is not UNSET:
            field_dict["content"] = content
        if description is not UNSET:
            field_dict["description"] = description
        if external_link is not UNSET:
            field_dict["external_link"] = external_link

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        category = d.pop("category")

        date = d.pop("date")

        title = d.pop("title")

        url = d.pop("url")

        def _parse_banner_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        banner_url = _parse_banner_url(d.pop("banner_url", UNSET))

        def _parse_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_external_link(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_link = _parse_external_link(d.pop("external_link", UNSET))

        website_by_id_v1_data = cls(
            category=category,
            date=date,
            title=title,
            url=url,
            banner_url=banner_url,
            content=content,
            description=description,
            external_link=external_link,
        )

        website_by_id_v1_data.additional_properties = d
        return website_by_id_v1_data

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
