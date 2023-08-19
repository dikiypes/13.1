"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item

item = Item("Смартфон", 10000, 20)
def test_init():
    assert item.get_name() == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20
    assert item.calculate_total_price() == 200000
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000




