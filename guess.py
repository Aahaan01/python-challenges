import random

number=random.randint(1,100)

def intro():
    print("Let's play a number guessing game!")
    print("I am thinking of a number between 1 to 100")
    if number%2==0:
        print("The number is even")
    else:
        print("The number is odd")
    print("Guess the number.")
    
def pick():
    chances=0
    while chances<6:
        try:
            guess=int(input("Enter a number"))
            if guess<=100 and guess>=1:
                chances=chances+1
                if chances<6:
                    if guess<number:
                        print("The number is too less")
                    if guess>number:
                        print("The number is too high")
                    if guess!=number:
                        print("Try again")
                    if guess==number:
                        print("You won")
                        break
        except:
            print("Please check Your number")

playing="yes"

while playing=="yes":
    intro()
    pick()
    playing=input("Do you waqnt to play again?")