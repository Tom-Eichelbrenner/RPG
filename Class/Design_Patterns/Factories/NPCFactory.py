from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.NPC import NPC


class NPCFactory(EntityFactory):
    @staticmethod
    def create(name, level, hp, dialog):
        return NPC(name, level, hp, dialog)
