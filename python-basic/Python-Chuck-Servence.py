#most common word

#get the name of the file and open it
""" name = input("Enter a file")
handle = open(name, 'r')
#count word frequency i.e. histogram
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigwordcount = count
#all done
print(bigword, bigcount) """

""" x = 1 + 2 ** 3 / 4 *5
print(x)

a = "hello "+"world"
print(a)

print(type(1.0))
print(type("Hello")) """

""" k = float(99) #typecasting
print(k)
i = int(42.0) #typecasting
print(i)
sval = "123"
print(type(sval))
ival = int(sval)
print(ival)
print(ival+7) """

# USER INPUT, Typecasting
""" name = input("Enter your name :")
print("Welcomne ",name)

inp = input("Europe floor? ")
usf = int(inp) + 1
print("US floor ",usf) """

#if conditional statement
""" x = 5
if x < 10:
    print("smaller")
if x > 20:
    print("bigger")
print("Finish") """

# if with indentation
""" x=5
if x>2:
    print("Bigger than 2")
    print("Still bigger")
print("Done with 2") """

""" for i in range(5):
    print(i)
    if i>2:
        print("Bigger than 2")
    print("Done with i ",i)
print("All done ") """

#nested if
""" x = 42
if x > 1:
    print("more than 1")
    if x < 100:
        print("less then 100")
print("All done ") """

#if-else
""" x = 4
if x>2:
    print("bigger")
else:
    print("smaller")
print("All done ") """

#if-elif-else
""" x=4
if x<2:
    print("small")
elif x<10:
    print("medium")
else:
    print("LARGE")
print("All done") """

#multi way puzzles
""" # 01
x = int(input("Enter a number"))
if x<2:
    print("Below 2")
elif x>=2:
    print("Two or more")
else:
    print("something else")

# #02
x = int(input("Enter a number"))
if x<2:
    print("Below 2")
elif x<20:
    print("Below 20")
#order not correct
elif x<10:
    print("Below 10")
else:
    print("something else") """

# #try anb except
""" astr = "Hello World"
try:
    istr = int(astr)
    print(istr)
except:
    print("cannot be type casted to int") """

# #try and except 2
""" astr = "Hello World"
try:
    istr = int(astr)
except:
    istr = -1

print("First", istr)

astr = "123"
try:
    istr = int(astr)
except:
    istr = -1

print("Second", istr) """

#try and except 3
""" astr = "Hello World"
try:
    print("Hello")
    istr = int(astr)
    print("There")
except:
    istr = -1

print("First", istr) """

#try and except 4
""" rawstr = input("Enter a positive number: ")
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("input number is ", ival)
else:
    print("Not a positive number") """

# #functions
""" def thing():
    print("Hello")
    print("Have fun")
thing()
print("zip")
thing() """

#built in function max(), min()
""" big = max("Hello World wizard")
print(big)

list1 = [2,4,7,8,9,2,0]
m = min(list1)
print(m)

li = [4,9,2,3,5,7,8,1,6,0]
maxima = max(li)
print(maxima) """

#int(), float()
""" f = 1+2*float(3)/4-5
print(f)

i = int(f)
print(i) """

#function defining and callling(invoking)
""" def display():
    print("I am not okay!")

display() """

#argument passing to functions
""" def greet(lang):
    if lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print("Bonjour")
    elif lang == 'bn':
        print("হ্যালো")
    else:
        print("Hello")


greet('es')
greet('fr')
greet('en')
greet('bn') """

#Return value
""" def add(x, y):
    return x+y

result = add(6,7)
print(result) """

#LOOP
""" n=5
while n>0:
    print(n)
    n=n-1
print("Blastoff!")
print(n) """

#break keyword
""" while True:
    line = input("> ")
    if line == "Done":
        break
    print(line)
print("Done!") """

# #continue keyword
""" while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "Done":
        break
    print(line)
print("Done!") """

#definite loop, for loop
""" for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!") """

#iteration
""" friends = ["Nazmul","Nissan","Piash"]
for friend in friends:
    print("Happy new year",friend)
print("Done") """

#iteration02
""" print("Before")
for num in [9, 41, 12, 3, 74, 15]:
    print(num)
print("After") """

