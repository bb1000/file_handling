<script type="text/javascript"
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
# File handling

## 

BB1000 Programming in Python

KTH

---

layout: false

## Learning objectives

+ File operations: open, close, read, write, etc.

+ Handling of input and output

+ Usage of string, list, dictionary, etc.

---

## String, list, dictionary...

Initialize an empty string/list/dictionary

```python
mystring = ""

mylist = []

mydictionary = {}
```

---

## String, list, dictionary...

Initialize an empty string/list/dictionary

```python
mystring = ""

mylist = []

mydictionary = {}
```

Check if a string is empty

+ Straightforward way

```python
if len(mystring) > 0:
    print("This string is not empty.")
else:
    print("This string is empty.")
```

---

## String, list, dictionary...

Initialize an empty string/list/dictionary

```python
mystring = ""

mylist = []

mydictionary = {}
```

Check if a string is empty

+ Straightforward way

```python
if len(mystring) > 0:
    print("This string is not empty.")
else:
    print("This string is empty.")
```

+ Pythonic way

```python
if mystring:
    print("This string is not empty.")
else:
    print("This string is empty.")
```

---

## String, list, dictionary...

Check if a list is empty

```python
if mylist:
    print("This list is not empty.")
else:
    print("This list is empty.")
```

---

## String, list, dictionary...

Check if a list is empty

```python
if mylist:
    print("This list is not empty.")
else:
    print("This list is empty.")
```

Check if a dictionary is empty

```python
if mydictionary:
    print("This dictionary is not empty.")
else:
    print("This dictionary is empty.")
```

https://docs.python.org/2/library/stdtypes.html#truth-value-testing

---

## Accessing elements ...

+ Characters in a string:

```python
mystring = "Tack!"

for c in mystring:
    print(c)
```

---

## Accessing elements ...

+ Characters in a string:

```python
mystring = "Tack!"

for c in mystring:
    print(c)
```

<pre>
T
a
c
k
!
</pre>

---

## Accessing elements ...

+ Characters in a string:

```python
mystring = "Tack!"

for c in mystring:
    print(c)
```

<pre>
T
a
c
k
!
</pre>

+ If you want to print in one line:

```python
mystring = "Tack!"

for c in mystring:
    print(c, end=" ")
```

---

## Accessing elements ...

+ Characters in a string:

```python
mystring = "Tack!"

for c in mystring:
    print(c)
```

<pre>
T
a
c
k
!
</pre>

+ If you want to print in one line:

```python
mystring = "Tack!"

for c in mystring:
    print(c, end=" ")
```

<pre>
T a c k ! 
</pre>

---

## Accessing elements ...

+ Elements in a list:

```python
mylist = ["apple", "pear", "banana"]

for element in mylist:
    print(element)
```

---

## Accessing elements ...

+ Elements in a list:

```python
mylist = ["apple", "pear", "banana"]

for element in mylist:
    print(element)
```

<pre>
apple
pear
banana
</pre>

---

## Accessing elements ...

+ Elements in a list:

```python
mylist = ["apple", "pear", "banana"]

for element in mylist:
    print(element)
```

<pre>
apple
pear
banana
</pre>

+ Keys in a dictionary:

```python
mydictionary = {"A": "adenine", "C": "cytosine", "G": "guanine", "T": "thymine"}

for key in mydictionary:
    print(key)
```

---

## Accessing elements ...

+ Elements in a list:

```python
mylist = ["apple", "pear", "banana"]

for element in mylist:
    print(element)
```

<pre>
apple
pear
banana
</pre>

+ Keys in a dictionary:

```python
mydictionary = {"A": "adenine", "C": "cytosine", "G": "guanine", "T": "thymine"}

for key in mydictionary:
    print(key)
```

<pre>
A
C
G
T
</pre>

---

## Accessing elements ...

+ If you want to access both the index and the element

```python
mylist = ["apple", "banana", "cherry"]

for index, element in enumerate(mylist):
    print("The element with index {} is {}".format(index, element))
```

---

## Accessing elements ...

+ If you want to access both the index and the element

```python
mylist = ["apple", "banana", "cherry"]

for index, element in enumerate(mylist):
    print("The element with index {} is {}".format(index, element))
```

<pre>
The element with index 0 is apple
The element with index 1 is banana
The element with index 2 is cherry
</pre>

