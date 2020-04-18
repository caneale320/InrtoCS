# Caleb Neale, can4ku

print("Think of a number between 1 and 100 and I'll guess it.")
num_guesses = int(input("How many guesses do I get? "))
top_bound = 100
bottom_bound = 0
guess = 50
count = 0
higher_lower = 0
run_again = "yes"


def calc_guess(up_or_down):
    """
    calculates a guess based off of whether the parameter is "higher" or "lower"
    check for logical errors/lies from the user and determines if the following while loop should run again
    """
    global guess
    if up_or_down == "higher":
        global bottom_bound
        bottom_bound = guess
    elif up_or_down == "lower":
        global top_bound
        top_bound = guess

    guess = (((top_bound - bottom_bound)//2) + bottom_bound)
    global run_again
    if guess <= bottom_bound or guess >= top_bound:
        print("Wait; how can it be both higher than " + str(bottom_bound) + " and lower than " + str(top_bound) + "?")
        run_again = "no"


while (count < num_guesses and higher_lower != "same") and run_again == "yes":
    higher_lower = input("Is the number higher, lower, or the same as " + str(guess) + "? ")
    calc_guess(higher_lower)
    count += 1
else:
    if higher_lower == "same":
        print("I won!")
    else:
        if run_again == "yes":
            answer = int(input("I lost; what was the answer? "))
            if answer > int(top_bound):
                print("That can't be; you said it was lower than " + str(top_bound) + "!")
            elif answer < int(bottom_bound):
                print("That can't be; you said it was higher than " + str(bottom_bound) + "!")
            else:
                print("Well played!")


