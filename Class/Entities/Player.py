import LivingEntity


class Player(LivingEntity):
    def __init__(self, name: str, level: int, hp: int, is_alive: bool):
        super().__init__(name, level, hp, is_alive)
        self.xp = 0
        self.inventory = []

    def get_xp(self):
        return self.xp

    def increase_xp(self, xp):
        self.xp += xp

        if self.xp == 100:
            self.increase_level()

    def get_inventory(self):
        return self.inventory

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def on_notify(self, event):
        if event == "quest_completed":
            print(f"Player {self.name} has completed a quest.")
