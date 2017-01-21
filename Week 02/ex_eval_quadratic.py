#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 14:15:59 2017

@author: dileep
"""

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic
    Returns the value of the quadratic a*x**2+b*x+c
    '''
    return (a*x**2+b*x+c)