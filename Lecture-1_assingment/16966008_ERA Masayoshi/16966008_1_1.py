#16966008 ERA Masayoshi
#!/usr/bin/python

c=0
print 'please input number'
ar=raw_input()
var=int(ar,10)
print var
print 'prime member is'
for i in range(1,var+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=1+count
    if count==2:
        print j
        c=c+1
print 'prime count is'
print c
