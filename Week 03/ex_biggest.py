#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 20:58:03 2017

@author: dileep
"""

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    largest = {'length' : 0, 'large_key' : 'z'}
    for key in aDict:
        if len(aDict[key]) > largest['length']:
            largest['length'] = len(aDict[key])
            largest['large_key'] = key
    return largest['large_key']
    
