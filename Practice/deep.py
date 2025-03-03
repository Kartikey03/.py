#Game of Rock, Paper and scissors

import random
while True:
    choices = ["Rock","Paper","Scissors"]
    computer = random.choice(choices)
    player = None
    
    while player in choices:
        player = input("Rock, Paper and Scissors: ").lower()

    if player == computer :
        print("Computer:", computer)
        print("Player:",player)
        print("Tie!")
    
    elif player == "Rock" :
        if computer == "Paper":
            print("Computer:", computer)
            print("Player:",player)
            print("You Win!")

        if computer == "Scissors":
            print("Computer:", computer)
            print("Player:",player)
            print("You Lose!")

    elif player == "Scissors" :
        if computer == "Paper":
            print("Computer:", computer)
            print("Player:",player)
            print("You Win!")

        if computer == "Rock":
            print("Computer:", computer)
            print("Player:",player)
            print("You Lose!") 

    elif player == "Paper" :
        if computer == "Scissors":
            print("Computer:", computer)
            print("Player:",player)
            print("You Win!")

        if computer == "Rock":
            print("Computer:", computer)
            print("Player:",player)
            print("You Lose!")       

    play_again = input("Press yes to play again or no ").lower()
    if play_again != "yes":
        break
print("Bye!!!")