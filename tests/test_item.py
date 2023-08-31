"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture()
def test_item():
    return Item(name="суперсмартфон", price=5000, quantity=20)

def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 100000

def test_apply_discount(test_item):
    test_item.pay_rate = 2
    test_item.apply_discount()
    assert test_item.price == 10000

def test_name(test_item):
    assert test_item.name == "суперсмарт"

def test_string_to_number(test_item):
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('7.0') == 7
    assert Item.string_to_number('5.5') == 5

def test_repr(test_item):
    assert repr(test_item) == "Item('суперсмарт', 5000, 20)"

def test_str(test_item):
    assert str(test_item) == 'суперсмарт'
