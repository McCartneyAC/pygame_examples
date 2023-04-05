room_list = []

# room 0
room = [
  "You are in A Dark Entry Hall. You have doors to the North, East, and West.",
  4,  #n
  7,  #e
  None,  #s
  2] #w  
room_list.append(room)
# room 1
room = [
  "You are on the Stairs. You can go up the stairs, but the door is locked.",
  None,  #n
  None,  #e
  None,  #s
  None
]  #w
room_list.append(room)
# room 2
room = [
  "You are in a Library. There are bookshelves everywhere. I wonder what they contain. You can go north or travel back to the Entry Hall (east)",
  3,  #n
  0,  #e
  None,  #s
  None
]  #w
room_list.append(room)
# room 3
room = [
  "You are in a Dining Room. Dinner is set but no one is there to eat it. You can travel East or South.",
  None,  #n
  4,  #e
  2,  #s
  None
]  #w
room_list.append(room)
# room 4

kitchen_text = "You are in the Kitchen. It's messy. You can travel West, South, or East." 
room = [
  kitchen_text,
  None,  #n
  5,  #e
  0,  #s
  3
]  #w
room_list.append(room)
# room 5
room = [
  "You are on the back porch. It's raining. Gross. You can go south or west. ",
  None,  #n
  None,  #e
  6,  #s
  4
]  #w
room_list.append(room)
# room 6
room = [
  "You are in the Den. The TV is on, but it's not a show you recognize. You can go north or south.",
  5,  #n
  None,  #e
  7,  #s
  None
]  #w
room_list.append(room)
# room 7
room = [
  "You are in the Living room. Nothing in here is alive, not even the plants. You can go North or West.",
  6,  #n
  None,  #e
  None,  #s
  0
]  #w
room_list.append(room)

item_list = []

item = [
  "book", "You read a mysterious book written in an ancient language.", 2
]
item_list.append(item)

current_items = []
current_room = 0
next_room = 0
ghosts_happiness = 0


done = False
print("You are wandering alone in the late afternoon. It's a beautiful autumn day and you let your feet carry you farther than you would normally go. You arive at an old Queen Anne style house and decide you'd like to take some photos of the house for your portfolio. \nYou go to the front door to knock, but notice that it's slightly open. You go inside.")
print("To leave the house, just type 'quit'. You can move around the house by typing directions. Some objects can be interacted with. ")
while done == False:
  print()
  print(room_list[current_room][0])
  do = input("What do you wish to do?\n")
  if do.lower() == "q" or do.lower() == "quit":
    print("you leave the house")
    done = True
  elif do.lower() == "n" or do.lower() == "north":
    next_room = room_list[current_room][1]
  elif do.lower() == "e" or do.lower() == "east":
    next_room = room_list[current_room][2]
  elif do.lower() == "s" or do.lower() == "south":
    next_room = room_list[current_room][3]
  elif do.lower() == "w" or do.lower() == "west":
    next_room = room_list[current_room][4]
  elif do.lower() == "read book":
    if current_room == 2:
      print(item_list[0][1])
      current_items.append(item[0])
      ghosts_happiness += 1
    else:
      print("there aren't any books in here")
  elif do.lower() == "clean kitchen":
    if current_room == 4:
      print(
        "you clean the kitchen. it feels much better in here. You hear a ghostly noise. ")
      kitchen = "clean"
      kitchen_text = "you are in the kitchen again."
      ghosts_happiness += 1
    else:
      print("You aren't in the kitchen.")
  elif do.lower() == "eat dinner":
    if current_room == 3 and kitchen == "clean":
      print("You enjoy a delightful meal and feel refreshed. ")
    elif current_room == 3 and kitchen == "messy":
      print(
        "you feel slightly sick. There are angry, ghostly noises coming from the attic."
      )
      ghosts_happiness -= 1
    else:
      print("There isn't anything to eat in this room")
  elif do.lower == "turn off tv": 
    if current_room == 6:
      print("you hear a ghostly noise")
      ghosts_happiness += 1
    else: 
      print("there is no TV here")

  elif do.lower == "watch tv":
    if current_room == 6: 
      print("you are mesmerized by the show. You zone out. You start to fall asleep.")
      done = True
    else: 
      print("there is no TV in this room.")
  else:
    print("I don't understand that command.")

  if not done and next_room == None:
    print("you can't go that way")
  elif not done:
    current_room = next_room
