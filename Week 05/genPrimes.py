#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 19:46:01 2017

@author: dileep
"""

def genPrimes():
    """Generates the sequence of prime numbers"""
    primes = [] 
    i = 2 
    while True:
        # A candidate number x is prime if (x % p) != 0 for all earlier primes p.
        isPrime = True
        for prime in primes:
            if (i % prime) == 0:
                isPrime = False
                break
        # Show the prime number and add it to the list.        
        if isPrime:
            primes.append(i)
            yield i
        # Generate another candidate.
        i += 1