#16966041  Masataka Hisano

#!/usr/bin/python
#-*- coding: utf-8; -*-

s = raw_input("Input number: ")
time = int(s,10)
flag=0
count=0
for x in range(2, time):
	for y in range(1,x+1):
		if x%y==0:
			flag+=1
	if flag==2:
		print(x)
		count+=1
	flag=0

print("primes"),
print(count)
