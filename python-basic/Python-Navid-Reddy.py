"""Getting started with python"""
# print(2 + 3)
# print(9 + 3)
# print(4 * 3)
# print(8 / 3)
# print(8 % 3)
# print(8 // 3)
# print(2**5)
# print("Zahid")
# print("Zahid's Den")
# print("Zahid\'s Den")
# print('she said,"It's a wonderful life"')
# print("she said,\"It's a wonderful life\"")
# print("Zahid " + "Islam")
# print("Zahid "*10)
# print("c:\docs\nahid")
# print(r"c:\docs\nahid") # raw string


"""Variables in python"""
# x = 2
# print(x)
# y = 3
# print(y)
# print(x + y)
# x = 9
# print(x + y)
# print(x + 19)
# z = x + 19
# print(z)
# channel = "youtube"
# print(channel)
# print(channel[0])
# print(channel[-1])
# print(channel[::-1])
# print(channel[2:4])
# print(channel[1:7])
# print(channel[1:7:2])
# print(channel[:2])
# print(channel[4:])
# print(channel[1:])
# print(channel[:])
# print(channel[::3])
# print(channel[3:10])
# print('my'+channel[3:])
# print(len(channel))
# print(len("Zahid"))


""" Lists in python """
# list1 = []
# list2 = list()
# num = [4, 9, 2, 3, 5, 7, 8, 1, 6]
# print(num)
# print(num[0])
# print(num[4:8])
# print(num[4:8:2])
# print(num[-1])
# print(num[::-1])
# print(num[-5])
#
# names = ["Zahid", "Jewel", "Nobin", "Robi"]
# print(names)
# print(len(names))
#
# prime = [2, 3, 5, 7, 11, 13, 17, 19]
# nested = [
#     [4, 9, 2],
#     [3, 5, 7],
#     [8, 1, 6]
# ]
#
# num.append(13)
# print(num)
# num.pop()
# print(num)
# num.insert(2, 11)
# print(num)
# num.remove(4)
# print(num)
# del num[0]
# print(num)
# num.pop(0)
# print(num)
# del num[2:4]
# print(num)
# li = [31, 37]
# num.extend(li)
# print(num)
# num.extend([41, 43, 47])
# print(sum(num))
# print(min(num))
# print(max(num))
# num.sort()
# print(num)
# num.sort(reverse=True)
# print(num)
# num.reverse()
# print(num)


""" Tuple """
# num = (4, 9, 2, 3, 5, 7, 8, 1, 6)
# names = ("Zahid", "Jewel", "Nobin", "Robi")
# print(len(names))
# print(num)
# print(num[0])
# print(num[1:4])
# print(num[::-1])
# print(num.index(9))
# print(num)


""" Set """
# s = set()
# s1 = {}
# num = {4, 9, 2, 3, 5, 7, 8, 1, 6}
# print(num)
# print(len(num))
#
# s2 = {1, 1, 2, 3, 4, 4, 5, 5, 5, 5, 5}
# print(s2)
# print(len(s2))
# s2.remove(1)
# print(s2)
# A = {1, 3, 5, 7, 9}
# B = {2, 3, 5, 7}
# print(A & B)
# print(A.intersection(B))
# print(A | B)
# print(A.union(B))
# print(A - B)
# print(A.difference(B))


"""Python set path in windwos and help"""
# print(help())
# quit()


""" More on variable """
# num = 5
# print(num)
# print(id(num))
# my_name = "Jewel"
# print(my_name)
# print(id(my_name))
# a = 10
# b = a
# print(a)
# print(id(a))
# print(b)
# print(id(b))  # memory efficiency
# print(id(10))
# k = 10
# print(k)
# print(id(k))
# a  = a + 1
# print(a)
# print(id(a))
# print(b)
# print(id(b))
# k = a
# print(k)
# print(id(k))
# b = 8
# print(b)
# print(id(b))
# print(id(10))  # ready for garbage collection
# PI = 3.141592353589793  # constant convention
# print(PI)
# print(type(PI))
# print(type(num))
# print(type(my_name))


