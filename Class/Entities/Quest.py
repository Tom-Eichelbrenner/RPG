import Entity
from RPG.Class.Entities.EntityTypes import EntityTypes  # Enum imports are bugged ?


class Quest(Entity):
    def __init__(self, name, description, reward):
        super.__init__(name, EntityTypes.QUEST)
        self.description = description
        self.reward = reward
        self.is_completed = False

    def get_description(self):
        return self.description

    def get_reward(self):
        return self.reward

    def is_completed(self):
        return self.is_completed
