#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 23:13:12 2017

@author: dileep
"""

low = 0
high = 100
mid = (low + high)//2

print("Please think of a number between 0 and 100!")

while mid != low and mid != high:
    print("Is your secret number " + str(mid) + "?")
    user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")  
    if user_input == 'h':
        high = mid
    elif user_input == 'l':
        low = mid
    elif user_input == 'c':
        print("Game over. Your secret number was:", mid)
        break
    else:
        print("Sorry, I did not understand your input.")
        continue
    mid = (low + high)//2
        
        