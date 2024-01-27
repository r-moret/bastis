from datetime import date
from domain.animal.treatment import Treatment


class Animal:
    def __init__(
        self,
        name: str,
        entry_date: date,
        birth_date: date | None = None,
        personality: str | None = None,
        physical_description: str | None = None,
    ) -> None:
        self.name = name
        self.entry_date = entry_date
        self.birth_date = birth_date
        self.personality = personality
        self.physical_description = physical_description
        self.treatments: list[Treatment] = []

    def add_treatment(
        self,
        medication: str,
        zone: str | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        periodicity: int | None = None,
    ) -> None:
        treatment = Treatment(medication, zone, start_date, end_date, periodicity)
        self.treatments.append(treatment)

    def remove_treatment(self, treatment: Treatment) -> None:  # TODO: Treatment or parameters?
        self.treatments.remove(treatment)
