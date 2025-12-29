"""Mission planning primitives for the seed-planting drone."""

from dataclasses import dataclass
from typing import List


@dataclass
class Waypoint:
    latitude: float
    longitude: float
    altitude: float
    action: str = "transit"


def seed_drop_pattern(start: Waypoint, spacing_m: float, count: int) -> List[Waypoint]:
    """Generate a straight-line seed drop pattern starting from the given waypoint."""
    steps: List[Waypoint] = []
    for i in range(count):
        steps.append(
            Waypoint(
                latitude=start.latitude,
                longitude=start.longitude + (spacing_m * i),
                altitude=start.altitude,
                action="drop",
            )
        )
    return steps
