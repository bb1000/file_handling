input_string = open("3_given_file_story","r")

lim=70

something = input_string.read()

print(something)

l=0

#for c in something:
#    if c=="\n":
#        val = l
#    l = l+1

#print(val)

#k=0

#for s in input_string.read().split("\n")
for s in something.split("\n"):
    if s == "": print
    w=0
    l = []
    for d in s.split():
        if w + len(d) + 1 <= lim:
            l.append(d)
            w += len(d) + 1
#            k = k + len(d) + 1
        else:
            print (" ".join(l))
            l = [d]
            w = len(d)
#            k= k + len(d)        
    if (len(l)): print (" ".join(l)+"\n")

 
