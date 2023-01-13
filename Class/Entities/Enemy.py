from Class.Entities.NPC import NPC


class Enemy(NPC):
    def __init__(self, name, level, hp, attack_power, dialogues):
        super().__init__(name, level, hp, dialogues)
        self.attack_power = attack_power

    def get_attack_power(self):
        return self.attack_power
