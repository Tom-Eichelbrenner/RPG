class Decorator:
    def __init__(self, entity):
        self.entity = entity
        self.abilities = []

    def add_ability(self, ability):
        if not hasattr(ability, "use"):
            raise ValueError("Ability must have a 'use' method")
        self.abilities.append(ability)

    def remove_ability(self, ability):
        self.abilities.remove(ability)

    def get_abilities(self):
        return self.abilities

    def use_abilities(self):
        for ability in self.abilities:
            ability.use()


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
