import random
import os
hand = ['ROCK','PAPER','SCISSOR']
quit =""
bot = random.choice(hand)

while quit != "N":
    bot = random.choice(hand)
    user = str(input("Enter Rock/Paper/Scissor: ")).upper()
    while user not in ['ROCK','PAPER','SCISSOR']:
        user = str(input("Invalid input! Enter Rock/Paper/Scissor: ")).upper()

    if user == bot:
        print("It a draw!")
    elif bot == "ROCK":
        if user == "PAPER":
            print("You win!")
        elif user == "SCISSOR":
            print("HAHAHA YOU LOSE SUCKER!")
    elif bot == "SCISSOR":
        if user == "ROCK":
            print("You win!")
        elif user == "PAPER":
            print("HAHAHA YOU LOSE SUCKER!")
    else:
        if user == "SCISSOR":
            print("You win!")
        elif user == "ROCK":
            print("HAHAHA YOU LOSE SUCKER!")
    
    print("Bot chooses",bot)
    
    quit = str(input("Play again? (Y/N): ")).upper()
    os.system('cls')
    while quit not in ["Y","N"]:
        quit = str(input("Invalid input! Play again? (Y/N): ")).upper()
        os.system('cls')
 
