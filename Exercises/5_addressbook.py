addressbook = {}
para = True
while para:
	invoer = input('name, e-mail: ')
	if invoer=='0':
		para = False
	else:
		d = invoer.split(',')
		addressbook[d[0]]=d[1]
name = list(addressbook.keys())
name.sort()

for i in range(len(name)):
#	print ("%d. %-20s %-20s"%(i+1, name[i], addressbook[name[i]]))
        print ("%d. %s %s"%(i+1, name[i], addressbook[name[i]]))

	