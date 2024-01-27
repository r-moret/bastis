from datetime import date, time
from domain.animal.treatment import Treatment
from domain.animal.veterinary import VetAppointment


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
        self.vet_appointments: list[VetAppointment] = []

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

    def remove_treatment(self, treatment: Treatment) -> None:
        self.treatments.remove(treatment)

    def add_vet_appointment(
        self,
        date: date,
        description: str | None = None,
        time_slot: tuple[time, time] | None = None,
    ) -> None:
        vet_appointment = VetAppointment(date, description, time_slot)
        self.vet_appointments.append(vet_appointment)

    def remove_vet_appointment(self, vet_appointment: VetAppointment) -> None:
        self.vet_appointments.remove(vet_appointment)
