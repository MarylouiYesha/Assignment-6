import random

guess= random.randint(0,10)

print("Welcome to 'Guess the number'!")
print("You should guess the random number I have to win!")

user_guess=int(input("Please input your guess:"))

while guess!=user_guess:
    if guess>user_guess:
        print("Your number is less than what I have")
        user_guess=int(input("Please input your guess:"))
    if guess<user_guess:
        print("Your number is greater than what I have")
        user_guess=int(input("Please inut your guess:"))
  

print ("Congrats you won the game!")

