#Katsumi Fukushima
#!/usr/bin/python
a = int(input('Number?:'))
for b in range(1,a):
    c=0
    for d in range(1,b):
        if(b%d==0):
             c+=1
    if(c<2):
        print b