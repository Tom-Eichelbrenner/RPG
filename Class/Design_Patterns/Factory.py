from RPG.Class.Entities.Enemy import Enemy
from RPG.Class.Entities.Item import Item
from RPG.Class.Entities.NPC import NPC
from RPG.Class.Entities.Player import Player


class Factory:
    def __init__(self):
        pass

    @staticmethod
    def create_entity(entity_type, name, level, hp, attack_power, dialog):
        if entity_type == "player":
            return Player(name, level, hp)
        elif entity_type == "npc":
            return NPC(name, level, hp, dialog)
        elif entity_type == "enemy":
            return Enemy(name, level, hp, attack_power)
        elif entity_type == "item":
            return Item(name, value, use_function)