""" Data Types in python """
# 1. None
# 2. Numeric
# # # a) int b) float c) complex d) bool
# 3. List
# 4. Tuple
# 5. Tuple
# 6. Set
# 7. String
# 8. Range
# 9. Dictionary

# num = 2.5
# # print(type(num))
# # num = 5
# # print(type(num))
# # num = 4 + 3j
# # print(type(num))
# # num = True
# # print(type(num))
# # a = 5.6
# # b = int(a)
# # print(type(b))
# # print(b)
# # k = float(b)
# # print(k)
# # print(type(k))
# # k = 6
# # c = complex(k)
# # print(c)
# # print(type(c))
# # f = complex(2, 3)
# # print(f)
# # print(type(f))
# # print(b < k)
# # bl = b < k
# # print(bl)
# # print(type(bl))
# # c2 = b > k
# # print(c2)
# # print(type(c2))
# #
# # lst = [4, 9, 2, 3, 5]
# # print(lst)
# # print(type(lst))
# # st = {4, 9, 2, 3, 5}
# # print(st)
# # print(type(st))
# # t = (4, 9, 2, 3, 5)
# # print(t)
# # print(type(t))
# # name = "Jewel"
# # print(name)
# # print(type(name))
# # st = "a"
# # print(type(st))
# # print(list(range(10)))
# # print(tuple(range(10)))
# # print(set(range(10)))
# # print(list(range(2, 11, 2)))
# # print(type(range))
# # dictionary = dict()
# # print(dictionary)
# # print(type(dictionary))
# # di = {"Jewel": "Nokia", "Nobin": "Samsung", "Rahul": "iPhone"}
# # print(di.keys())
# # print(di.values())
# # print(di["Jewel"])
# # print(di.get("Rahul"))


""" Operators in python"""
# 1. Arithmetic Operator
# 2. Assignment Operator
# 3. Relational Operator
# 4. Logical Operator
# 5. Unary Operator

# x = 2
# y = 3
# print(x + y)
# print(x - y)
# print(x * y)
# print(x % y)
# x = 8
# x = x + 2
# print(x)
# x += 2
# print(x)
# x *= 3
# print(x)
# a, b = 5, 6
# print(a)
# print(b)
# n = 7
# n = - n
# print(n)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a > b)
# print(a >= b)
# print(a <= b)
#
# a, b = 5, 4
# print(a < 8 and b < 5)
# print(a < 8 and b < 2)
# print(a < 8 or b < 2)
# x = True
# print(not x)
# x = not x
# print(x)


""" Number System in Python """
# 1. Binary
# 2. Decimal
# 3. Octal
# 4. Hexadecimal
# print(bin(25))
# print(oct(25))
# print(hex(25))
# print(0b0101)
# print(0b011101)
# print(0xA)
# print(0xF)
# print(0o71)
# print(0o174)
# print(0b110011010)
# print(oct(0b110011010))
# print(hex(0b110011010))


""" Bitwise Operators """
# 1. Complement(~)
# 2. And(&)
# 3. Or(|)
# 4. XOR(^)
# 5. Left Shift(<<)
# 6. Right Shift(>>)
# a = 12
# print(~a)
# b = 13
# print(a & b)
# print(a | b)
# print(a ^ b)
# print(~(a ^ b))  # XNOR
# print(a << 2)
# print(b << 2)
# print(a >> 2)
# print(b >> 2)


""" import math functions in python """
# import math
# x = 25
# print(math.sqrt(25))
# print(math.ceil(5.2))
# print(math.floor(5.2))
# print(round(5.2))
# print(math.factorial(6))
# print(math.pow(2, 6))
# print(math.radians(90))
# print(math.degrees(math.pi*.5))
# print(math.degrees(math.pi*.25))
# print(math.pi)
# print(math.e)
# print(math.log(100, 10))
# print(math.log10(90))
# print(math.log2(256))
# print(math.exp(1))
# print(math.exp(3))
# print(math.exp(-1))
# print(math.sin(math.pi))
# print(math.sin(math.pi*.25))
# print(math.sin(math.pi*.50))
# print(math.cos(math.pi*.3333))



