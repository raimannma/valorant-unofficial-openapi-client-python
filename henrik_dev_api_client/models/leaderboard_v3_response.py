from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.leaderboard_v3_data import LeaderboardV3Data
    from ..models.pagination import Pagination


T = TypeVar("T", bound="LeaderboardV3Response")


@_attrs_define
class LeaderboardV3Response:
    """
    Attributes:
        data (LeaderboardV3Data):
        results (Pagination):
        status (int):
    """

    data: "LeaderboardV3Data"
    results: "Pagination"
    status: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        results = self.results.to_dict()

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "results": results,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.leaderboard_v3_data import LeaderboardV3Data
        from ..models.pagination import Pagination

        d = dict(src_dict)
        data = LeaderboardV3Data.from_dict(d.pop("data"))

        results = Pagination.from_dict(d.pop("results"))

        status = d.pop("status")

        leaderboard_v3_response = cls(
            data=data,
            results=results,
            status=status,
        )

        leaderboard_v3_response.additional_properties = d
        return leaderboard_v3_response

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
