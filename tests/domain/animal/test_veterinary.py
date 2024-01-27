from datetime import date, time

import pytest
from domain.animal.veterinary import VetAppointment


def test_create_vetappointment_with_start_time_greater_than_end_time():
    with pytest.raises(ValueError):
        VetAppointment(date=date(2024, 1, 1), time_slot=(time(18, 00), time(17, 30)))


def test_set_start_time_greater_than_end_time():
    appointment = VetAppointment(date=date(2024, 1, 1), time_slot=(time(17, 00), time(18, 00)))

    with pytest.raises(ValueError):
        appointment.time_slot = (time(18, 00), time(17, 30))