#maxima
""" def maxima(list1):
    is_largest = list1[0]
    for num in list1:
        if num > is_largest:
            is_largest = num
    return is_largest


A = [9, 41, 1042, 12, 3, 74, 111, 711, 2, 98, 15]
m = maxima(A)
print("Maximum number:",m) """

#Counting element number i.e. list length
""" def list_length(list1):
    i = 0
    for num in list1:
        i = i+1
    return i

A = [9, 41, 1042, 12, 3, 74, 111, 711, 2, 98, 15]
length = list_length(A)
print("Number of elements in list:",length) """

#Sum of a list elements
""" def Summation(list1):
    sum = 0
    for num in list1:
        sum = sum+num
    return sum


A = [9, 41, 1042, 12, 3, 74, 111, 711, 2, 98, 15]
sum = Summation(A)
print("Summation of elements in list:",sum) """

#average of element of a list
""" def average(list1):
    i = 0
    sum = 0
    for num in list1:
        i = i+1
        sum = sum+num
    avg = sum/i
    return avg


A = [9, 41, 1042, 12, 3, 74, 111, 711, 2, 98, 15]
a = average(A)
# print("Average of elements in list:",a)
print(f'Average = {a: .2f}') """

#Filtering a loop e.g. value larger than 100
""" def greater(list1):
    for num in list1:
        if num > 100:
            print(num)

A = [9, 41, 1042, 12, 3, 74, 111, 711, 2, 98, 15]
greater(A) """

#searching a value in list using boolean variable
""" def LinearSearch(list1, key):
    found = False
    for num in list1:
        if num == key:
            print("N:",num, " K:",key, " Matched")
            found = True
            break
        print("N:",num, " K:",key, " Not Matched")
    if found == True:
        print("Found in list")
    else:
        print("Not in list")

A = [9, 41, 1042, 12, 3, 74, 111, 711, 2, 98, 15]
number = int(input("Enter a number to search for: "))
LinearSearch(A, number) """

#minima
""" def minima(list1):
    is_smallest = list1[0]
    for num in list1:
        if num < is_smallest:
            is_smallest = num
    return is_smallest


A = [9, 41, 1042, 12, 3, 74, 111, 711, 2, 98, 1, 15]
m = minima(A)
print("Minimum number:",m) """

#minima using None
""" def minima(list1):
    is_smallest = None
    for num in list1:
        if is_smallest is None:
            is_smallest = num
        elif num < is_smallest:
            is_smallest = num
    return is_smallest


A = [9, 41, 1042, 12, 3, 74, 111, 711, 2, 98, 1, 15]
m = minima(A)
print("Minimum number:",m) """

#String
""" str1 = "Hello"
str2 = " There"
str3 = str1+str2
print(str3)

name = input("Enter your name: ")
print("Hello", name)

fruit = "banana"
print(fruit[2])
print(len(fruit)) """

#string index
""" fruit = "banana"
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
print(end="\n")
for l in fruit:
    print(l)

#using for loop
fruit = "banana"
for l in fruit:
    print(l)
print(end="\n") """

#count no of a particular letter in a string
""" word = input("Enter a sentence: ")
l = input("Enter a letter: ")
count = 0
for letter in word:
    if letter == l:
        count = count + 1
# print(l,"is ",count,"times in ",word)
print(f'{l} is {count} times in "{word}"') """

#slicing string
""" s="monty python"
print(s[2:8])
print(s[:8])
print(s[4:])
print(s[::-1]) """

#string concatenation
""" a= "Hello"
b = a + " There"
print(b) """

#in as logical operator
""" fruit="banana"
ans="n" in fruit
print(ans)
ans="l" in fruit
print(ans) """

#string library i.e. methods of string object
""" str = "hello World. what is going on! "
lowercase = str.lower()
print(lowercase)

uppercase = str.upper()
print(uppercase)

print("Zahid".lower())
print("Zahid".upper())
print("zahidul islam".title())

length = len(str)
print(length)

stripped = str.strip() #strips off any whitespace from left or right
print(stripped)
print(len(stripped))

s = str.split() #Returns a list of splitted words
print(s)
print(len(s))

c = str.capitalize()
print(c)

f = str.find('t')
print(f)

f2 = str.find('o')
print(f2)#not okay!

f3 = str.find('z')
print(f3)

r = str.replace("ll", "kk")
print(r)

q = str.startswith('h')#boolean True or False
print(q)

m = str.startswith(' ')
print(m)

t = str.endswith('j')
print(t) """

