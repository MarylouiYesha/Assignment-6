import random
import sys
def main_game():
    rnumber = []
    ynumber = []

    one_random_num = random.randrange(0, 9)
    rnumber.append(one_random_num)

    two_random_num=random.randrange(0,9)
    rnumber.append(two_random_num)

    three_random_num=random.randrange(0,9)
    rnumber.append(three_random_num)

    print("Welcome to lottery game!")
    a =int(input("Please input your number: "))
    if 0<= a <=9:       
        ynumber.append(a)
    else:
        print("error!")
    
    b = int(input("Please input your number: "))
    if 0<= b <= 9:        
        ynumber.append(b)
    else:
        print("error!")
    
    c = int(input("Please enter you number: "))
    if 0<= c <= 9:        
        ynumber.append(c)        
    else:
        print ("error!")
    

    print("Winning Numbers", sorted(rnumber))


    if sorted(ynumber) == sorted(rnumber):
        print("Winner")
    else:
        print ("You loss")

    s_game=input ("Try again y/n ('Y' if yes and 'N' if no): ")
    if s_game == "Y":
        main_game()
    else:
        sys.exit()
   
main_game()
