from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
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
#
while True:
    print(f"{player.current_room.name},\n{player.current_room.description}")
    travel_to = input('(Press "n" fo North, "e" for East, "s" for South, "w" for West, "q" to quit)\nWhere to?')
    print("______________________________________________________________")
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if travel_to == 'n' or travel_to == 'e' or travel_to == 's' or travel_to == 'w' or travel_to == 'q':
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
        else:
            print("not an option")
    else:
        print("Enter one of the optional directions.\n")
