#variables

""" var = 10
print(var)
var = 4.5
print(var)
var = "Hello"
print(var)

print(format(8/9,".3f"))
print(format("Hello", "<40"))
print(format("Hello", ">40"))
print(format("Hello", "^"))

var = 90
print(var)
_var = 90
print(_var)
print(help("keywords"))
print("Hello \nWelcome to my world!") """

#implicit line joining methods
"""
print("Hello"
      "Welcome")

print("Hello\
welcome")
"""

#arithmetic operator
"""

x = 12
y = 8
print(-x)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)

print(end="\n\n")
"""

#logical operator
"""
print(x==y)
print(x!=y)
print(x>y)
print(x>=y)
print(x<y)
print(x<=y)
"""
#membership operator
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
print(5 in li)
print(5 not in li)
print(11 in li)
print(11 not in li)
"""
#boolean operator
"""
print(5 < 6 and 4 == 4)
print(5 > 6 and 5 == 5)
print(5 < 6 or 5 == 5)
print(6 > 7 and 6 == 6)
print(not 10 > 5)
"""
#precedence and associativity
"""
print(2+7*5)
print((2+7)*5)
print(2+5-1)
print(2**3**4)
print((2**3)**4)
"""

#input and output function
"""
name = input("Enter your name > ")
print("Hello", name)
print(f"Hello {name}")
print('''Hello,how are you?
are you planning to go to bandarban?''')

"""
#control statement
# sequential control
"""
print("Hello")
print("welcome")
print("welcome to bandarban")
"""

# selection control
"""
var = int(input("enter an integer > "))
if var < 10:
      print("less than 10")
else:
      print("greater than or equal to 10")
"""
# iterative control
"""
var = 0
while var < 10:
      print(var, end=" ")
      var = var + 1
"""

#if-else condition
"""
marks = int(input("Enter your marks in math > "))
if marks >= 33 and marks <=100:
      print("You passed")
elif marks < 33 and marks >=0:
      print("Sorry! you failed!")
else:
      print("invalid input!")
print("thank you")
"""
# nested if statements, if-elif-else

#nested if-else
"""
name = "Jewel"
school = "BAHS"

if school == "BAHS":
      if name == "Jewel":
            print("school True, name True")
      else:
            print("school True, name False")
else:
      print("school False, name False")
"""

#if-elif-else
"""
x = 20
y = 45
z = 23

if x>y :
      print(f"{x} is greater than {y}")
elif y>z :
      print(f"{y} is greater than {x} and {z}")
else:
      print(f"{z} is the greatest")
"""

# for loop
"""
# ex-01
for letter in "Python":
      print(letter, end=" ")
print(end="\n")
# ex-02
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
for num in li:
      print(num, end=" ")
"""

#while loop
#indefinite loop
#finite loop

"""
count = 1
while count <= 5:
    print(count)
    count = count + 1
print("good bye")
"""

#loop controls break and continue
# ex-01
# using break
"""
i = 0
while True:
    if i > 20:
        break
    if i % 4 != 0:
        print(i, end=" ")
    i = i + 1
print("Done")
"""

# ex-02
# using break and continue
"""
i = 0
while True:
    i = i + 1
    if i > 20:
        break
    if i % 4 == 0:
        continue
    else:
        print(i, end=" ") 
print("Done")
"""

# ex-03
# using break and continue
"""
di = dict()
name = "Zahidul Islam Jewel"
for letter in name:
    if letter in di:
        continue
    if letter in ['a', 'e', 'i', 'o', 'u']:
        print(letter, end=" ")
        di[letter] = di.get(letter, 0) + 1
    
print(end="\n\n")
print(di)
print("Done")
"""

#list
"""
animals = ["dog", "cat", "snake", "rat"]
print(animals)
print(animals[2])
print(animals[0:2])
print(animals[::-1])
print(sorted(animals))
#nested list
li = [[4, 9, 2], [3, 5, 7], [8, 1,6]]
print(li)
print(li[0])
print(li[0][1])
print(li[2][2])

li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
for num in li:
      print(num, end=" ")
"""
#list operations
#replace
#insert
#sort
#delete
#append
#reverse
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
print(len(li))
#li[2] = 33
print(li)
li.insert(0, 11)
print(li)
li.sort()
print(li)
li.reverse()
print(li)
li.remove(11)
print(li)
li.append(12)
print(li)
li.sort()
print(li)
print(li.count(1))
li2 = li.copy()
print(li2)
del li[9]
print(li)
li.clear()
print(li)
del li
print(li)
"""

