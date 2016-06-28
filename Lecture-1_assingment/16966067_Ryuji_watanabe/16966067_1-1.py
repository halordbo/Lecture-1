#!/usr/bin/python
#16966067 Watanabe Ryuji
c=0
flag=0
t=raw_input("input natural number->")
value=int(t,10)
for i in range(2,value+1):
    #print i
    flag = 1
    for j in range(2,i):
        #print j
        if i%j==0:
            flag=0
            break
    if flag==1:
        c+=1
print "num of prime",c
