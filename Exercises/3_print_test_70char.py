input_string = open("3_given_file_story","r")

lim=70
for s in input_string.read().split("\n"):
    if s == "": print
    w=0
    l = []
    for d in s.split():
    	if w + len(d) + 1 <= lim:
            l.append(d)
            w += len(d) + 1
        else:
            print (" ".join(l))
            l = [d]
            w = len(d)
    if (len(l)): print (" ".join(l))

