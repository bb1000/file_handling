from sys import argv
import random
amin = {"A": "Ala" , "C": "Cys", "D": "Asp", "E": "Glu", "F": "Phe" , "G": "Gly", "H": "His", "I": "Ile" , "K": "Lys" , "L": "Leu", "M": "Met","N": "Asn", "P": "Pro", "Q": "Gln", "R": "Arg", "S": "Ser" , "T": "Thr" , "V": "Val" , "W": "Trp", "Y": "Tyr"}

amin1=list(amin.keys())
rnumb = int(argv[1])
nfiles = int(argv[2])

for i in range(nfiles):
	out = open('sek%i.fasta'%(i+1), 'w')
	print('> Sequence %d'%(i+1)+': ', file = out)
	sek = []
	for d in range(rnumb):
		sek.append(random.choice(amin1))
	sek = ''.join(sek)
	for i in range(0,len(sek),70):
		print(sek[i:i+70], file = out)
	out.close()
		
