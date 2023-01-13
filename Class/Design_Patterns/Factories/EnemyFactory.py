from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.Enemy import Enemy


class EnemyFactory(EntityFactory):
    @staticmethod
    def create(name, level, hp, attack_power):
        return Enemy(name, level, hp, attack_power)