#parsing and extracting
""" data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ', atpos)
print(sppos)
host = data[atpos+1: sppos]
print(host)

email = "<recommendations@explore.pinterest.com>"
atpos = email.find('@')
print(atpos)
endpos = email.find('>',atpos)
print(endpos)
hostName = email[atpos+1:endpos]
print(hostName) """

#newline
""" hw = "Hello\nWorld"
print(hw)
print(len(hw)) """

#File Reading
""" import os
sep = os.sep
path = os.getcwd()
x = open(f"{path}{sep}files{sep}mbox-short.txt")
print(fhand)
print(type(fhand)) """

#file handling
""" import os
sep = os.sep
path = os.getcwd()
xfile = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in xfile:
    print(line) """

#reading line by line
""" import os
sep = os.sep
path = os.getcwd()
x = open(f"{path}{sep}files{sep}mbox-short.txt")
count = 0
for line in x:
    print("# Line ",count+1,"#")
    print(line)
    count = count+1

print("Line count: ",count) """

#reading word by word
""" import os
separator = os.sep

count = 0
gollum = open(f"files{separator}gollum.txt") # x file handle, not data
bigString = gollum.read() #reading file,converted to strings(one single string!)
# print(bigString)
# print(len(bigString))
# print(bigString[:35])#prints a string

words = bigString.split()
print(words)
print(len(words))
print(words[:5]) """

#searching through a file
""" import os
sep = os.sep
path = os.getcwd()
fhand = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in fhand:
    if line.startswith("From:"):
        print(line) """

#searching through a file(fixed)
""" import os
sep = os.sep
path = os.getcwd()
fhand = open(f"{path}{sep}files{sep}mbox-short.txt")
count=0
for line in fhand:
    line = line.rstrip()#removes a newline
    if line.startswith("From:"):
        count = count+1
        print(line)
print("Total number of mail",count) """

#skipping with continue and not,searching through a file
""" import os
sep = os.sep
path = os.getcwd()
fhand = open(f"{path}{sep}files{sep}mbox-short.txt")
count=0
for line in fhand:
    line = line.rstrip()#removes a newline
    if not line.startswith("From:"):
        continue
    print(line)
    count = count + 1

print("Total number of mail",count) """

#using 'in' operator to select line with 'not'
# not A and not B = not (A or B)
""" import os
sep = os.sep
path = os.getcwd()
fhand = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in fhand:
    line = line.rstrip()#removes a newline
    if not line.startswith("From:") and "@uct.ac.za" not in line: 
        continue
    print(line) """
    
# not A or not B = not (A and B)
""" import os
sep = os.sep
path = os.getcwd()
fhand = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in fhand:
    line = line.rstrip()#removes a newline
    if not line.startswith("From:") or "@uct.ac.za" not in line:
        continue
    print(line) """

#word counting
""" fname = input("Enter the file name: ")
fhand = open(fname) #line by line
print(fhand)
print(type(fhand))
print("\n")
count = 0
characters = fhand.read()#character by character#a single big string
print(type(characters))
print("\n")
print(len(characters))#prints total character number
words = characters.split() #words by words, a list
print(words)#prints a list
print(len(words))#prints words number
for word in words:
    if word == "gollum":
        # print(word)
        count = count+1

print(f"The are {count} gollum in {fname}") """

#search and count a word taken from user
""" fname = input("Enter a file name: ")
fhand = open(fname)#line by line
fcharcters = fhand.read()#character by charcter,a big string
fwords = fcharcters.split()#word by word, list
print(fwords)
print("\n")
key = input("Enter a word to search and count: ")
count = 0
for wd in fwords:
    #if wd.startswith(key):
    if wd == key:
        count = count+1
        # print(key,"-",count)
        print(f"{key} - {count}")

# print(key,"is",count,"times in",fname)
print(f"{key} is {count} times in {fname}") """

