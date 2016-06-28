#!/usr/bin/python

#16966027 suematsu keishi

change = "Hello world this is python !".split(' ')

ch = change[1]
change[1] = change[2]
change[2] = ch

ch = change[0]
change[0] = change[3]
change[3] = ch

ch = change[5]
change[5] = change[4]
change[4] = ch

edit = ' '.join(change)
print edit

