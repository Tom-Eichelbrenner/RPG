class Entity:
    def __init__(self, name: str, entity_type: int):
        self.name = name
        self.type = entity_type

    def get_type(self):
        return self.type

    def get_name(self):
        return self.name

    def on_notify(self, event):
        pass
