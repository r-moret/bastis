from datetime import date

import pytest
from domain.animal.treatment import Treatment


@pytest.fixture
def treatment():
    return Treatment(medication="Clorhexidina")


def test_create_treatment_with_end_date_earlier_than_start_date():
    with pytest.raises(ValueError):
        Treatment("Clorhexidina", start_date=date(2024, 1, 2), end_date=date(2024, 1, 1))


def test_create_treatment_with_end_date_and_no_start_date():
    with pytest.raises(ValueError):
        Treatment("Clorhexidina", end_date=date(2024, 1, 1))


def test_set_new_end_date_with_no_start_date(treatment: Treatment):
    with pytest.raises(ValueError):
        treatment.end_date = date(2024, 1, 1)


def test_remove_start_date_when_having_end_date():
    treatment = Treatment(
        medication="Clorhexidina",
        start_date=date(2024, 1, 2),
        end_date=date(2024, 1, 5),
    )
    with pytest.raises(ValueError):
        treatment.start_date = None


def test_create_treatment_with_negative_periodicity():
    with pytest.raises(ValueError):
        Treatment(medication="Clorhexidina", periodicity=-10)


def test_set_negative_periodicity(treatment: Treatment):
    with pytest.raises(ValueError):
        treatment.periodicity = -10
