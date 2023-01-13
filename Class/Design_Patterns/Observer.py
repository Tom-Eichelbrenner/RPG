class Observer:
    def __init__(self):
        self.quests = []
        self.subscribers = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def remove_quest(self, quest):
        self.quests.remove(quest)

    def get_quests(self):
        return self.quests

    def update_quests(self, entity):
        for quest in self.quests:
            quest.update(entity)

    def subscribe(self, entity):
        self.subscribers.append(entity)

    def unsubscribe(self, entity):
        self.subscribers.remove(entity)

    def notify(self, event):
        for subscriber in self.subscribers:
            subscriber.on_notify(event)