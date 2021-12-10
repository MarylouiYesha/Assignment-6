import random
import sys
def main_game():
    rnumber = []
    ynumber = []

    print("Welcome to lottery game!")
    a =int(input("Please input your number: "))
    if 0<= a <=9:
        one_random_num = random.randrange(0, 9)
        rnumber.append(one_random_num)
        ynumber.append(a)
    else:
        print("error!")
    
    b = int(input("Please input your number: "))
    if 0<= b <= 9:
        two_random_num=random.randrange(0,9)
        rnumber.append(two_random_num)
        ynumber.append(b)
    else:
        print("error!")
    
    c = int(input("Please enter you number: "))
    if 0<= c <= 9:
        three_random_num=random.randrange(0,9)
        rnumber.append(three_random_num)
        ynumber.append(c)        
    else:
        print ("error!")
    

    print("Winning Numbers", sorted(rnumber))


    if sorted(ynumber) == sorted(rnumber):
        print("Winner")
    else:
        print ("You loss")

    s_game=input ("Try again y/n ('y' if yes and 'n' if no): ")
    if s_game == "Y" or "y":
        main_game()
    else:
        sys.exit()
   
main_game()
