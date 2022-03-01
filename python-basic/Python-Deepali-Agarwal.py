# elementary examples
"""
x = 8+9
print(x)
print(id(x))
y = 8/3
print(y)
z = 8//3
print(z)
print(2**3)
m = 4*"abc "
print(m)
print(type(m))
"""

# lists
# mutable
"""
l=list()#empty list
l1=[]#empty list
li = [4, 9, 2 , 3, 5, 7, 8, 1, 6]
print(li)
print(len(li))
print(li[2:5])
print(li[::-1])
print(sum(li))
print(sum(li[2:7]))
li2 = [11,13,17,19,23,29]
c = [li, li2]
print(c)
d = li + li2
print(d)
print(sorted(d))
print(sorted(d, reverse=True))
d.insert(4, 1001)
print(d)
print(sorted(d))
d.remove(1001)#value
print(d)
d.append(77)
print(d)
d.pop()#of last index
print(d)
d.pop(0)#index
print(d)
del d[2:7]
print(d)
d.extend([44, 77, 89])
print(d)
print(max(d))
print(min(d))
print(max(d)-min(d))
d.sort()
print(d)
print(dir(d))
"""

# tuples
# immutable
"""
import sys

d = tuple()#empty tuple
e = ()#empty tuple
t = (4, 9, 2, 3, 5, 7, 8, 1, 6)
print(t)
print(len(t))
print(sum(t))
print(t[1])
print(t[1:4])
print(dir(t))
x = t.index(4)
print(x)
print(sys.getsizeof(t))#sys module
a = tuple("Zahid")
print(a)
b = tuple([4, 9, 2, 3, 5])#converting to tuple
print(b)
f = (b, t)
print(f)
g = b+t
print(g)
print(t[::-1])
del t
print(t)
"""

# sets
# mutable
"""
a = set()#empty set
print(a)

c = {1, 2, 3, 7, 5, "numberphile"}
print(c)
b = set("Jewel")
print(b)

c.add(11)
print(c)
c.update([14])#input as list,one or more
print(c)
c.update([12,24,21])
print(c)
c.remove(24)
print(c)
c.pop()
print(c)
c.discard("numberphile")
print(c)
c.pop()
print(c)
#c.clear()
#print(c)
f = c.copy()
print(f)
g = {4, 9, 2, 3, 8,13}

#frozen set,makes set immutable
h = frozenset(g)#immutable
print(g)
print(h)

i = f and g
print(i)

u = f or g
print(u)
"""

# dictionaries
# mutable
# key:value pairs
"""
di = dict()#empty dict
d = {}#empty dict

b = {1:"Kamal", 2:"Ahmed", 3:"Akash", 4:"Jadav"}
print(b)

f = {"Name":"Jewel","Age": 28, "Profession":"Student"}
print(f)

f1 = {1:[1, 2, 4], 2:"Hello"}
print(f1)

f2 = dict([(1,4),(2,7),(3,9)])#paired tuple as input
print(f2)

f3 = {1:"Hello", 2:60, 3:{5:"Zahid", 6:70}}
print(f3)

b[5] = "Malar"#adding values in dictionary
print(b)

b[1] = "Nithiya"#updating dictionary
print(b)

f["Hobby"] = "Trekking"
print(f)

print(b[4])
print(f["Hobby"])

print(b.get(1))
print(f.get("Name"))

del b[1]
print(b)

#del f3[3]
#print(f3)

print(f3[3][6])
print(f3[3][5])
del f3[3][6]
print(f3)

b.pop(2)
print(b)

b.popitem()
print(b)

b.clear()
print(b)

j = f.copy()
print(j)

print(j.keys())#retuns a list of keys
print(j.items())#returns list of (key,value) tuple
"""

# user defined program
"""
num1 = float(input("Enter number 1- "))
num2 = float(input("Enter number 2- "))
sum = num1 + num2
print("Summation: ",sum,end="\n")
print(type(sum))

a, b, c = input("Enter the numbers: ").split()
#print("a = ", a)
#print("b = ", b)
#print("c = ", c)
print("value of a is {} \nvalue of b is {} \nvalue of c is {}".format(a, b, c))
summation = int(a) + int(b) + int(c)
print("Summation: ", summation)

"""

