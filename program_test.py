from sys import argv,stderr
#import sys
#from sys import argv 
#print sys.argv
#sys.stdout.write("boe")
if len(argv) != 3 :
    print ("Usage: python healthy_herb.py color place")
    print ("fatal error \n", file=stderr)
#    sys.stderr.write("fatal error\n")
    exit()
print(argv)
a=argv[1]
b=argv[2]
c=a+b
print(c)
          
