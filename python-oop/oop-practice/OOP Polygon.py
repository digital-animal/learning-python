# ================================================
# ================ Class Polygon =================
# ================================================
from abc import ABC, abstractclassmethod

class Polygon(ABC):
    __color = None
    @abstractclassmethod
    def area(self):
        pass
    @abstractclassmethod
    def perimeter(self):
        pass

class Triangle(Polygon):
    index = 1
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.id = Triangle.index
        Triangle.index += 1
    def get_base(self):
        return self.base
    def get_height(self):
        return self.height
    def set_base(self, b):
        self.base = b
    def set_height(self, h):
        self.height = h
    def area(self):
        return 0.5*self.base*self.height
    def perimeter(self):
        pass
    def __str__(self):
        return f"Triangle_{str(self.id).zfill(3)} [base: {self.get_base()}, height: {self.get_height()}, area: {self.area()}, perimeter: {self.perimeter()}]"


class Square(Polygon):
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


class Rectangle(Polygon):
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


t1 = Triangle(4,9)
# print(t1.get_base())
# print(t1.get_height())
# print(t1.area())
print(t1)

t2 = Triangle(9,2)
print(t2)
t3 = Triangle(8,6)
print(t3)
print()
s1 = Square(8)
# print(s1.get_side())
# print(s1.area())
# print(s1.perimeter())
print(s1)
s2 = Square(12)
print(s2)
print()
r1 = Rectangle(4,9)
# print(r1.get_width())
# print(r1.get_height())
# print(r1.area())
# print(r1.perimeter())
print(r1)
r2 = Rectangle(9,2)
print(r2)
r3 = Rectangle(10,8)
print(r3)
