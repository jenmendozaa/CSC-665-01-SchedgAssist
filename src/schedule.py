"""
schedule.py

Defines classes/functions for representing a weekly schedule grid.
"""

from dataclasses import dataclass, field
from typing import List, Tuple

from .config import BLOCKS_PER_DAY, DAYS_PER_WEEK, TOTAL_BLOCKS


@dataclass
class WeeklySchedule:
    """
    Represents a 7-day schedule with half-hour blocks.

    blocks[i] = 0 → free
    blocks[i] = 1 → occupied

    Block index i runs from 0..TOTAL_BLOCKS-1, where
    i = day * BLOCKS_PER_DAY + block_in_day
    """

    blocks: List[int] = field(default_factory=lambda: [0] * TOTAL_BLOCKS)

    def is_free_block(self, idx: int) -> bool:
        """Return True if block idx is free."""
        return self.blocks[idx] == 0

    def occupy_block(self, idx: int) -> None:
        """Mark block idx as occupied."""
        self.blocks[idx] = 1

    def occupy_range(self, start: int, duration: int) -> None:
        """Mark a range [start, start+duration) as occupied."""
        for i in range(start, start + duration):
            if 0 <= i < TOTAL_BLOCKS:
                self.blocks[i] = 1

    def free_range(self, start: int, duration: int) -> None:
        """Mark a range [start, start+duration) as free."""
        for i in range(start, start + duration):
            if 0 <= i < TOTAL_BLOCKS:
                self.blocks[i] = 0

    def day_block_to_index(self, day: int, block_in_day: int) -> int:
        """Convert (day, block_in_day) -> global index 0..TOTAL_BLOCKS-1."""
        return day * BLOCKS_PER_DAY + block_in_day

    def index_to_day_block(self, idx: int) -> Tuple[int, int]:
        """Convert global index -> (day, block_in_day)."""
        day = idx // BLOCKS_PER_DAY
        block_in_day = idx % BLOCKS_PER_DAY
        return day, block_in_day

    def pretty_print(self) -> None:
        """
        Print a rough view of the schedule:
        - Each row = day
        - 'X' = occupied, '.' = free
        """
        day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for day in range(DAYS_PER_WEEK):
            row = []
            for b in range(BLOCKS_PER_DAY):
                idx = self.day_block_to_index(day, b)
                row.append("X" if self.blocks[idx] == 1 else ".")
            print(f"{day_names[day]}: {''.join(row)}")

    def get_occupied_blocks(self) -> List[int]:
        """Return a list of indices that are occupied."""
        return [i for i, v in enumerate(self.blocks) if v == 1]
