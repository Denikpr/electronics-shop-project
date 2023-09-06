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

def test_apply_discount(test_phone):
    test_phone.pay_rate = 2
    test_phone.apply_discount()
    assert test_phone.price == 250000

def test_repr(test_phone):
    assert repr(test_phone) == "Phone('Nokia', 125000, 5, 3)"