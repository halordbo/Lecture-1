#16966005 今村　有杜
#!/usr/bin/python


r=raw_input('input number: ')
t=int(r,10)
lean=[50]
st=50
mi=-1
ma=101
dict={1:25,2:15,3:8,4:4,5:2,6:1,7:1}
for x in range(1,7):
		
	
	
	if t > st:
		mi=st
		st=st+dict[x]
		if st>=ma:
			st=ma-1
		lean.append(st)
		print('high')
	elif t < st:
		ma=st
		st=st-dict[x]
		if st<=mi:
			st=mi+1
		lean.append(st)
		print('low')
	elif t ==st:
		print('just!! number is '),
		print(t)
		break

if t==st:
	print('just!! number is '),
	print(st)


print(lean)
succes=0
sf=0
print('100kai')
for t in range (1,101):
	lean=[50]
	st=50
	mi=-1
	ma=101
	sf=0
	for x in range(1,7):
		
	
	
		if t > st:
			mi=st
			st=st+dict[x]
			if st>=ma:
				st=ma-1
			lean.append(st)
		
		elif t < st:
			ma=st
			st=st-dict[x]
			if st<=mi:
				st=mi+1
			lean.append(st)
			
		elif t ==st:
			print('just!! number is '),
			print(t)
			succes=succes+1
			sf=1
			break
	if t ==st and sf==0:
			print('just!! number is '),
			print(t)
			succes=succes+1
			
print('suc:'),
print(succes)

