from sys import argv
inp=open(argv[1],'r')

out1 = argv[1][:argv[1].find(".")]

out=open(out1+"_shift.xyz",'w')

lines=inp.readlines()
coords = []
atoms = 0
hatms = ['CU','MG','ZN','NA','CA']

x=3
y=4
z=2

for line in lines:
  if line.startswith('HETATM'):
    woorden=line.split()
    for atm in hatms:
      if woorden[11]==atm:
        atoms+=1
        coord=(woorden[11],float(woorden[6])+x,float(woorden[7])+y,float(woorden[8])+z)
        coords.append(coord)

print("      %d" % atoms, file= out)
print("\n", file = out)
for i in coords:
   print("%s %8.3f %8.3f %8.3f" % i, file = out)