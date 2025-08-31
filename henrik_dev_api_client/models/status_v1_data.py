from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.status_incident import StatusIncident


T = TypeVar("T", bound="StatusV1Data")


@_attrs_define
class StatusV1Data:
    """
    Attributes:
        incidents (list['StatusIncident']):
        maintenances (list['StatusIncident']):
    """

    incidents: list["StatusIncident"]
    maintenances: list["StatusIncident"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        incidents = []
        for incidents_item_data in self.incidents:
            incidents_item = incidents_item_data.to_dict()
            incidents.append(incidents_item)

        maintenances = []
        for maintenances_item_data in self.maintenances:
            maintenances_item = maintenances_item_data.to_dict()
            maintenances.append(maintenances_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "incidents": incidents,
                "maintenances": maintenances,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.status_incident import StatusIncident

        d = dict(src_dict)
        incidents = []
        _incidents = d.pop("incidents")
        for incidents_item_data in _incidents:
            incidents_item = StatusIncident.from_dict(incidents_item_data)

            incidents.append(incidents_item)

        maintenances = []
        _maintenances = d.pop("maintenances")
        for maintenances_item_data in _maintenances:
            maintenances_item = StatusIncident.from_dict(maintenances_item_data)

            maintenances.append(maintenances_item)

        status_v1_data = cls(
            incidents=incidents,
            maintenances=maintenances,
        )

        status_v1_data.additional_properties = d
        return status_v1_data

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
