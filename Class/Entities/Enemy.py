import NPC


class Enemy(NPC):
    def __init__(self, name: str, level: int, hp: int, attack_power: int, dialogues):
        super().__init__(name, level, hp, dialogues)
        self.attack_power = attack_power

    def get_attack_power(self):
        return self.attack_power
