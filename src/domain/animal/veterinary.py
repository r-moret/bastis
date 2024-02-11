from __future__ import annotations

from datetime import date, time
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.animal.animal import Animal


class VetAppointment:
    def __init__(
        self,
        date: date,
        animal: Animal,
        description: str | None = None,
        time_slot: tuple[time, time] | None = None,
    ) -> None:
        self.date = date
        self.description = description
        self.time_slot = time_slot

        self.animal = animal

    @property
    def time_slot(self) -> tuple[time, time] | None:
        return self._time_slot

    @time_slot.setter
    def time_slot(self, new_time_slot: tuple[time, time] | None) -> None:
        VetAppointment.validate_time_slot(new_time_slot)
        self._time_slot = new_time_slot

    @staticmethod
    def validate_time_slot(time_slot: tuple[time, time] | None) -> None:
        if time_slot is None:
            return

        start, end = time_slot
        if start > end:
            raise ValueError("VetAppointment end time must be later than its start time")
