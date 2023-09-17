import csv
import os

FILENAME = '__items.csv'
PATH_ABSOLUTE = os.path.join(os.path.dirname(__file__), FILENAME)


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        self.price = price
        self.__name = name
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def calculate_total_price(self):
        '''
        Вычисляем стоймость товара в наличии.
        '''
        return self.price * self.quantity

    def apply_discount(self):
        '''
        Вычисляем цену товара со скидкой.
        '''
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name, language):
        self.__name = name[:10]
        self.__language = language

    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        try:
            with open(PATH_ABSOLUTE, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                  item = cls(row['name'], Item.string_to_number(row['price']), Item.string_to_number(row['quantity']))
        except FileNotFoundError:
            # Обработка ошибки, возникающей в том случае, если файл не найден
            print("_Отсутствует файл item.csv_")

    @staticmethod
    def string_to_number(number):
        return int(float(number))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity