import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self):
        self.message = "Файл item.csv поврежден"


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """
        Вывод информации о классе Item.
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Информация о классе. Вывод значения поля self.name.
        """
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    @classmethod
    def instantiate_from_csv(cls, filename):
        cls.all.clear()
        file_path = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(file_path,  encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if not ('name' in row and 'price' in row and 'quantity' in row):
                        raise InstantiateCSVError
                    item = cls(row['name'], Item.string_to_number(row['price']), Item.string_to_number(row['quantity']))
        except InstantiateCSVError as ex:
            print(ex.message)
        except FileNotFoundError:
            print('Отсутствует файл')



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
        self.price *= self.pay_rate

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise TypeError("Складывать можно только объекты класса Item и его дочерние классы")
