# # class
# # object
# # method

# class Computer:
#     def config(self):
#         print("i5, 16GB, 256GB")
#
#
# comp1 = Computer()
# print(type(comp1))
# comp1.config()
# Computer.config(comp1) # same as previous line
#
# comp2 = Computer()
# comp2.config()
# Computer.config(comp2)


# # __init__ method in python
# # constructor

# class Computer:
#     def __init__(self, cpu, ram): # constructor
#         # print("in __init__")
#         self.cpu = cpu
#         self.ram = ram
#     def config(self):
#         print(f"Config: {self.cpu} - {self.ram}GB")
#
#
# comp1 = Computer("i7", 16)
# comp1.config()
# comp2 = Computer("Ryzen 3", 8)
# comp2.config()

# # constructor
# # self and comparing objects in python

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"Name = {self.name} and Age = {self.age}")
#     def compare(self, obj):
#         if self.age == obj.age:
#             return True
#         else:
#             return False
#
#
# c1 = Person("Navin", 30)
# print(id(c1))
# c1.display()
#
#
# c2 = Person("Rashi", 22)
# print(id(c2))
# c2.display()
#
# c3 = Person("Zubin", 30)
# print(id(c3))
# c3.display()
#
# print("Comparing object c1 and c2")
# if c1.compare(c2):
#     print("objects are same")
# else:
#     print("objects are not same")
#
# print("Comparing object c1 and c3")
# if c1.compare(c3):
#     print("objects are same")
# else:
#     print("objects are not same")


# # types of variable
# # instance variable
# # class variable i.e. static variable

# class Car:
#     wheels = 4 # class variable outside __init__
#     def __init__(self):
#         self.mil = 10  # instance variable i.e. object variable
#         self.com = "BMW"
#
# c1 = Car()
# c2 = Car()
#
# c1.mil = 8 # c1.mil is changed now..overriding default class variable
# # as c1 is object variable(instance variable) only object cant  modify this
#
# Car.wheels = 5 # class variable can only be modified by class
#
# print("C1:", c1.com, c1.mil, c1.wheels)
# print("C2:", c2.com, c2.mil, c2.wheels)

# # methods in python
# instance methods
# class methods
# static methods

# class Student:
#     school = "Telusko" #class variable i.e static variable
#
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1  # instance variable
#         self.m2 = m2  # instance variable
#         self.m3 = m3  # instance variable
#
#     def avg(self): # instance method
#         return (self.m1 + self.m2 + self.m3)/3
#
#     def get_m1(self): # accessor # instance method
#         return self.m1
#
#     def get_m2(self): # accessor # instance method
#         return self.m2
#
#     def get_m3(self): # accessor # instance method
#         return self.m3
#
#     def set_m1(self, marks): # mutator # instance method
#         self.m1 = marks
#
#     def set_m2(self, marks): # mutator # instance method
#         self.m2 = marks
#
#     def set_m3(self, marks): # mutator # instance method
#         self.m3 = marks
#
#     def print_marks(self):
#         print(f"{self.m1}, {self.m2}, {self.m3}")
#
#     @classmethod # decorators
#     def getSchoolName(cls): # class methods # self replaced by cls
#         return cls.school
#
#     @staticmethod # decorators
#     def info():  # static method
#         print("this is static method in Student class")
#
#
# s1 = Student(67, 75, 95)
# s1.print_marks()
# print("Student 1: ", s1.avg())
# print()
# s2 = Student(89, 92, 55)
# print("Student 2: ", s2.avg())
# s2.print_marks()
# print()
# print(s1.get_m1())
# s1.set_m1(84)
# s1.print_marks()
# print()
#
# s1.info()
# Student.info()
# print()
#
# print(s1.getSchoolName())
# print(Student.getSchoolName())


