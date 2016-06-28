#!/usr/bin/python
# Name : Yuta Kiyama,Student Number:16966015
input = int(raw_input())
all_idnum=[]
for i in range(2,input+1):
    if i%2:
        if [k for k in all_idnum if i%k==0]==[]:
            all_idnum.append(i)
       
    if i==2:all_idnum.append(i)
        
print all_idnum
            
            