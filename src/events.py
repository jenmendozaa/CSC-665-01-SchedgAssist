"""
events.py

Defines the Event class (things we want to schedule).
"""

from dataclasses import dataclass


@dataclass
class Event:
    """
    Represents an event to schedule (like a study session).

    duration_blocks: number of half-hour blocks required.
    deadline_day: last day index (0..6) by which the event should be scheduled.
    priority: higher = more important.
    event_type: e.g., "study", "workout", "meeting".
    preferred_time: rough preference for time of day ("morning", "afternoon", "evening", or None).
    """
    name: str
    duration_blocks: int
    deadline_day: int
    priority: int = 1
    event_type: str = "study"
    preferred_time: str | None = None  # "morning", "afternoon", "evening" or None
