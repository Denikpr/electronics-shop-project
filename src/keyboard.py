from src.item import Item

class Keyboard(Item):
    def __init__(self, name, price, quantity, language):
        super().__init__(name, price, quantity)
        self.__language = 'EN'
        self.language = language
