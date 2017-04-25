#!python
file=input("Which inputfile? ")

if "." in file:
     file = file[:file.find(".")]

try:
     inp= open(file+".e1",'r')
except:
     print ('File cannot be opened:', file+".e1")
     exit()
     
out= open(file+".e2", 'w')

totnumb = 0

for line in inp:
     totnumb = totnumb + 1
     
inp.seek(0)
     
number = 0

for line in inp:
    number2=float(line)
    number = number + number2

ave= number/totnumb
    
out.write("%f \n" % ave)
out.close()
