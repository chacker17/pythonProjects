# This program simulates the rolling of a die. User is asked if they'd like to roll and a random number is
# generated between 1 and 6 as the value on the die.

# Written 6.20.2020 by CMH

import random

roll = input("Do you want to roll the die? 1 for yes, 0 to quit: ")

# Input validation, must be 0 or 1
while roll != '1' and roll != '0':
    roll = input("Do you want to roll the die? 1 for yes, 0 to quit: ")

    if roll == '1':
        break

# Roll the die if user selects
while roll == '1':
    dieVal = random.randint(1, 6)
    print("You rolled {}".format(dieVal))

    # Ask user if they want to roll again and validate input
    roll = input("Do you want to roll the die again? 1 for yes, 0 to quit: ")

    while roll != '1' and roll != '0':
        roll = input("Do you want to roll the die? 1 for yes, 0 to quit: ")

        if roll == '1':
            break

    if roll == '0':
        break

if roll == '0':
    print("Thank you for playing!")