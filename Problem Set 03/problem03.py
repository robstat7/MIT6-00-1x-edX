#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 15:53:26 2017

@author: dileep
"""

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    from string import ascii_lowercase
    
    string = ''
    
    for letter in ascii_lowercase:
        if letter not in lettersGuessed:
            string += letter
            
    return string
        
    