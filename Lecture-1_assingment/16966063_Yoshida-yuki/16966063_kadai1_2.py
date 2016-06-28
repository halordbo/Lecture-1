#!/usr/bin/python
#Name_Yuki_Yoshida
#ID_16966063
a =range(1, 100+1)
print(a)
l=1
g=100

x=50

for i in range(1,8+1):
 print('Is your number more than')
 print(x)
 print('?')
 print('prease input high or low or equal')
 high=int("1")
 equal=int("0")
 low=int("-1")
 b=input()
 print('========================')
 
  
 if b==1: 
   a =range(x,g+1) 
   l =x 
   x =x+(g-l)/2+(g-l)%2 

 if b==-1: 
   a =range(l,x+1) 
   g =x 
   x =x-(g-l)/2+(g-l)%2 
 if b==0:
   break
  
print('ANSWER=')
print(a)

