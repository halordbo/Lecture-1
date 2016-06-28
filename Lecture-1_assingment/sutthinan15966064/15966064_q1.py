# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:17:15 2016

@author: Sutthinan Anantarattanachai
"""

def primes(n):
    "Find primes <=n by Sieve of Eratosthenes"
    k = n+1
    sieve = [True] * (k/2)
    for i in xrange(3,int(k**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2:i] = [False] * ((k-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,k/2) if sieve[i]]

n=input('Enter a number: ')
print primes(n)
