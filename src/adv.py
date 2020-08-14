from room import Room
from player import Player
from item import Item

# Declare all the items and rooms

item = {
    "pencil" : Item("pencil", "to write with."),
    "paper" : Item("paper", "could be written on."),
    "rock" : Item("rock", "just a rock."),
    "scissors" : Item("scissors", "to cut with.")
}

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons."),

    'trail': Room("Forest trail", """A long, winding dirt trail through the thick forest 
    which leads north to the Cave Entrance and south to a bridge."""),

    'bridge': Room("Old bridge","""It's destroyed and there is no other way to cross
    the raging river south."""),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
}

# Put items in rooms

room["outside"].items.append(item['pencil'])
room["trail"].items.append(item['rock'])
room["foyer"].items.append(item['paper'])
room["overlook"].items.append(item['scissors'])

# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].s_to = room['trail']
room['trail'].s_to = room['bridge']
room['trail'].n_to = room['outside']
room['bridge'].n_to = room['trail']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    decision = input(f"""
    {player.current_room}
    -----------------------------------------------------------
    | "n" fo North, "e" for East, "s" for South, "w" for West | 
    | "i" for Inventory, or "q" to quit                       |
    -----------------------------------------------------------
    
Whats Next?""")
    split_decision = decision.split()
    
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if len(split_decision) == 1:
        decision = decision.lower()[0]
        if decision == "n" or decision == "e" or decision == "s" or decision == "w":
            player.go_to(decision)
        elif decision == "i":
            player.show_items()
        elif decision == "q":
            print('You left the game')
            break
        else:
            print(
                "Invalid key. Please type North, East, South, or West to move or q to quit the game.")
    elif len(split_decision) == 2:
        if split_decision[0] == "take":
            player.on_take(split_decision[1].lower())
        elif split_decision[0] == "drop":
            player.on_drop(split_decision[1].lower())
        else:
            print("Not an available action.")
    else:
        print("Not an option.")