# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:21:15 2016

@author: Sutthinan Anantarattanachai
"""

print('pick one number between 1 to 100')
L=1;
R=100;
def find(L,R):
    x=(L+R)/2;
    n=input('your number is '+repr(x)+' [Y=1/N=0]: ')
    if n==1:
        print "found"
    elif n==0:
        n=input('Then is your number more than '+repr(x)+'? [Y=1/N=0]: ')
        if n==1:
            find(x+1,R)
        else:
            find(L,x-1)
        
find(L,R)