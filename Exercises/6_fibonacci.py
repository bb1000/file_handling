#!/usr/bin/python
from sys import argv
amount_numbers = int(argv[1])
list = [0,1]
rest = amount_numbers - 2
i = 0
while i < rest:
	b = list[i] + list[i+1]
	list.append(b)
	i+=1
print ("%d-terms in list Fibonacci:"%amount_numbers)
for i in list:
	print (i)
#print(" ".join(str(list)))
#print(list)
#for i in list:
#        print (str(i)+" ")
#for i in list:
print(' '.join(str(x) for x in list))