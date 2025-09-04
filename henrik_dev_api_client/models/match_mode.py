from typing import Literal, cast

MatchMode = Literal["Competitive", "Custom", "Practice", "Unknown", "Unrated"]

MATCH_MODE_VALUES: set[MatchMode] = {
    "Competitive",
    "Custom",
    "Practice",
    "Unknown",
    "Unrated",
}


def check_match_mode(value: str) -> MatchMode:
    if value in MATCH_MODE_VALUES:
        return cast(MatchMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MATCH_MODE_VALUES!r}")
