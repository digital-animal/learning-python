# ================================================
# ================ Class Polygon =================
# ================================================
from abc import ABC, abstractclassmethod
import math

class Shape(ABC):
    __color = None
    @abstractclassmethod
    def area(self):
        pass
    @abstractclassmethod
    def perimeter(self):
        pass

class Triangle(Shape):
    index = 1
    def __init__(self, a, b, c):
        assert (a + b > c) and (b + c > a) and (c + a > b)

        self.a = a
        self.b = b
        self.c = c
        self.id = Triangle.index
        Triangle.index += 1
    def get_a(self):
        return self.a
    def get_b(self):
        return self.b
    def get_c(self):
        return self.c
    def set_a(self, x):
        self.a = x
    def set_b(self, b):
        self.b = y
    def set_c(self, z):
        self.c = z
    def area(self):
        s = self.perimeter()/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        return area
    def perimeter(self):
        P = (self.a+self.b+self.c)
        return P
    def __str__(self):
        return f"Triangle_{str(self.id).zfill(3)} [a: {self.get_a()}, b: {self.get_b()}, c: {self.get_c()}, area: {self.area()}, perimeter: {self.perimeter()}]"


class Square(Shape):
    index = 1
    def __init__(self, side):
        self.side = side
        self.id = Square.index
        Square.index += 1
    def get_side(self):
        return self.side
    def set_side(self, l):
        self.side = l
    def area(self):
        return self.side**2
    def perimeter(self):
        return 4*self.side
    def __str__(self):
        return f"Square_{str(self.id).zfill(3)} [side: {self.get_side()}, area: {self.area()}, perimeter: {self.perimeter()}]"


class Rectangle(Shape):
    index = 1
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.id = Rectangle.index
        Rectangle.index += 1
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def set_width(self, w):
        self.width = w
    def set_height(self, h):
        self.height = h
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
    def __str__(self):
        return f"Rectangle_{str(self.id).zfill(3)} [width: {self.get_width()}, height: {self.get_height()}, area: {self.area()}, perimeter: {self.perimeter()}]"

class Circle(Shape):
    index = 1
    def __init__(self,radius):
        self.radius = radius
        self.id = Circle.index
        Circle.index += 1
    def get_radius(self):
        return self.radius
    def set_radius(self, r):
        self.radius = r
    def area(self):
        area = round(math.pi*self.radius**2,2)
        return area
    def perimeter(self):
        perimeter = round(2*math.pi*self.radius,2)
        return perimeter
    def __str__(self):
        return f"Circle_{str(self.id).zfill(3)} [radius: {self.get_radius()}, area: {self.area()}, perimeter: {self.perimeter()}]"

class Sphere(Circle):
    index = 1
    def __init__(self, radius):
        super().__init__(radius)
        self.id = Sphere.index
        Sphere.index += 1
    def get_radius(self):
        return super().get_radius()
    def set_radius(self, r):
        super().set_radius()
    def area(self):
        area = 4*math.pi*self.radius**2
        return area
    def volume(self):
        volume = round((4*math.pi*self.radius**3)/3, 2)
        return volume
    def __str__(self):
        return f"Sphere_{str(self.id).zfill(3)} [radius: {self.get_radius()}, area: {self.area()}, volume: {self.volume()}]"

t1 = Triangle(3,4,5)
t2 = Triangle(6,8,10)
t3 = Triangle(5,12,13)
# t4 = Triangle(5,6,12) # assertion error a + b > c
# t5 = Triangle(1,2,3) # assertion error a + b > c
print(t1)
print(t2)
print(t3)
# print(t4) # assertion error a + b > c
# print(t5) # assertion error a + b > c
print()

s1 = Square(8)
s2 = Square(12)
print(s1)
print(s2)
print()

r1 = Rectangle(4,9)
r2 = Rectangle(8,6)
r3 = Rectangle(10,8)
print(r1)
print(r2)
print(r3)
print()

c1 = Circle(10)
c2 = Circle(12)
print(c1)
print(c2)
print()

sp1 = Sphere(10)
print(sp1)