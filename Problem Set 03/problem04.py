#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 18:52:16 2017

@author: dileep
"""
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_left = 8
    lettersGuessed = list()
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")
    while isWordGuessed(secretWord, lettersGuessed) == False and guesses_left != 0:
        print("You have " + str(guesses_left) + " guesses left.")
        print("Available Letters:",getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guessInLowerCase = guess.lower()
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed) )
            print("-------------")
            continue
        elif guessInLowerCase in secretWord:
            lettersGuessed.append(guessInLowerCase)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            
        else:
            lettersGuessed.append(guessInLowerCase)
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
            guesses_left -= 1
        print("-------------")
        
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print("Congratulations, you won!")
        
    else:
        print("Sorry, you ran out of guesses. The word was", secretWord)



















