from room import Room
from player import Player
from item import Item

# Declare all the items and rooms

items = {
    "pencil" : Item("pencil", "to write things down."),
    "rock" : Item("rock", "just a rock"),
    "paper" : Item("paper", "could be written on"),
    "scissors" : Item("scissors", "can cut something")
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

room['outside'].add_item('pencil')
room['foyer'].add_item('paper')
room['trail'].add_item('rock')
room['overlook'].add_item('scissors')

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
player = Player(room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    print(f"""
    {player.current_room.name}, {player.current_room.description}

    There are {player.current_room.items or "no items"} in this room.
    -----------------------------------------------------------
    | "n" fo North, "e" for East, "s" for South, "w" for West | 
    | "i" for Inventory, or "q" to quit                       |
    -----------------------------------------------------------""")
    travel_to = input("\nWhat Next?")
    player_input = travel_to.lower().split(" ")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if len(player_input) == 1:
        if travel_to == 'n' or travel_to == 'e' or travel_to == 's' or travel_to == 'w' or travel_to == 'q' or travel_to == "i":
            if travel_to == "n" and player.current_room.n_to:
                player.current_room = player.current_room.n_to
            elif travel_to == "e" and player.current_room.e_to:
                player.current_room = player.current_room.e_to
            elif travel_to == "s" and player.current_room.s_to:
                player.current_room = player.current_room.s_to
            elif travel_to == "w" and player.current_room.w_to:
                player.current_room = player.current_room.w_to
            elif travel_to == "q":
                print("You Left the Game")
                break
            elif travel_to == "i":
                print("Inventory", player.show_items(player.items) or "is empty")
            else:
                print("Not an available direction.")
        else:
            print("Enter a cardinal direction.")
    elif len(player_input) == 2:
        if player_input[0] == "take":
            if player_input[1] not in player.current_room.items:
                print("That is not in this room.")
            else:
                print("You have picked up the", player_input[1])
                player.current_room.remove_item(player_input[1])
                player.add_item(player_input[1])
        elif player_input[0] == "drop":
            if player_input[1] not in player.items:
                print("You don't have", player_input[1])
            else:
                print("You have dropped the", player_input[1])
                player.current_room.add_item(player_input[1])
                player.remove_item(player_input[1])
        else:
            print("Not an available action.")
    else:
        print("Not an option")