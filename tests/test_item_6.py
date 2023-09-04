from src.item_6 import Item, InstantiateCSVError
import pytest
import os

def test_init():
    item = Item("Смартфон", 10000, 20)
    assert item.get_name() == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20

def test_calculate_total_price():
    item = Item("Тестовый товар", 500, 10)
    assert item.calculate_total_price() == 5000

def test_apply_discount():
    item = Item("Тестовый товар", 100, 5)
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 90

def test_string_to_number():
    assert Item.string_to_number("10.5") == 10

def test_repr():
    item = Item("Тестовый товар", 100, 5)
    assert repr(item) == "Item('Тестовый товар', 100, 5)"

def test_str():
    item = Item("Тестовый товар", 100, 5)
    assert str(item) == "Тестовый товар"

def test_set_name():
    item = Item("Тестовый товар", 100, 5)
    item.set_name("Тест")
    assert item.get_name() == "Тест"

def test_instantiate_from_missing_csv():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('test.csv')

def test_instantiate_from_corrupted_csv():
    with open('test_items.csv', 'w') as file:
        file .write('name,price,quantity\n')
        file.write('Test, 5')

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('test_items.csv')

    os.remove('test_items.csv')