---

## Accessing elements ...

+ If you want to access both the index and the element

```python
mylist = ["apple", "banana", "cherry"]

for index, element in enumerate(mylist):
    print("The element with index {} is {}".format(index, element))
```

<pre>
The element with index 0 is apple
The element with index 1 is banana
The element with index 2 is cherry
</pre>

+ If you want to access two lists at the same time

```python
names = ["Alice", "Bob", "Carol"]
fruits = ["apple", "banana", "cherry"]

for name, fruit in zip(names, fruits):
    print("{} likes {}".format(name, fruit))
```

---

## Accessing elements ...

+ If you want to access both the index and the element

```python
mylist = ["apple", "banana", "cherry"]

for index, element in enumerate(mylist):
    print("The element with index {} is {}".format(index, element))
```

<pre>
The element with index 0 is apple
The element with index 1 is banana
The element with index 2 is cherry
</pre>

+ If you want to access two lists at the same time

```python
names = ["Alice", "Bob", "Carol"]
fruits = ["apple", "banana", "cherry"]

for name, fruit in zip(names, fruits):
    print("{} likes {}".format(name, fruit))
```

<pre>
Alice likes apple
Bob likes banana
Carol likes cherry
</pre>

---

## Slicing sequences

If you want to access a subset of the sequence (e.g. a substring)

```python
mystring = "ATATCGCGATCG"

print(mystring[:4], mystring[4:8], mystring[8:])
```

---

## Slicing sequences

If you want to access a subset of the sequence (e.g. a substring)

```python
mystring = "ATATCGCGATCG"

print(mystring[:4], mystring[4:8], mystring[8:])
```

<pre>
ATAT CGCG ATCG
</pre>

---

## Slicing sequences

If you want to access a subset of the sequence (e.g. a substring)

```python
mystring = "ATATCGCGATCG"

print(mystring[:4], mystring[4:8], mystring[8:])
```

<pre>
ATAT CGCG ATCG
</pre>

```python
mystring = "ATATCGCGATCG"

print(mystring[:4:2], mystring[4:8:2], mystring[8::2])
```

---

## Slicing sequences

If you want to access a subset of the sequence (e.g. a substring)

```python
mystring = "ATATCGCGATCG"

print(mystring[:4], mystring[4:8], mystring[8:])
```

<pre>
ATAT CGCG ATCG
</pre>

```python
mystring = "ATATCGCGATCG"

print(mystring[:4:2], mystring[4:8:2], mystring[8::2])
```

<pre>
AA CC AC
</pre>

---

## Slicing sequences

If you want to access a subset of the sequence (e.g. a substring)

```python
mystring = "ATATCGCGATCG"

print(mystring[:4], mystring[4:8], mystring[8:])
```

<pre>
ATAT CGCG ATCG
</pre>

```python
mystring = "ATATCGCGATCG"

print(mystring[:4:2], mystring[4:8:2], mystring[8::2])
```

<pre>
AA CC AC
</pre>

```python
mystring = "ATATCGCGATCG"

print([::-1])
```

---

## Slicing sequences

If you want to access a subset of the sequence (e.g. a substring)

```python
mystring = "ATATCGCGATCG"

print(mystring[:4], mystring[4:8], mystring[8:])
```

<pre>
ATAT CGCG ATCG
</pre>

```python
mystring = "ATATCGCGATCG"

print(mystring[:4:2], mystring[4:8:2], mystring[8::2])
```

<pre>
AA CC AC
</pre>

```python
mystring = "ATATCGCGATCG"

print([::-1])
```

<pre>
GCTAGCGCTATA
</pre>

---

## Split and join

The built-in `split` function splits a string using a delimiter

```python
mystring = "My name is Tom."
mylist = mystring.split()
print(mylist)
```

---

## Split and join

The built-in `split` function splits a string using a delimiter

```python
mystring = "My name is Tom."
mylist = mystring.split()
print(mylist)
```

<pre>
['My', 'name', 'is', 'Tom.']
</pre>

---

## Split and join

The built-in `split` function splits a string using a delimiter

```python
mystring = "My name is Tom."
mylist = mystring.split()
print(mylist)
```

<pre>
['My', 'name', 'is', 'Tom.']
</pre>

The opposite of `split` is `join`

