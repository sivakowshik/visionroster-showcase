"""Count people per zone from detection boxes.

Sample code for the showcase repo, not the product implementation.
"""
from dataclasses import dataclass


@dataclass
class Box:
    x: float  # centre x, 0-1
    y: float  # centre y, 0-1
    label: str
    score: float


# Zones as (x_min, y_min, x_max, y_max) in normalised coordinates
ZONES = {
    "queue": (0.0, 0.0, 0.4, 1.0),
    "counter": (0.4, 0.0, 0.6, 1.0),
    "dining": (0.6, 0.0, 1.0, 1.0),
}


def blur_faces(frame):
    """Placeholder. In the real pipeline faces are blurred before anything
    is stored or shown. Here we just pass the frame through."""
    return frame


def count_by_zone(boxes, min_score=0.5):
    counts = {name: 0 for name in ZONES}
    for b in boxes:
        if b.label != "person" or b.score < min_score:
            continue
        for name, (x0, y0, x1, y1) in ZONES.items():
            if x0 <= b.x < x1 and y0 <= b.y <= y1:
                counts[name] += 1
                break
    return counts
