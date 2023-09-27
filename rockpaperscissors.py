import random
start = input("Would you like to play a game?\n")
while start.lower() == "yes":
    user = input("Select one:\n   rock, paper, scissors\n").lower()
    my_list = ["rock", "paper", "scissors"]
    random_index = random.randrange(3)
    computer = my_list[random_index]
    winner = "no one"
    if user == computer: 
        winner = "tied"
    elif user == "rock" and computer == "scissors":
        winner = "user"
    elif user == "rock" and computer == "paper":
        winner = "computer"
    elif user == "scissors" and computer == "rock":
        winner = "computer"
    elif user == "scissors" and computer == "paper":
        winner = "user"
    elif user == "paper" and computer == "rock":
        winner = "user"
    elif user == "paper" and computer == "scissors":
        winner = "computer"
    else:
        print("I'm sorry I didn't catch that")
    # TODO: if logic, for if they don't type paper,scissor, or rock
    print("the computer chose", computer)
    if winner == "computer": 
        print("You Lose! Better luck next time")
    elif winner == "user": 
        print("Congratulations! You Win!")
    elif winner == "tied":
        print("Tied game :(")
    game = input("do you want to play again?\n")
    if game.lower() == "no":
        start = "no"


# TW's Version (with chatGPT)

import random
def play_game(): 
    user = input("Select one:\n   rock, paper, scissors\n").lower()
    my_list = ["rock", "paper", "scissors"]
    computer = random.choice(my_list)

    if user in my_list:
        winner_dict = {
            # mccartney note: probably a dictionary is too much here and a simple list-of-lists would have sufficed. 
            ("rock", "scissors"): "user",
            ("scissors", "paper"): "user",
            ("paper", "rock"): "user",
        }

        if user == computer:
            print("It's a tie!")
        elif (user, computer) in winner_dict:
            print("Congratulations! You win!")
        else:
            print("You Lose! Better luck next time")
    else:
        print("Invalid input. Please select from 'rock', 'paper', or 'scissors'.")

    print("The computer chose", computer)

start = input("Would you like to play a game? (yes/no)\n")
while start.lower() == "yes":
    play_game()
    start = input("Do you want to play again? (yes/no)\n")
