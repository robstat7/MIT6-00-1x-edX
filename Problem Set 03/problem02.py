#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:28:00 2017

@author: dileep
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter + ' '
        else:
            word += '_ '
            
    return word
        
        