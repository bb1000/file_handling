#!python
file=input("Which inputfile? ")
out = open(file,'a')
number=float(input("Give number: "))
number2=29+number
#out.write(number2+"\n")
out.write(str(number2)+"\n")
out.write("%f \n" % number2)
out.close()
