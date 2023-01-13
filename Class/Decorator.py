class Decorator:
    def __init__(self, entity):
        self.entity = entity
        self.abilities = []

    def add_ability(self, ability):
        self.abilities.append(ability)

    def remove_ability(self, ability):
        self.abilities.remove(ability)

    def get_abilities(self):
        return self.abilities


class FireballAbility:
    def __init__(self, entity):
        self.entity= entity

    def use(self):
        print(f"{self.entity.get_name()} casted Fireball")


class HealAbility:
    def __init__(self, entity):
        self.entity = entity

    def use(self):
        print(f"{self.entity.get_name()} healed himself!")
