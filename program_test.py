from sys import argv
if len(argv) != 3 :
    print ("Usage: python healthy_herb.py color place")
    exit()
print(argv)
a=argv[1]
b=argv[2]
c=a+' '+b
print(c)
          