#program to remove duplicates from a list
"""
li = [4, 9, 4, 7, 2,2, 3, 5, 7, 8, 1, 6, 7, 11, 8, 19, 11, 23, 29, 22, 6, 41, 1]

print(li)
li2 = list()
for num in li:
    if num in li2:
        continue
    else:
        li2.append(num)
print(li2)
"""

#python tuples
"""
t = (4, 9, 2, 3, 5, 7, 8, 1, 6)
print(t)
print(t.count(4))
print(t.index(5))

#nested tuple
t2 = ((1, 2), (3, 4), (5, 6))
print(t2)
print(t2[0])
print(t2[1][1])

t3 = tuple() #empty tuple
"""

#sequences
"""
s = "comprehension"
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
t = (4, 9, 2, 3, 5, 7, 8, 1, 6)

print(len(s))
print(len(li))
print(len(t))

print(s[3])
print(li[3])
print(t[3])

print(s[:3])
print(li[:3])
print(t[:3])

print(s.count('e'))
print(li.count(2))
print(t.count(3))

print(s.index('i'))
print(li.index(3))
print(t.index(1))

print('m' in s)
print('k' not in s)
print('c' not in s)

s1 = "Hi"
s2 = " Hello"
s3 = s1 + s2
print(s3)

lx = [4, 9, 2]
ly = [3, 5, 7]
l = lx + ly
print(l)

tx = (4, 9, 2)
ty = (3, 5, 7)
t2 = tx + ty
print(t2)

print(min(li))
print(max(t))
print(sum(li))
print(sum(t))
"""
#list assignment and list copy
"""
li = list(range(10))
print(li)
li2 = li #assigned
print(li2)

li3 = li.copy()
#li3 = list(li) #same operation
print(li3)

li.insert(0,11)
print(li)
print(li2)
print(li3)

l = [x for x in range(5)]
print(l)
m = [x**2 for x in [1, 3, 5, 7]]
print(m)
"""

#range function
"""
for x in range(1,11):
    print(x, end=" ")
"""
#functions
"""
def avg(a, b, c):
    return (a+b+c)/3

average = avg(4, 9, 2)
print(average)
"""

#function types,actual and formal parameters
"""
def evenOdd(num):
    if num%2 == 0:
        print("Even")
    else:
        print("Odd")


evenOdd(17)
evenOdd(24)
"""
#keyword and default arguments
# keyword argument
"""
def avg(a , b, c):
    return (a+b+c)/3


average = avg(c=4, a=5, b=3)
print(average)
"""

# default argument
"""
def avg(a , b, c=0):
    return (a+b+c)/3

x = int(input("x > "))
y = int(input("y > "))
#z = int(input("z > "))

average = avg(x, y)
print(average)
"""

#local and global variables

# ex-01
"""
def func1():
    n = 5
    print(f"n = {n}")


def func2():
    n = 10
    print(f"n = {n}")
    func1()


func2()
"""

# ex-02
"""
n = 10 #global variable

def func1():
    print(f"n = {n}")

def func2():
    n = 20 #local to this function
    print(f"n = {n}")
    func1()

func2()
"""

#updating global variable
"""
var = 10
def func1():
    global var
    var = var + 1 #while incrementing treated as local variable
    print(f"var = {var}")

func1()
"""

# anonymous function and lambda function
"""
sum = lambda x, y: x + y
print(f"Sum is {sum(10, 20)}")
"""

#variable length argument
"""
def func1(*mylist):
    for num in mylist:
        print(num, end=" ")
    print(end="\n")
    return


func1(10, 20, 30)
func1(10, 20)
func1(10, 20, 30, 40)
"""

#numeric functions
"""
import math

print(abs(-5))
print(round(5.24961, 3))
print(math.ceil(5.2))
print(math.ceil(-5.2))
print(math.floor(5.2))
print(math.trunc(5.2))
print(math.factorial(5))
print(math.fabs(-6))
print(math.pow(6, 2))
print(math.sqrt(6))
print(math.sin(3.141592653*.166))
print(math.log(10, 10))
print(math.pi)
print(math.e)
print(math.e)
print(math.exp(4))
print(math.log2(4))
print(max(4, 9, 2))
print(min(4, 9, 2))

li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
print(max(li))
print(min(li))

print(math.modf(12))
print(math.modf(1.2))
print(math.degrees(math.pi))
print(math.radians(90))
print(math.radians(270)) 
"""

