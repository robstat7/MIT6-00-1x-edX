#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:04:22 2017

@author: dileep
"""

def calculate(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Calculates the remaining balance after one year provided with the initial 
    outstanding balance, annual interest rate and the minimum monthly payment rate
    '''
    monthlyInterestRate = annualInterestRate/12.0
    for month in range(12):
        minimumMonthlyPayment = monthlyPaymentRate * balance  
        balance -= minimumMonthlyPayment
        balance += balance * monthlyInterestRate

    print ("Remaining balance: " + str(round(balance, 2)))
    

calculate(balance, annualInterestRate, monthlyPaymentRate)
        