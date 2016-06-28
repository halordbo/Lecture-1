#16966041  Masataka Hisano

#!/usr/bin/python
#-*- coding: utf-8; -*-

list = [1]
for x in range(1,100):
	list.append(x)
s = raw_input("Input number under 100: ")
number = int(s,10)

median = 50
dict = {1:25,2:12,3:8,4:4,5:2,6:1,7:1}

for y in range(1,7):
	if number >100:
		print("Please input number under 100")
		break
	elif number > median:
		median = median + dict[y]
		print("high")
	elif number == median:
		print("finished")
		break
	elif number < median:
		median = median - dict[y]
		print("low")
if number == median:
	print(median),
	print("is your input")		
