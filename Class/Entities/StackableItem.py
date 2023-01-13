import Item


class StackableItem(Item):
    def __init__(self, name, description, item_type, max_stack_size):
        super.__init__(name, description, item_type)
        self.max_stack_size = max_stack_size

    def get_max_stack_size(self):
        return self.max_stack_size
