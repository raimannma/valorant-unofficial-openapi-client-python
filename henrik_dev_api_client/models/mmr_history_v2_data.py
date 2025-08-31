from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.mmr_history_v2_history import MMRHistoryV2History
    from ..models.mmrv3_account import MMRV3Account


T = TypeVar("T", bound="MMRHistoryV2Data")


@_attrs_define
class MMRHistoryV2Data:
    """
    Attributes:
        account (MMRV3Account):
        history (list['MMRHistoryV2History']):
    """

    account: "MMRV3Account"
    history: list["MMRHistoryV2History"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account = self.account.to_dict()

        history = []
        for history_item_data in self.history:
            history_item = history_item_data.to_dict()
            history.append(history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account": account,
                "history": history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mmr_history_v2_history import MMRHistoryV2History
        from ..models.mmrv3_account import MMRV3Account

        d = dict(src_dict)
        account = MMRV3Account.from_dict(d.pop("account"))

        history = []
        _history = d.pop("history")
        for history_item_data in _history:
            history_item = MMRHistoryV2History.from_dict(history_item_data)

            history.append(history_item)

        mmr_history_v2_data = cls(
            account=account,
            history=history,
        )

        mmr_history_v2_data.additional_properties = d
        return mmr_history_v2_data

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
