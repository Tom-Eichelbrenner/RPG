from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.Item import Item

class PlayerFactory(EntityFactory):
    @staticmethod
    def create(name, value, use_function):
        return Item(name, value, use_function)
