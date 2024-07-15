
# stone, paper ,scisors

import random

choices = [1,2,3]

while(1):
    player = int(input("Enter your choice: \n1 => STONE \n2 => PAPER \n3 => SCISORS\n0 => End Game\n"))

    computer = random.choice(choices)
    if player == 0:
        break
    if (player == 1 and computer == 1) or (player == 2 and computer == 2) or (player == 3 and computer == 3):
        print("\nTie\n")
    elif(player == 1 and computer == 2):
        print("Your Choice : STONE\nComputer Choice : PAPER")
        print("\nYOU LOSE\n")
    elif(player == 1 and computer == 3):
        print("Your Choice : STONE\nComputer Choice : Scisors")
        print("\nYOU WIN\n")
    elif(player == 2 and computer == 1):
        print("Your Choice : PAPER\nComputer Choice : STONE")
        print("\nYOU WIN\n")
    elif(player == 2 and computer == 3):
        print("Your Choice : PAPER\nComputer Choice : Scisors")
        print("\nYOU LOSE\n")
    elif(player == 3 and computer == 1):
        print("Your Choice : Scisors\nComputer Choice : STONE")
        print("\nYOU LOSE\n")
    elif(player == 3 and computer == 2):
        print("Your Choice : Scisors\nComputer Choice : PAPER")
        print("\nYOU WIN\n")


print("\nGame ENDS here")

