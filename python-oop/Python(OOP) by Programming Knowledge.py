# OBJECT ORIENTED PROGRAMMING
# OOPS
# class, objects
# # # ex-01
# class Car:  # empty class
#     pass
#
# # # creating instances of class
# ford = Car()  # object i.e. instance of class Car
# honda = Car()  # object
# audi = Car()  #object
# #
# ford.speed = 200  # attribute
# honda.speed = 220  # attribute
# audi.speed = 250  # attribute
# #
# ford.color = "red"  # attribute
# honda.color = "blue"  # attribute
# audi.color = "black"  # attribute
#
# print(ford.speed)
# print(ford.color)
#
# ford.speed = 300
# ford.color = "blue"
# #
# print(ford.speed)
# print(ford.color)
# ======================================================

# # # ex-02
# #
# class Rectangle:
#     pass
#
# rect1 = Rectangle()  # object
# rect2 = Rectangle()  # object
# #
# rect1.width = 40  # attribute
# rect2.width = 10  # attribute
# rect1.height = 20  # attribute
# rect2.height = 30  # attribute
# #
# print(f"Area of rectangle 1: {rect1.height*rect1.width}")
# print(f"Area of rectangle 2: {rect2.height*rect2.width}")

# # =====================================================
# # # ex-03
# # # using init method
# # # using self keyword
# #
# class Rectangle:
#     def __init__(self, height, width):  # constructor
#         # print("the __init__ is called.")
#         self.height = height
#         self.width = width
#
#     def area(self):
#         area = self.width*self.height
#         return area
#
#
# rect1 = Rectangle(40, 20)  # object
# rect2 = Rectangle(10, 30)  # object
#
# print(f"Area of rectangle 1: {rect1.area()}")
# print(f"Area of rectangle 1 : {Rectangle.area(rect1)}")
# print(f"Area of rectangle 2: {rect2.area()}")
# print(f"Area of rectangle 2 : {Rectangle.area(rect2)}")

# # =======================================================
# # # ex-04
# class Hello:
#     def __init__(self, name=""):
#         self.name = name
#         self.age = 24
#         print("__init__")
#
#
# hello_again = Hello()
# hello = Hello("Zahid")
# print(hello.name)
# print(hello.age)
# print(hello_again.age)

# =======================================================
# # #encapsulation in python
# # # # ex-01
# class Car:
#     def __init__(self, speed, color):
#         self.__speed = speed
#         self.__color = color
#         # self.speed = speed
#         # self.color = color
#
#     # setter i.e mutator
#     def set_speed(self, value):
#         self.__speed = value
#         # self.speed = value
#
#     # getter i.e. accessor
#     def get_speed(self):
#         return self.__speed
#         # return self.speed
#
#     # setter i.e mutator
#     def set_color(self, val):
#         self.__color = val
#         # self.color = val
#
#     # getter i.e. accessor
#     def get_color(self):
#         return self.__color
#         # return self.color
#
#     def __gt__(self, other):
#         return self.__speed > other.__speed
#         # return self.speed > other.speed
#
# #
# ford = Car(200, "red")
# honda = Car(250, "blue")
# audi = Car(300, "black")
# #
# # ford.set_speed(350)
# #
# if ford > honda and ford > audi:
#     print("Ford is the speediest")
# elif audi > honda and audi > ford:
#     print("Audi is the speediest")
# elif honda > ford and honda > audi:
#     print("Honda is the speediest")
# #
# # #
# # # # ford.speed = 400
# # ford.set_speed(350)
# # # # ford.__speed = 280
# # #
# # print(ford.speed)
# print(f"speed of ford: {ford.get_speed()}")
# print(f"color of ford: {ford.get_color()}")
# # print(ford.__color)
# # # print(ford.color)
# # #
# audi.set_color("Dark")
# print(audi.get_color())
#

# # ===========================================================
# # # ex-02
# class Hello:
#     def __init__(self):
#         self.a = 10
#         self._b = 20
#         self.__c = 30  # private or protected
#         # print(self.__c)

