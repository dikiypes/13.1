class LanguageMixin:
    def __init__(self, language='EN', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = language

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self

    def __str__(self):
        return self.language


class Keyboard(LanguageMixin):
    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN'):
        super().__init__(language=language)  # Вызываем конструктор миксина
        self._name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"Keyboard('{self.get_name()}', {self.price}, {self.quantity}, '{self.language}')"

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self._name

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    def instantiate_from_csv():
        with open("../src/items.csv", 'r', encoding='cp1251') as file:
            file = file.readlines()
            for line in file[1:]:
                line = line.strip().split(',')
                name = line[0]
                price = float(line[1])
                quantity = int(line[2])
                Keyboard(name, price, quantity)

    def __setattr__(self, name, value):
        if name == "language" and value not in ['EN', 'RU']:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        super().__setattr__(name, value)

    @staticmethod
    def string_to_number(string):
        return int(float(string))

