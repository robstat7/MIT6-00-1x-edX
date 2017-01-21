#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:32:56 2017

@author: dileep
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    small = a if a < b else b
    while small >= 1:
        if a%small == 0 and b%small == 0:
            return small
        else:
            small -= 1

