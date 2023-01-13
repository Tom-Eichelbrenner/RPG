import Entity
import EntityTypes  # Enum imports are bugged ?


class Item(Entity):
    def __init__(self, name, description, item_type):
        super.__init__(name, EntityTypes.ITEM)
        self.description = description
        self.item_type = item_type

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_item_type(self):
        return self.item_type