#COUNTING LINES
""" fname = input("Enter a file name: ")
fhand = open(fname)#line by line

count = 0
for line in fhand:
    # line = line.rstrip()
    if line.startswith("Subject:"):
        count = count+1
        #print(count,":",line)

print("there is",count,"subject lines in ",fname) """

#counting line with try and except
""" fname = input("Enter a file name: ")
try:
    flines = open(fname)#line by line
except:
    print("Invalid file name. \nenter file name with proper extension.")
    quit()
count = 0
for line in flines:
    #line = line.rstrip()
    if line.startswith("Subject:"):
        count = count+1
        #print(count,":",line)

print("there is",count,"subject lines in ",fname) """

#loop iteration and range function, list operation
""" list1 = list(range(1,39,3))
print(list1)

for num in list1:
    print(num,end=" ")
print(end="\n")

for i in range(len(list1)):
    print(list1[i],end=" ")
print(end="\n\n")

a = list(range(1,19,4))
print("List a:",a)

b = list(range(2,29,5))
print("List b:",b)

c = a + b
print("unsorted a+b:",c)
c = sorted(c)
print("sorted a+b :",c)

d = a and b
print("a and b",d)

e = a or b
print("a or b",e)

print(c[8:4:-1])
print(c[:]) """

#list operation continued
""" list1 = list(range(1,39,3))
print(list1)
list1.reverse()
print(list1)
list1.append(999)
print(list1)
list1.sort()
print(list1)
list1.remove(37)
print(list1)
list1.remove(list1[1])
print(list1)
pos = list1.index(19)
print(pos)
list1.insert(1,42)
print(list1)
list1.pop()
print(list1)
n = list1.count(7)
print(n)
print(9 in list1)
print(10 in list1)
print(19 not in list1)
print(32 not in list1)
list1.sort()
print(list1)
print(max(list1))
print(min(list1))
print(sum(list1))
print(sum(list1)/len(list1))
 """
#average of elements of list
""" numlist = list()
while True:
    inp = input("Enter number: ")
    if inp == "done":
        break
    value = float(inp)
    numlist.append(value)

print(numlist)
average = sum(numlist)/len(numlist)
print("Average: ",average) """

#average using for loop
""" total = 0
count = 0
while True:
    inp = input("Enter number: ")
    if inp == "done":
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total/count
print("Average: ",average) """

#string and list, split()
""" sentence = "well well well gollum i had to say something about but i couldn't"
words = sentence.split()#returns a list of words splitted by space
print(words)
counter = len(words)
print(counter)
for wd in words:
    print(wd, end="|")
print(end="\n\n")
for i in range(len(words)):
    print(words[i],end="|")
print(end="\n") """

#list,split,string example 02
""" line = "kamal;babul;ataur;rahim"
words = line.split(";")
print(words)
for wd in words:
    print(wd) """

# parsing 'mbox-short.txt'
""" import os
path = os.getcwd()
fhand = open(f"{path}{sep}files{sep}mbox-short.txt")
charset = fhand.read()#reading character by character and converting to a single big string
print(charset)
print(len(charset))
words = charset.split()#word by word..returns a list of words
print(words)
print(len(words)) """

#splitting using continue and more
""" import os
path = os.getcwd()
fhand = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):
        continue
    words = line.split()
    print(words)
    # print(words[1]) """

#parsing single line
""" line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
words = line.split()
print(words)
email = words[1]
print(email)
parts = email.split("@")
print(parts)
hostname = parts[1]
print(hostname) """

#printing days from email address
""" import os
sep = os.sep
path = os.getcwd()
fhand = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    # print(wds)
    #gurdian
    if len(wds) < 3 or wds[0] != 'From':#order should be correct
        continue
    print(wds[2]) """

#dictionaries, into
""" purse = dict()
purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75
print(purse)
print(purse["money"])
purse["candy"] = purse["candy"]+2
print(purse)
print(purse["tissues"]) """

#frequency, histogram
""" counts = dict()
names = ["thror", "thrain", "thorin","nori", "dori", "fili", "kili", "balin", "dawlin", "thorin", "kili", "fili", "thorin","thrain", "thror","balin","thorin"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts) """

