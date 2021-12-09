#Program 1: Lottery
import random
import sys
#Create a program that ask 3 numbers (0-9) from the user.
def main_game():
    print("Welcome to lottery game!")
    a, b, c =input("Please input your 3 numbers (0-9) (ex: 0 5 7): ").split()

#Generate 3 random winning numbers (0-9)
    rnumber = []
    while len(rnumber) < 3:
        random_num = random.randrange(0, 9)
        rnumber.append(random_num)
    print("Winning numbers are:", rnumber)

#Display “Winner” if all 3 input numbers matched the generated numbers

    if (sorted(a and b and c)) == (sorted(rnumber)):
        print("Winner")
#Display ”You loss” if not
    else:
        print ("You loss")


def second_game():
#Display ”Try again y/n” after each game
    s_game=input ("Try again y/n ('y' if yes and 'n' if no:").lower()
#If the user enter “y” the user will play again
    if (s_game) == "y" or "Y":
        main_game()

#if “n” the program will exit
    else:
        sys.exit()
       
main_game()
second_game()