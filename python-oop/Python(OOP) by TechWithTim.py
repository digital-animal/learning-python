# # # 01 OOP in Python - Intro

# in python everything is object
# i.e integer, list, string, dictionary...everything
import turtle
# x = 5
# y = "string"
# f = 5.5
# print(type(x))
# print(type(y))
# help(int)
# print(x.__add__(6))
# print(x.__mul__(6))
# print(f.__round__())

# help(str)
# print(y.upper())

# z = turtle.Turtle()

# def fun(x):
#     return x + 1
#
#
# print(fun(5))

#___________________________________________
# # # 02 OOP in Python - Creating Classes
# class Dog:
#     def __init__(self, name, age):  # constructor
#         self.name = name
#         self.age = age
#     def speak(self):
#         print(f"My favourite dog {self.name} and he is {self.age} years old.")
#     def setAge(self, age): # setter i.e. mutators
#         self.age = age
#     def getAge(self): # getter i.e. accessors
#         return self.age
#     def add_weight(self, weight):
#         self.weight = weight
# d1 = Dog("Tiger", 4)
# d2 = Dog("Mapple", 2)
# d1.speak()
# d2.speak()
# d1.setAge(8)
# d1.speak()
# print(f"my dog is {d2.getAge()} years old")
# print(f"my do is {d1.getAge()} years old")
# print(d1.age)
# print(d1.name)
# d3 = Dog("Drake", 9)
# d3.add_weight(18)
# print(d3.weight)

#__________________________________________________
# # 03 OOP in Python - inheritance
# # ex-01
# class Dog:  # parent class
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print(f"Name: {self.name} and Age: {self.age} years.")
#
#     def talk(self):
#         print("Bark!")
# class Cat(Dog):  # child class
#     def __init__(self, name, age, color):
#         super().__init__(name, age) # automatically adding self.name and self.age
#         self.color = color
#     def talk(self):  # method overriding
#         print("Meow")
#
# d1 = Dog("Drake", 5)
# d1.speak()
# d1.talk()
#
# c1 = Cat("Rabbit", 2, "White")
# c1.speak()
# c1.talk()

# # ex-02
# class Vehicle:
#     def __init__(self, price, gas, color):
#         self.price = price
#         self.gas = gas
#         self.color = color
#
#     def fillUpTank(self):
#         self.gas = 100
#
#     def emptyTank(self):
#         self.gas = 0
#
#     def gasLeft(self):
#         return self.gas
#
# class Car(Vehicle):
#     def __init__(self, price, gas, color, speed):
#         super().__init__(price, gas, color)
#         self.speed = speed
#
#     def beep(self):
#         print("Beep! Beep!")
#
#
# class Truck(Vehicle):
#     def __init__(self, price, gas, color, tire):
#         super().__init__(price, gas, color)
#         self.tire = tire
#
#     def beep(self):
#         print("Honk! Honk!")
#
#
#
# c1 = Car(2000, 20, "Red", 145)
# c1.beep()
# print(f"for Car C1 ..\nPrice:{c1.price}  Gas:{c1.gas}  Color:{c1.color}  Speed:{c1.speed}")
# print(end="\n")
# t1 = Truck(3000, 50, "Dark", 6)
# t1.beep()
# print(f"for Truck T1 ..\nPrice:{t1.price}  Gas:{t1.gas}  Color:{t1.color}  Tire:{t1.tire}")


# #_____________________________________________
# # # 04 OOP in Python - Overloading Methods
# # operator overloading
# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         self.coordinate = (self.x, self.y)
#
#     def move(self, x, y):
#         self.x += x
#         self.y += y
#
#     def __add__(self, p):
#         return Point(self.x + p.x, self.y + p.y)
#     def __sub__(self, p):
#         return Point(self.x - p.x, self.y - p.y)
#     def __mul__(self, p):
#         return self.x*p.x + self.y*p.y
#     def __str__(self):
#         return f"({str(self.x)}, {str(self.y)})"
#
#
#     def length(self):
#         from math import sqrt
#         return sqrt(self.x**2 + self.y**2)
#
#     # def __len__(self):
#     #     from math import sqrt
#     #     return sqrt(self.x**2 + self.y**2)
#
#     # comparing
#     def __gt__(self, p):
#         return self.length() > p.length()
#     def __ge__(self, p):
#         return self.length() >= p.length()
#     def __lt__(self, p):
#         return self.length() < p.length()
#     def __le__(self, p):
#         return self.length() <= p.length()
#     def __eq__(self, p):
#         return self.x == p.x and self.y == p.y
#
#
# p1 = Point(3, 4)
# p2 = Point(3, 4)
# p3 = Point(1, 3)
# p4 = Point(0, 1)
# p5 = p1 + p2
# p6 = p4 - p1
# p7 = p2 * p3
# print(f"{p5}\n{p6}\n{p7}")
# print(p1 == p2)
# print(p1 > p2)
# print(p1 >= p2)
# print(p1 < p2)
# print(p1 <= p2)

# # # 05 OOP in Python - Static Methods and Class Methods
# # # types of class
# # # class variable vs instance variable
#
# class Dog:
#     dogs = []
#
#     def __init__(self, name):
#         self.name = name
#         self.dogs.append(self)
#
#     @classmethod  # decorators
#     def num_dogs(cls):
#         return len(cls.dogs)
#
#     @staticmethod  # decorators
#     def bark(n):
#         """barks n times"""
#         for i in range(n):
#             print("Bark! ")
#
#
#
# # print(Dog.num_dogs())
# tim = Dog("Tim")
# jim = Dog("Jim")
# # print(Dog.dogs)
# # print(Dog.num_dogs())
# # Dog.bark(5)

# #_________________________________________________
# # # 006 OOP in Python - Public and Private Classes
# # # types of classes
#
# class _Private:
#     def __init__(self, name):
#         self.name = name
#
# class NonPrivate:
#     def __init__(self, name):
#         self.name = name
#         self.priv = _Private(name)
#
#     def _display(self):
#         print("Hello")
#     def display(self):
#         print("Hi")