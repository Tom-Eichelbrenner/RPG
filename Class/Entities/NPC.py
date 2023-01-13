from RPG.Class.Entities.LivingEntity import LivingEntity


class NPC(LivingEntity):
    def __init__(self, name: str, level: int, hp: int, dialogues: list):
        super().__init__(name, level, hp, True)
        self.dialogues = dialogues

    def get_dialogues(self):
        return self.dialogues

    def add_dialogues(self, dialogue: str):
        self.dialogues.append(dialogue)
