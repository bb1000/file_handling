#!python
file=input("Which inputfile? ")

if "." in file:
     file = file[:file.find(".")]

try:
     inp= open(file+".knx",'r')
except:
     print ('File cannot be opened:', file+".knx")
     exit()

outas = open(file+".asx",'w')
outob = open(file+".obx",'w')

totnumb = 0

for line in inp:
     totnumb = totnumb + 1

inp.seek(0)     

number = 0

line = inp.readline()
number = number + 1 
while "Herb" not in line:
     line = inp.readline()
     number = number + 1

while number < totnumb:
     line = inp.readline()
     number = number + 1
     spacepos = line.find(' ')
     if (line[:spacepos-1]) == "asterix":
             outas.write(line[spacepos+1:])
     if (line[:spacepos-1]) == "obelix":
             outob.write(line[spacepos+1:])

inp.close()
outas.close()
outob.close()
 
