"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture()
def test_item():
    return Item(name="tv", price=5000, quantity=20)

def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 100000

def test_apply_discount(test_item):
    test_item.pay_rate = 2
    test_item.apply_discount()
    assert test_item.price == 10000