#string function
"""
s = "jewel"
print(s)
print(s.capitalize())
print(s.upper())
t = "ZAHID"
print(t.lower())
print(s.count("j"))

u = "floxinoxinihilipilification"
print(u.count("i"))

z = "The quick brown fox jumps over the lazy dog"
print(z.startswith("T"))
print(z.endswith("dog"))

f = z.split()
print(f)

print(len(f))
print(z.find('y'))
print(z.find('a'))
print(z.find('quick'))
print(z.find('i'))
print(z.find('la'))

print(len(z))
print(z.title())
print(z.upper())
print(z.islower())
print(t.isupper())
print(t.swapcase())
print(z.swapcase())
print(s.swapcase())

str = "Hello zahid welcome to bandarban"
print(str.replace("zahid", "Jewel"))

print(str.isdigit())

d = "2441139"
print(d.isdigit())

print(str.isalpha())
print(z.isalpha())
print(t.isalpha())

greet = "!!!!!!hello!!!!!"
print(greet.strip("!"))

h = " hello "
print(h.lstrip())
print(h.rstrip())
print(h.strip())

k = "aaaaaalaaaaalaaaaa"
print(k.strip("a"))
print(k.lstrip("a"))
print(k.rstrip("a"))
"""

#MODULES in python programming
"""
import math
import sys
print(math.factorial(8))
#help(math)

#print(sys.path)
"""
#dictionaries
"""
temp = dict() #empty dictionary
temp["sum"] = 33.4
temp["mon"] = 36.4
temp["tue"] = 42.4
temp["wed"] = 31.4
print(temp)
print(temp.keys())
print(temp.values())
print(temp.items())#tuples of (key, value)

id = {"name": "zahid", "age": 28, "passion": "trekking", "profession": "studnet"}
print(id.keys())
print(id.values())
print(id.items())
print(id['name'])
print(temp["tue"])

di = dict(temp)
#di = temp
#di = temp.copy()
print(di)
print(len(di))
del di["mon"]
print(di)

print("sum" in di)
print("mon" in di)
"""

#creating dictionaries
"""
my_dict = {1: "apple", 2: "ball", 3: "cat"}
print(my_dict)
my_dict[4] = "rat"
my_dict[5] = "mice"
print(my_dict)
#another way
di = dict([(1,"apple"), (2, "ball"), (3,"cat")])
print(di)
#another way 
a = [1, 2, 3]
b = ["apple", "ball", "cat"]
my_dict = dict()

for i in range(len(a)):
    my_dict[a[i]] = b[i]
print(my_dict)
"""
#basic dictionary operations
"""
#access
my_dict = {1: "apple", 2: "ball", 3: "cat"}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict[3])
print(my_dict.get(1))
print(my_dict.get(4))

#insert
my_dict[4] = "rat"
my_dict[5] = "snake"
print(my_dict)
my_dict[2] = "bat"
print(my_dict)
print(len(my_dict))
"""

#dictionary methods_fromkeys()
"""
li = [1, 3, 5, 7]
print(dict.fromkeys(li))
print({}.fromkeys(range(1, 7), 10))
"""

#dictionary methods_setdefault()
"""
students = {"John": 20, "rai": 21, "anna": 22}
print(students.setdefault("john"))
print(students)

print(students.setdefault("malar"))
print(students)

print(students.setdefault("robi", 19))
print(students)
"""

#dictionary method update()
#concatenating two dictionary
"""
# ex-01
students = {"John": 20, "rai": 21, "anna": 22}
my_dict = {1: "apple", 2: "ball", 3: "cat"}
my_dict.update(students)
print(my_dict)

students.update(my_dict)
print(students)
"""
# ex-02
"""
dict1 = {1: "a", 2: "b"}
list1 = [3, "c"]
dict1.update([list1])
print(dict1)
dict1.update(y=3, z=2, x=1)
print(dict1)
dict2 = {1: "apple"}
dict1.update(dict2)
print(dict1)
dict2.update(dict1)
print(dict2)
"""
#deleting elements from dictionary
"""
students = {"John": 20, "rai": 21, "anna": 22, "ricky": 23}
del students["John"]
print(students)
students.pop("anna")
print(students)
students.clear()
print(students)
del students
print(students)
"""

# working with files
"""
import os

path = os.getcwd()
separator = os.sep
print(path)
print(separator)
file_name = input("Enter file name> ")

text_file = open(f"{path}{separator}{file_name}", "w")
text_file.write("Hello guys..wanna go to bandarban?")
text_file.close()
"""