# decision making programs
# if-else
# if-elif-else
# nested if-else
"""
a1, b1 = input("Enter two numbers: ").split()
a = int(a1)
b = int(b1)

if a > b:
    print("{} is greater than {}".format(a, b))
elif a == b:
    print("{} is equal to {}".format(a, b))
else:
    print("{} is less than {}".format(a, b))
"""

# OPERATORS IN PYTHON
# arithmetic operator (+,-,*,/,%,//,**)
# relational operator (>, >=, ==, !=, <=, <)
# logical operator (and, or, not)
# bitwise operator (&, !, ~, ^, >>, <<)
# assignment operator (=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
##special operator (identity, membership) BELOW
# identity operator (is, is not) #comparison
# membership operator (in, not in)
"""
a = 10
b = 10.0
if a is b:
    print("True")
else:
    print("False")

c = 10
d = 10.0
if a is not b:
    print("True")
else:
    print("False")


li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
if 4 in li:
    print("True")
else:
    print("False")

if 10 not in li:
    print("True")
else:
    print("False")
"""

# inbuilt operator
"""
import operator
x = 24
y = 8
print(operator.add(x,y))
print(operator.sub(x,y))
print(operator.mul(x,y))
print(operator.truediv(x,y))
print(operator.floordiv(x,y))
print(operator.pow(x,y))
print(operator.mod(x,y))
print(operator.lt(x,y))
print(operator.le(x,y))
print(operator.gt(x,y))
print(operator.ge(x,y))
print(operator.eq(x,y))
print(operator.ne(x,y))
"""

# LOOPS IN PYTHON

# FOR LOOP
"""
for num in range(3, 20, 3):
    print(num, end=" ")
print(end="\n")
print(end="\n")

for letter in "Zahidul Islam Jewel":
    print(letter, end="")
print(end="\n")

li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
for num in li:
    print(num,end=" ")
print(end="\n")

di = {1:"Zahid", 2:"Islam", 3:"Jewel"}
for i in di:
    print(i, di[i])  
    
#factorial of a number
n = int(input("Enter an integer - "))
f = 1
for i in range(1, n+1):
    f=f*i

print("Factorial of {} = {}".format(n,f))


#checking prime or not
counter = 0
n = int(input("Enter an integer - "))
for i in range(2,(n+1)//2):
    if n%i == 0:
        counter = counter + 1
        break
if counter ==0 :
    print("Prime!")
else:
    print("Not a Prime!")
"""
# WHILE LOOP
# while else loop
# pass statement
"""
i = 0
while True:
    print(i, end=" ")
    i = i + 1
    if i == 10:
        break


#factorial of a number using while
n = int(input("Enter an integer - "))
f = 1
j = 1
while j <= n:
    f = f*j
    j = j+1

print("Factorial of {} = {}".format(n,f))
"""

# while else loo
"""
i = 3
while i < 6:
    print(i, end=" ")
    i = i + 1
else:
    print("\nElse!")


m = 1
while m < 10:
    print(m, end=" ")
    m = m+1
    if m == 20:
        break
else:
    print("\nelse executed!")

#else is an integrated part of while
#if break executed..then the control...
#...comes out of whole while-else loop

#pass statement
for i in range(0, 20, 5):
    if i == 10:
        pass
    else:
        print(i)
"""

# FUNCTION
"""
ex-01
def add(x, y):#function definition
    return x+y

sum = add(4, 7)#function calling i.e. invoking..by passing arguments
print(sum)

#ex-02
def evenOdd(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")


n = int(input("Enter number > "))
evenOdd(n)


#ex-03
#factorial using function
def fact(n):
    f = 1
    j = 1
    while j <= n:
        f = f*j
        j = j+1
    return f


num = int(input("Enter an integer - "))
result = fact(num)
print("Factorial of {} = {}".format(num,result))
"""

# SWITCH-CASE i.e. switcher
# not switch-case in python
# dictionary mapping

# ex-1
"""
def fun(x):
    switcher = {
        0: "zero",
        1: "One",
        2: "Two",
        3: "Three",#last comma is important
    }

    return switcher.get(x, "option not available!")

option = int(input("Enter an option > "))
result = fun(option)
print(result)


#ex-2...alt.
def a():
    return "Hello"
def b():
    return "Bye"
def fun(x):
    switcher = {
        0: a(),
        1: b(),
        2: "Two",
        3: "Three",#last comma is important
    }

    return switcher.get(x, "option not available!")


option = int(input("Enter an option > "))
result = fun(option)
print(result)
"""