#count equivalent get() method
""" counts = dict()
names = ["thror", "thrain", "thorin","nori", "dori", "fili", "kili", "balin", "dawlin", "thorin", "kili", "fili", "thorin","thrain", "thror","balin","thorin"]
for name in names:
    #first method
    if name in counts:
        x = counts[name]
    else:
        x = 0
    #equivalent line
    # x = counts.get(name, 0)
print(x) """

#alternative histogram with get() dictionary method
""" counts = dict() #dictionary constructor
names = ["thror", "thrain", "thorin","nori", "dori", "fili", "kili", "balin", "dawlin", "thorin", "kili", "fili", "thorin","thrain", "thror","balin","thorin"]
for name in names:
    counts[name] = counts.get(name, 0) + 1
    #dict.get(key, default value) is a dictionary method to add element in dictionary
print(counts) """

#countimng words in textfile
""" import os 
sep = os.sep
path = os.getcwd()
file_hand = open(f"{path}{sep}files{sep}mbox-short.txt")
file_char = file_hand.read()
file_words = file_char.split()
counts = dict()
for word in file_words:
    counts[word] = counts.get(word, 0) + 1
print(counts) """

#counting pattern using get
""" counts = dict()
line = input("Enter a line of text: ")
words = line.split() # returns list of words
print("words: ",words)
print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts: ",counts) """

# counting 'letter'/character frequency in a sentence
""" counts = dict()
charset = input('Enter a string > ')
for ch in charset:
    counts[ch]=counts.get(ch, 0) + 1
print(counts) """

#counting words
""" counts = dict()
fname = input("Enter a file name: ")
line = open(fname)
charset = line.read()
words = charset.split()
print("words: ",words)
print(end="\n")
print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts: ",counts)
print(end="\n")

for key in counts.keys():
    print(key, counts[key]) """

#retrieving lists of keys, values and items
# dictionary.keys()
# dictionary.values()
# dictionary.items()
""" hobbit = {"gollum":3, "thorin":2, "gandalf":4, "bilbo":5, "smaug":3}
hobbit_list = list(hobbit)
print(hobbit_list)

print(hobbit.keys()) #LIST of keys
print(hobbit.values()) #LIST of values
print(hobbit.items()) #TUPLE """

#iterating within tuple
""" hobbit = {"gollum":3, "thorin":2, "gandalf":4, "bilbo":5, "smaug":3}
for key, value in hobbit.items():
    print(f"{key}: {value}") """

# counting highest frequency of a word
# dr.chuck's version
""" name = input('Enter a filename: ')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount) """

# counting highest frequency of a word
# my second version
""" fname = input("Enter a file name with extension> ")
fhand = open(fname)
big_string = fhand.read()
word_list = big_string.split()

counts = dict()

for word in word_list:
    counts[word] = counts.get(word, 0) + 1
# print(counts)

big_word = None
big_count = None

for word, count in counts.items():
    if big_word is None or count > big_count:
        big_word = word
        big_count = count

print(f"Maximum occuring word is - {big_word} - {big_count} times") """

# my first version
""" counts = dict()
fname = input("Enter a file name: ")
try:
    fhand = open(fname)#line by line
except:
    print("Invalid file name. \nenter file name with proper extension.")
    quit()

charset = fhand.read()
words = charset.split()
print("words: ",words)
print("Counting...")
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("Counts: ",counts)
print(end="\n")

max_frequency = None
max_word = None

for wd, frequency in counts.items():
    if max_frequency is None or frequency > max_frequency:
        max_word = wd
        max_frequency = frequency

print(max_word, max_frequency) """

# creating a dictionary from file
# finding most common word
""" fname = input("Enter a filename: ")
if len(fname) < 1:
    fname = "clown.txt"

try:
    hand = open(fname)#line by line
except:
    print("Invalid file name. \nenter file name with proper extension.")
    quit()


di = dict()

for line in hand:
    line = line.rstrip()
    words = line.split()
    #print(words)
    for wd in words:
    #idiom: retrieve/create/update counter
        di[wd] = di.get(wd, 0) + 1
#print(di)

max_word = None
max_frequency = None
for key, value in di.items():
    #print(key,value)
    if max_frequency is None or value > max_frequency:
        max_word = key
        max_frequency = value
print(end="\n")
print(max_word, max_frequency) """

