#Nakamura Yuki 16966034
#!/usr/bin/python
print "input number "
x = int(raw_input())
print "result"
for c in range(1,x+1):
	d = 0
	for b in range(1,c):
		if( c%b == 0):
			d+=1
	if(d < 2):
		print c
