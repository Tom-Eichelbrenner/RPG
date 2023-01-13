import Factory
from RPG.Class.Singleton import Singleton


class GameEnv(metaclass=Singleton):
    def __init__(self):
        self.entities = []
        self.player = None
        self.factory = Factory
        self.observer = Observer

    def add_entity(self, entity):
        self.entities.append(entity)
        self.observer.update_quests(entity)

    def update_entity(self, entity):
        for i, e in enumerate(self.entities):
            if e.name == entity.name:
                self.entities[i] = entity
                self.observer.update_quests(entity)
                break

    def delete_entity(self, entity_name):
        for i, e in enumerate(self.entities):
            if e.name == entity_name:
                del self.entities[i]
                self.observer.update_quests(e)
                break

    def get_environment(self):
        return {"entities": self.entities, "player": self.player}

    def run(self):
        self.player = self.factory.create_player()
        while self.player.is_alive():
            # update environment and handle player actions
            pass
