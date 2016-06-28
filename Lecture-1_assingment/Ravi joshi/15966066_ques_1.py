#!/usr/bin/python
# author: Joshi Ravi Prakash
# student id: 15966066
# date: 27 June 2016
# question: 1


length = None
while not length:
	try:
		length = int(raw_input('Number? '))
	except ValueError:
		print 'Invalid Number'

# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
primes = [True] * length

for i in range(2,length):
	primes[i] = True

for i in range(2,length):
	if primes[i]:
		for j in range(i*i,length,i):
			primes[j] = False

# print and count all prime numbers
print "\nFollowing are the prime numbers till ", length
count = 0
for i in range(2,length):
	if primes[i]:
		print i,
		count += 1

print "\nTotal prime numbers -", count