#file handling
"""
import os

path = os.getcwd()
separator = os.sep
print(path)
print(separator)
file_name = input("Enter file name> ")

text_file = open(f"{path}{separator}{file_name}", "w")
text_file.write("Hello guys..wanna go to bandarban?")
text_file.close()

text_file = open(f"{path}{separator}{file_name}", "a")
text_file.write("\n9 months and i am away from my love..bandarban.")
text_file.close()

text_file = open(f"{path}{separator}{file_name}", "r")
print(text_file.read())
text_file.close()

"""

#renaming and deleting files
"""
path = os.getcwd()
separator = os.sep
print(path)
print(separator)

old_name = input("Enter old name> ")
new_name = input("Enter new name> ")

os.rename(f"{path}{separator}{old_name}", f"{path}{separator}{new_name}")

# print(os.getcwd()) #returns path
"""

# removing files
"""
import os

path = os.getcwd()
separator = os.sep
print(path)
print(separator)

file_name = input("Enter file name> ")
os.remove(f"{path}{separator}{file_name}")
"""

#managing directories
"""
import os

path = os.getcwd()
separator = os.sep
print(path)
print(separator)

print(os.listdir())
os.mkdir(f"{path}{separator}newhome")
print(os.getcwd())
os.chdir(f"{path}{separator}newhome")
print(os.getcwd())
# os.mkdir("zahid")
print(os.getcwd())
"""

#EXCEPTION HANDLING
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
#print(li[10]) #index error
#print(list1) #name error
#print(2+"jewel")#type error

import math

num = int(input("Enter a number > "))
result = math.factorial(num)
print(result) #value erro 7.4, -5 etc
"""

# EX-02
"""
import math

num = int(input("Enter a number > "))
try:
    result = math.factorial(num)
    print(result)
except ValueError:
    print("ValueError! Enter a positive integer.")
"""

# raise error

# raise ValueError(4)
# raise NameError
# ex-01
"""
try:
    num = int(input("Enter a positive number > "))
    if num <= 0:
        raise ValueError("That is not positive number")
    print(f"You entered {num}")
except ValueError as error:
    print(error)
"""
# ex-02
# try and finally
"""
import math
num = int(input("input > "))
try:
    result = math.factorial(num)
    print(result)
finally: #always executed
    print("goodbye!")
"""

# object oriented programming
# OOP
# class and object
# class and method

# ex-01
"""
class Person:
    def personName(self):
        pass
    def display(self, name):
        print("Hello", name)


person1 = Person()
person1.display("Hasan")

person2 = Person()
person2.display("Jewel")
"""

# ex-02
"""
class Person:
    def __init__(self, name):  #  constructor
        self.name = name
    def personName(self):
        pass
    def display(self):
        print("Hello", self.name)  # voila :D


person1 = Person("Hasan")
person1.display()

person2 = Person("Jewel")
person2.display()
"""

# class and isntance variables
# fields

# ex-01
"""
class Student:
    college = "Ananda Mohan College" # class variable
    # local to class
    # accessible by all the objects
    # common to all
    # @staticmethod # to avoid self

    def __init__(self, name, id):
        self.id = id  # instance i.e object variable
        self.name = name  # accessible by particular object
    def display(self):
        print("Student Name: ", self.name)
        print("Student ID: ", self.id)
        print("College Name: ", Student.college)


student1 = Student("Zahidul Islam", "01234")
student1.display()
print(end="\n")

student2 = Student("Jewel", "02231")
student2.display()
"""

# INHERITANCE
"""
class Animal:
    def __init__(self, name):
        self.name = name
    def eating(self):
        print(f"{self.name} eats")
    def walking(self):
        print(f"{self.name} walks")

class Dog(Animal):
    # def __init__(self, name): # this constructor not needed
    #     self.name = name
    def barking(self):
        print(f"{self.name} barks")

print("# Parent class")
cat1 = Animal("Cat")
cat1.eating()
cat1.walking()
print(end="\n")

print("# Child class")
dog1 = Dog("Dog")
dog1.eating()
dog1.walking()
dog1.barking()
"""

# multi level inheritance
"""
class Person:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Name : {self.name}")


class Employee(Person):
    def show(self):
        print(f"{self.name} is an employee")

class Programmer(Employee):
    def printing(self):
        print(f"{self.name} is a programmer")