#
# hello = Hello()
# print(hello.a)
# print(hello._b)
# # print(hello.__c)
# print()
# # print(hello._Hello__c)


# ===========================================================
# # # ex-03
# class Rectangle:
#     def __init__(self, height, width):  # constructor
#         # print("the __init__ is called.")
#         self.__height = height
#         self.__width = width
#
#     def set_height(self, h):
#         self.__height = h
#
#     def set_width(self, w):
#         self.__width = w
#
#     def get_height(self):
#         return self.__height
#
#     def get_width(self):
#         return self.__width
#
#     def area(self):
#         area = self.__width*self.__height
#         return area
#
#     def perimeter(self):
#         perimeter = 2*(self.__height + self.__width)
#         return perimeter
#
# #
# rect1 = Rectangle(40, 20)  # object
# rect2 = Rectangle(10, 30)  # object
# print("Before..\n")
# print(f"Area of rectangle 1: {rect1.area()}")
# print(f"Area of rectangle 2: {rect2.area()}")
# print(f"Perimeter of rectangle 1: {rect1.perimeter()}")
# print(f"Perimeter of rectangle 2: {rect2.perimeter()}")
#
# rect1.set_height(55)
# rect1.set_width(45)
#
# rect2.set_height(75)
# rect2.set_width(60)
#
# print("After..\n")
# print(f"Area of rectangle 1: {rect1.area()}")
# print(f"Area of rectangle 2: {rect2.area()}")
# print(f"Perimeter of rectangle 1: {rect1.perimeter()}")
# print(f"Perimeter of rectangle 2: {rect2.perimeter()}")


# # ===========================================================
# # # defining a private method
# #
# class Hello:
#     def __init__(self):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
# #
# #     # this method is public
# #     # it can access all private and public..
# #     # ..variables of this class..
# #     # ..and can be called from outside the class
#     def public_method(self):
#         print("I am inside public_method()")
#         print(self.a)
#         print(self._b)
#         print(self.__c)
# #
# #     # this method is private..
# #     # so can only be accessed inside the class..
# #     # ..cannot be accessed or called from..
# #     # ..outside the class
#     def __private_method(self):
#         print("I am inside __private_method()")
#         print(self.a)
#         print(self._b)
#         print(self.__c)
# #
#     def calling_method(self):
#         print("> Calling public method inside the class: ")
#         self.public_method()
#         print("> Calling private method inside the class: ")
#         self.__private_method()
#
# #
# hello = Hello()
# # print("## Calling public method from outside of the class")
# # hello.public_method()
# #
# # print("## Calling private method from outside of the class")
# # hello.__private_method()  # this call will led to traceback..
# # # # ..not possible calling from outside the class Hello.
# #
# print("## Calling the 'calling' method outside the class")
# hello.calling_method()

# # # =======================================================
# # # python inheritance
# # # super class i.e. parent class
# class Polygon:
#     __width = None  # private # class variable
#     __height = None  # private # class variable
#
#     def __init__(self):
#         pass
#
#     def set_data(self, w, h):
#         self.__width = w
#         self.__height = h
#
#     def get_width(self):
#         return self.__width
#
#     def get_height(self):
#         return self.__height
#
#
# # # # subclass i.e.child class
# class Rectangle(Polygon):
#     def area(self):
#         # return self.__width * self.__height # gives value error
#         return self.get_width() * self.get_height()
#
# #
# # # # sub class i.e.child class
# class Triangle(Polygon):
#     def area(self):
#         # return (self.__width * self.__height)/2  # value error..private variables are not accessible
#         return (self.get_width() * self.get_height()) / 2
# #
# #
# # # # child class can access public variables, methods of..
# # # # .. a parent class. not the private variables and methods
# #
# rect = Rectangle()
# tri = Triangle()
# # #
# rect.set_data(40, 30)
# tri.set_data(40, 30)
# print(f"Area of rectangle:  {rect.area()}")
# print(f"Area of triangle:  {tri.area()}")
# #