""" working with pycharm run, debug, trace, .py file """
# x = 5
# y = 8
# z = x + y
# print(z)


""" User input in python, command line """
# x = int(input("Enter 1st number > "))
# y = int(input("Enter 2nd number > "))
# z = x + y
# print(z)

# name = input("Enter your name > ")
# print(name)

# name = input("Enter your name > ")[0]
# print(name)

# result = eval(input("Enter an expression > "))
# print(result)

# # using argv
# import sys
# x = sys.argv[1]
# y = sys.argv[2]
# z = int(x) + int(y)
# print(z)


""" if elif else statement in python """
# x = int(input("Enter a number > "))
# r = x % 2
# if r == 0:
#     print("even")
#     if x > 5:
#         print("greater")
#     else:
#         print("smaller")
# else:
#     print("Odd")
#
# print("bye")


# print "one" for 1, "two" for 2...and so on...
# di = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }
# li = []
# num = int(input("Enter a number."))
# while num > 0:
#     r = num % 10
#     li.append(r)
#     num = num // 10
#
# # print(li)
# li.reverse()
#
# for digit in li:
#     print(di[digit], end=" ")



""" while loop in python """
# i = 1
# while i <= 5:
#     print(f"{i}: Hello, World")
#     i = i + 1

# i = 1
# while i <= 5:
#     print(f"{i}: Hello, World.", end="")
#     j = 1
#     while j <= 5:
#         print(f"{j}: python.", end="")
#         j = j + 1
#     print(end="\n")
#     i = i + 1


""" for loop in python """
# # ex-01
# li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
# for num in li:
#     print(num, end=" ")
# print(end="\n")
# # ex-02
# name = "Zahid"
# for l in name:
#     print(l, end=" ")
# print(end="\n")
# # ex-03
# for num in range(1, 11):
#     print(num, end=" ")
# print(end="\n")
# # ex-04
# for num in range(11, 21, 2):
#     print(num, end=" ")
# # ex-05
# print(end="\n")
# # ex-06
# for num in range(20, 10, -1):
#     print(num, end=" ")
# print(end="\n")
# # ex-07
# for num in range(1, 21):
#     if num % 5 == 0:
#         continue
#     print(num, end=" ")


"""break, continue and pass in python"""
# # break
# # candy problem
# x = int(input("How many candies you want? "))
# av = 5
# i = 1
# while i <= x:
#     if i > av:
#         print("Out of stock...")
#         break
#     print(f"candy {i}")
#     i += 1
#
# print("Bye...have a good day!")


# # printing numbers from 1 to 100
# # except numbers divisible by 3 or 5
#
# for num in range(1, 101):
#     if num % 3 == 0 or num % 5 == 0:
#         print(end="\n")
#         continue
#     print(num, end=" ")


# # pass
# # aka skipping
# # printing those numbers that are not multiple of 4 in range [1-100]
#
# for num in range(1, 101):
#     if num % 4 ==0:
#         pass
#     else:
#         print(num, end=" ")
#
# print("Done!")


""" Pattern Programming """
# patter-01,printing square #
# # method-01
# for i in range(4):
#     print("# "*4, end="\n")

# # # method-02
# for i in range(4):
#     for j in range(4):
#         print("# ", end="")
#     print(end="\n")


# # patter-02,printing lower triangle
# # right angle traingle
# for i in range(4):
#     for j in range(i+1):
#         print("# ", end=" ")
#     print(end="\n")


# # patter-03,printing upper triangle
# # right angle traingle

# for i in range(4):
#     for j in range(4-i, 0, -1):
#         print("# ", end=" ")
#     print(end="\n")


