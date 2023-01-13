import LivingEntity

class Player(LivingEntity):
    def __init__(self, name, level, hp):
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