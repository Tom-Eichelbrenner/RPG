class EntityFactory:
    def __init__(self):
        pass

    @staticmethod
    def create(entity_type, *args, **kwargs):
        if entity_type not in ["Enemy", "Item", "NPC", "Player"]:
            raise ValueError("Invalid entity type.")
        factory_class = eval(f"{entity_type}Factory")
        return factory_class.create(*args, **kwargs)
