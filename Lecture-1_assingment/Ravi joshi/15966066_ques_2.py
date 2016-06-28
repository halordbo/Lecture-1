#!/usr/bin/python
# author: Joshi Ravi Prakash
# student id: 15966066
# date: 27 June 2016
# question: 2

print "Guess a number from 1 to 100"

start,end=1,100
mid = (start+end)/2
for i in range(7):
	print mid
	lim = str(raw_input('is number correct[y/n]'))
	if lim == "y":
		print "found"
		break
	else:
		high = str(raw_input('is number higher [y/n]'))
		if high == "y":
			start = mid + 1
		else:
			end = mid - 1
	mid = (start+end)/2