```
mystring = '/'.join(['My', 'name', 'is', 'Tom.'])
print(mystring)
```

---

## Split and join

The built-in `split` function splits a string using a delimiter

```python
mystring = "My name is Tom."
mylist = mystring.split()
print(mylist)
```

<pre>
['My', 'name', 'is', 'Tom.']
</pre>

The opposite of `split` is `join`

```
mystring = '/'.join(['My', 'name', 'is', 'Tom.'])
print(mystring)
```

<pre>
My/name/is/Tom.
</pre>

---

## Find

The built-in `find` function finds the position of the substring in a string.

```python
mystring = "one apple, two apples, three apples, four apples"

find_position = mystring.find("apple")
while find_position != -1:
    print(find_position)
    find_position = mystring.find("apple", find_position + 1)
```

---

## Find

The built-in `find` function finds the position of the substring in a string.

```python
mystring = "one apple, two apples, three apples, four apples"

find_position = mystring.find("apple")
while find_position != -1:
    print(find_position)
    find_position = mystring.find("apple", find_position + 1)
```

<pre>
4
15
29
42
</pre>

https://docs.python.org/3/library/stdtypes.html#str.find

---

## String formatting

+ Old style

```python
import math

print("The value of pi is approximately %f" % math.pi)
```

<pre>
The value of pi is approximately 3.141593
</pre>

---

## String formatting

+ Old style

```python
import math

print("The value of pi is approximately %f" % math.pi)
```

<pre>
The value of pi is approximately 3.141593
</pre>

```python
import math

print("The value of pi is approximately %.8f" % math.pi)
print("The value of pi is approximately %20.12f" % math.pi)
```

<pre>
The value of pi is approximately 3.14159265
The value of pi is approximately       3.141592653590
</pre>

---

## String formatting

+ The `format` method

```python
import math

print("The value of pi is approximately {}".format(str(math.pi)))
print("The value of pi is approximately {}".format(math.pi))

print("The value of pi is approximately {:f}".format(math.pi))
print("The value of pi is approximately {:.8f}".format(math.pi))
print("The value of pi is approximately {:20.12f}".format(math.pi))
```

---

## String formatting

+ The `format` method

```python
import math

print("The value of pi is approximately {}".format(str(math.pi)))
print("The value of pi is approximately {}".format(math.pi))

print("The value of pi is approximately {:f}".format(math.pi))
print("The value of pi is approximately {:.8f}".format(math.pi))
print("The value of pi is approximately {:20.12f}".format(math.pi))
```

<pre>
The value of pi is approximately 3.141592653589793
The value of pi is approximately 3.141592653589793
The value of pi is approximately 3.141593
The value of pi is approximately 3.14159265
The value of pi is approximately       3.141592653590
</pre>

---

## String formatting

+ The formatted string literals (f-string, new in Python 3.6)

```python
import math

print(f"The value of pi is approximately {math.pi}")
print(f"The value of pi is approximately {math.pi:.8f}")
print(f"The value of pi is approximately {math.pi:20.12f}")
```

---

## String formatting

+ The formatted string literals (f-string, new in Python 3.6)

```python
import math

print(f"The value of pi is approximately {math.pi}")
print(f"The value of pi is approximately {math.pi:.8f}")
print(f"The value of pi is approximately {math.pi:20.12f}")
```

<pre>
The value of pi is approximately 3.141592653589793
The value of pi is approximately 3.14159265
The value of pi is approximately       3.141592653590
</pre>

https://docs.python.org/3/tutorial/inputoutput.html

---

## What we have learned so far

+ How to initialize an empty string/list/dictionary

+ How to check if a string/tuple/list/dictionary is empty

+ How to use `for` loop to access the elements

+ How to use `enumerate` and `zip`

+ How to slice a sequence using `[start:stop:step]`

+ How to use `split` and `join`

+ How to format a string

---

## Opening file

The built-in `open` function

+ `open` accepts a file name and a mode as arguments

+ file name: a string

+ mode: 'r' for reading; 'w' for writing

+ `open` returns a file object

+ after reading, the opened file should be closed

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

---

## Reading/writing file

+ The `read` method

  Reads the entire file, unless a `size` argument is provided

+ The `readline` method

  Reads one line from the file

+ The `readlines` method

  Reads all lines from the file into a list