# # # ==========================================================
# import math
#
# # creating module in python
# # module creating codes..
# # .. goes into dir/arithemetica.py
# # ***************************************************
# # # part-01
# # def add(a, b):
# #     return a + b
# #
# # def sub(a, b):
# #     return a - b
# #
# # def multi(a, b):
# #     return a*b
# #
# # def div(a, b):
# #     return a/b
# #
# # def power(a, b):
# #     return a**b
# #
# # if __name__ == "__main__":
# #     x, y = 8, 3
# #     print(f"Addition: {add(x, y)}")
# #     print(f"Subtraction: {sub(x, y)}")
# #     print(f"Multiplication: {multi(x, y)}")
# #     print(f"Division: {div(x, y)}")
# #     print(f"Power: {power(x, y)}")
# # ****************************************************
# # # part-02
# from dir import arithmetica
#
# print(arithmetica.add(8, 5))
# print(arithmetica.sub(8, 5))
# print(arithmetica.multi(8, 4))
# print(arithmetica.div(8, 4))
# print(arithmetica.power(8, 4))
# print(arithmetica.power(2,8))
# # part-03
# import dir.arithmetica as ar
# print(ar.sub(9, 4))
# print(ar.power(9, 3))

# # =======================================================
# # multiple inheritance in python
# # example using geometric, geometric, rectangle, triangle, main
# class Shape:
#     __color = None
#
#     def set_color(self, color):
#         self.__color = color
#
#     def get_color(self):
#         return self.__color
# #
#
# class Polygon:
#     __width = None
#     __height = None
#
#     def __init__(self):
#         pass
#
#     def set_data(self, w, h):
#         self.__width = w
#         self.__height = h
#
#     def get_width(self):
#         return self.__width
#
#     def get_height(self):
#         return self.__height
#
#
# class Rectangle(Polygon, Shape):
#     def area(self):
#         return self.get_width() * self.get_height()
#
#
# class Triangle(Polygon, Shape):
#     def area(self):
#         return (self.get_width() * self.get_height()) / 2
#
# #
# if __name__ == "__main__":
#     rect = Rectangle()
#     tri = Triangle()
#
#     rect.set_data(40, 30)
#     tri.set_data(40, 30)
#
#     rect.set_color("red")
#     tri.set_color("blue")
#
#     print(f"Area of rectangle:  {rect.area()}")
#     print(f"Area of triangle:  {tri.area()}")
#
#     print(f"Rectangle is {rect.get_color()}")
#     print(f"Triangle is {tri.get_color()}")

# # =====================================================
# # using built-in function super() in python classes
# # super() function
#
# class Parent:
#     def __init__(self, name):
#         print("Parent __init__", name)
#
#
# class Parent2:
#     def __init__(self, name):
#         print("Parent2 __init__", name)
#
#
# class Child(Parent, Parent2):
#     def __init__(self):
#         print("Child __init__")
#         super().__init__("Max")  # this goes to Parent class not Parent2 class
#         # so how to call Parent2? solution...
#         print()
#         Parent2.__init__(self, "Tim")
#         Parent.__init__(self, "Jim")
#
#
# child = Child()
# print(Child.__mro__) # method resolution order


# # =====================================================
# # operator overloading in python
# # everything is object in python
# print(2 + 2) # + is addition operator here
# print('2' + '2') # + is concatenation operator here
# # '+' operator is overloaded here
# print(2 * 8)
# print('2' * 8)
# '*' operator is overloaded here

# # ex-01
# class Number:
#     def __init__(self, num):
#         self.num = num
#
#     # solution
#     def __add__(self, other):
#         return self.num + other.num
#
#
# n1 = Number(1)
# n2 = Number(2)
#
# n = n1 + n2  # adding two Number object..not two numbers..
# # # ..directly adding two objects will return error..
# # # ..operator overloading can solve this
# # #  n1 -> self, n2 -> other
# print(n)
# print(n1.__add__(n2))
# print(Number.__add__(n1,n2))
# #
# x = Number(5)
# y = Number(7)
# print(x.__add__(y))
# print(Number.__add__(x, y))
# print(x + y)

