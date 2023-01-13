from RPG.Class.Entities.Entity import Entity


class LivingEntity(Entity):
    def __init__(self, name: str, level: int, stats: list, is_alive: bool):
        super().__init__(name)
        self.level = level
        self.stats = stats
        self.is_alive = is_alive

    def get_level(self):
        return self.level

    def get_stats(self):
        return self.stats

    def get_stat(self, stat):
        if stat in self.stats:
            return self.stats[stat]
        else:
            return None

    def set_stats(self, stats):
        self.stats = stats

    def increase_level(self):
        self.level += 1
