# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.items = []

    def go_to(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
        else:
            print("Not an avaiable direction.")

    def show_items(self):
        if self.items:
            print(f'__Inventory__\n{", ".join([item.name + ": " + item.description for item in self.items])}')
        else:
            print(f'Inventory is empty.')

    #looped error print for not in room condition

    def on_take(self, the_item):
        if self.current_room.items:
            for item in self.current_room.items:
                if item.name != the_item:
                    continue
                if item.name == the_item:
                    self.items.append(item)
                    self.current_room.items.remove(item)
                    print(f'You have picked up the {item.name}')
                else:
                    print("This item is not in this room.")
        else:
            print("There is nothing in this room.")

    def on_drop(self, the_item):
        if self.items:
            for item in self.items:
                if item.name == the_item:
                    self.items.remove(item)
                    self.current_room.items.append(item)
                    print(f'You have dropped the {item.name}')
                else:
                    print("You do not have this item.")
        else:
            print("You do not have anything in your inventory.")

    ### ABILITIES ###
    def use_lightsource(self, the_item):
        # if lightsource equipped
        #    "room is lit up"
        pass

    ## EDT ##
    def attack(self, the_item):
        # if weapon equipped (mainhand)
        #    "swing <item>""
        pass

    def block(self, the_item):
        # if sheild equipped (offhand)
        pass