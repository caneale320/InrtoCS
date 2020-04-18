# Caleb Neale, can4ku

import random

answer = int(input("What should the answer be? "))
num_guesses = int(input("How many guesses? "))

if answer == -1:
    answer = random.randrange(1, 101)

count = 0
user_guess = ""


def guess():
    """
    asks user for a guess
    then adds to the counter after each guess
    then checks if there are any guesses left and checks guess against the answer to determine a response
    """
    global user_guess
    user_guess = int(input("Guess a number: "))
    global count
    count += 1
    if user_guess < answer and count < num_guesses:
        print("The number is higher than that.")
    elif user_guess > answer and count < num_guesses:
        print("The number is lower than that.")


def did_you_win():
    """checks if the user wins and prints the appropriate response"""
    if user_guess == answer:
        print("You win!")
    else:
        print("You lose; the answer was " + str(answer) + ".")


while count < num_guesses and user_guess != answer:
    guess()
else:
    did_you_win()
