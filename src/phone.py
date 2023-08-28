from src.item import Item
class Phone:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self.number_of_sim = number_of_sim
        self.all.append(self)

    def __repr__(self):
        return f"Phone('{self.get_name()}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return self.get_name()

    def __add__(self, other):
        if isinstance(other, (Phone, Item)):
            return self.quantity + other.quantity
        else:
            raise TypeError("You can only add Phone or Item instances")

    def __radd__(self, other):
        return self.__add__(other)

    def __setattr__(self, name, value):
        if name == "number_of_sim" and value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        super().__setattr__(name, value)

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

    def instantiate_from_csv(file_name='../src/items.csv'):
        with open(file_name, 'r') as file:
            file = file.readlines()
            for line in file[1:]:
                print(line)
                line = line.strip().split(',')
                name = line[0]
                price = float(line[1])
                quantity = int(line[2])
                number_of_sim = int(line[3])
                Phone(name, price, quantity, number_of_sim)

    def check_number_of_sim(self, number_of_sim):
        if number_of_sim > 0:
            return number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")


    @staticmethod
    def string_to_number(string):
        return int(float(string))
