#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:50:33 2017

@author: dileep
"""
length=0
curr=s[0]
l_substring=s[0]
for i in range(len(s) - 1):
    if s[i + 1] >= s[i]:
        curr += s[i + 1]
        if len(curr) > length:
            length = len(curr)
            l_substring = curr
    else:
        curr=s[i + 1]
print("Longest substring in alphabetical order is: " + l_substring)
