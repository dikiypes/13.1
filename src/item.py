class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.get_name()}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.get_name()

    def get_name(self):
        return self._name

    def set_name(self, name):
        if len(name) < 10:
            self._name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    def instantiate_from_csv():
        with open("../src/items.csv", 'r', encoding='cp1251') as file:
            file = file.readlines()
            for line in file[1:]:
                line = line.strip().split(',')
                name = line[0]
                price = float(line[1])
                quantity = int(line[2])
                Item(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        return int(float(string))
