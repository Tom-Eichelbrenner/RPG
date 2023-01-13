import Entity
from EntityTypes import EntityTypes  # Enum imports are bugged ?


class LivingEntity(Entity):
    def __init__(self, name: str, level: int, hp: int, stats: list, is_alive: bool):
        super().__init__(name, EntityTypes.LIVING_ENTITY)
        self.level = level
        self.hp = hp
        self.stats = stats
        self.is_alive = (self.hp != 0)
        self.damage_taken = 0

    def get_level(self):
        return self.level

    def get_hp(self):
        return self.hp - self.damage_taken

    def get_stats(self):
        return self.stats

    def get_stat(self, stat):
        if stat in self.stats:
            return self.stats[stat]
        else:
            return None

    def set_damage_taken(self, damage_taken):
        self.damage_taken += damage_taken

    def set_stats(self, stats):
        self.stats = stats

    def increase_level(self):
        self.level += 1

    def has_been_killed(self):
        return self.is_alive is True
