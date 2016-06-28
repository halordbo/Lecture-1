#!/usr/bin/python
#16966067 Watanabe Ryuji
sent=raw_input("input 1 sentence->")
words=sent.split(" ")
rewords=list(reversed(words))
print " ".join(rewords)