# TUPLES, Introduction
""" t = tuple()
print(type(t))

x = (1,4,9)
print(x)
print("max:",max(x))
print("min:",min(x))
print(x[1])

(x, y) = (4, 9)
print(x)
print(y)
print(x, y)
print((x, y))

di = dict()
di["gollum"] = 2
di["thorin"] = 4
di["bilbo"] = 5
di["gandalf"] = 4
di["balin"] = 3
di["smaug"] = 3
print(di)
for (k,v) in di.items():
    print(k,v)
t = di.items()#list of tuples
print(t)
t2 = tuple(t)#converting list to tuples
print(t2) """

# #comparing tuples
""" t1 = (0,1,2) < (5,1,2)
print(t1)
t2 = (6,1,2) < (5,1,2)
print(t2)
t3 = ("Jewel","Nazmul") > ("Nazmul","Jewel")
print(t3)
t4 = ("Zahid","Nazmul") > ("Nazmul","Jewel")
print(t4) """

#sorting list of tuples, sorted() function
# sort by key
""" d = {"a":10,"z":26,"x":24,"y":25,"b":2,"c":22}
t = d.items()
print(t)
s = sorted(t)
print(s)

for k,v in s:
    print(k,v) """

#now, writing a code to sort by values instead of keys
""" d = {"a":10,"z":26,"x":24,"y":25,"b":2,"c":22}
print(d)
li = list()
for (k,v) in d.items():
    li.append((v,k))
print(li)
li = sorted(li, reverse=True)
print(li)
li = sorted(li)
print(li)
L = list()

for (k,v) in li:
    L.append((v,k))
print(L)
L = dict(L)
print(L) """

#top 10 most common word
# classic way
""" fname = input("Enter a file name:")
try:
    fhand = open(fname)
except:
    print("Invalid file name. \nenter correct file name with proper extension.")
    quit()

li = list()
di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for wd in words:
        di[wd] = di.get(wd, 0) + 1
print(di)

for (k, v) in di.items():
    new_tup = (v, k)
    li.append(new_tup)
li_new = sorted(li,reverse=True)
print(li_new)

for (val, key) in li_new[:10]:
    print(key, val) """

#top 10 most common word
#modern way, list comprehension
""" fname = input("Enter a file name> ")
try:
    fhand = open(fname)
except:
    print("Invalid file name. \nenter correct file name with proper extension.")
    quit()

li = list()
di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for wd in words:
        di[wd] = di.get(wd, 0) + 1
print(di)

#lambda
#list comprehension
#dynamic list
new_list = sorted([(v,k) for k,v in di.items()],reverse=True)
print(new_list)

for v, k in new_list[0:10]:
    print(k, v) """

#FIVE most common word
""" fname = input("Enter a file name> ")
if len(fname) < 1:
    fname = "clown.txt"

try:
    fhand = open(fname)
except:
    print("Invalid file name. \nenter correct file name with proper extension.")
    quit()

li = list()
di = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for wd in words:
        di[wd] = di.get(wd, 0) + 1
#print(di)
#x = di.items() # list of tuples
#print(x)

#list comprehension
#dynamic list
new_list = sorted([(v,k) for k,v in di.items()],reverse=True)
#print(new_list)

for v, k in new_list[0:5]:
    print(k, v) """

# # top ten occurring words in a text
""" fname = input("Enter file name> ")
fhand = open(fname)
big_string = fhand.read()
words = big_string.split()

L = list()
D = dict()

for word in words:
    D[word] = D.get(word, 0) + 1

new_list = sorted([(v,k) for (k,v) in D.items()], reverse=True)

for v,k in new_list[:10]:
    print(k,v) """

#REGULAR EXPERSION
#using re.search() like find()
# find() vs re.search()
# using find
""" import os
sep = os.sep
path = os.getcwd()
hand = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if line.find("From:") >= 0:
        print(line)
print()
# using re
import re
import os
sep = os.sep
hand = open(f"files{sep}mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line) """

