import csv
import os

FILENAME = 'items.csv'
PATH_ABSOLUTE = os.path.join(os.path.dirname(__file__), FILENAME)

class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        self.price = price
        self.__name = name[:10]
        self.quantity = quantity
        Item.all.append(self)

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
    def name(self, name):
        self.__name = name[:10]