""" OOP """
""" Object Oriented Programming"""
# class
# object
# method
""" 
class Computer:
    def config(self):
        print("i5, 16GB, 256GB")
        pass

comp1 = Computer()
print(type(comp1))
comp1.config()
Computer.config(comp1) # same as previous line

comp2 = Computer()
comp2.config()
Computer.config(comp2)

# __init__ method in python

class Computer:
    def __init__(self, cpu, ram): # constructor
        print("in it")
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print("Config: ", self.cpu, self.ram)


comp1 = Computer("i7", 16)
print("Computer 1:")
comp1.config()

comp2 = Computer("Ryzen 3", 8)
print("Computer 2:")
comp2.config() 
"""

# # constructor, self and comparing objects in python
"""
class Computer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name = {self.name} and Age = {self.age}")
    def compare(self, obj):
        if self.age == obj.age:
            return True
        else:
            return False



# c1 = Computer("Navin", 30)
# c1.display()
# print(id(c1))


# c2 = Computer("Rashi", 22)
# print(id(c2))
# c2.display()

# c3 = Computer("Zubin", 30)
# c3.display()

# print("Comparing object c1 and c2")
# if c1.compare(c2):
#     print(f"objects are same")
# else:
#     print("objects are not same")


# print("Comparing object c1 and c3")
# if c1.compare(c3):
#     print(f"objects are same")
# else:
#     print("objects are not same")
"""

# # types of variable
# # instance variable
# # class variable i.e. static variable
""" 
class Car:
    wheels = 4 # class variable outside __init__

    def __init__(self):
        self.mil = 10  # instance variable i.e. object variable
        inside __init__ constructor
        self.com = "BMW"

c1 = Car()
c2 = Car()

c1.mil = 8  # c1.mil is changed now..overriding default class variable
# as c1 is object variable(instance variable)
# only object cant  modify this

Car.wheels = 5 # class variable
# can only be modified by class

print("C1:", c1.com, c1.mil, c1.wheels)
print("C2:", c2.com, c2.mil, c2.wheels)
"""


# # methods in python
# instance methods
# class methods
# static methods
"""
class Student:

    school = "Telusko" #class variable


    def __init__(self, m1, m2, m3):
        self.m1 = m1  # instance variable
        self.m2 = m2  # instance variable
        self.m3 = m3  # instance variable
    def avg(self): # instance method
        return (self.m1 + self.m2 + self.m3)/3

    # def get_m1(self): # accessor
    #     return self.m1
    # def set_m1(self, marks): # mutators
    #     self.m1 = marks

    @classmethod # decorators
    def getSchoolName(cls): # class methods # self replace by cls
        return cls.school

    @staticmethod # decorators
    def info():  # static method
        print("this is static method in Student class")


s1 = Student(67, 75, 95)
print("Student 1: ", s1.avg())
s2 = Student(89, 92, 55)
print("Student 2: ", s2.avg())

# print(s1.get_m1())
# print(s1.info())
# # print(s2.getSchoolName())
# # print(Student.getSchoolName())
# print(Student.info())
print(s1.info())
"""


# inner class in python
"""
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()
        # inner class Laptop object is created..
        # just outside the inner class..
        # but inside the outer class..
        # self.lap is outer class(Student)..
        # object of inner class Laptop now..


    def show(self):
        print(self.name, self.roll)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.CPU = "i5"
            self.RAM = 8
        def show(self): # function overriding
            print(self.brand, self.CPU, self.RAM)


s1 = Student("Jewel", 81)
s2 = Student("Raju", 79)
print(s1.name, s1.roll)
print(s2.name, s2.roll)

s1.show()
s2.show()
# print(s1.lap.brand, s1.lap.CPU, s1.lap.RAM)

lap1 = s1.lap
print(s1.name, lap1.brand, lap1.CPU, lap1.RAM)
# print(id(lap1))

lap2 = s2.lap
# print(id(lap2))
print(s2.name, lap2.brand, lap2.CPU, lap2.RAM)

lap3 = Student.Laptop()
# creating object of inner class..
# outside of outer class..
# inner class must be mentioned with dot(.)..
print(lap3.brand, lap3.CPU, lap3.RAM)
s1.show()
# lap3.show()
"""

