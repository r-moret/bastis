from datetime import date


class Treatment:
    def __init__(
        self,
        medication: str,
        zone: str | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        periodicity: int | None = None,
    ) -> None:
        self.medication = medication
        self.zone = zone
        self.start_date = start_date
        self.end_date = end_date
        self.periodicity = periodicity
