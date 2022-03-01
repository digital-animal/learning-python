# ===========================================
# ============= Class Rectangle =============
# ===========================================
from abc import ABC
from abc import ABCMeta
from abc import abstractmethod
import math

# class Quadrilateral(metaclass=ABCMeta):
class Quadrilateral(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Parallelogram(Quadrilateral):
    index = 1
    def __init__(self,a, b, d1, d2):
        super().__init__()
        self.a = a
        self.b = b
        self.d1 = d1
        self.d2 = d2
        self.id = Parallelogram.index
        Parallelogram.index += 1

    def get_a(self):
        return self.a
    def get_b(self):
        return self.b

    def get_d1(self):
        return self.d1
    def get_d2(self):
        return self.d2

    def set_a(self, a):
        self.a = a
    def set_b(self, b):
        self.b = b

    def set_d1(self, d1):
        self.d1 = d1
    def set_d2(self, d2):
        self.d2 = d2

    def area(self):
        return Parallelogram.triangle_area(self.a,self.b,self.d1)*2
    def perimeter(self):
        return 2*(self.a+self.b)
    @staticmethod
    def triangle_area(x,y,z):
        assert x + y > z and y + z > x and z + x > y
        s = (x + y + z)/2
        area = math.sqrt(s*(s-x)*(s-y)*(s-z))
        return area
    def __str__(self):
        return f"Parallelogram_{str(self.id).zfill(3)} [a: {self.a}, b: {self.b}, d1: {self.d1}, d2: {self.d2}, area: {round(self.area(), 2)}, perimeter: {self.perimeter()}]"

class Rhombus(Parallelogram):
    index = 1
    def __init__(self,a,b,d1,d2):
        if b is not None:
            assert a == b
        super().__init__(a,b,d1,d2)
        self.id = Rhombus.index
        Rhombus.index += 1
    def area(self):
        return 0.5*self.d1*self.d2
    def __str__(self):
        return f"Rhombus_{str(self.id).zfill(3)} [a: {self.a}, b: {self.b}, d1: {self.d1}, d2: {self.d2}, area: {self.area()}, perimeter: {self.perimeter()}]"


class Rectangle(Parallelogram):
    index = 1
    def __init__(self, width, height,d1=None,d2=None):
        super().__init__(width,height,d1,d2) # correct here
        self.set_width(width)
        self.set_height(height)
        # try:
        #     self.d1 = self.d2 = math.sqrt(self.width**2+self.height**2)
        # except Exception as e:
        #     print(e)
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
        return 2*(self.width + self.height)
    def __str__(self):
        return f"Rectangle_{str(self.id).zfill(3)} [Width: {self.get_width()}, Height: {self.get_height()}, Area: {self.area()}, Perimeter: {self.perimeter()}]"


class Square(Rectangle, Rhombus):
    index = 1
    def __init__(self, side, side2=None):
        if side2 is not None:
            assert side == side2
        super().__init__(side, side2) # correct here
        self.set_side(side)
        self.id = Square.index
        Square.index += 1
    def get_side(self):
        return self.side
    def set_side(self, side):
        self.side = side
    def area(self):
        return self.get_side()**2
    def perimeter(self):
        return self.get_side()*4

    def __str__(self):
        return f"Square_{str(self.id).zfill(3)} [Side: {self.get_side()}, Area: {self.area()}, Perimeter: {self.perimeter()}]"

p1 = Parallelogram(5,12,13,13)
print(p1)
p2 = Parallelogram(10,10,18,16)
print(p2)
print()

r1 = Rhombus(10,10,18,10)
print(r1)
r2 = Rhombus(20,20,36,24)
print(r2)
r3 = Rhombus(28,28,36,42)
print(r3)

print()
rect1 = Rectangle(4,9)
print(rect1)
rect2 = Rectangle(12,8)
print(rect2)
print()

square1 = Square(10)
print(square1)
square2 = Square(6)
print(square2)
square3 = Square(4,4)
print(square3)