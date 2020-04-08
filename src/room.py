# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, desc, items):
        self.name = name
        self.desc = desc
        self.items = items

    def __str__(self):
        return f"\nYou are here -> {self.name}\n\n   {self.desc}"
