#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 14:20:53 2017

@author: dileep
"""
num_vowels = 0
for i in range(len(s)):
    if s[i] in 'aeiou':
        num_vowels += 1
print("Number of vowels:", num_vowels)
        
