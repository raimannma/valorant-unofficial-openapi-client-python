from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mmrv3_account import MMRV3Account
    from ..models.mmrv3_current import MMRV3Current
    from ..models.mmrv3_peak import MMRV3Peak
    from ..models.mmrv3_seasonal import MMRV3Seasonal


T = TypeVar("T", bound="MMRV3Data")


@_attrs_define
class MMRV3Data:
    """
    Attributes:
        account (MMRV3Account):
        current (MMRV3Current):
        seasonal (list['MMRV3Seasonal']):
        peak (Union['MMRV3Peak', None, Unset]):
    """

    account: "MMRV3Account"
    current: "MMRV3Current"
    seasonal: list["MMRV3Seasonal"]
    peak: Union["MMRV3Peak", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mmrv3_peak import MMRV3Peak

        account = self.account.to_dict()

        current = self.current.to_dict()

        seasonal = []
        for seasonal_item_data in self.seasonal:
            seasonal_item = seasonal_item_data.to_dict()
            seasonal.append(seasonal_item)

        peak: Union[None, Unset, dict[str, Any]]
        if isinstance(self.peak, Unset):
            peak = UNSET
        elif isinstance(self.peak, MMRV3Peak):
            peak = self.peak.to_dict()
        else:
            peak = self.peak

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "current": current,
                "seasonal": seasonal,
            }
        )
        if peak is not UNSET:
            field_dict["peak"] = peak

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mmrv3_account import MMRV3Account
        from ..models.mmrv3_current import MMRV3Current
        from ..models.mmrv3_peak import MMRV3Peak
        from ..models.mmrv3_seasonal import MMRV3Seasonal

        d = dict(src_dict)
        account = MMRV3Account.from_dict(d.pop("account"))

        current = MMRV3Current.from_dict(d.pop("current"))

        seasonal = []
        _seasonal = d.pop("seasonal")
        for seasonal_item_data in _seasonal:
            seasonal_item = MMRV3Seasonal.from_dict(seasonal_item_data)

            seasonal.append(seasonal_item)

        def _parse_peak(data: object) -> Union["MMRV3Peak", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                peak_type_1 = MMRV3Peak.from_dict(data)

                return peak_type_1
            except:  # noqa: E722
                pass
            return cast(Union["MMRV3Peak", None, Unset], data)

        peak = _parse_peak(d.pop("peak", UNSET))

        mmrv3_data = cls(
            account=account,
            current=current,
            seasonal=seasonal,
            peak=peak,
        )

        mmrv3_data.additional_properties = d
        return mmrv3_data

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
