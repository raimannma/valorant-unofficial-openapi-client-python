from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.status_incident_content import StatusIncidentContent
    from ..models.status_incident_update import StatusIncidentUpdate


T = TypeVar("T", bound="StatusIncident")


@_attrs_define
class StatusIncident:
    """
    Attributes:
        created_at (str):
        id (int):
        incident_severity (str):
        platforms (list[str]):
        titles (list['StatusIncidentContent']):
        updated_at (str):
        updates (list['StatusIncidentUpdate']):
        archive_at (Union[None, Unset, str]):
        maintenance_status (Union[None, Unset, str]):
    """

    created_at: str
    id: int
    incident_severity: str
    platforms: list[str]
    titles: list["StatusIncidentContent"]
    updated_at: str
    updates: list["StatusIncidentUpdate"]
    archive_at: Union[None, Unset, str] = UNSET
    maintenance_status: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        id = self.id

        incident_severity = self.incident_severity

        platforms = self.platforms

        titles = []
        for titles_item_data in self.titles:
            titles_item = titles_item_data.to_dict()
            titles.append(titles_item)

        updated_at = self.updated_at

        updates = []
        for updates_item_data in self.updates:
            updates_item = updates_item_data.to_dict()
            updates.append(updates_item)

        archive_at: Union[None, Unset, str]
        if isinstance(self.archive_at, Unset):
            archive_at = UNSET
        else:
            archive_at = self.archive_at

        maintenance_status: Union[None, Unset, str]
        if isinstance(self.maintenance_status, Unset):
            maintenance_status = UNSET
        else:
            maintenance_status = self.maintenance_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "id": id,
                "incident_severity": incident_severity,
                "platforms": platforms,
                "titles": titles,
                "updated_at": updated_at,
                "updates": updates,
            }
        )
        if archive_at is not UNSET:
            field_dict["archive_at"] = archive_at
        if maintenance_status is not UNSET:
            field_dict["maintenance_status"] = maintenance_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_incident_content import StatusIncidentContent
        from ..models.status_incident_update import StatusIncidentUpdate

        d = dict(src_dict)
        created_at = d.pop("created_at")

        id = d.pop("id")

        incident_severity = d.pop("incident_severity")

        platforms = cast(list[str], d.pop("platforms"))

        titles = []
        _titles = d.pop("titles")
        for titles_item_data in _titles:
            titles_item = StatusIncidentContent.from_dict(titles_item_data)

            titles.append(titles_item)

        updated_at = d.pop("updated_at")

        updates = []
        _updates = d.pop("updates")
        for updates_item_data in _updates:
            updates_item = StatusIncidentUpdate.from_dict(updates_item_data)

            updates.append(updates_item)

        def _parse_archive_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        archive_at = _parse_archive_at(d.pop("archive_at", UNSET))

        def _parse_maintenance_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        maintenance_status = _parse_maintenance_status(d.pop("maintenance_status", UNSET))

        status_incident = cls(
            created_at=created_at,
            id=id,
            incident_severity=incident_severity,
            platforms=platforms,
            titles=titles,
            updated_at=updated_at,
            updates=updates,
            archive_at=archive_at,
            maintenance_status=maintenance_status,
        )

        status_incident.additional_properties = d
        return status_incident

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