+ The `write` method

  Accepts a string as argument, and writes the string to file

---

## Example from Back in the Day

Imagine researcher Miraculix has a student Kaningentix, who has called all his
datafiles with a suffix `.knx`.

Miraculix has to split out the herbs for Asterix and Obelix with suffix `.asx`
and `.obx`.

```
$ cat allherbs.knx
Creator of file: Kaningentix
First test
Herbs Celts
aster: herb1
obeli: herb2
aster: herb3
aster: herb4
obeli: herb5
```

---

## Example from Back in the Day

Imagine researcher Miraculix has a student Kaningentix, who has called all his
datafiles with a suffix `.knx`.

Miraculix has to split out the herbs for Asterix and Obelix with suffix `.asx`
and `.obx`.

```
$ cat allherbs.knx
Creator of file: Kaningentix
First test
Herbs Celts
aster: herb1
obeli: herb2
aster: herb3
aster: herb4
obeli: herb5
```

To read this file in Python, we need to open it first.

```python
f_inp = open("allherbs.knx", 'r')
```

'r' means that the file is opened in read-only mode.

---

## Example from Back in the Day

File are usually read line per line. Sometimes it is useful to know the total
number of the lines in the file.

```python
num_lines = 0
for line in f_inp:
    num_lines += 1
```

---

## Example from Back in the Day

File are usually read line per line. Sometimes it is useful to know the total
number of the lines in the file.

```python
num_lines = 0
for line in f_inp:
    num_lines += 1
```

Other ways of getting number of lines:

```python
f_inp.seek(0)
lines = list(f_inp)
num_lines = len(lines)
```

```python
f_inp.seek(0)
lines = f_inp.readlines()
num_lines = len(lines)
```

```python
f_inp.close()
```

Note that `inp.seek(0)` is used to make sure that we start over from the
beginning of the file.

---

## Example from Back in the Day

In most cases all the information can be retrieved by reading the file once.

```python
f_inp = open("allherbs.knx", 'r')

for line in f_inp:
    if "aster:" in line:
        print(line)
    elif "obeli:" in line:
        print(line)

f_inp.close()
```

---

## Example from Back in the Day

In most cases all the information can be retrieved by reading the file once.

```python
f_inp = open("allherbs.knx", 'r')

for line in f_inp:
    if "aster:" in line:
        print(line)
    elif "obeli:" in line:
        print(line)

f_inp.close()
```

<pre>
aster: herb1

obeli: herb2

aster: herb3

aster: herb4

obeli: herb5

</pre>

---

## Example from Back in the Day

We can use lists to save the herbs that belong to Asterix or Obelix.

```python
herbs_asx = []
herbs_obx = []

f_inp = open("allherbs.knx", 'r')

for line in f_inp:
    if "aster:" in line:
        herb = line.split()[1]
        herbs_asx.append(herb)
    elif "obeli:" in line:
        herb = line.split()[1]
        herbs_obx.append(herb)

f_inp.close()

print(herbs_asx)
print(herbs_obx)
```

---

## Example from Back in the Day

We can use lists to save the herbs that belong to Asterix or Obelix.

```python
herbs_asx = []
herbs_obx = []

f_inp = open("allherbs.knx", 'r')

for line in f_inp:
    if "aster:" in line:
        herb = line.split()[1]
        herbs_asx.append(herb)
    elif "obeli:" in line:
        herb = line.split()[1]
        herbs_obx.append(herb)

f_inp.close()

print(herbs_asx)
print(herbs_obx)
```

<pre>
['herb1', 'herb3', 'herb4']
['herb2', 'herb5']
</pre>

---

## Example from Back in the Day

If we want to save the herbs to file

```python
f_out_asx = open("allherbs.asx", 'w')
f_out_obx = open("allherbs.obx", 'w')

for herb in herbs_asx:
    f_out_asx.write(herb + '\n')

for herb in herbs_obx:
    f_out_obx.write(herb + '\n')

f_out_asx.close()
f_out_obx.close()
```

---

## Example from Back in the Day

If we want to save the herbs to file

```python
f_out_asx = open("allherbs.asx", 'w')
f_out_obx = open("allherbs.obx", 'w')

for herb in herbs_asx:
    f_out_asx.write(herb + '\n')

for herb in herbs_obx:
    f_out_obx.write(herb + '\n')

f_out_asx.close()
f_out_obx.close()
```

