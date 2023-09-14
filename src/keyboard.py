from src.item import Item


class Mixin:
    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Mixin, Item):
    def __init__(self, name, price, quantity):
        Mixin.__init__(self)
        Item.__init__(self, name, price, quantity)