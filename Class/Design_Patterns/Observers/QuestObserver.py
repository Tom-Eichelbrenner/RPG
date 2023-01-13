from Class.Design_Patterns.Observers import Observer
class QuestObserver(Observer):
    def __init__(self):
        super().__init__()
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def remove_quest(self, quest):
        self.quests.remove(quest)

    def get_quests(self):
        return self.quests

    def update_quests(self, entity):
        for quest in self.quests:
            quest.update(entity)