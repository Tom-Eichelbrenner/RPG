from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.NPC import NPC

class NPCFactory(EntityFactory):
    @staticmethod
    def create(name, level, hp, dialog):
        if not name or not level or not hp or not dialog:
            raise ValueError("All arguments are required.")
        if not isinstance(level, int) or not isinstance(hp, int):
            raise ValueError("Level and hp must be integers.")
        return NPC(name, level, hp, dialog)