# class A:
#     pass
# print(dir(A))
# a = dir(A)
# print(a)

# # ex-02
# # overloading plus(+),
# greater than(>)..
# ..less then(<) operator
# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius
#
#     def setRadius(self, r):
#         self.__radius = r
#
#     def getRadius(self):
#         return self.__radius
#
#     def area(self):
#         return pi * self.__radius ** 2
#
#     def __add__(self, circle_object):
#         R = self.__radius + circle_object.__radius
#         return Circle(R)
#
#     def __lt__(self, circle_object):
#         return self.__radius < circle_object.__radius
#
#     def __gt__(self, circle_object):
#         return self.__radius > circle_object.__radius
#
#     def __eq__(self, other):
#         return self.__radius == other.__radius
#
#     def __str__(self): # __str__ is used by built-in print() function
#         return f"Circle Area: {str(self.area())}"
#
#
# c1 = Circle(2)
# c2 = Circle(3)
# c3 = c1 + c2 # i.e. c3 = Circle(5)...from Circle(R)
# # c3 = Circle.__add__(c1, c2)
# # # c3 = c1.__add__(c2) # both are same..above one and this one
# print(c1.getRadius())
# print(c1.area())
# print(c2.getRadius())
# print(c2.area())
# print(c3.getRadius())
# print(c3.area())
# print(c1 < c2)  # c1.__lt__(c2)
# print(c1 > c2)  # c1.__gt__(c2)
# print(c3 > c2)  # c3.__gt__(c2)
# print(c1 == c2)
# print(c1 == c3)
# print(c2 == c3)
# print(c2.__eq__(c3))
# print(c1)
# print(c2)
# print()
# print(c3)
# print(c3.__str__())
# print(Circle.__str__(c3))
# print(str(c3))

# # # # =====================================================
# # # what is composition
# # # how to use class composition in python
# #
# class Salary:  # content class
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#
#     def annual_salary(self):
#         return (self.pay * 12) +  self.bonus
#
# #
# # #
# class Employee:  # container class
#     # Employee class(container) contains..
#     # ..content of Salary class
#     def __init__(self, name, age, pay, bonus):
#         self.name = name
#         self.age = age
#         self.obj_salary = Salary(pay, bonus) # instantiation fo Salary Class....
#         # ...inside Employee Class
#         # ... not a independent object
#
#     def total_salary(self):
#         return self.obj_salary.annual_salary()
#
# #
# emp = Employee("Max", 25, 12000, 10000)
# print(emp.total_salary())

# # # =====================================================
# # aggregation in python
# # using class aggregation in python
#
# class Salary:
#     def __init__(self, pay, bonus):
#         self.pay = pay
#         self.bonus = bonus
#
#     def annual_salary(self):
#         return (self.pay * 12) + self.bonus
#
#
# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.obj_salary = salary # passing a copy of salary object
#
#     def total_salary(self):
#         return self.obj_salary.annual_salary()
#
#
# salary = Salary(12000, 10000) # independent object
# emp = Employee("Max", 25, salary)
# print(emp.total_salary())

# # # =====================================================

# # abstract classes in python
# # creating abstract class with builtin module
# # using abc module
# #
# from abc import ABC, abstractclassmethod
#
#
# class Shape(ABC):
#     @abstractclassmethod  # decorator
#     def area(self): # must be implemented in subclass
#         pass
#
#     @abstractclassmethod
#     def perimeter(self): # must be implemented in subclass
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.__side = side
#
#     def area(self):
#         return self.__side ** 2
#
#     def perimeter(self):
#         return 4 * self.__side
#
#
# # geometric = Shape()  # instantiation of abstract class should not be possible
# square = Square(5)
# print(f"Area: {square.area()}")
# print(f"Perimeter: {square.perimeter()}" )
