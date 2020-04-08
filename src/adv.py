from room import Room
from player import Player
from item import Item

# Declare all the rooms

press = Item('Press', 'A large press with two doors and two drawers'),
bed = Item('Bed', 'A single bed in the corner of the room')
clothes_bin = Item(
    'Clothes Bin', 'A clothes bin half filled with dirty clothes sits tight to the wall')

room = {
    'your_bedroom':  Room("Inside your bedroom",
                          "The north wall has a window, south of you a door leading out of your bedroom", [press, bed]),

    'upstairs_hallway':    Room("Upstairs Hallway", "You are in a hallway, to the north a door, to your east another door, the hallway extends to the south", [clothes_bin])

    #     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    # into the darkness. Ahead to the north, a light flickers in
    # the distance, but there is no way across the chasm."""),

    #     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    # to north. The smell of gold permeates the air."""),

    #     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    # chamber! Sadly, it has already been completely emptied by
    # earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['your_bedroom'].s_to = room['upstairs_hallway']
room['upstairs_hallway'].n_to = room['your_bedroom']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
Tom = Player(room['your_bedroom'], ['ball', 'spud'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print("============================================================")
print("""
    \n
    You wake up in your bed and reach for your phone to check the latest updates on Slack.\n
    You discover your phone isn't where you left it.\n
    OBJECTIVE: FIND YOUR PHONE\n
    """)
user_input = ""
while user_input != 'q':
    print("============================================================")
    print(Tom.loc)
    print(Tom)
    user_input = input("\nwhat would you like to do?: ")
    actions = user_input.split()
    if len(actions) == 1:
        if user_input == 's':
            Tom.move_player(Tom.loc.s_to)
        else:
            print("Not a valid input!")
    else:
        print("more than one")
