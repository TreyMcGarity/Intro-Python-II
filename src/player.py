# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room, items = None):
        self.current_room = current_room
        self.items = []

    def show_items(self, items):
        return self.items

    def add_item(self, item):
        return self.items.append(item)

    def remove_item(self, item):
        return self.items.remove(item)