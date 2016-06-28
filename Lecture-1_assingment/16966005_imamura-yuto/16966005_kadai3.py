# -*- coding: utf-8 -*-
##16966005 今村　有杜
#!/usr/bin/python



st='Hello world, this is python!'
stl=[]
stl=st.split(' ')

def s_list(route):
	route_=route[:]
	row=[]
	box=route_
	row.append(box)
	for node in xrange(len(route)-1):
		row.append(box)		
		row[node+1]=row[node][:]
		row[node+1].append(row[node][0])
		row[node+1].pop(0)
	return row
print s_list(stl)
