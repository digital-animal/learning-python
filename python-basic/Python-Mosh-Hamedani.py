#into
"""
print("Zahidul Islam Jewel")
print("*" * 20)
"""

#variables
"""
price = 10
rating = 4.6
name = "Zahid"
is_published = True #boolean
print(price)
"""
#getting input
"""
name = input("What is your name? ")
print("Welcome",name)
"""

#type conversion
"""
birth_year = int(input("Birth Year> "))
age = 2019 - birth_year
print(age)
print(type(age))
"""

#strings
"""
course = "Python 'Course' for Beginners"
print(course)

print(course[0:7])
print(course[::-1])
note = '''
hello zahid.
how are you
'''
print(note)
name = "Jennifer"
print(name[1:-1])
"""

#formatted string
"""
first = "John"
last = "smith"
message = f'{first} [{last}] is a coder'
print(message)
"""

#string methods
"""
course = "python for beginners"
print(len(course))
print(course.capitalize())
print(course.upper())
print(course.find("s"))
print(course.replace("s","x"))
print("x" in course)
"""

#arithmetic operations
"""
x=12
y=8
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y)
print(x**y)
"""

#operator precedence
#parenthesis>exponentiation>division/multiplication>addition/subtraction
#if equal precedence then left>right
"""
x = 10 + 3*2**2
print(x)
y = (2+3)*10-3**2
print(y)
"""

#math functions
"""
x = 2.9
print(round(x))
y = 2.1
print(round(y))
z = -2.9
print(abs(z))
"""

#math module
"""
import math
print(math.sqrt(2001))
print(math.sin(1.62))
print(math.ceil(2.9))
print(math.floor(2.9))
print(math.fabs(-4.9))
print(math.factorial(10))
"""

#if-condition
"""
is_hot = True
if is_hot:
    print("DrinkWater!")
else:
    print("No Worries!")
"""

#logical operators
#and, or, not
#logical and
"""
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")
"""
#logical or
"""
has_high_income = False
has_good_credit = True
if has_high_income or has_good_credit:
    print("Eligible for loan")
"""

#logical not
"""
has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
"""

#comparision operators
"""
temperature = 35
if temperature >= 30:
    print("Hot day")
else:
    print("Not a hot day")
"""

#username validation
"""
name = input("Enter name > ")
if len(name) < 3:
    print("Name must be at least of 3 characters.")
elif len(name) > 30:
    print("Name length cannot exceed 30 characters:")
else:
    print("Valid name")
"""
#while loop
#ex-01
"""
i = 1
while True:
    print(i,end=" ")
    i = i+1
    if i > 10:
        break
"""
#ex-02
"""
j = 1
while True:
    print("*"*j)
    j = j+1
    if j > 10:
        break
"""
#for loops
"""
#ex-01
for letter in "Python":
    print(letter, end="")
#ex-02
for name in ["Zahid", "Jewel", "Tuhin"]:
    print(name)
#ex-03
for num in range(10):
    print(num, end=" ")
"""

#nested loops
"""
for x in range(4):
    for y in range(4):
        print(f'({x},{y})',end=" ")
    print(end="\n")
"""
#exercise
'''
input: li = [5, 2, 5, 2, 2]
output:
*****
**
*****
**
**
'''
#solution-1
"""
li = [5, 2, 5, 2, 2]
for i in li:
    print("*"*i)
"""

#solution-2
"""
li = [5, 2, 5, 2, 2]
for x in li:
    for y in range(x):
        print("*", end="")
    print(end="\n")
"""
#lists
"""
names = ["Zahid", "Hasan", "Tuhin", "Islam"]
print(names)
print(names[1])
print(names[-1])
print(names[2:])
print(names[::-1])
print(names[:2])
print(names[:])
names[0] = "Jewel"
print(names)
"""
#program to find the largest number in a list
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
largest = li[0]

for num in li:
    if num > largest:
        largest = num

print("Largest number in the list: ", largest)
"""
#using max()
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
print("Largest number in the list: ", max(li))
"""

#program to find the smallest number in a list
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
smallest = li[0]

for num in li:
    if num < smallest:
        smallest = num

print("Smallest number in the list: ", smallest)
"""
#using min()
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
print("Smallest number in the list: ", min(li))"""

#2D list
"""
matrix = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

print(matrix[0])
print(matrix[0][1])
print(matrix[2][2])
print(end="\n")
for row in matrix:
    for item in row:
        print(item,end=" ")
    print(end="\n")
"""

#list methods
#list functions
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
li.append(10)
print(li)
li.insert(1, 12)#li.list(index, item)
print(li)
li.remove(5)
print(li)
#li.clear()
print(li)
li.pop()
print(li)
print(li.index(6))
print(15 in li)
li.pop(0)
print(li)
print(li.count(5))
print(li.count(6))
li.sort()
print(li)
li.reverse()
#sorted(li, reverse=True)
print(li)
li2 = li.copy()
li.append(20)
print(li)
print(li2)
"""

#program to remove duplicates in a list
#solution-01,using set
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6, 12, 7, 6, 4, 9]
print(li)
s = set(li)
print(s)
li2 = list(s)
print(li2)
"""
#solution-02:
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6, 12, 7, 6, 4, 9]
print("Old list: ",li)
di = dict()
li2 = list()
for num in li:
    di[num] = di.get(num, 0) + 1
