#16966005 今村　有杜
#!/usr/bin/python

s=raw_input('input number: ')
st=int(s,10)
h=0
count=0
for x in range(1,st+1):
	for y in range(1,x+1):
		if x%y==0:
			h=h+1
	if h==2:
		print(x)
		count=count+1
	h=0

print("sosu:"),
print(count)
	
	
	
