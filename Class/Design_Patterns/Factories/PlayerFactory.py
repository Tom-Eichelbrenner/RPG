from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.Player import Player

class PlayerFactory(EntityFactory):
    @staticmethod
    def create(name, level, hp):
        if not name or not level or not hp:
            raise ValueError("All arguments are required.")
        if not isinstance(level, int) or not isinstance(hp, int):
            raise ValueError("Level and hp must be integers.")
        return Player(name, level, hp)