# inheritance in python
# oop
# # single level + multi level inheritance
"""
class A:
    def __init__(self):
        pass

    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")

class B(A):# class B inherits class A
    def __init__(self):
        pass

    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

class C(B): # C inherits class B and so class A
    def __init__(self):
        pass
    def feature5(self):
        print("Feature 5 working")

print("Parent Class Object")
a1 = A()
a1.feature1()
a1.feature2()
print(end="\n")
print("Child Class Object")
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()

print(end="\n")
print("Grand Child Class Object")
c1 = C()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
c1.feature5()
"""

# multiple inheritance
# oop
"""
class A:
    def __init__(self):
        pass

    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")

class B:
    def __init__(self):
        pass

    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")

class C(A, B): # C inherits class B and so class A
    def __init__(self):
        pass
    def feature5(self):
        print("Feature 5 working")

print("Parent1 Class Object")
a1 = A()
a1.feature1()
a1.feature2()
print(end="\n")

print("Parent2 Class Object")
b1 = B()
b1.feature3()
b1.feature4()

print(end="\n")
print("Child Class Object")
c1 = C()
c1.feature1()  # from class A
c1.feature2()  # from class A
c1.feature3()  # from class B
c1.feature4()  # from class B
c1.feature5()  # c's own method
"""

# constructor in inheritance in python
# method resolution order (MRO)
# single level inheritance
# multi level inheritance
# multiple inheritance
# ex-01
# for single level inheritance
"""
class A:
    def __init__(self):
        print("in A init")
    def feature1A(self):
        print("Feature 1 of A")
    def feature2A(self):
        print("Feature 2 of A")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")
    def feature1B(self):
        print("Feature 1 of B")
    def feature2B(self):
        print("Feature 2 of B")

a1 = A()
b1 = B()
print(end="\n")
print("***Object A***")
a1.feature1A()
a1.feature2A()
print(end="\n")

print("***Object B***")
b1.feature1A()
b1.feature2A()
b1.feature1B()
b1.feature2B()
"""

# ex-02
# for multiple inheritance
"""
class A:
    def __init__(self):
        print("in A init")
    def feature1A(self):
        print("Feature 1 of A")
    def feature2A(self):
        print("Feature 2 of A")

class B:
    def __init__(self):
        print("in B init")
    def feature1B(self):
        print("Feature 1 of B")
    def feature2B(self):
        print("Feature 2 of B")

class C(A, B):
    def __init__(self):
        super().__init__()
        # inherits A()'s constructor
        # doesn't inherit C()'s constructor
        # using MRO(method resolution order)
        # LEFT to RIGHT
        print("in C init")

    def feature1C(self):
        print("Feature 1 of C")
    def feature2C(self):
        print("Feature 2 of C")

    def feat(self):
        super().feature2A()
# a1 = A()
# b1 = B()
c1 = C()

# print(end="\n")
# print("***Object A***")
# a1.feature1A()
# a1.feature2A()
# print(end="\n")
#
# print("***Object B***")
# b1.feature1B()
# b1.feature2B()
# print(end="\n")

print("***Object C***")
c1.feature1C()
c1.feature2C()
print(end="\n")
c1.feat()
"""

# introduction to polymorphism in python
# poly = many....morph = form
# loose coupling
# dependency injection
# interface
# duck typing in python
# if there's a bird
# that looks like a duck
# which is walking like a duck,
# quacking like a duck
# & swimming like a duck
# then that bird is a duck

