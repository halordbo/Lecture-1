#!/usr/bin/env python
#author:Dwivedi Neelesh
#student id: 15966067
#ques 2
print('Think of a number between 1-100')

first,last=1,100

for i in range(7):
	mid = (first+last)/2
	print 'Guess No.',(i+1),' =',mid
	num = raw_input('If guess is correct enter y else n')
	if (str(num)=='y' or i==6):
		break
	num = raw_input('If your number is higher than guess enter 1 else enter 0')
	if (int(num)==1):
		first = mid +1
	elif (int(num)==0):
		last = mid -1

