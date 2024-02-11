from datetime import date

import pytest
from domain.animal.animal import Animal
from domain.animal.treatment import Treatment


def test_create_treatment_with_end_date_earlier_than_start_date(animal: Animal):
    with pytest.raises(ValueError):
        Treatment("Clorhexidina", animal, start_date=date(2024, 1, 2), end_date=date(2024, 1, 1))


def test_create_treatment_with_end_date_and_no_start_date(animal: Animal):
    with pytest.raises(ValueError):
        Treatment("Clorhexidina", animal, end_date=date(2024, 1, 1))


def test_set_new_end_date_with_no_start_date(treatment: Treatment):
    with pytest.raises(ValueError):
        treatment.end_date = date(2024, 1, 1)


def test_remove_start_date_when_having_end_date(treatment):
    treatment.start_date = date(2024, 1, 2)
    treatment.end_date = date(2024, 1, 5)

    with pytest.raises(ValueError):
        treatment.start_date = None


def test_create_treatment_with_negative_periodicity(animal: Animal):
    with pytest.raises(ValueError):
        Treatment(medication="Clorhexidina", animal=animal, periodicity=-10)


def test_set_negative_periodicity(treatment: Treatment):
    with pytest.raises(ValueError):
        treatment.periodicity = -10
