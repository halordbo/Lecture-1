#!/usr/bin/python
# Name : Yuta Kiyama,Student Number:16966015
low=1
high=100
for i in range(0,7):
    input=raw_input(str((low+high)/2)+"?:")
    if input=="low":low=(low+high)/2
    elif input == "high": high=(low+high)/2
    elif input=="equal":break
        

        
