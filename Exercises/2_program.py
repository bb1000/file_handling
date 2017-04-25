file1=input("Which inputfile f? ")
file2=input("Which inputfile g? ")

file1=open(file1,'r')
file2=open(file2,'r')

out=open("2_output",'w')

lines1=file1.readlines()
length1=len(lines1)

lines2=file2.readlines()
length2=len(lines2)

number_1=[]
number_2=[]

for line in lines1:
#    number_1[line] = int(file1.readline())
    number_1.append(float(line))
    
for line in lines2:
#    number_2[line] = int(file2.readline())
    number_2.append(float(line))

j=0
i=0

if length2 <= length1:
    while j <= length2-1:
        if number_2[j] <= number_1[i]:
            out.write(str(number_2[j])+"\n")
            j=j+1
        else:
            out.write(str(number_1[i])+"\n")
            i=i+1    
    else:
        for k in range(0, (length1-length2)-1):
            out.write(str(number_1[k+i])+"\n")

if length1 < length2:
    while i <= length1-1:
        if number_2[j] <= number_1[i]:
            out.write(str(number_2[j])+"\n")
            j=j+1
        else:
            out.write(str(number_1[i])+"\n")
            i=i+1
    else:
        for k in range(0, (length2-length1)-1):
            out.write(str(number_2[k+j])+"\n")
                
out.close()
