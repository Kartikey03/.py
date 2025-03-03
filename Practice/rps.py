import random

def game():
    player = input("Rock, Paper and Scissors:").lower()
    choices = ["rock","paper","scissors"]
    computer = random.choice(choices)

    if player == computer :
        print("Computer:", computer)
        print("Player:",player)
        print("Tie!")

    elif player == "Rock".lower() :
        if computer == "Paper".lower():
            print("Computer:", computer)
            print("Player:",player)
            print("You Win!")

    if computer == "Scissors".lower():
        print("Computer:", computer)
        print("Player:",player)
        print("You Lose!")

    elif player == "Scissors".lower() :
        if computer == "Paper".lower():
            print("Computer:", computer)
            print("Player:",player)
            print("You Win!")

        if computer == "Rock".lower():
            print("Computer:", computer)
            print("Player:",player)
            print("You Lose!") 

    elif player == "Paper".lower() :
        if computer == "Scissors".lower():
            print("Computer:", computer)
            print("Player:",player)
            print("You Win!")

        if computer == "Rock".lower():
            print("Computer:", computer)
            print("Player:",player)
            print("You Lose!")

    ask=input("You want to play ahead?")
    if ask == "yes".lower():
        game()
    else:
        print("GAMS MARAO")
game()