from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bundle import Bundle


T = TypeVar("T", bound="FeaturedBundle")


@_attrs_define
class FeaturedBundle:
    """
    Attributes:
        bundle (Bundle):
        bundle_remaining_duration_in_seconds (int):
        bundles (list['Bundle']):
    """

    bundle: "Bundle"
    bundle_remaining_duration_in_seconds: int
    bundles: list["Bundle"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bundle = self.bundle.to_dict()

        bundle_remaining_duration_in_seconds = self.bundle_remaining_duration_in_seconds

        bundles = []
        for bundles_item_data in self.bundles:
            bundles_item = bundles_item_data.to_dict()
            bundles.append(bundles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "Bundle": bundle,
                "BundleRemainingDurationInSeconds": bundle_remaining_duration_in_seconds,
                "Bundles": bundles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bundle import Bundle

        d = dict(src_dict)
        bundle = Bundle.from_dict(d.pop("Bundle"))

        bundle_remaining_duration_in_seconds = d.pop("BundleRemainingDurationInSeconds")

        bundles = []
        _bundles = d.pop("Bundles")
        for bundles_item_data in _bundles:
            bundles_item = Bundle.from_dict(bundles_item_data)

            bundles.append(bundles_item)

        featured_bundle = cls(
            bundle=bundle,
            bundle_remaining_duration_in_seconds=bundle_remaining_duration_in_seconds,
            bundles=bundles,
        )

        featured_bundle.additional_properties = d
        return featured_bundle

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
