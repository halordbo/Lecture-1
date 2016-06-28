#16966008 ERA Masayoshi
#!/usr/bin/python

c=100
q=50
p=0
Quit=100
hoge= range(0,c+1)
answer=raw_input
print var
ar='piyopiyo'
while ar!='equal':
    if c==100:
        c=hoge[int(c/2)]
    print "answer is"
    print hoge[int(c)]
    print "? your answer is hight/ low/ equal"
    ar=raw_input()
    if ar=='hight':
        print c
        while ar!='equal':
            if ar=='hight':
                p=q%2
                q=q/2
                c=c+p+q
            elif ar=='low':
                p=q%2
                q=q/2
                c=c-q-p
            print "answer is"
            print hoge[c]
            print "? your answer is hight/ low/ equal"
            ar=raw_input()
            if 100<=hoge[c]:
                hoge[c]=100
                ar='equal'
    elif ar =='low':
        print c
        while ar!='equal':
            if ar=='hight':
                p=q%2
                q=q/2
                c=c+int(q)+p
            elif ar=='low':
                p=q%2
                q=q/2
                c=c-q-p
            print "answer is"
            if hoge[c]==0:
                Quit=0
                hoge[c]=1
            print hoge[c]
            print "? your answer is hight/ low/ equal"
            ar=raw_input()
            if Quit==0:
                ar='equal'
    elif ar =='equal':
        print hoge[c]
        break
print 'Finish!!!your answer is'
print hoge[c]
