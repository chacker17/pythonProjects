# This program simulates the rolling of a user-specific number of dice with a user-specified number of sides.
# Each die has an independently randomly produced number between 1 and the number of sides the user specifies they
# want on their dice. User can repeat as many times as they want. Once the user chooses to quit the program, produces
# a histogram of all of the rolls from that session.

# Written 6.20.2020 by CMH

import random
import numpy as np
import matplotlib.pyplot as plt


# User-defined functions
def validateinput(rollval, order):
    while rollval != 1 and rollval != 0:
        if order == 1:
            rollval = int(input("Do you want to roll the die? 1 for yes, 0 to quit: "))
        elif order == 2:
            rollval = int(input("Do you want to roll the die again? 1 for yes, 0 to quit: "))

        if rollval == 1 or rollval == 0:
            return rollval


numSides = int(input("How many sides do you want on your dice?: "))
numDice = int(input("How many dice would you like to roll?: "))
diceToRoll = np.linspace(1, numDice, numDice)
# print(diceToRoll)
roll = int(input("Do you want to roll the die? 1 for yes, 0 to quit: "))

# Input validation, must be 0 or 1
if roll != 1 and roll != 0:
    roll = validateinput(roll, 1)

# Roll the dice
allDieVals = []
while roll == 1:

    dieVal = []
    for i in diceToRoll:
        dieVal += [random.randint(1, numSides)]

    print(dieVal)
    allDieVals += dieVal  # Save all numbers rolled to make histogram at the end

    # Ask user if they want to roll again and validate input
    roll = int(input("Do you want to roll the die again? 1 for yes, 0 to quit: "))

    if roll != 1 and roll != 0:
        roll = validateinput(roll, 2)

    if roll == 0:
        break

print("Thank you for playing!")

# Show the user a histogram of all of their rolls
plt.figure(figsize=[10, 6])
plt.hist(allDieVals, color='#0504aa', bins=np.linspace(1, numSides+1, numSides+1), align='left', rwidth=0.8, density=True)
plt.xlim(0, numSides+1)
plt.xlabel('Die Value', fontsize=15)
plt.ylabel('Proportion', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.title('Frequency of each die value being rolled during this session', fontsize=15)
plt.show()
