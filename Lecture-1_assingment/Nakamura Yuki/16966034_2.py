#Nakamura Yuki 16966034
#!/usr/bin/python

def find(x,low,high,n):
	print "count"
	print n
	n = n - 1
	if(n < 0):
		print "not found"
	elif(x == (low+high)/2):
		print "found"
		return 0
	elif(x >= (high+low)/2):
		print "high"
		find(x,(high+low)/2,high,n)
	else:
		print "low"
		find(x,low,(high+low)/2,n)


print "input number "
x = int(raw_input())
find(x,0,101,7)
