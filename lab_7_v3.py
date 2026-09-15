
## Helper Functions ------------------------
def check_for_items():
    global current_room
    global inventory
    for item in inventory:
        if current_room == item[2]:
            item[1] = True
            print(f"You found a {item[0]}")

def check_win():
    global inventory
    return all(item[1] for item in inventory)
def change_room():
    global room_list
    global current_room
    global inventory
    direction = input("Which direction do you choose? n,e,s,w or choose i to see your inventory")
    if direction.lower() == "n":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
        print()  # change the current room to the current room's list position 1
    elif direction.lower() == "e":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    elif direction.lower() == "s":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    elif direction.lower() == "w":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You cannot go that way")
        else:
            current_room = next_room
    elif direction.lower() == "i":
        print("Your inventory is:")
        for item in inventory:
            if item[1]:
                print(item[0])

    else:
        print("Please choose again")


## Data Structures -------------------------
inventory = [
    ["book", False, 1],
    ["candle", False, 8],
    ["map", False, 9]
]
room_list = []
room = ["You enter the foyer of the apartment. There are rooms to the north, east, and west.",8,9, None,1]
room_list.append(room)
room = ["library",2,0,None, None]
room_list.append(room)
room = ["Dining Room",3,8,1,None]
room_list.append(room)
room = ["Kitchen",None,4,2,None]
room_list.append(room)
room = ["bedroom 1",5,6,8,3]
room_list.append(room)
room = ["Balcony ",None,None,4,None]
room_list.append(room)
room = ["bedroom 3",None,None,7,4]
room_list.append(room)
room = ["Bedroom2 ",6,None,9,8]
room_list.append(room)
room = ["Ballroom ",4,7,0,2]
room_list.append(room)
room = ["Washroom ",7,None,None,0]
room_list.append(room)
current_room = 0 #set the starting room.
# print(room_list[current_room][0])
# 2-dimensional array (a list of lists)


## Actual Game Loop ---------------------
done = False
while not done:
    print(room_list[current_room][0])
    print()
    check_for_items()
    print()
    if check_win():
        print("You win the game! You exit the spooky house")
        done = True
    else:
        change_room()



