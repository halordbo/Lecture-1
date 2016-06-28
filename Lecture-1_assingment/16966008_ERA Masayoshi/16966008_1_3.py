#16966008 ERA Masayoshi
#!/usr/bin/python

text=raw_input("please write text")
print text
words=text.split(" ")
rewords=list(reversed(words))
#print rewords
print " ".join(rewords)
