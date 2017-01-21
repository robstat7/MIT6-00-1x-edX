#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:18:29 2017

@author: dileep
Decimal fraction (between 0 and 1) to binary conversion.
"""
num = x = float(input("Enter a decimal fraction between 0 and 1: "))
count = 0
binary = '0.'
rem = (num*2)%1
while num != 0 and count < 8:
    binary += str(int(num))
    num = rem*2
    rem = num%1
    count += 1
print("Binary of", x, "is",binary)
