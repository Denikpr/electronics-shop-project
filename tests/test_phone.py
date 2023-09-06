import pytest
from src.phone import Phone
@pytest.fixture()
def test_phone():
    return Phone("Nokia", 125_000, 5, 3)

def test_name(test_phone):
    assert test_phone.name == "Nokia"

def test_number_of_sim(test_phone):
    assert test_phone.number_of_sim == 3

def test_calculate_total_price(test_phone):
    assert test_phone.calculate_total_price() == 625000

