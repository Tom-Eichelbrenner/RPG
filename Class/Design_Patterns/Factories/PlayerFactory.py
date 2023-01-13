from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.Player import Player


class PlayerFactory(EntityFactory):
    @staticmethod
    def create(name, level, hp):
        return Player(name, level, hp)
