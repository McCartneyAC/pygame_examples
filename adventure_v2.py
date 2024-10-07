# A text-based aventure game using functions rather than iterating over lists:

print("you are in a big, spooky Haunted House")

#######################################################################
def entrance(): # define a subroutine then end with (): 
    choice = input("Which floor do you choose? 1, 2, 3, or basement?  ")
    if choice == "1":
        first_floor()
    elif choice == "2": 
        second_floor()
    elif choice == "3":
        third_floor()
    elif choice.lower() == "basement":
        basement()
    elif choice.lower() == "q":
        print("quit")
    else:
        print("that is not a choice")
        entrance() #recursion
 #######################################################################       
def first_floor():
    print("There is a long hallway.")
    choice = input("which room do you choose? A, B, or C?")
    if choice.lower() == "a":
        print("A scary ghost frightened you to death. Game over")
    elif choice.lower() == "b":
        print("You read from a Witch's Spellbook.")
        print("You feel more powerful")
        entrance() 
    elif choice.lower() == "c":
        print("You walk into a room, but there is a hole in the floor. You fall into the basement.")
        basement()
##########################################################################        
def basement():
    print("You find yourself in the basement.")
    print("It smells of mildew")
    choice = input("Do you choose to (A) walk upstairs or (B) look around?")
    if choice.lower() == "a":
        entrance()
    elif choice.lower() == "b":
        choice = input("You look around. You find that the basement is full of canned and pickled vegetables, sausages drying, and cheese being aged. Do you (a) eat the food or (b) go back upstairs?")
        if choice.lower() == "a":
            print("You eat the food. It's pretty delicious")
            basement()
        if choice.lower() == "b":
            entrance()
##########################################################################
def second_floor():
    print("You arrive on the second floor")
    choice = input("Do you choose the door on the left or the door on the right?")
    if choice == "left":
        potions()
    elif choice == "right":
        print()
    else: 
        print("You go back to the main floor")
        entrance()
'''
def potions(): 
    print("You find yourself in a room full of bubbling potions. You decide to drink one of them. You see potions that are red, green, yellow, and blue.")
    choice = input("Which color potion do you drink?")
    if choice.lower() == "red":
        print("Huh. That wasn't a potion. That was raspberry compte")
    elif choice.lower() == "green":
    elif choice.lower() == "yellow":
    elif choice.lower() == "blue":
    else: 
        print("You didn't drink a potion.")
        second_floor()
'''    
def third_floor():
    print("This floor is under construction. You go back downstairs")
    second_floor()
    


entrance() # starts the game
        
        
        
        
        
        
        
    
