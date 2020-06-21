# User plays a game of hangman. If the user chooses two players then the second player inputs a word, otherwise the
# word is randomly chosen from a pre-made list of words.

# Written 6.21.2020 by CMH

import random
from getpass import getpass

# Determine how many players there are
while True:
    numPlayers = input("How many players are there? (1 or 2): ")
    try:
        numPlayers = int(numPlayers)
    except ValueError:
        print("Please only input a number!")
        continue
    else:
        if numPlayers != 1 and numPlayers != 2:
            print("Please only enter 1 or 2")
        else:
            break

# Load in word list if there's only only player
if numPlayers == 1:
    wordsListRaw = open("words.txt", "r")
    wordsList = wordsListRaw.readlines()
    wordsListRaw.close()

maxWrong = 10
play = 1
while play == 1:  # Loop with whole game in it

    guessed = 0
    numWrong = 0
    numGuessed = 0
    lettersGuessed = ''

    if numPlayers == 1:
        word = random.choice(wordsList)  # Choose a random word
        userDisp = []
        for i in range(len(word) - 1):
            userDisp.append('-')
        wordLength = len(word)-1
    else:
        word = getpass("Please enter a word for your partner to guess: ")
        userDisp = []
        for i in range(len(word)):
            userDisp.append('-')
        wordLength = len(word)

    # Keep guessing letters until user guesses the word or gets too many wrong
    while guessed == 0:
        print(userDisp)

        # Get a single character guess from the user
        while True:
            letterGuess = input("Please guess a letter: ")
            if letterGuess.isalpha() and len(letterGuess) == 1:
                alreadyGuessed = lettersGuessed.find(letterGuess)
                if alreadyGuessed == -1:  # Haven't already guessed
                    break
                else:
                    print("You already guessed that letter! Try again!")
            else:
                print("Please enter a single a-z character only")

        lettersGuessed = lettersGuessed + letterGuess  # Store the character just guessed

        # Look for guessed character in the word
        currIdx = 0
        idx = []
        while currIdx < len(word):
            found = word.find(letterGuess, currIdx)
            if found != -1:
                idx.append(int(found))
                currIdx = found + 1
            else:
                break

        # Update user display accordingly
        if len(idx) >= 1:  # Letter is actually in the word
            for i in range(len(idx)):
                userDisp[idx[i]] = letterGuess
                numGuessed += 1
            print("You guessed right!")
        else:  # Incorrect guess
            numWrong += 1
            print("Letter is not in the word. You've made {} wrong guesses".format(numWrong))

        # User loses if they guess too many wrong
        if numWrong == maxWrong:
            print("You made too many bad guesses! The word was {}".format(word))

            while True:
                play = input("Would you like to play again? 1 for yes and 0 for no: ")
                try:
                    play = int(play)
                except ValueError:
                    print("Please only input a number!")
                    continue
                else:
                    if play != 0 and play != 1:
                        print("Please only enter 0 or 1")
                    else:
                        break

            break  # Break out of this game's loop to start a new one or to quit

        # User wins if they guess the word
        if numGuessed == wordLength:
            print("Congrats! You correctly guessed the word: {}".format(word))

            while True:
                play = input("Would you like to play again? 1 for yes and 0 for no: ")
                try:
                    play = int(play)
                except ValueError:
                    print("Please only input a number!")
                    continue
                else:
                    if play != 0 and play != 1:
                        print("Please only enter 0 or 1")
                    else:
                        break

            break  # Break out of this game's loop to start a new one or to quit