# x = 5
# x = "Jewel"
"""
class PyCharm:
    def execute(self):
        print("compiling...")
        print("running...")
        print(("debugging..."))

class MyEditior:
    def execute(self):
        print("Spell Check..")
        print("Convention Check..")
        print("Unit Test..")
        print("compiling...")
        print("running...")
        print(("debugging..."))

class Laptop:
    def code(self, IDE):
        IDE.execute()


# ide = PyCharm()
ide = MyEditior()

lap1 = Laptop()
lap1.code(ide)
"""

# operator overloading in python
# polymorphism

# a = 5
# b = "World"
# print(a + b)
# in python 'int' is not integer type
# 'int' is an object of class type
# a = 5
# b = 6
# print(a + b)
# print(int.__add__(a, b))
"""
p = '5'
q = '6'
print(str.__add__(p, q))

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s0 = Student(m1, m2)

        return s0

    def __gt__(self, other):
        m_s = self.m1 + self.m2
        m_o = other.m1 + other.m2
        if m_s > m_o:
            return True
        else:
            return False

    def __str__(self):
        # return self.m1, self.m2  # return a tuple
        return "{} {}".format(self.m1, self.m2)

s1 = Student(58, 69)
s2 = Student(60, 95)

s3 = s1 + s2  # Student.__add__(s1, s2)
# '+' operator is overloaded here
# it adds two object s1 & s2
# s1 + s2 returns an object...
# to s3 from def __add__(self, other)
print(s3.m1)
print(s3.m2)

if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")

a = 9
print(a)
print(a.__str__())

print(s1.__str__())

print(s1)
print(s2)
"""

# method overloading
# and method overriding
"""
class Studnet:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # def sum(self, a=None, b=None, c=None):  # default argument
    #     s = 0
    #     if a!=None and b!=None and c!=None:
    #         s = a + b + c
    #     elif a!=None and b!=None:
    #         s = a + b
    #     else:
    #         s = a
    #
    #     return s

    def sum(self, a=0, b=0, c=0):  # default argument
        # much better than previous one
        s = a + b + c

        return s

s1 = Studnet(50, 60)
print(s1.sum(5))
print(s1.sum(5, 9))
print(s1.sum(5, 9, 6))
"""

# now method overriding
"""
class A:
    def show(self):
        print("in A show")

class B(A):
    # pass
    def show(self):
        print("in B show")



a1 = A()
a1.show()
b1 = B()
b1.show()
"""
## END OF OOP
## END OF OBJECT ORIENTED PROGRAMMING


"""Exception Handling in python"""
# # # ZeroDivisionError example(Runtime Error)
# #
# # a = int(input("Enter 1st number > "))
# # b = int(input("Enter 2nd number > "))
# # result = a / b
# # print(result)
# # print("Bye!")
#
#
# # solution of this...try and except
# # ZeroDivisionError example(Runtime Error)
#
# try:
#     a = int(input("Enter 1st number > "))
#     b = int(input("Enter 2nd number > "))
#     print("Before Division")
#     result = a / b
#     print(result)
#
#     k = int(input("Enter another number > "))
#     print(k)
#
# # except Exception:
# # except Exception as e:
# #     print("Number cannot be divided by Zero(0)", e)
#
# except ZeroDivisionError as e:
#     print("Number cannot be divided by Zero(0)..", e)
#
# except ValueError as err:
#     print("Invalid Input..", err)
# except Exception as error:
#     print("Something went wrong...", error)
#
# finally:
#     print("After Division")
#
# print("Bye!")


""" Multi Threading in Python """
""" Thread """
# from threading import *
# from time import sleep

# # multi threading example
# class Hello(Thread):
#     def run(self):
#         for i in range(100):
#             print("Hello")
#             sleep(.1)

# class Hi(Thread):
#     def run(self):
#         for i in range(100):
#             print("Hi")
#             sleep(.1)

# t1 = Hello()
# t2 = Hi()

# # t1.run()
# # t2.run()

# t1.start()
# # sleep(.1)
# t2.start()

