invoer=input('Geef je zin: ')
woorden= invoer.split()
lijst=[]
for woord in woorden:
    if len(woord) >= 3:
        if woord[2].isupper() or woord[-1].isupper():
            lijst.append(woord.upper())
        else:
            lijst.append(woord)
    else:
        lijst.append(woord)
print (' '.join(lijst))
