from datetime import date, time

import pytest
from domain.animal.animal import Animal
from domain.animal.veterinary import VetAppointment


def test_create_vetappointment_with_start_time_greater_than_end_time(animal: Animal):
    with pytest.raises(ValueError):
        VetAppointment(
            date=date(2024, 1, 1), animal=animal, time_slot=(time(18, 00), time(17, 30))
        )


def test_set_start_time_greater_than_end_time(vet_appointment: VetAppointment):
    with pytest.raises(ValueError):
        vet_appointment.time_slot = (time(18, 00), time(17, 30))
