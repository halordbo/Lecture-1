#!/usr/bin/python
#16966067 Watanabe Ryuji
N=100
seq=range(1,N+1)
index=N/2
step=0
for i in range(1,7+1):
    if index < 1:
        index=1
    elif index > 100:
        index = 100
    num = seq[index-1]#deciding display number
    print "predicted number:",num
    t=raw_input("high?low?equal? ->")
    #print t
    
    step=(N/(2**(i+1))+step%2)
    if step < 1:
        step=1
    #print step
    if t=="high":
        index+=step
    elif t=="low":
        index-=step
    elif t=="equal":
        print "yeah!"
        break
    else:
        print "input error"
        break
    
