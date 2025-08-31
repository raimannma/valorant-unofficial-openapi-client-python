from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.featured_bundle import FeaturedBundle


T = TypeVar("T", bound="StoreFeaturedV1")


@_attrs_define
class StoreFeaturedV1:
    """
    Attributes:
        featured_bundle (FeaturedBundle):
    """

    featured_bundle: "FeaturedBundle"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        featured_bundle = self.featured_bundle.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "FeaturedBundle": featured_bundle,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.featured_bundle import FeaturedBundle

        d = dict(src_dict)
        featured_bundle = FeaturedBundle.from_dict(d.pop("FeaturedBundle"))

        store_featured_v1 = cls(
            featured_bundle=featured_bundle,
        )

        store_featured_v1.additional_properties = d
        return store_featured_v1

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
