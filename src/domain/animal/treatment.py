from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from domain.animal.animal import Animal


class Treatment:
    def __init__(
        self,
        medication: str,
        animal: Animal,
        zone: str | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        periodicity: int | None = None,
    ) -> None:
        Treatment.validate_dates(start_date, end_date)

        self.medication = medication
        self.zone = zone
        self._start_date = start_date
        self._end_date = end_date
        self.periodicity = periodicity

        self.animal = animal

    @property
    def start_date(self) -> date | None:
        return self._start_date

    @start_date.setter
    def start_date(self, new_start_date: date | None) -> None:
        Treatment.validate_dates(new_start_date, self.end_date)
        self._start_date = new_start_date

    @property
    def end_date(self) -> date | None:
        return self._end_date

    @end_date.setter
    def end_date(self, new_end_date: date | None) -> None:
        Treatment.validate_dates(self.start_date, new_end_date)
        self._end_date = new_end_date

    @property
    def periodicity(self):
        return self._periodicity

    @periodicity.setter
    def periodicity(self, new_periodicity: int | None) -> None:
        if new_periodicity is not None and new_periodicity <= 0:
            raise ValueError("Periodicity must be a positive integer")

        self._periodicity = new_periodicity

    @staticmethod
    def validate_dates(start_date: date | None, end_date: date | None) -> None:
        if end_date is not None:
            if start_date is None:
                raise ValueError("Treatment cannot have end_date if start_date is None")

            if start_date > end_date:
                raise ValueError("Treatment end_date must be later than start_date")
