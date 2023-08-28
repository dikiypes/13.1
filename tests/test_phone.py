from src.phone import Phone
from src.item import Item
import pytest
import os
def test_init():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.get_name() == "iPhone 14"
    assert phone.price == 120000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2

def test_calculate_total_price():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.calculate_total_price() == 120000 * 5

def test_apply_discount():
    phone = Phone("iPhone 14", 120000, 5, 2)
    phone.pay_rate = 0.9
    phone.apply_discount()
    assert phone.price == 120000 * 0.9

def test_string_to_number():
    assert Phone.string_to_number("10.5") == 10

def test_repr():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone) == "iPhone 14"

def test_add():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 80000, 3, 1)
    assert phone1 + phone2 == 5 + 3
    with pytest.raises(TypeError):
        phone1 + 10

def test_radd():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    phone2 = Phone("Samsung Galaxy", 80000, 3, 1)
    assert phone2 + phone1 == 3 + 5
    with pytest.raises(TypeError):
        10 + phone1

def test_set_name():
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    phone2 = Phone("iPhone 14 256", 120000, 5, 2)
    assert phone1._name == "iPhone 14"
    assert phone2._name == "iPhone 14 256"
def test_check_number_of_sim_positive():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.check_number_of_sim(3) == 3

def test_check_number_of_sim_negative():
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone = Phone("iPhone 14", 120000, 5, 0)





