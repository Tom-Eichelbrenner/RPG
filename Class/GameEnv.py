from RPG.Class.Design_Patterns.Factories import EntityFactory
from RPG.Class.Design_Patterns.Observers import ItemObserver, LivingEntityObserver, QuestObserver
from RPG.Class.Design_Patterns.Singleton import Singleton
from RPG.Class.Entities import Item, LivingEntity, Quest


class GameEnv(metaclass=Singleton):
    def __init__(self):
        self.entities = []
        self.player = None
        self.factory = EntityFactory()
        self.item_observer = ItemObserver()
        self.living_entity_observer = LivingEntityObserver()
        self.quest_observer = QuestObserver()

    def add_entity(self, entity):
        self.entities.append(entity)
        if isinstance(entity, Item):
            self.item_observer.notify(entity)
        elif isinstance(entity, LivingEntity):
            self.living_entity_observer.notify(entity)
        elif isinstance(entity, Quest):
            self.quest_observer.notify(entity)

    def update_entity(self, entity):
        for i, e in enumerate(self.entities):
            if e.name == entity.name:
                self.entities[i] = entity
                if isinstance(entity, Item):
                    self.item_observer.notify(entity)
                elif isinstance(entity, LivingEntityObserver):
                    self.living_entity_observer.notify(entity)
                elif isinstance(entity, Quest):
                    self.quest_observer.notify(entity)
                break

    def delete_entity(self, entity_name):
        for i, e in enumerate(self.entities):
            if e.name == entity_name:
                del self.entities[i]
                if isinstance(e, Item):
                    self.item_observer.notify(e)
                elif isinstance(e, LivingEntityObserver):
                    self.living_entity_observer.notify(e)
                elif isinstance(e, Quest):
                    self.quest_observer.update_quests(e)
                break

    def get_environment(self):
        return {"entities": self.entities, "player": self.player}

    def run(self):
        self.player = self.factory.create("Player", "Ash")
        self.living_entity_observer.subscribe(self.player)
        while self.player.is_alive():
            # update environment and handle player actions
            pass
