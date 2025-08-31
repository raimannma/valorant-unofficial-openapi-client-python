from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_incident_content import StatusIncidentContent


T = TypeVar("T", bound="StatusIncidentUpdate")


@_attrs_define
class StatusIncidentUpdate:
    """
    Attributes:
        author (str):
        created_at (str):
        id (int):
        publish (bool):
        publish_locations (list[str]):
        translations (list['StatusIncidentContent']):
        updated_at (str):
    """

    author: str
    created_at: str
    id: int
    publish: bool
    publish_locations: list[str]
    translations: list["StatusIncidentContent"]
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        author = self.author

        created_at = self.created_at

        id = self.id

        publish = self.publish

        publish_locations = self.publish_locations

        translations = []
        for translations_item_data in self.translations:
            translations_item = translations_item_data.to_dict()
            translations.append(translations_item)

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "author": author,
                "created_at": created_at,
                "id": id,
                "publish": publish,
                "publish_locations": publish_locations,
                "translations": translations,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_incident_content import StatusIncidentContent

        d = dict(src_dict)
        author = d.pop("author")

        created_at = d.pop("created_at")

        id = d.pop("id")

        publish = d.pop("publish")

        publish_locations = cast(list[str], d.pop("publish_locations"))

        translations = []
        _translations = d.pop("translations")
        for translations_item_data in _translations:
            translations_item = StatusIncidentContent.from_dict(translations_item_data)

            translations.append(translations_item)

        updated_at = d.pop("updated_at")

        status_incident_update = cls(
            author=author,
            created_at=created_at,
            id=id,
            publish=publish,
            publish_locations=publish_locations,
            translations=translations,
            updated_at=updated_at,
        )

        status_incident_update.additional_properties = d
        return status_incident_update

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
