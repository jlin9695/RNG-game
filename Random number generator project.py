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