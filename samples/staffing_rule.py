"""Turn occupancy into a suggested staff count. Simple rule, sample only."""
import math

MIN_STAFF = 2  # never fewer than two on the floor


def staff_needed(queue, dining, customers_per_staff=8):
    load = queue * 1.5 + dining * 0.5  # people waiting need more attention
    return max(MIN_STAFF, math.ceil(load / customers_per_staff))