```
$ cat allherbs.asx
herb1
herb3
herb4
```

```
$ cat allherbs.obx
herb2
herb5
```

---

## Example from Back in the Day

If we do both reading and writing in one program

```python
f_inp = open("allherbs.knx", 'r')
f_out_asx = open("allherbs.asx", 'w')
f_out_obx = open("allherbs.obx", 'w')

for line in f_inp:

    if "aster:" in line:
        herb = line.split()[1]
        f_out_asx.write(herb + '\n')

    elif "obeli:" in line:
        herb = line.split()[1]
        f_out_obx.write(herb + '\n')

f_inp.close()
f_out_asx.close()
f_out_obx.close()
```
---

## Choice of input file

Imagine Kaningentix didn't have only the file `allherbs.knx`, but also
`alldiseases.knx` and `allforces.knx`. Miraculix likes to have a program in
which he can decide upon the file to be decomposed.

```python
input_file_name = input("Please specify the input file name: ")
```

Miraculix is then asked to specify the input file name. He typed `allherbs`.
The string "allherbs" is saved in the variable `input_file_name`.

https://docs.python.org/3/library/functions.html#input

---

## Choice of input file

Now Miraculix can interact with the program

```python
input_file_name = input("Please specify the input file name: ")

f_inp = open(input_file_name + ".knx", 'r')
f_out_asx = open(input_file_name + ".asx", 'w')
f_out_obx = open(input_file_name + ".obx", 'w')

for line in f_inp:

    if "aster:" in line:
        herb = line.split()[1]
        f_out_asx.write(herb + '\n')

    elif "obeli:" in line:
        herb = line.split()[1]
        f_out_obx.write(herb + '\n')

f_inp.close()
f_out_asx.close()
f_out_obx.close()
```
---

## Choice of input file

Imagine now that Miraculix gives a name of a file which does not exist. The
program breaks. Therefore, a test can be built in.

```python
input_file_name = input("Please specify the input file name: ")

try:
    f_inp = open(input_file_name + ".knx", 'r')

except IOError:
    print("File cannot be opened: " + input_file_name + ".knx")
    exit()
```

---

## Choice of input file

Imagine now that Miraculix gives a name of a file which does not exist. The
program breaks. Therefore, a test can be built in.

```python
input_file_name = input("Please specify the input file name: ")

try:
    f_inp = open(input_file_name + ".knx", 'r')

except IOError:
    print("File cannot be opened: " + input_file_name + ".knx")
    exit()
```

When a file is given in which does not exist, a simple message is given out and
the program terminates.

<pre>
Please specify the input file name: something
File cannot be opened: something.knx
</pre>

https://docs.python.org/3/tutorial/errors.html#handling-exceptions

---

## File name and extension

In the previous example we have dealt with three files, `allherbs.knx`,
`allherbs.asx`, and `allherbs.obx`.

The common part in the names of the files is the part in front of the `.`
delimiter.  The part after `.` is the file extension.

We can use some simple code to detect the file name and the file extension.

```python
input_file_name = input("Please specify the input file name: ")

if "." in input_file_name:
    parts = input_file_name.split('.')
    input_file_name = '.'.join(parts[:-1])
```

---

## File name and extension

In the previous example we have dealt with three files, `allherbs.knx`,
`allherbs.asx`, and `allherbs.obx`.

The common part in the names of the files is the part in front of the `.`
delimiter.  The part after `.` is the file extension.

We can use some simple code to detect the file name and the file extension.

```python
input_file_name = input("Please specify the input file name: ")

if "." in input_file_name:
    parts = input_file_name.split('.')
    input_file_name = '.'.join(parts[:-1])
```

Using libraries, this can be done nicer:

```python
import os
input_file_name = input("Please specify the input file name: ")
input_file_name, input_file_extension = os.path.splitext(input_file_name)
```

---

## Example from Back in the Day

```
$ cat allherbs.knx
Creator of file: Kaningentix
First test
Herbs Celts
aster: herb1
obeli: herb2
aster: herb3
aster: herb4
obeli: herb5
```

---

## Example today

It would be nicer to have the full names in the file.