# inbuilt function for precision handling
"""
import math

d = 5.81234
print(math.trunc(d))
print(math.ceil(d))
print(math.floor(d))
print(round(d, 3))

f = 9.83217
print(round(f, 4))
print("%.3f" %d)

print("{0:.2f}".format(d))
"""

# map(), lambda(), filter() function
# lambda()
"""
#def add(x, y):
#    return x+y

#lambda-01
c = lambda a, b: a+b
#sum = c(4, 7)
#print(sum)
print(c(8,9))

s = lambda p, q, r: p+r-r*p
print(s(2, 3, 4))
"""

# map function()

# ex-01
"""
def square(x):
    return x*x

li = [4, 9, 2, 3, 5, 7]

t = map(square, li)
#print(list(t))
#print(set(t))
print(tuple(t))
"""
# ex-02...alt
"""
d = lambda x: x*x

li = [4, 9, 2, 3, 5, 7]
t = map(d, li)
print(list(t))
#print(set(t))
#print(tuple(t))
"""

# multiplying two list using map
"""
li = [4, 9, 2, 3, 5, 7]
li2 = [1, 3, 5, 7, 9, 11]

def mul(x, y):
    return x*y


a = map(mul, li, li2)
print(list(a))
"""

# filter function
"""

def evenSort(num):
    if num%2 == 0:
        return True
    else:
        return False
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]

q = filter(evenSort, li)
print(list(q))
"""

# MODULES
# a module defines functions,classes,variables

# math module
# creating own module
"""
import math

# from math import sqrt
import arithmetic # own math module

print(arithmetic.add(5, 7))
print(arithmetic.sub(5, 7))
print(arithmetic.mul(5, 7))
print(arithmetic.div(5, 7))
print(arithmetic.mod(5, 7))

"""

# calendar module
"""
from calendar import *
from datetime import date

c = calendar(2018)
#print(c)

m = month(2019, 11)
#print(m)

l = isleap(2019)
print(l)

r = leapdays(2000, 2022)
print(r)

d = monthrange(2019, 11)
print(d) #(4, 30) 1st day - Friday, 30 days

e = weekday(2019, 11, 17)
print(e)

#age calculator
y = int(input("Enter birth year > "))
m = int(input("Enter birth month > "))
d = int(input("Enter birth day > "))

bd = date(y, m, d)
#print(bd)

cd = date.today()
#print(cd)

age = ((cd - bd).days)/365
print(age,"Years")
"""

# pyautogui module
# moveTo()
# click()
# dragTo()
# position()
"""
import pyautogui, time

time.sleep(2)
#934 883

#print(pyautogui.position())
pyautogui.moveTo(417, 327,duration=5)
#pyautogui.click(417, 327)
pyautogui.dragTo(934, 883,duration=5)
"""

# text editing using pyautogui
"""
import pyautogui as df
import time
#(x=1294, y=592)
time.sleep(2)
print(df.position())
df.moveTo(1294, 592, duration=2)
df.click(1294, 592)
df.typewrite("pyautogui is fun!")
"""

# opening url
"""
import pyautogui as df
import time
#294, 56
time.sleep(2)
print(df.position())
df.moveTo(294, 56, duration=2)
df.click(294, 56)
df.typewrite("https://www.prothomalo.com")
df.typewrite(["enter"])
"""

# prompt, confirms, password, alert box
"""
import pyautogui as df
#df.prompt("Enter your name > ")
#df.confirm("Submit > ")
#df.alert("Error 404!")
df.screenshot("a.jpg")
df.password("Enter password > ")
"""

# pyqrcode module
"""
import pyqrcode as df
a = df.create("http://www.prothomalo.com")
a.svg("s.svg")
a.eps("t.eps")
#a.png("u.png")
"""

#xlswriter module
#used to create .xlsx file

""" import os
import xlsxwriter as df
sep = os.sep
path = os.getcwd()
w = df.Workbook(f"{path}{sep}files{sep}newfile.xlsx")
w1 = w.add_worksheet("myworksheet")
w.close() """