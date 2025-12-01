"""
heuristics.py

Contains simple heuristic / baseline algorithms for placing events.
"""

from typing import Optional

from .schedule import WeeklySchedule
from .events import Event
from .config import BLOCKS_PER_DAY


def first_fit(schedule: WeeklySchedule, event: Event) -> Optional[int]:
    """
    Simple baseline:
    - Scan from the beginning of the week
    - Find the first range of free blocks that fits the event
      and finishes before or on the deadline day.

    Returns:
        start_idx (int) of chosen slot, or None if no valid slot exists.
    """
    max_block = (event.deadline_day + 1) * BLOCKS_PER_DAY

    for start in range(0, max_block - event.duration_blocks + 1):
        # Check all blocks in the range are free
        all_free = True
        for i in range(start, start + event.duration_blocks):
            if not schedule.is_free_block(i):
                all_free = False
                break
        if all_free:
            return start

    return None


def earliest_day_fit(schedule: WeeklySchedule, event: Event) -> Optional[int]:
    """
    Slightly smarter baseline:
    - Try each day from 0..deadline_day
    - For each day, look for the first fit within that day.
    This tends to avoid spreading events across days weirdly.

    Returns:
        start_idx or None.
    """
    for day in range(event.deadline_day + 1):
        start_idx = day * BLOCKS_PER_DAY
        end_idx = (day + 1) * BLOCKS_PER_DAY

        for start in range(start_idx, end_idx - event.duration_blocks + 1):
            all_free = True
            for i in range(start, start + event.duration_blocks):
                if not schedule.is_free_block(i):
                    all_free = False
                    break
            if all_free:
                return start

    return None
