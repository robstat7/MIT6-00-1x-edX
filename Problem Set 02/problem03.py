#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:35:44 2017

@author: dileep
"""

def calculate_lowest(balance, annualInterestRate):
    '''
    Calculates the minimum fixed monthly payment 
    needed in order pay off a credit card balance within 12 months
    using bisection search
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    tmpBalance = balance
    low = balance / 12.0
    high = (balance * (1 + monthlyInterestRate) ** 12) / 12.0
    monthlyPayment = round((low + high) / 2, 2)
    while True:
        tmpBalance = balance
        for month in range(12):
            tmpBalance -= monthlyPayment
            tmpBalance += tmpBalance * monthlyInterestRate
        if abs(tmpBalance - 0.01) < 0.1:
            print ("Lowest Payment: ", monthlyPayment)
            break
        elif tmpBalance < 0:
            high = monthlyPayment
            monthlyPayment = round((low + high) / 2, 2)
        else:
            low = monthlyPayment
            monthlyPayment = round((low + high)/2, 2)
            
calculate_lowest(balance, annualInterestRate)
        