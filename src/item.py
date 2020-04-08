class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return self.name.lower()
