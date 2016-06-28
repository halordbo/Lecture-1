#!/usr/bin/python

#16966027 suematsu keishi

import random

print "generate random number"
n = random.randint(1,100)

for i in range(7):
	number = raw_input('think your number ')
	number = int(number)

	if number == n:
		print "Equal"
		break
	elif number < n:
		print "Low"
	else:
		print "High"
		
