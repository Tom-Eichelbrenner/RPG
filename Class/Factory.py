class Factory:
    def __init__(self):
        pass

    def create_player(self):
        player = Player("Player1")
        player.level = 1
        player.hp = 100
        return player

    def create_npc(self, name, level, hp, dialog):
        npc = NPC(name)
        npc.level = level
        npc.hp = hp
        npc.dialog = dialog
        return npc

    def create_enemy(self, name, level, hp, attack_power):
        enemy = Enemy(name)
        enemy.level = level
        enemy.hp = hp
        enemy.attack_power = attack_power
        return enemy

    def create_item(self, name, value, use_function=None):
        item = Item(name)
        item.value = value
        item.use_function = use_function
        return item
