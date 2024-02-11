from datetime import date

import pytest
from domain.animal.animal import Animal
from domain.animal.treatment import Treatment
from domain.animal.veterinary import VetAppointment


@pytest.fixture
def animal():
    return Animal("Obi", date(2018, 2, 8), date(2019, 5, 1), "Lovely", "Not so furry")


@pytest.fixture
def treatment(animal: Animal):
    return Treatment("Clorhexidina", animal, "Cuello")


@pytest.fixture
def vet_appointment(animal: Animal):
    return VetAppointment(date(2024, 1, 8), animal)
