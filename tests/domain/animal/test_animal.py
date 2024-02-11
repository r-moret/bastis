from datetime import date, time

from domain.animal.animal import Animal
from domain.animal.treatment import Treatment
from domain.animal.veterinary import VetAppointment


def test_add_treatment(animal: Animal, treatment: Treatment):
    animal.add_treatment(treatment)

    assert animal == treatment.animal
    assert len(animal.treatments) == 1
    assert animal.treatments[0] == treatment


def test_remove_treatment(animal: Animal, treatment: Treatment):
    animal.add_treatment(treatment)
    animal.remove_treatment(treatment)

    assert len(animal.treatments) == 0


def test_add_vet_appointment(animal: Animal):
    vet_appointment = VetAppointment(
        date(2024, 5, 1), "Vacuna rabia", tuple[time(15, 0, 0), time(16, 0, 0)]
    )

    animal.add_vet_appointment(vet_appointment)

    assert len(animal.vet_appointments) == 1
    assert animal.vet_appointments[0] == vet_appointment


def test_remove_vet_appointment(animal: Animal):
    new_vet_appointment = VetAppointment(
        date(2024, 5, 1), "Vacuna rabia", tuple[time(15, 0, 0), time(16, 0, 0)]
    )

    animal.add_vet_appointment(new_vet_appointment)
    animal.remove_vet_appointment(new_vet_appointment)

    assert len(animal.vet_appointments) == 0
