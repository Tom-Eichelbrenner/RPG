from RPG.Class.LivingEntity import LivingEntity


class NPC(LivingEntity):
    def __init__(self, name, level, hp, dialogues):
        super().__init__(name, level, hp, True)
        self.dialogues = dialogues

    def get_dialogues(self):
        return self.dialogues

    def add_dialogues(self, dialogue):
        self.dialogues.append(dialogue)