print("# Parent")
p1 = Person("Zahid")
p1.display()
print(end="\n")

print("# Child")
e1 = Employee("Hasan")
e1.display()
e1.show()
print(end="\n")

print("# GrandChild")
prog1 = Programmer("Robi")
prog1.display()
prog1.show()
prog1.printing() 
"""

# multiple inheritance
# two or more base class
"""
class ArborealAnimal:
    def __init__(self, name):
        self.name = name
    def climbing(self):
        print(f"{self.name} can climb.")

class TerrestrialAnimal:
    def __init__(self, name):
        self.name = name
    def running(self):
        print(f"{self.name} can run.")

class AquaticAnimal:
    def __init__(self, name):
        self.name = name
    def swimming(self):
        print(f"{self.name} can swim")

class Snake(ArborealAnimal, TerrestrialAnimal, AquaticAnimal):
    def Hunting(self):
        print(f"{self.name} can hunt.")
    def Killing(self):
        print(f"{self.name} can kill.")


print("### Arboreal Class ###")
ar1 = ArborealAnimal("Monkey")
ar1.climbing()
print(end="\n")

print("### Terrestrial Class ###")
tr1 = TerrestrialAnimal("Tiger")
tr1.running()
print(end="\n")

print("### Aquatic Class ###")
aq1 = AquaticAnimal("Fish")
aq1.swimming()
print(end="\n")

print("### Snake Class ###")
snk1 = Snake("Snake")
snk1.climbing()
snk1.running()
snk1.swimming()
snk1.Hunting()
snk1.Killing()
print(end="\n")
"""


#method overriding

# ex-01
"""
class A:
    def display(self):
        print("display() method belongs to class A, not B")

class B(A): # class B inherits A
    pass

b1 = B()
b1.display()
"""

# ex-02
# now with overriding
"""
class A:
    def display(self):
        print("this display() method belongs to class A, not B")

class B(A): # class B inherits A
    def display(self):
        print("this display() method belongs to class B(overriding)")

b1 = B()
b1.display()
"""

# encapsulation
# private method
"""
class Car:
    def __init__(self):
        self.__updatesoftware()  # private method only can be called inside the class
    def drive(self):
        print("driving")
    def __updatesoftware(self): #private method, cannot be called outside the class
        print("updating software")

black_car = Car()
black_car.drive()
"""

# encapsulation
# privte variable
"""
class Car:
    __maxspeed = 0 # private variable
    __name = " " #private variable

    def __init__(self):
        self.__maxspeed = 200 # initialisze private variable
        self.__name = "supercar"

    def drive(self):
        print("driving")
        print(self.__maxspeed)
        
    def setSpeed(self, speed):
        self.__maxspeed = speed
        print(self.__maxspeed) # modification of private variable, possible only inside class, not outside

redcar = Car()
redcar.drive()
# redcar._maxspeed = 300 # not possible
redcar.setSpeed(100)
"""

# polymorphism
# ex-01
"""
class Dog:
    def sound(self): # polymorphism
        print("Woof Woof")

class Cat:
    def sound(self): # polymorphism
        print("Meow Meow")

def makeSound(animal):
    animal.sound()

cat_obj = Cat()
dog_obj = Dog()
makeSound(cat_obj) # alike cat_obj.sound()
makeSound(dog_obj) # alike dog_obj.sound()
"""

#time module
"""
import time
print(time.time())
# print(time.localtime())
# print(time.localtime(time.time()))
print(time.asctime())
"""

# time methods continued
# ex-01
"""
import time
t = (1992, 9, 24, 9, 20, 3, 0, 0, 0)
print(time.mktime(t))
print(time.localtime(time.mktime(t)))
"""

# ex-02
"""
import time
time.sleep(5)
print("Hello World!") 
"""

#calendar module
# ex-01

""" import calendar
print(calendar.month(2019, 11))
print(calendar.calendar(2019))
print(calendar.weekday(1992, 9, 24))
print(calendar.isleap(2018))
print(calendar.isleap(1800))
print(calendar.isleap(2000))
print(calendar.leapdays(2000,2019))
# print(help(calendar)) """

#set operations
"""
fruits = {"apple", "banana", "mango", "orange"}
print(fruits)
fruits.add("grapes")
print(fruits)
s = frozenset([4, 9, 2, 3, 5, 7, 8, 1, 6]) #makes it immutable
print(s)

num = {1, 1, 2, 3, 4, 3, 4, 5,7}
print(num)

st = set()
print(st)
print(type(st))

num1 = set(num)
print(num1)
num2 = num.copy()
print(num2)
"""

