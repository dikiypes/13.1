from src.keyboard import Keyboard
import pytest
def test_keyboard_creation():
    keyboard = Keyboard("Mechanical Keyboard", 100, 10)
    assert keyboard.get_name() == "Mechanical Keyboard"
    assert keyboard.price == 100
    assert keyboard.quantity == 10
    assert keyboard.language == "EN"

def test_change_language():
    keyboard = Keyboard("Mechanical Keyboard", 100, 10)
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang().change_lang()
    assert keyboard.language == "RU"
def test_repr():
    keyboard = Keyboard("Mechanical Keyboard", 100, 10)
    assert repr(keyboard) == "Keyboard('Mechanical Keyboard', 100, 10, 'EN')"

def test_str():
    keyboard = Keyboard("Mechanical Keyboard", 100, 10)
    assert str(keyboard) == "Mechanical Keyboard"
    assert str(keyboard.language) == 'EN'



def test_calculate_total_price():
    keyboard = Keyboard("Mechanical Keyboard", 100, 10)
    assert keyboard.calculate_total_price() == 1000


def test_invalid_language_assignment():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'