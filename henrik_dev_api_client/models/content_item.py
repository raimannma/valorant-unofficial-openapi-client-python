from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_item_localized_names_type_0 import ContentItemLocalizedNamesType0


T = TypeVar("T", bound="ContentItem")


@_attrs_define
class ContentItem:
    """
    Attributes:
        asset_name (str):
        name (str):
        id (Union[None, Unset, str]):
        localized_names (Union['ContentItemLocalizedNamesType0', None, Unset]):
    """

    asset_name: str
    name: str
    id: Union[None, Unset, str] = UNSET
    localized_names: Union["ContentItemLocalizedNamesType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_item_localized_names_type_0 import ContentItemLocalizedNamesType0

        asset_name = self.asset_name

        name = self.name

        id: Union[None, Unset, str]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        localized_names: Union[None, Unset, dict[str, Any]]
        if isinstance(self.localized_names, Unset):
            localized_names = UNSET
        elif isinstance(self.localized_names, ContentItemLocalizedNamesType0):
            localized_names = self.localized_names.to_dict()
        else:
            localized_names = self.localized_names

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "assetName": asset_name,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if localized_names is not UNSET:
            field_dict["localizedNames"] = localized_names

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_item_localized_names_type_0 import ContentItemLocalizedNamesType0

        d = dict(src_dict)
        asset_name = d.pop("assetName")

        name = d.pop("name")

        def _parse_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_localized_names(data: object) -> Union["ContentItemLocalizedNamesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                localized_names_type_0 = ContentItemLocalizedNamesType0.from_dict(data)

                return localized_names_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ContentItemLocalizedNamesType0", None, Unset], data)

        localized_names = _parse_localized_names(d.pop("localizedNames", UNSET))

        content_item = cls(
            asset_name=asset_name,
            name=name,
            id=id,
            localized_names=localized_names,
        )

        content_item.additional_properties = d
        return content_item

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
