#!/usr/bin/env python
#author:Dwivedi Neelesh
#student id: 15966067
#ques 1
num = int(raw_input('Enter Number'))
print [x for x in range(2,num) if not [t for t in range(2,x) if not x%t]]