#using re.search() like startswith()
#startswith("expression") ~ re.search("^expression")
# using startwith
""" import os
sep = os.sep
path = os.getcwd()
hand = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

print()
# using re.search
import re
import os
sep = os.sep
path = os.getcwd()
hand = open(f"{path}{sep}files{sep}mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line) """

#matchinga and extracting data
#using re.findall() instead of re.search()
""" import re
x = "My 2 favourite number are 19 and 42 "
y = re.findall("[0-9]+",x)
print(y)
# z = re.findall("[aeiou]",x)
z = re.findall("[aeiou]+",x)
print(z)
w = re.findall("[ab]+",x)
print(w)
expression = "i am 28. I am preparing for my first job. i aspire to find a job in 2020. I want to fly to america in 2022. bt then i will be 30. i need score 330+ in GRE"
a = re.findall("[0-9]+",expression)
print(a) """

# # #greedy matching
""" import re

x = "From: Using the : character"
y = re.findall("^F.+:",x)
print(y)
z = "My name: Zahidul Islam Jewel: I am Bangladeshi"
w = re.findall("^M.+:",z)
print(w) """

# #non-greedy matching
""" import re
x = "From: Using the : character"
y = re.findall("^F.+?:",x)
print(y) """

# # fine tuning string extraction
""" import re
x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("\S+@\S+",x)
print(y) """

# # #  finding emails
""" import re

fname = input("Enter file name> ")
fhand = open(fname)
big_string = fhand.read()
x = re.findall("\S+@\S+", big_string)
print(x)
print(len(x)) """

# a better version
# this will extract email only if there is a 'From' in the beginning
""" import re

x = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("^From (\S+@\S+)",x)
print(y) """

# 01 parsing data using string and slicing
""" data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1: sppos]
print(host) """

# 02 parsing data using double split()
""" data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
words = data.split()
print(words)
email = words[1]
print(email)
pieces = email.split("@")
print(pieces)
print(pieces[1]) """

# 03 parsing data using regular expression
""" import re
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# y = re.findall("@([^ ]*)",data)
y = re.findall("@([^ ]+)", data)
print(y) """

# 04 fine tuned version
""" import re
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("^From .*@([^ ]*)",data)
print(y) """

# span confidence :/
""" import re
import os
path = os.getcwd()
sep = os.sep
hand = open(f"{path}{sep}files{sep}mbox-short.txt")
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)",line)
    if len(stuff) !=1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print("List:",numlist)
print("Maximum:",max(numlist)) """

# escape character
# extracting real dollar
""" import re
x = "We just received $10 for cookies."
y = re.findall("\$[0-9.]+",x)
print(y) """

# NETWORK PROGRAMS
""" import socket
mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80)) """

# An HTTP request in python
""" import socket

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating a socket
mysock.connect(("data.pr4e.org", 80)) #connect the socket to data.pr4e.org domain
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n".encode() # converts unicode to utf-8
mysock.send(cmd)

while True:
    data = mysock.recv(512) #receives upto 512 characters at a time
    if len(data) < 1:
        break
    print(data.decode()) # converting to unicode again
mysock.close() #closing connection """

# bout character and strings...
# ord() i.e. ordinal function
""" print(ord("0"))
print(ord("A"))
print(ord("a"))
print(ord("\n"))
print(ord("&")) """

# using urllib in python
# alternative of socket()
# reading webpages
""" import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt") # returns an object alike file
# fhand can be treated like a file
for line in fhand:
    print(line.decode().strip()) """

# creating a dictionary of file using urllib
# treating webpage like a file
""" import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
di = dict()
for line in fhand:
    line = line.decode().strip()
    words = line.split()
    for wd in words:
        di[wd] = di.get(wd, 0) + 1
print(di) """

# reading a webpages
""" import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen("http://dr-chuck.com/page1.htm")
for line in fhand:
    print(line.decode().strip()) """

# WEB SCRAPPING
# extracting anchor tags i.e. href
""" import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter> ") # http://dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
print(type(soup))

#retrieve all of the anchor tags
tags = soup("a")
# print(type(tags))
print(tags)
print(end="\n")

for tag in tags:
    print(tag.get("href",None)) """

# same code with ssl certificate
""" import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter> ") #http://www.dr-chuck.com/
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href",None)) """

