class Entity:
    def __init__(self, name: str):
        self.name = name

    def get_type(self):
        pass

    def get_name(self):
        return self.name

    def on_notify(self, event):
        pass
