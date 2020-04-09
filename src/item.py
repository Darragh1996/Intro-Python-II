class Item:
    def __init__(self, name, desc, too_heavy=False):
        self.name = name
        self.desc = desc
        self.too_heavy = too_heavy

    def __repr__(self):
        return self.name.lower()

    def inspect(self):
        return self.desc
