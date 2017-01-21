#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:17:17 2017

@author: dileep
"""
count = 0
for i in range(len(s)-2):
    if s[i:i+3] == "bob":
        count += 1
print("Number of times bob occurs is:", count)
    