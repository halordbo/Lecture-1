#!/usr/bin/python

#16966027 suematsu keishi

number = raw_input('Number? ')
number = int(number)

counter = 0
primes = []

for n in range(2, number):
	isprime = True
	for i in range(2, n):
		counter += 1
		if n % i == 0:
			isprime = False
			break
	if isprime:
		primes.append(n)

print primes, len(primes)
