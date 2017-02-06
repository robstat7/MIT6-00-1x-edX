#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:11:33 2017

@author: dileep
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretWord = list(secretWord) # Converting the string into a list of seperate letters
    if set(secretWord) < set(lettersGuessed): # Converting lists into the subsets and checking for 'is a subset' condition
        return True
    else:
        return False