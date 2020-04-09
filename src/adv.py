from room import Room
from player import Player
from item import Item

# Declare all the rooms

note = Item('note', 'A messily written note. Mostly illegible.')
press = Item('Press', 'A large press with two doors and two drawers', True)
bed = Item('Bed', 'A single bed in the corner of the room', True)
basket = Item(
    'Basket', 'A clothes bin half filled with dirty clothes.')
laptop = Item('Laptop', 'A laptop with a "property of Tom" sticker on it.')

room = {
    'your_bedroom':  Room("Inside your bedroom",
                          "The north wall has a window, south of you a door leading out of your bedroom.", [press, bed]),

    'upstairs_hallway':    Room("Upstairs Hallway", "You are in a hallway, to the north a door, to your east another door, the hallway extends to the south.", [basket]),

    'landing': Room("Stairs Landing", """You are on the stairs landing. A hallway extends to the north, there are two doors: one to your south and one to your east.
        A staircase descends to your west.""", []),

    'toms_bedroom':   Room("Tom's bedroom", """You are in your housemates room. He slumbers in his bed.""", [laptop]),

    #     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    # chamber! Sadly, it has already been completely emptied by
    # earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['your_bedroom'].s_to = room['upstairs_hallway']
room['upstairs_hallway'].n_to = room['your_bedroom']
room['upstairs_hallway'].s_to = room['landing']
room['landing'].n_to = room['upstairs_hallway']
room['landing'].s_to = room['toms_bedroom']
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
Player = Player(room['your_bedroom'], [note])
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
    *** type 'help' for hints ***\n
    """)
user_input = ""
while user_input != 'q':
    print("============================================================")
    print(Player.loc)
    print(Player)
    user_input = input("\nwhat would you like to do?: ")
    actions = user_input.split()
    if len(actions) == 1:
        try:
            if actions[0] == 'help':
                print(
                    """============================================================\n
                    Type 'n', 's', 'e', or 'w' to move north, south, east, or west respectively.\n
                    Type 'get' followed by the item name to take add the item to your inventory\n """)
            elif actions[0] == 's':
                Player.move_player(Player.loc.s_to)
                print(
                    "============================================================\nYou go south")
            elif actions[0] == 'w':
                Player.move_player(Player.loc.w_to)
                print(
                    "============================================================\nYou go west")
            elif actions[0] == 'n':
                Player.move_player(Player.loc.n_to)
                print(
                    "============================================================\nYou go north")
            elif actions[0] == 'e':
                Player.move_player(Player.loc.e_to)
                print(
                    "============================================================\nYou go east")
        except:
            print(
                "============================================================\nUnable to do that")
    elif len(actions) > 1:
        item_is_there = False
        if actions[0] == 'get':
            for i in Player.loc.items:
                if actions[1] == i.__repr__() and i.too_heavy != True:
                    item_is_there = True
                    Player.take_item(i)
                    Player.loc.remove_item(i)
                    print(
                        f"============================================================\n {actions[1]} added to your inventory")
                    break
            if item_is_there == False:
                print(
                    f"============================================================\n Cannot get {actions[1]}")
        elif actions[0] == 'drop':
            item_is_there = False
            for i in Player.inventory:
                if actions[1] == i.__repr__():
                    Player.drop_item(i)
                    Player.loc.add_item(i)
                    item_is_there = True
                    print(
                        f"============================================================\n {actions[1]} removed from your inventory")
                    break
            if item_is_there == False:
                print(f"could not drop {actions[1]}")
        elif actions[0] == 'inspect':
            all_items = Player.inventory + Player.loc.items
            item_is_there = False
            for i in all_items:
                if actions[1] == i.__repr__():
                    print(
                        "============================================================")
                    print(i.inspect())
                    item_is_there = True
                    break
            if item_is_there == False:
                print(f"could not inspect {actions[1]}")
        else:
            print("failed")
