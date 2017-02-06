#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:57:17 2017

@author: dileep
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    for key in aDict:
        total += len(aDict[key])
        
    return total
        