# # inner class in python
# # class inside class
#
# class Student:
#     def __init__(self, name, roll):
#         self.name = name
#         self.roll = roll
#         self.lap = self.Laptop()
#         # inner class Laptop object is created..
#         # just outside the inner class..
#         # but inside the outer class..
#         # self.lap is outer class(Student)..
#         # object of inner class Laptop now..
#
#     def show(self):
#         print(self.name, self.roll)
#         self.lap.show()
#
#     class Laptop:
#         def __init__(self):
#             self.brand = "HP"
#             self.CPU = "i5"
#             self.RAM = 8
#
#         def show(self): # function overriding
#             print(self.brand, self.CPU, self.RAM)
#
#
# s1 = Student("Jewel", 81)
# s2 = Student("Raju", 79)
# print(s1.name, s1.roll)
# print(s2.name, s2.roll)
# s1.show()
# s2.show()
# print()
#
# print(s1.lap.brand, s1.lap.CPU, s1.lap.RAM)
# print()
#
# lap1 = s1.lap
# print(s1.name, lap1.brand, lap1.CPU, lap1.RAM)
# print(id(lap1))
# print()
#
# lap2 = s2.lap
# print(id(lap2))
# print(s2.name, lap2.brand, lap2.CPU, lap2.RAM)
# print()
#
# lap3 = Student.Laptop()
# # creating object of inner class..
# # # outside of outer class..
# # # inner class must be mentioned with dot(.)..
#
# print(lap3.brand, lap3.CPU, lap3.RAM)
# print()
#
# s1.show()
# print()
#
# lap3.show()


# # inheritance in python
# # oop
# # single level inheritance
# # multi level inheritance

# class A:
#     def __init__(self):
#         pass
#
#     def feature1(self):
#         print("Feature 1 working")
#
#     def feature2(self):
#         print("Feature 2 working")
#
# class B(A):# class B inherits class A
#     def __init__(self):
#         super().__init__()
#         pass
#
#     def feature3(self):
#         print("Feature 3 working")
#
#     def feature4(self):
#         print("Feature 4 working")
#
# class C(B): # C inherits class B and so class A
#     def __init__(self):
#         super().__init__()
#         pass
#
#     def feature5(self):
#         print("Feature 5 working")
#
#
# print("Parent Class Object")
# a1 = A()
# a1.feature1()
# a1.feature2()
# print(end="\n")
#
# print("Child Class Object")
# b1 = B()
# b1.feature1()
# b1.feature2()
# b1.feature3()
# b1.feature4()
#
# print(end="\n")
# print("Grand Child Class Object")
# c1 = C()
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()


# # multiple inheritance
# # oop

# class A:
#     def __init__(self):
#         pass
#
#     def feature1(self):
#         print("Feature 1 working")
#     def feature2(self):
#         print("Feature 2 working")
#
# class B:
#     def __init__(self):
#         pass
#
#     def feature3(self):
#         print("Feature 3 working")
#     def feature4(self):
#         print("Feature 4 working")
#
# class C(A, B): # C inherits class A & class B
#     def __init__(self):
#         super().__init__()
#         pass
#
#     def feature5(self):
#         print("Feature 5 working")
#
# print("Parent1 Class Object")
# a1 = A()
# a1.feature1()
# a1.feature2()
# print(end="\n")
#
# print("Parent2 Class Object")
# b1 = B()
# b1.feature3()
# b1.feature4()
#
# print(end="\n")
# print("Child Class Object")
# c1 = C()
# c1.feature1()  # from class A
# c1.feature2()  # from class A
# c1.feature3()  # from class B
# c1.feature4()  # from class B
# c1.feature5()  # c's own method


# # constructor in inheritance in python
# # method resolution order (MRO)
# # single level inheritance
# # multi level inheritance
# # multiple inheritance
# ex-01
# for single level inheritance

# class A:
#     def __init__(self):
#         print("in A __init__")
#
#     def feature1A(self):
#         print("Feature 1 of A")
#
#     def feature2A(self):
#         print("Feature 2 of A")
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("in B __init__")
#
#     def feature1B(self):
#         print("Feature 1 of B")
#
#     def feature2B(self):
#         print("Feature 2 of B")
#
# a1 = A()
# b1 = B()
# print(end="\n")
# print("***Object A***")
# a1.feature1A()
# a1.feature2A()
# print(end="\n")
#
# print("***Object B***")
# b1.feature1A()
# b1.feature2A()
# b1.feature1B()
# b1.feature2B()


