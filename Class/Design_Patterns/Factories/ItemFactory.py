from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.Item import Item


class ItemFactory(EntityFactory):
    @staticmethod
    def create(name, value, use_function):
        if not name or not value or not use_function:
            raise ValueError("All arguments are required.")
        return Item(name, value, use_function)
