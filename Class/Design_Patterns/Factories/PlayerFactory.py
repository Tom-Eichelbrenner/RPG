from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.Player import Player


class PlayerFactory(EntityFactory):
    @staticmethod
    def create(name, level=1, hp=100):
        if not name:
            raise ValueError("A name is required.")

        return Player(name, level, hp)