#set operations part-1
#unsorted
#no indexing
""" set1 = {4, 9, 2, 3, 5, 7, 8, 1, 6}
set2 = {1, 4, 7, 10, 13, 16, 19, 22}
# membership
print(6 in set1)
print(11 in set1)
set1.add(10)
print(set1)
set1.remove(8)
print(set1)

# union i.e or
set3 = set1 | set2
print(set3)

# intersection i.e. and
set4 = set1 & set2
print(set4)

# difference
set5 = set1 - set2
print(set5)

set1.clear()
print(set1)

set6 = set1.copy()
print(set6)

# symmetric difference i.e. XOR
set7 = set1 ^ set2
print(set7)
print(len(set1)) """


#type() and dir() function
""" num = 7
value = 3.14
li = [4, 9, 2]
print(type(num))
print(type(value))
print(type(li))
print(help(type))
print(dir())
import math
print(dir(math)) """

#iterators(part-1)
""" 
#R-01: iterating
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
for num in li:
    print(num, end=" ")

#R-02: indexing
print(end="\n")
for i in range(len(li)):
    print(li[i], end=" ")
print(end="\n")

#R-03: list comprehension 
print([x for x in li])

li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
print(iter(li)) # returns list iterable object
iterator = iter(li)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) 
"""

#iterators(part-2)
"""
#R-01 using for loop and iterator
print("### using for iterable....")
colors = ["red", "green", "blue", "yellow", "orange"]

for color in colors:
    print(color)
print(end="\n")

#R-02 using built in iterator
print("### using iterable multiple time....not using for")

colors = ["red", "green", "blue", "yellow", "orange"]
iterator = iter(colors)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(end="\n")

#R-03 by creating an iter function
print("### using iterable functio..try and except..")
colors = ["red", "green", "blue", "yellow", "orange"]

def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)

print_each(colors)
"""

# GENERATORS
# generator iterator
"""
#R-01 using for loop and iterator
def fib(mymax): # generator function
    a, b = 0, 1
    while True:
        c = a + b
        if(c < mymax):
            # print("Before yield keyword")
            yield c #is it like return?
            # print("After yield keyword")
            a = b 
            b = c
        else:
            break


generator = fib(10)
# print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# print(next(generator))
"""

# REGULAR EXPRESSION
# REGEX

#limitations of string
"""
s = "my name is alice"
s2 = s.replace("alice", "john")
print(s2)

str = "main street broad road"
str2 = str.replace("road", "rd")
print(str2)

str3 = str[0:17] + str[17:].replace("road", "rd")
print(str3)
"""

# match(), search(), findall() functions
"""
import re
line = "pet:cat i love cats"
match = re.match(r"pet:\w\w\w", line)
print(match.group(0))
match = re.search(r"pet:\w\w\w", line)
print(match.group(0))

line = "i love cats pet:cat"
# var = re.match(r"pet:\w\w\w", line)
# print(var.group(0))
var = re.search(r"pet:\w\w\w", line)
print(var.group(0))

line = "pet:cat i love cats pet:cow i love cow"
var = re.search(r"pet:\w\w\w", line)
print(var.group(0))
var = re.findall(r"pet:\w\w\w", line)
print(var)
"""

# replace() and split() function
"""
import re

line = "i love cats pet:cat i love cow, pet:cow thank you"
s = re.split(r"pet:\w\w\w", line)
print(s)

str1 = "zahidulislam.jewel@gmail.com and zahid.jewel@yahoo.com"
var = re.sub(r"@\w+", "@hotmail", str1)
print(var)
"""

#Recursive function
"""
# ex-01
import re

def counter(c):
    if c <= 0:
        return c
    else:
        return c + counter(c-1)

print(counter(5))

# ex-02
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
"""

#negative index in list
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
print(li[0])
print(li[-1])
print(li[-2])
li.insert(-1, 11)
print(li)
li.insert(-3, 14)
print(li)
print(li[-3:-1])
del li[-2]
print(li)
"""

#looping with index_enumerate function
""" li = [4, 9, 2, 3, 5, 7, 8, 1, 6]

for num in li:
    print(num, end=" ")

for i in range(len(li)):
    # print(i, li[i])
    print(f"i={i} & l[{i}]={li[i]}")

# using enumerate
# print(help(enumerate))
for i, j in enumerate(li):
    print(i, j)