```
$ cat allherbs_2.knx
Creator of file: Kaningentix
First test
Herbs Celts
asterix: petroleum
obelix: kerosine
asterix: cyanine
asterix: diesel
obelix: lpgas
```

---

## Example today

It would be nicer to have the full names in the file.

```
$ cat allherbs_2.knx
Creator of file: Kaningentix
First test
Herbs Celts
asterix: petroleum
obelix: kerosine
asterix: cyanine
asterix: diesel
obelix: lpgas
```

... and Miraculix will get ...

```
$ cat allherbs_2.asx
petraoleum
cyanine
diesel
```

```
$ cat allherbs_2.obx
kerosine
lpgas
```

---

## Some other type of printing

We know that the following code works

```python
file_name = "obelix_dog"
my_file_obj = open(file_name, 'w')
my_file_obj.write("Idefix")
my_file_obj.close()
```

---

## Some other type of printing

We know that the following code works

```python
file_name = "obelix_dog"
my_file_obj = open(file_name, 'w')
my_file_obj.write("Idefix")
my_file_obj.close()
```

It is also possible to say

```python
file_name = "obelix_dog"
my_file_obj = open(file_name, 'w')
print("Idefix", file=my_file_obj)
my_file_obj.close()
```

---

## Some other type of printing

It should be known that we should provide a string to `write`

```python
file_name = "obelix_wprocs"
file_obj = open(file_name, 'w')

number = 5
file_obj.write(str(number))

file_obj.close()
```

String formatting is also useful

```python
file_obj.write("{:d}\n".format(number))
```

Finally, the `open` function can have three options: read ('r'), write ('w') -
and append ('a'). In the "append" mode, the extra output is written at the end
of the file.

---

## How to read strings and numbers?

In a file, Asterix keeps tracks of his weapons:

```
$ cat weapons.asx
knife: 4
spear: 2
arrow: 3
fist: 2
```

---

## How to read strings and numbers?

In a file, Asterix keeps tracks of his weapons:

```
$ cat weapons.asx
knife: 4
spear: 2
arrow: 3
fist: 2
```

The total sum of his weapons is given by `readlines()` followed by a `split()`
of each line.

```python
f_inp = open("weapons.asx", 'r')
lines = f_inp.readlines()
f_inp.close()

number = 0
for line in lines:
    number += int(line.split()[1])

print(number)
```

---

## How to read strings and numbers?

In a file, Asterix keeps tracks of his weapons:

```
$ cat weapons.asx
knife: 4
spear: 2
arrow: 3
fist: 2
```

The total sum of his weapons is given by `readlines()` followed by a `split()`
of each line.

```python
f_inp = open("weapons.asx", 'r')
lines = f_inp.readlines()
f_inp.close()

number = 0
for line in lines:
    number += int(line.split()[1])

print(number)
```

<pre>
11
</pre>

`split` separates parts of a line by a space, and save them in a list. Remark
that `line.split()` gives access to a list of strings.

---

## The sys-module and some easy way of input

`argv` contains the vector of arguments passed to a program via the command line. `argv[0]` is the filename of the program, `argv[1]` is then the first argument given, `argv[2]` the second etc. `argv` has to be imported from the module `sys`.

Imagine that a program `program_test.py` contains two lines of code:

```
from sys import argv
print(argv)
```

The output of `python program_test.py` is then

```
['program_test.py', 'a', 'b']
```

argv[0] contains then the name `program_test.py`, argv[1] and argv[2] contain `a` and `b`, respectively.

---

## The sys-module and some safe way of input

Miraculix made a program `healthy_herb.py` which says whether or not a herb is safe to be eaten or not. As input parameters, the program needs to know the color of the herb as well as its sites in the forest:

`python healthy_herb.py green river`

To make sure that his collaborators provide these from the beginning, Miraculix hard coded a small test:       

```
from sys import argv
if len(argv) != 3 :
   print ("Usage: python healthy_herb.py color place")
   exit()

```

Of course, in the code, the arguments still have to be defined:

```
color = argv[1]
place = argv[2]

```

---

## References

"Python for Data Analysis", Wes McKinney, O'Reilly Media, Sebastopol, CA: 2013

"Python for Informatics", Charles Severance, 2013, http://www.pythonlearn.com/book.php#python-for-informatics

http://www.pythonforbeginners.com

