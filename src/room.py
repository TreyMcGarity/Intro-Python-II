# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description, n_to = None, e_to = None, s_to = None, w_to = None, items = None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.items = []

    def show_item(self, items):
        return self.items

    def add_item(self, item):
        return self.items.append(item)

    def remove_item(self, item):
        return self.items.remove(item)