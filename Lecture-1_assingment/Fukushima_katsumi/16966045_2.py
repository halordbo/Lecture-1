#Katsumi Fukushima
#!/usr/bin/python

x = int(input('Number?:'))

def find(x,i,f,n):
    if(n==8):
         print('NOT FOUND')
    elif(x==(i+f)/2):
         print('equal')
         print (i+f)/2
    elif(x>=(i+f)/2):
         print('high')
         n+=1
         find(x,(i+f)/2,f,n)
    else:
         print('low')
         n+=1
         find(x,i,(i+f)/2,n)

find(x,0,101,1)