n=int(raw_input())

for a in range(2,n):
    if n%a==0:
        break

if a==n:
    print('n is prime number')
else:
    print('n is not prime number')
