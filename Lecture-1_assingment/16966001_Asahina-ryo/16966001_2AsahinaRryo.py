import random

n=int(raw_input())
r=random.randint(1,100)

lower=1
bigger=100
c=0
while 1:
    n=int(raw_input())
    if(n==m):
        print" hit m ="+str(m)
        break
    else:
        if(n<m):
            print" lower "
            lower+=1
            m=(m+lower)/2
        else:
            print" higher "
            bigger-=1
            m=(m+bigger)/2
