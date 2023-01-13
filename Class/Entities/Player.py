from Class.Entities import LivingEntity


class Player(LivingEntity):
    def __init__(self, name: str, level: int, hp: int):
        self.name = name
        self.level = level
        self.hp = hp
        self.xp = 0
        self.inventory = []

    def get_xp(self):
        return self.xp

    def get_inventory(self):
        return self.inventory

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def on_notify(self, event):
        if event == "quest_completed":
            print(f"Player {self.name} has completed a quest.")

    def has_been_killed(self):
        return self.hp == 0