print(end="\n")

for i, j in enumerate(li, 1):
    print(i, j) """

# range vs xrange function
"""
import sys

print(range(10))  # returns generator object
print([x for x in range(11)])
print([x for x in range(1, 11)])
print([x for x in range(1, 11, 2)])
print([x for x in range(-11, 5, 2)])

print(sys.getsizeof(range(100)))

li = [x for x in range(-11, 5, 2)]
print(li[0:3])
print(type(range(10)))
"""

# append va extend method in list
# appending a list into another list using extend
"""
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
li.append(11)
print(li)
li.extend([x for x in range(12,18)])
print(li)
s = [24, 36, 48]
li.extend(s)
print(li)
print(len(s))
str1 = ["zahid", "jewel", "tuhin"]
s.extend(str1)
print(s)
print(len(s)) 
"""

#input() in python 3
"""
num = int(input("Enter an integer > "))
print(num)
print(type(num))
d = eval(input("Enter a digit(0-9) > "))
print(d)
print(type(d))
"""

#program to find square of each elements of a list using map()
"""
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# solution-01 using def function
def square(x):
    return x*x

print(list(map(square, li)))


# solution-01 using lambda function

print(list(map(lambda x:x**2, li)))
"""

# adding two list using map()
"""
A = [1, 3, 5, 7]
B = [1, 1, 1, 1]

print(list(map(lambda x, y: x+y, A, B)))
print(tuple(map(lambda x, y: x+y, A, B)))
"""

#filter and reduce function
#filter()
#printing even numbers 1 through 10
"""
# using for loop
for x in range(1, 11):
    if x % 2 == 0:
        print(x, end=" ")
print(end="\n")

# using filter
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))
"""

#reduce()
#sum of elements of a list
"""
import functools
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(functools.reduce(lambda x, y: x + y, li))

print(functools.reduce(lambda x, y: x*y, li))
"""

# list comprehension in python programming
"""
print([x for x in range(1, 11)])
print([x for x in range(1, 11) if x % 2 == 0])
print([x for x in range(1, 11,2)])
print([x if x > 2 else x+1 for x in range(1, 11)])

list1 = [1, 2, 2, 3]
# print(list1*4)
print([x*10 for x in list1])

words = ["hello","a","jewel"]
print([x.upper() for x in words])

str1 = "1971 was a memorable year for 7.5 crore bangalies"
print([x for x in str1 if x.isdigit()])
print([x for x in str1 if x.isalpha()])

list2 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
print([x[0] for x in list2])
print([x[1] for x in list2])

def square(x):
    return x**2

print([square(x) for x in range(1, 11)])

A = [1, 3, 5, 7]
B = [1, 1, 1, 1]

print([x+y for x in A for y in B])
print([A[x]+B[x] for x in range(0, len(A))])
"""

# lambda + map + filter vs list comprehension
""" list1 = list()
for num in range(1, 11):
    list1.append(num)
print(list1)

# 2day way
print([x for x in range(1, 11)])

import timeit
import functools
num = [1.2, 2.3, 4.5]
print(list(map(lambda x: int(x), num)))
print(timeit.timeit('list(map(lambda x: int(x), [1.2, 2.3, 4.5]))'))

print([int(x) for x in num])
print(timeit.timeit('[int(x) for x in [1.2, 2.3, 4.5]]'))

print(list(filter(lambda x: x%2 == 0, range(1, 11))))
print([x for x in range(1, 11) if x%2 == 0 ])

print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4]))
print(sum([x for x in [1, 2, 3, 4]]))

if __name__ == '__main__':
    print(__name__) # retuns the name of the module we are working on

def mul(a, b):
    return a*b

print(mul(5, 6))
print(__name__) #returns name of the module """

# import multiply (defined in another file)
"""
result = multiply.add(12, 18)
print(__name__)
print(result)

product = multiply.mul(12, 18)
print(__name__)
print(product)
"""

#Bitwise Operator
# bitwise and
# bitwise or
# bitwise xor
"""
a = 20 # 0001 0100
b = 4  # 0000 0100
print(a & b)
print(a | b)
print(a ^ b)

print("a: ",bin(a))
print("b: ",bin(b))
print("AND: ", bin(a & b))
print("OR: ", bin(a | b))
print("XOR:", bin(a ^ b))

print(bin(10))
print(int(0b100))

#bitwise complement i.e. not operator(unary operator)
a = 20
print(~a)
b = 10
print(~b)

#bitwise left shift
print(a<<2)
print(a<<1)

#bitwise right shift
print(a>>3)
print(a>>2)
print(a>>1)
"""

