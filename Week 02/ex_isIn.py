#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 20:30:11 2017

@author: dileep
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        if char == aStr:
            return True
        else:
            return False
    if char == aStr[len(aStr)//2]:
        return True
    return(isIn(char,aStr[:len(aStr)//2]) if char < aStr[len(aStr)//2] else isIn(char,aStr[len(aStr)//2:]))