print(di)

for key, value in di.items():
    #if value==1:
        li2.append(key)

print("Updated list: ",li2)
"""


#solution-03:
"""
li = [4, 9, 2, 3, 5, 7, 8, 1, 6, 12, 7, 6, 4, 9]
print("Old list: ",li)

li2 = list()

for num in li:
    if num not in li2:
        li2.append(num)
print(li2)
"""

#tuples
"""
# immutable
t = (4, 9, 2, 3, 5, 7, 8, 1, 6, 12, 7, 6, 4, 9)
print(t)
print(t.count(2))
print(t[0])
print(t.index(4))
"""

#unpacking
#for list and tuples
"""
coordinates = (1, 2, 3)
#x = coordinates[0]
#y = coordinates[1]
#z = coordinates[2]

x, y, z = coordinates
print(x)
print(y)
print(z)
"""

#dictionaries
"""
customer = {
    "name": "Zahid",
    "age": 27,
    "is_verified": True
}

print(customer["name"])
print(customer["age"])
print(customer["is_verified"])
customer["birthday"] = customer.get("birthday", "sept 24")
print(customer)
customer["hobby"] = "trekking"
print(customer)
"""

#program to spell a number in words
#eg. 1234=One Two Three Four
"""
#solution-01(my solution)
number_set = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

li = list()
num = int(input("Enter a number > "))
while num != 0:
    digit = num % 10
    li.append(digit)
    num = num // 10
#print(li)
li.reverse()
print(li)
for num in li:
    print(number_set[num], end=" ")
"""

#solution-02(mosh's solution)
"""
number_set = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
 

num = input("Enter a number > ")
for digit in num:
    print(number_set[digit], end=" ")
"""

#FUNCTIONS
#ex-01
"""
def greetUser():
    print("Hi there!")
    print("Welcome!")


print("start")
greetUser()
print("finish")
"""
#function parameters and arguments
"""
def greetUser(name):
    print("Hi there!")
    #print("Welcome!", name)
    #print("Welcome!{}".format(name))
    print(f"Welcome!{name}")


name = "Jewel"
print("start")
greetUser(name)#positional arguments
print("finish")
"""

#keyword arguments
#positional arguments vs keyword arguments
"""
def greetUser(first_name,last_name):
    print("Hi there!")
    #print("Welcome!")
    #print("Welcome!{} {}".format(first_name, last_name))
    print(f"Welcome!{first_name} {last_name}")



print("#start")
greetUser(last_name="Smith", first_name="Jhon")#keyword arguments
print("#finish")
"""

#return statements
"""
def square(num):
    return num*num

print(square(25))
"""

#exceptions
#try and except

#1st way
"""
try:
    age = int(input("Age"))
    print(age)
except:
    print("ValueError")
    print("Enter a positive numeric value for age")
"""

#2nd way
"""
try:
    age = int(input("Age"))
    print(age)
except ValueError:
    print("Invalid value")
    print("Enter a positive numeric value for age")
"""
#ex-02
#exit code must be 0 i.e. correct
"""
try:
    num1, num2 = input("Enter two positive number > ").split()
    x = int(num1)
    y = int(num2)
    print(x, y)
    result = x / y
    print(result)
except ZeroDivisionError:
    print("Number cannot be divided by zero!")
except ValueError:
    print("Invalid value")
    print("Enter a positive numeric value for age")
"""
#comments in python
#single line comment
#multi-line comment


#CLASSES
#OOP

#pascal naming convention
"""
class Point:
    x = 10
    y = 20
    def move(self):
        print("move")

    def draw(self):
        print("draw")

#creating objects i.e. instances of class
point = Point()

point.draw()
point.move()
a = point.x
b = point.y
print(a,b)
"""
#constructor
#default function called when an object is created
"""
class Point:
    def __init__(self, x, y):#constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

#creating objects i.e. instances of class
point = Point(11, 20)

point.draw()
point.move()
a = point.x
b = point.y
print(a, b)
"""


#inheritence
"""
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def mew(self):
        print("mew")


dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.mew()
"""

# modules
# creating a module
# a module to findMax and findMin
"""
import utils
list1 = [4, 9, 2, 3, 5, 7, 8, 1, 6]
maxima = utils.findMax(list1)
print("maxima: ", maxima)
minima = utils.findMin(list1)
print("minima: ", minima)
"""

# packages
# importing from packages
# 1st way
"""
import ecommerce.shipping
ecommerce.shipping.calc_shipping()
"""
#2nd way
"""
from ecommerce.shipping import calc_shipping
calc_shipping()
"""
# 3rd way
"""
from ecommerce import shipping
shipping.calc_shipping()
"""
#4th way
"""
from ecommerce import shipping as ship
ship.calc_shipping()
"""

#generating random variables
"""
import random
for i in range(3):
    #print(random.random())
    #print(random.randint(10, 20))

li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
print(random.choice(li))
"""

#program of rolling of two dice
#solution-01
"""
import random

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]
x = random.choice(dice1)
y = random.choice(dice2)
print(f"({x}, {y})")
"""

#solution-02
"""
import random

class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return (x, y) #returing tuple

dice = Dice()
print(dice.roll())
"""
#BASIC ENDS HERE
# 3 hour 44 minutes


#files and directories
#pathlib