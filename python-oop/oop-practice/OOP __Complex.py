from abc import ABC, ABCMeta, abstractmethod
import math
class ComplexNumber(metaclass=ABCMeta):
    pass

class ComplexCartesian(ComplexNumber):
    def __init__(self,real,img=0):
        self.real = real
        self.img = img

    def conjugate(self):
        return ComplexCartesian(self.real, -self.img)
    def modulus(self):
        mod = round(math.sqrt(self.real**2+self.img**2), 2)
        return mod
    def argument(self):
        x = self.real
        y = self.img
        if x > 0 and y > 0:
            theta = round(abs(math.atan2(y, x))*(180/math.pi), 2)
            return theta
        elif x < 0 and y >= 0:
            theta = 180 - round(abs(math.atan2(y, x)) * (180 / math.pi), 2)
            return theta
        elif x < 0 and y < 0:
            theta = 180 + round(abs(math.atan2(y, x)) * (180 / math.pi), 2)
            return theta
        elif x > 0 and y < 0:
            theta = 360 - round(abs(math.atan2(y, x)) * (180 / math.pi), 2)
            return theta
        elif x == 0 and y == 0:
            return 0
        elif x == 0 and y > 0:
            return 90
        elif x == 0 and y < 0:
            return 270
        elif x > 0 and y == 0:
            return 0
        elif x < 0 and y == 0:
            return 180

    def cartesian(self):
        pass
    def euler(self):
        r = self.modulus()
        t = self.argument()

    def polar(self):
        pass
    def plot(self):
        pass
    def __add__(self, other):
        x = self.real + other.real
        y = self.img + other.img
        return ComplexCartesian(x,y)
    def __sub__(self, other):
        x = self.real - other.real
        y = self.img - other.img
        return ComplexCartesian(x, y)
    def __mul__(self, other):
        a1 = self.real
        b1 = self.img
        a2 = other.real
        b2 = other.img
        real = a1*a2 - b1*b2
        img = a1*b2 + a2*b1
        return ComplexCartesian(real, img)
    def __truediv__(self, other):
        a1 = self.real
        b1 = self.img
        a2 = other.real
        b2 = other.img
        real = round((a1*a2 + b1*b2)/(a2**2+b2**2),2)
        img = round((a2*b1 - a1*b2)/(a2**2+b2**2),2)
        return ComplexCartesian(real, img)

    def __str__(self):
        if self.img >0 and self.img > 1:
            return f"{self.real} + {self.img}i"
        if self.img >0 and self.img == 1:
            return f"{self.real} + i"
        elif self.img < 0 and abs(self.img) > 1:
            return f"{self.real} - {abs(self.img)}i"
        elif self.img < 0 and abs(self.img) == 1:
            return f"{self.real} - i"
        elif self.img == 0:
            return f" {self.real}"

class ComplexPolar(ComplexNumber):
    def __init__(self, radius , theta):
        self.radius  = radius
        self.theta = theta

    def __str__(self):
        if self.radius != 0:
            pass

class ComplexEuler(ComplexNumber):
    pass

# c1 = ComplexCartesian(1,1)
# c1 = ComplexCartesian(-1,-1)
# c1 = ComplexCartesian(3,4)
# c1 = ComplexCartesian(8,-6)
# print(c1)
# print(c1.conjugate())
# print(c1.modulus())
# print(c1.conjugate().modulus())
#
# print(c1.argument())

# c2 = ComplexCartesian(-3,5)
# c3 = ComplexCartesian(7,-2)
# c4 = c2 + c3
# print(c2)
# print(c3)
# print(c4)
# print(c4.modulus())
# print(c4.argument())
# print(c4.conjugate())
# print(c3-c2)

c5 = ComplexCartesian(3,4)
c6 = ComplexCartesian(2,-3)
c7 = c5*c6
print(c7)
c8 = c5/c6
print(c8)
print(c8.conjugate())
print(c8.modulus())
print(c8.argument())