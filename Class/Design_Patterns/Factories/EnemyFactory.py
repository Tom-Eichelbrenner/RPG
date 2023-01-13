from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.Ennemy import Ennemy

class EnemyFactory(EntityFactory):
    @staticmethod
    def create(name, level, hp, attack_power):
        return Ennemy(name, level, hp, attack_power)
