# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, loc, items):
        self.loc = loc
        self.inventory = items

    def __str__(self):
        return f"\n   You have these items: {self.inventory}"

    def move_player(self, new_loc):
        self.loc = new_loc

    def take_item(self, item):
        self.inventory.append(item)

    def drop_item(self, item):
        self.inventory.remove(item)
