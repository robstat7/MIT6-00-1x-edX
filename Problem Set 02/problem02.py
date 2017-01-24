#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:58:38 2017

@author: dileep
"""

def calculate_lowest(balance, annualInterestRate):
    '''
    Calculates the minimum fixed monthly payment 
    needed in order pay off a credit card balance within 12 months
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    tmpBalance = balance
    monthlyPayment = 0
    while tmpBalance > 0:
        tmpBalance = balance
        monthlyPayment += 10
        for month in range(12):
            tmpBalance -= monthlyPayment
            tmpBalance += tmpBalance * monthlyInterestRate
            
    print ("Lowest Payment:", monthlyPayment)


calculate_lowest(balance, annualInterestRate)
