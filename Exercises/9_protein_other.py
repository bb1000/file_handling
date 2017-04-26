from sys import argv
inp = open(argv[1],'r')
out_atom = open('ATOM.out','w')
out_hetatom = open('HETATOM.out','w')

lines = inp.readlines()
print ('Coordinates of ATOM', file=out_atom)
print ('Coordinates of HETATOM', file=out_hetatom)

for line in lines:
   if line.startswith('ATOM'):
      l = line.split()
      coord = (l[11], float(l[6]), float(l[7]), float(l[8]))
      print ("%5s %8.3f %8.3f %8.3f"%coord, file=out_atom)
	
   if line.startswith('HETATM'):
      m = line.split()
      coord2 = (l[11], float(l[6]), float(l[7]), float(l[8]))
      print ("%5s %8.3f %8.3f %8.3f"%coord2, file=out_hetatom)

	
