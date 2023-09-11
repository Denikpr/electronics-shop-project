import pytest
from src.keyboard import Keyboard,Mixin


@pytest.fixture()
def test_kb():
    return Keyboard("Dark keyboard", 500, 5)

def test_name(test_kb):
    assert test_kb.name == "Dark keyboard"


def test_calculate_total_price(test_kb):
    assert test_kb.calculate_total_price() == 2500

def test_apply_discount(test_kb):
    test_kb.pay_rate = 2
    test_kb.apply_discount()
    assert test_kb.price == 1000
