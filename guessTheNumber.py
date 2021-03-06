# This program randomly generates a number and lets the user guess what the number is. Every time the user guesses the
# program tells them whether their guess was too high or too low until the user correctly guesses the number.

# Written 6.20.2020 by CMH

import random
import matplotlib.pyplot as plt

def checkNumber(userInput):
    err = 1

    while err == 1:
        try:
            val = int(userInput)
            return val
        except ValueError:
            err = 1
            print("That's not a number!")
            userInput = input("Please enter a number: ")

play = 1
while play == 1:
    maxVal = input("Welcome! What is the maximum value you would like the number to take?: ")
    maxVal = checkNumber(maxVal)

    val = random.randint(1, maxVal)

    allGuessed = []
    numGuesses = 1
    trialNums = [1]
    guess = input("Please enter your guess: ")
    guess = checkNumber(guess)
    allGuessed.append(guess)

    while guess != val:
        if guess > val:
            print("Your guess is too high!")
        elif guess < val:
            print("Your guess is too low!")

        guess = input("Please enter your guess: ")
        guess = checkNumber(guess)

        allGuessed.append(guess)
        numGuesses += 1
        trialNums.append(numGuesses)

        if guess == input:
            break

    print("Congrats! You guessed the number correctly!")

    plt.figure(figsize=[10, 6])
    plt.plot(trialNums, allGuessed, color='#0504aa')
    plt.xlim(0, numGuesses + 1)
    plt.xlabel('Guess Number', fontsize=15)
    plt.ylabel('Number Guessed', fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.title('Numbers guessed in this session', fontsize=15)
    plt.show()

    # See if the user wants to play again
    play = input("Would you like to play again? 1 for yes, 0 to quit: ")
    play = checkNumber(play)

    # Validate input
    while play != 1 and play != 0:
        play = input("Would you like to play again? 1 for yes, 0 to quit: ")
        play = checkNumber(play)

        if play == 1 or play == 0:
            break

    if play == 0:
        break

print("Thank you for playing!")

# Add graph of guesses