# # ex-02
# # for multiple inheritance

# class A:
#     def __init__(self):
#         print("in A __init___")
#     def feature1A(self):
#         print("Feature 1 of A")
#     def feature2A(self):
#         print("Feature 2 of A")
#
# class B:
#     def __init__(self):
#         print("in B __init__")
#     def feature1B(self):
#         print("Feature 1 of B")
#     def feature2B(self):
#         print("Feature 2 of B")
#
# class C(A, B):
#     def __init__(self):
#         super().__init__()
#             # inherits A's constructor
#             # doesn't inherit C's constructor
#             # using MRO(method resolution order)
#             # LEFT to RIGHT
#         print("in C __init__")
#
#     def feature1C(self):
#         print("Feature 1 of C")
#     def feature2C(self):
#         print("Feature 2 of C")
#
#     def feat(self):
#         super().feature2A()
#
# a1 = A()
# b1 = B()
# c1 = C()
#
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
#
# print("***Object C***")
# c1.feature1C()
# c1.feature2C()
# print(end="\n")
# c1.feat()


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

# class PyCharm:
#     def execute(self):
#         print("compiling...")
#         print("running...")
#         print(("debugging..."))
#
# class MyEditior:
#     def execute(self):
#         print("Spell Check..")
#         print("Convention Check..")
#         print("Unit Test..")
#         print("compiling...")
#         print("running...")
#         print(("debugging..."))
#
# class Laptop:
#     def code(self, IDE):
#         IDE.execute()
#
# ide = PyCharm()
# # ide = MyEditior()
#
# lap1 = Laptop()
# lap1.code(ide)


# # operator overloading in python
# # polymorphism


# a = 5
# b = "World"
# print(a + b)
    # # in python 'int' is not integer type
    # # 'int' is an object of class type
# a = 5
# b = 6
# print(a + b)
# print(a.__add__(b))
# print(int.__add__(a, b))

# p = '5'
# q = '6'
# print(p+q)
# print(p.__add__(q))
# print(str.__add__(p, q))

# a = 9
# print(a)
# print(a.__str__())

# example of operator overloading
# class Student:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s0 = Student(m1, m2) # object s0 created of Student class
#         return s0
#
#     def __gt__(self, other):
#         self_marks = self.m1 + self.m2
#         other_marks = other.m1 + other.m2
#         if self_marks > other_marks:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         # return self.m1, self.m2  # return a tuple
#         # return "{} {}".format(self.m1, self.m2)
#         return f"({self.m1}, {self.m2})"
#
# s1 = Student(58, 69)
# s2 = Student(60, 95)
# #
# s3 = s1 + s2
# # s3 = Student.__add__(s1, s2)
#     # # '+' operator is overloaded here
#     # # it adds two object s1 & s2
#     # # s1 + s2 returns an object...
#     # # to s3 from def __add__(self, other)
# print(s3.m1)
# print(s3.m2)
#
# if s1 > s2:
#     print("s1 wins")
# else:
#     print("s2 wins")
#
# print(s1.__str__())
# print(s1)
# print(s2)
# print(s3)


# # method overloading
# # and method overriding
# # example method overriding
# class Studnet:
#     def __init__(self, m1, m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     # def sum(self, a=None, b=None, c=None):  # default argument
#     #     s = 0
#     #     if a!=None and b!=None and c!=None:
#     #         s = a + b + c
#     #     elif a!=None and b!=None:
#     #         s = a + b
#     #     else:
#     #         s = a
#     #     return s
#
#     def sum(self, a=0, b=0, c=0):  # default argument
#         # much better than previous one
#         s = a + b + c
#         return s
#
#
# s1 = Studnet(50, 60)
# print(s1.sum(5))
# print(s1.sum(5, 9))
# print(s1.sum(5, 9, 6))


# # now method overriding
# class A:
#     def show(self):
#         print("in A show")
#
# class B(A):
#     # pass
#     def show(self):
#         print("in B show")
#
# a1 = A()
# a1.show()
# b1 = B()
# b1.show()
