#!/usr/bin/python
#Name_Yuki_Yoshida
#ID_16966063
x=0
print('a=')
a=input()
#a1=int(a,10)
print('----------------')

for i in range(2,a+1):
   count=0
   for j in range(2,i+1):
      if i%j==0:
         count=count+1
   if count ==1:
      print(j)
      x=x+1
print('ans=')
print(x)
    

   
   