# string methods..translate()...maketrans()
# maketrans()
""" # ex-01
s = "abcde"
print(ord("a"))
di = {"a": "1", "b": "2", "c": "3", "d": "4"}
t = s.maketrans(di)
print(t)

# ex-02
string = "hello guys and welcome"
dict1 = {"a": "1", "b": "2", "c": "3", "d": "4"}
table = string.maketrans(dict1)
print(table)
print(chr(97))
# ord("a")

# ex-03
string = "hello guys and welcome"
str1 = "abcde"
str2 = "12345"
tb = string.maketrans(str1, str2)
print(tb)
print(chr(98))

# ex-04
string = "((Hello guys $& and welcome"
str1 = "abcde"
str2 = "12345"
str3 = "($&"
t = string.maketrans(str1, str2, str3)
print(t)
print(chr(38))
print(chr(36))

# ex-06
string = "hello guys and welcome"
dict1 = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5"}
table = string.maketrans(dict1)
print(table)
# # print(chr(97))
# # ord("a")
s = string.translate(table)
print(s)


# ex-07
string = "hello guys and welcome"
str1 = "abcde"
str2 = "12345"
tb = string.maketrans(str1, str2)
# print(tb)
# print(chr(98))
s = string.translate(tb)
print(s)

# ex-08
string = "((Hello guys $& and welcome"
str1 = "abcde"
str2 = "12345"
str3 = "($&"
t = string.maketrans(str1, str2, str3)
print(t)
# print(chr(38))
# print(chr(36))

s = string.translate(t)
print(s) """

#namespace and variable scope
"""
# x = 4
# print(x)
# x = 5
# print(x)

def f1():
    x = 4
    print(x)
    print("Inside f1(): ", dir())

f1()
# print(x) #invalid due to variable scope within f1()
print(dir())
print("Outside f1() but inside main() \n ", dir())
"""

#LGBE Rule
"""
y = 10  # global variable, global scope
def inner():
    x = 4 #local to inner, local scope
    # y = 5 #local to inner(), different than global y
    # y = y + 1 # global varibale cannot be modified inside the local scope
    # keyword global is needed
    global y
    y = y + 1
    print(f"x: {x} inside inner() ")
    print(f"y: {y} inside inner() ")

print(f"y: {y} outside inner() ")
inner()
print(f"y: {y} outside inner() ")
# print(f"x: {x} outside inner() ")
"""

# ex-02
"""
y = 10  # global
def outer():
    z = 4  # enclosing variable
    def inner():
        x = 4
        # z = z + 1 # invalid, UnboundLocalError
        nonlocal z
        z = z + 1 # now valid
        print(f"x: {x} inside inner()")
        print(f"y: {y} inside inner()")
        print(f"z: {z} inside inner()")
    print(f"z: {z} inside outer() but outside inner()")
    inner()
print(f"Y: {y} outside outer but inside main()") # built in function print()...built in scope
outer()
"""

# ex-03
# python follows LEGB Rule
"""
x = 5
def fun():
    x = 10
    def inner():
        x = 15
        print(f"x: {x}")
    inner()

fun()
"""
# Closure_Nested Functions
# ex-01
"""
def outer():
    x = 3 # accessible by nested function
    def inner(): # nested function
        print(x)
    inner()
# inner() # cannot be called here, local to outer
outer()
"""

# ex-02
"""
def f():
    print("Hi")

f() # function call
print(f)
f  # function object reference
g = f  # g object is created of f class
g() # g is now object of class f...f is treated as class
"""

# ex-03
"""
def outer():
    x = 3 # accessible by nested function
    def inner(): # nested function
        print(x)
    return inner()
# inner() # cannot be called here, local to outer
a = outer()
print(a) 
"""

# ex-04
"""
def outer():
    x = 3
    def inner():
        y = 3
        result = x + y
        return result
    # return inner() # executing function definition
    return inner # returning inner function reference i.e..class to an object

a = outer() # creating object of class outer
print(a)
print(a.__name__) # returns the name which fucntion it points to
# inner() # NameError
# print(inner()) # NameError
a()
print(a())  #CLOSURE

"""

# ex-05
"""
def outer():
    msg = "hello"
    def inner():
        print(msg)
    return inner

a = outer() # a is an object of class outer..
# outer function is treated as a class
a()  #CLOSURE
"""
