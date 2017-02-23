<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
# File handling

## 

BB1000 Programming in Python
KTH

---

layout: false

## Example from Back in the Day

Imagine researcher Miraculix has a student Kaningentix, who has called all his datafiles with a suffix .knx The first task is then to reduce the title to its essentials. Miraculix has to split out the herbs for Asterix and Obelix with suffix .asx and .obx

```
>>> cat allherbs.knx
Creator of file: Kaningentix
First test
Herbs Celts
aster: herb1
obeli: herb2
aster: herb3
aster: herb4
obeli: herb5

```

For reading and writing, the files have to be opened.

```
>>> file="allherbs"
>>> inp = open(file+".knx",'r')
>>> outas = open(file+".asx",'w')
>>> outob = open(file+".obx",'w')

```

The 'r' points at a file aimed only to be read, while 'w' is aimed only for writing.

---

## Example from Back in the Day

As the file is read line per line, it is important to know the total number of the lines (`totnumb`). Since the file has been read up till the end, Miraculix has to start again from the beginning using `inp.seek(0)`. 

```
>>> totnumb = 0
>>> for line in inp:
        totnumb = totnumb + 1
>>> inp.seek(0)

```

Each line of `inp` is read in, and its content is analyzed. Remark that the lines are counted, using `number` - and that its value has to be initiated in the beginning.

```
>>> number = 0
>>> line = inp.readline() 
>>> number = number + 1
>>> while "Herb" not in line:
>>>       line = inp.readline()
>>>       number = number + 1

```

---

## Example from Back in the Day

As long as the program didn't reach the end of the file (so, as long as the number of read lines is smaller than the total amount of lines in the file), the next line is read.

```
>>> while number < totnumb:
>>>     line = inp.readline()
>>>     number = number + 1

```

Within this loop, the first five characters of the line are examined.

```
>>>     if (line[:5]) == "aster":
>>>           outas.write(line[7:12]+"\n")
>>>     if (line[:5]) == "obeli":
>>>           outob.write(line[7:12]+"\n")

```

Finally, all files are closed. The writing only occurs at the moment of closing.

```
>>> inp.close()
>>> outas.close()
>>> outob.close()

```

---

## Choice of input file

Imagine Kaningentix didn't have only the file allherbs.knx, but also alldiseases.knx and allforces.knx. Miraculix likes to have a program in which he can decide upon the file to be decomposed.

```
>>> file = raw_input("Which inputfile? ")
Which inputfile?

```

Miraculix can write then `allherbs.knx`. The only part which is important is the one in front of the ".". Remark that the name of the file is like an array and that only from element "0" until (but not including) the "." is retained.   

```
>>> if "." in file:
>>>      file = file[:file.find(".")]
>>> file
'allherbs'

```

---

## Reading until space

In the program above, the input file is read based upon the number of characters - which also meant that Asterix was abbreviated to `aster` and Obelix to `obeli`. It would have been better to read until the first space. 

```
>>> while number < totnumb:
>>>     line = inp.readline()
>>>     number = number + 1
>>>     spacepos = line.find(' ')
>>>     if (line[:spacepos-1]) == "aster":
>>>           outas.write(line[spacepos+1:12]+"\n")
>>>     if (line[:spacepos-1]) == "obeli":
>>>           outob.write(line[spacepos+1:12]+"\n")

```

---

## Reading until end of line

Still it makes not much sense to use the program above, since the herbs should have names which have all the exact same length. In the example of Miraculix, each line (and therefore the name of the herb) ends on another space or on a hard enter.

<!--
     if (line[:spacepos-1]) == "aster":
            outas.write(line[spacepos+1:]+"\n")
     if (line[:spacepos-1]) == "obeli":
            outob.write(line[spacepos+1:]+"\n")
-->

```
>>>      if (line[:spacepos-1]) == "aster":
>>>            outas.write(line[spacepos+1:])
>>>      if (line[:spacepos-1]) == "obeli":
>>>            outob.write(line[spacepos+1:])
	       
```

---

## Example today

In this way, the input could be

```
>>> cat allherbs_2.knx
Creator of file: Kaningentix
First test
Herbs Celts
asterix: petraoleum
obelix: kerosine
asterix: cyanine
asterix: diesel
obelix: lpg

```

... and Miraculix will get ...

```
>>> cat allherbs_2.asx
petraoleum
cyanine
diesel

```

```
>>> cat allherbs_2.obx
kerosine
lpg

```

---
