#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:24:15 2017

@author: dileep
"""

def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return (0)
      