# t1.join()
# t2.join()
# print("Bye...")  # main thread is executing this



""" File Handling in Python """
""" File Handle """
# import os
# path = os.getcwd()
# sep = os.sep

# f1 = open(f"{path}{sep}python-basic{sep}files{sep}gollum.txt")
# g = f1.read() # reads line by line
# g = f1.readline()
# g = f1.readline(4)
# print(g)
# f1.close()

# f2 = open(f"{path}{sep}python-basic{sep}files{sep}mydata.txt", "r")
# print(f2.readline().rstrip())
# for data in f2:
#     print(data.rstrip())
# f2.close()

# f3 = open(f"{path}{sep}python-basic{sep}files{sep}mydata.txt", "a")
# f3.write(" Now tell me about yourself. ")
# f3.write("What is your plan?")
# f3.close()

# f4 = open(f"{path}{sep}python-basic{sep}files{sep}mydata.txt", "r")
# f5 = open(f"{path}{sep}python-basic{sep}files{sep}newdata.txt", "w")
# for text in f4:
#     f5.write(data)
# f4.close()
# f5.close()


# img = open(f"{path}{sep}python-basic{sep}files{sep}images{sep}artistic.png", "rb")

# img2 = open(f"{path}{sep}python-basic{sep}files{sep}images{sep}love.png", "wb")

# # for info in img:
# #     print(info)

# for code in img:
#     img2.write(code)
    
# img2.close()
# img.close()


""" Comments in Python """

# this is a comment
# this is another comment


""" Linear Search """

# pos = -1
# def linearSearch(li, key):
#     i = 0
#
#     while i < len(li):
#         if key == li[i]:
#             # globals()['pos'] = i
#             global pos
#             pos = i
#             return True
#         i = i + 1
#     return False
#
#
# li = [5, 8, 4, 6, 9, 2]
# key = int(input("Enter a key to search in the list >> "))
#
# if linearSearch(li, key):
#     print(f"{key} found at index {pos}.")
# else:
#     print(f"{key} not found in the list.")
#
# print("Bye..")


""" Binary Search """

# pos = -1
# def binSearch(li, key):
#     low = 0
#     high = len(li) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#         if key < li[mid]:
#             high = mid - 1
#         elif key > li[mid]:
#             low = mid + 1
#         elif key == li[mid]:
#             global pos
#             pos = mid
#             return True
#         else:
#             return False
#
#
# li = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# key = int(input("Enter a key to search in the list >> "))
#
# if binSearch(li, key):
#     print(f"{key} found at index {pos}.")
# else:
#     print(f"{key} not found in the list.")
#
# print("Bye..")


""" Bubble Sort """

# def bubbleSort(li):
#     for i in range(len(li)-1, 0, -1):
#         for j in range(i):
#             if li[j] > li[j+1]:
#                 li[j], li[j+1] = li[j+1], li[j] #pythonic swapping
#                 # temp = li[j]
#                 # li[j] = li[j+1]
#                 # li[j+1] = temp
#
#
#
# li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
# print("Given List: ", li)
# bubbleSort(li)
# print("Sorted List: ", li)


""" Selection Sort """


# def selectionSort(li):
#     for i in range(len(li)):
#         min_index = i
#         for j in range(i+1, len(li)):
#             if li[j] < li[min_index]:
#                 min_index = j
#         li[min_index], li[i] = li[i], li[min_index]
#         # print(li)
#
#
# li = [4, 9, 2, 3, 5, 7, 8, 1, 6]
# print("Given List: ", li)
# selectionSort(li)
# print("Sorted List: ", li)


""" MySQL Workbench """

# # installing mysql workbench

""" python database connectivity """

# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="zij112489", database="shangshaptak")
# # this database doesn't exist..so create this and check again later
# mycursor = mydb.cursor()
# mycursor.execute("select * from team_members ")
# for i in mycursor:
#     print(i)

""" python, git, pycharm, github """




