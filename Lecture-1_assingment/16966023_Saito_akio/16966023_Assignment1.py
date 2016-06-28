# Question.1
print ('Question.1')
print ('Program to Count by prime numbers')
n = input('Number? ')

for i in range(2,n+1):
        k=0
        for j in range(2,i):
                if (i%j==0):
                        k=1
        if (k==0):
                print(i)

# Question.2
import random
print ('Question.2')
m = random.randint(1,100)

low = 1
high = 100

for i in range(0,7):
    n = input('input number ')
    if(n == m):
        print "equal"
        break
    if(m<n):
        print "high"
    if(n<m):
        print "low"


# Question.3
print ('Question.3')
x = "I'm student in Kyutech. I'm study robotics."
y = "Hello world, this is python!"
print " ".join(x.split()[::-1])
print " ".join(y.split()[::-1])
