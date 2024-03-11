
# russian roulette
import random
import os
play = ""
warn = False
while play != "N":
    barrel = [1,2,3,4,5,6]
    bullet = random.choice(barrel)
    user = ""
    barrel_position = random.choice(barrel)
    if barrel_position == bullet:
        barrel_position = random.choice(barrel)
        
    player1 = 1
    print("=====Russian Roulette=====")

    while not warn:
        understood = str(input("Do you know how russian roulette work? (Y/N): ")).upper()
        while understood not in ['Y','N']:
            understood = str(input("Invalid Input Eneter Y to know the game or N to continue: ")).upper()
        if understood != "Y":
            warn = True
            print("""
        Russian roullete is a do or die game, you have a revolver with 6 barrel. 1 bullet is randomly insert in barrel so you have to survive until someone died or you die.
        You can Enter SHOOT to shoot Yourslef if you think the bullet not in the barrel position or you could Enter Spin to spin and shoot you self if you think the bullet in the barrel position.
        please be warn! if you choose spin there is 1/6 chance you might die!
        thank you for playing and have fun!
         """)
            print("=============================")
        else:
            print("Goodluck player!")
            warn = True
            print("=============================")
    
    
    
    dead = False
    print("Player 1")
    while not dead:

        user = str(input("Enter Shoot or Spin: ")).upper()
        while user not in ['SHOOT','SPIN']:
            user = str(input("Invalid Input! Enter Shoot or Spin: ")).upper()
        if user == "SPIN":
            barrel_position = random.choice(barrel)
            if barrel_position == bullet:
                os.system('cls')
                print("You died!")
                dead = True
            else:
                print("You still Alive!")
                if player1 == 1:
                    print("Player 2")
                    player1 = 0
                else:
                    print("Player 1")
                    player1 = 1
        elif user == "SHOOT":
            if barrel_position == bullet:
                os.system('cls')
                print("You dead!")
                dead = True
            elif barrel_position == barrel[0]:
                print("You alive!")
                barrel_position = barrel[1]
            elif barrel_position == barrel[1]:
                print("You alive!")
                barrel_position = barrel[2]
            elif barrel_position == barrel[2]:
                print("You alive!")
                barrel_position = barrel[3]
            elif barrel_position == barrel[3]:
                print("You alive!")
                barrel_position = barrel[4]
            elif barrel_position == barrel[4]:
                print("You alive!")
                barrel_position = barrel[5]
            else:
                print("You alive!")
                barrel_position = barrel[0]
            if not dead:
                if player1 == 1:
                    print("Player 2")
                    player1 = 0
                else:
                    print("Player 1")
                    player1 = 1
        
    if player1 == 1:
        print("player 1 died!")
    else:
        print("player 2 diad!")

    play = str(input("Play Again? (Y/N): ")).upper()
    while play not in ['Y','N']:
        play = str(input("Invalid Input! Play Again?(Y/N): ")).upper()


print("Thank You for playing :D")




