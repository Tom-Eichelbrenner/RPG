from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Entities.Enemy import Enemy


class EnemyFactory(EntityFactory):
    @staticmethod
    def create(name, level, hp, attack_power):
<<<<<<< HEAD
        if not name or not level or not hp or not attack_power:
            raise ValueError("All arguments are required to create an Enemy")
        if not isinstance(level, int) or not isinstance(hp, int) or not isinstance(attack_power, int):
            raise ValueError("Level, hp and attack_power must be integers.")
        return Ennemy(name, level, hp, attack_power)
=======
        return Enemy(name, level, hp, attack_power)
>>>>>>> 3f429cc590eaa7b2dea43a2292fef31b719b93db
