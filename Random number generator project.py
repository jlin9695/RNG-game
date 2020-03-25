"""
import random

def guessing_game(g):
    try:
        int(g)
    except ValueError:
        print("Warning! What you typed in was either not a number or contained things that were not numbers. Please make sure you are answering properly with numbers.")
        g = input("Please guess a number between 0 and 20: ")
        return guessing_game(g)
    g = int(g)
    if g == number:
        return "Congratulations! You guessed the number correctly!"
    elif g > number and g <= 20:
        return "Your guess was too high, please try again!"
    elif g < number and g <= 20:
        return "Your guess was too low, please try again!"
    else:
        return "The game cannot continue due to an invalid input or answer. Please make sure your guess is between 0 and 20."

number = random.randint(0,20)
guess = input("Please guess a number between 0 and 20: ")



print(guessing_game(guess))

while guess != number:
    try:
        guess = int(input("Please guess a number between 0 and 20: "))
        print(guessing_game(guess))
    except ValueError:
        print("Warning! What you typed in was either not a number or contained things that were not numbers. Please make sure you are answering properly with numbers.")
        guess = int(input("Please guess a number between 0 and 20: "))
        
This was the first try. The set of code below is the final draft.
"""
import random

#def randomfunction(g):
    #return int(g)
def num_check(g):
    try:
        return int(g)
    except ValueError:
        print("Value Error, please try again!")
        return input("Please enter a number this time, not a character or string of words: ")

def guessing_game(g):
    #try:
        #int(g)
    #except ValueError:
        #print("Warning! What you typed in was either not a number or contained things that were not numbers. Please make sure you are answering properly with numbers.")
        #g = input("Please guess a number between 0 and 20: ")
        #return guessing_game(g)
    #g = int(g)
    if g == number:
        print("Congratulations! You guessed the number correctly!")
        return g
    elif g > number and g <= 20:
        print("Your guess was too high, please try again!")
        return g
    elif g < number and g <= 20:
        print("Your guess was too low, please try again!")
        return g
    else:
        print("The game cannot continue due to an invalid input or answer. Please make sure your guess is between 0 and 20.")
        return g

number = random.randint(0,20)
guess = input("Please guess a number between 0 and 20: ")
#while True:
    #if x == "Value Error, please check again!":
        #print("This is not a number. Try typing in your answer as a number, not a character or string of words: ")
        #guess = input("Please guess a number between 0 and 20: ")
    #else:
        #pass
while type(guess) != int:
    guess = num_check(guess)
answer = guessing_game(guess)

while answer != number:
    try:
        print("Your guess was " + str(answer) + ".")
        guess = input("Please guess a number between 0 and 20: ")
        while type(guess) != int:
            guess = num_check(guess)
        answer = guessing_game(guess)
    except ValueError:
        print("Warning! What you typed in was either not a number or contained things that were not numbers. Please make sure you are answering properly with numbers.")
        guess = input("Please guess a number between 0 and 20: ")
        while type(guess) != int:
            guess = num_check(guess)
        answer = guessing_game(guess)
#guess = guessing_game(guess)
#print(type(guess))
