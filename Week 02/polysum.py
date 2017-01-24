#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 21:26:51 2017

@author: dileep
"""

import math

roundoff = 4

def polysum(n, s):
    '''
    Input n, the number of sides of a regular polygon, and s, length of each side of it
    Returns the sum of the area and square of the perimeter of the regular polygon
    '''
    return (round((0.25*n*s**2)/math.tan(math.pi/n) + (n*s)**2, roundoff))   