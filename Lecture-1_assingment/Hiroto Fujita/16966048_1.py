#Hiroto Fujita 
#!/usr/bin/python
a = int(raw_input('Number? '))
for c in range(1,a):
    b=0
    for d in range(1,c):
        if(c%d==0):
             b+=1
    if(b<2):
        print c