# WEB SERVICES
# XML 01
""" import xml.etree.ElementTree as et
data ='''
<person>
    <name>Zahidul Islam</name>
    <phone type="int">01729327789</phone>
    <email hide="yes"/>
</person>
'''
tree = et.fromstring(data)
print("Name:",  tree.find("name").text)
print("Phone: ", tree.find("phone").text)

print("Attr: ", tree.find("phone").get("type"))
print("Attr: ", tree.find("email").get("hide")) """

# XML 02
# parsing xml
""" import xml.etree.ElementTree as et

data ='''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Zahid</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Jewel</name>
        </user>
        <user x="4">
            <id>004</id>
            <name>Tonmoy</name>
        </user>
    </users>
</stuff>
'''
stuff = et.fromstring(data)
li = stuff.findall("users/user")
# li = stuff.findall("users/user/name")
# print(li)
print("User count:", len(li))
print(end="\n")
for item in li:
    print("Name: ",item.find("name").text)
    print("Id: ",item.find("id").text)
    print("Attribute: ",item.get("x"))
    print(end="\n") """

# JSON
# Java Script Object Notation
# #Example 01
""" import json
data = '''{
    "name" : "Zahid",
    "Phone" : {
        "type": "int",
        "number": "01729327784"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data) #info is a dictionary
print(info)
print("Name: ", info["name"])
print("Phone Type: ", info["Phone"]["type"])
print("Phone Number: ", info["Phone"]["number"])
print("Hide: ", info["email"]["hide"]) """

# JSON Example 02
""" import json
data = '''
[
    {
        "id":"001",
        "x":"2",
        "name":"chuck"
    },
    {
        "id":"009",
        "x":"7",
        "name":"Zahid"
    }

]
'''
# list of two dictionaries
info = json.loads(data) # info is a list of dictionaries
print("User Count: ",len(info))
print(info)
for item in info:
    print("Name: ", item["name"])
    print("Id: ", item["id"])
    print("Attribute: ", item["x"])
    print(end="\n") """


# WORKING WITH API
# google map's api
# retrieving lat,lon from address
# Check it Later
# geocode, geojson
""" import urllib.request, urllib.parse, urllib.error
import json
import ssl
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location) """
# Twitter API
# Skipped for now
# must check later


# OOPS
# Object Oriented Programming
# #creating first class
""" class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print("so far", self.x)


an = PartyAnimal()

an.party()
an.party()
an.party()
# PartyAnimal.party(an) """

#type() and dir() function
""" x = list()
print(type(x))
print(dir(x))

y = dict()
print(type(y))
print(dir(y))

z = set()
# print(type(z))
# print(dir(z))

w = tuple()
print(type(w))
print(dir(w))

s = "Hello World"
print(type(s))
print(dir(s)) """

# string object
""" s = " hello There " #s is a object of class string
print(s)

print(s.split())
x = s.strip()
print(x)
print(x.capitalize())
print(s.lower())
print(s.upper())
print(s.index("T"))
print(s.find("r"))
print(s.replace("T"," "))
print(s.isascii())
print(s.isdigit()) """

# object life cycle
# constructor
# destructor
# Example 01
""" class PartyAnimal:
    x = 0

    def __init__(self):
        print("I am constructed")

    def party(self):
        self.x = self.x + 1
        print("so far",self.x)

    def __del__(self):
        print("I am destructed",self.x)

an = PartyAnimal() #constructor
# print(type(an))
# print(dir(an))
an.party()
an.party()
an = 42 #destruction
print("an contains",an) """

# #Constructor Example 02
""" class PartyAnimal:
    x = 0
    name = ""

    def __init__(self, z): # called only when object is created
        self.name = z
        print(self.name,"constructed")

    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)


s = PartyAnimal("Sally") #object creation of class PartyAnimal
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()
j.party()
s.party() """

# inheritance example
""" class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name,"constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name,"party count",self.x)

class FootballFan(PartyAnimal): #inheriting PartyAnimal Class
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"points",self.points)


s = PartyAnimal("Sally")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown() """

#DATABASES
#SQL
#emaildb
#creating a email database from file
""" import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close() """

#retrieving friendlist from twitter using twitter api
#skipped for now
#must check later
#very impressive
#creating twitter database