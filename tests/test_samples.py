from samples.occupancy import Box, count_by_zone
from samples.staffing_rule import staff_needed


def test_count_by_zone():
    boxes = [
        Box(0.1, 0.5, "person", 0.9),
        Box(0.2, 0.5, "person", 0.3),  # low confidence, ignored
        Box(0.5, 0.5, "person", 0.8),
        Box(0.8, 0.5, "chair", 0.9),   # not a person
    ]
    assert count_by_zone(boxes) == {"queue": 1, "counter": 1, "dining": 0}


def test_quiet_period_keeps_minimum():
    assert staff_needed(queue=0, dining=2) == 2


def test_rush_adds_staff():
    assert staff_needed(queue=12, dining=20) == 4
