# ==================================================
# ================== OOP Fraction ==================
# ==================================================

class Fraction:
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bottom = self.denom*other.denom
        return Fraction(top,bottom)
    def __sub__(self, other):
        top = self.num * other.denom - self.denom * other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)
    def __mul__(self, other):
        top = self.num *  other.num
        bottom = self.denom * other.denom
        return Fraction(top, bottom)
    def __truediv__(self, other):
        top = self.num *  other.denom
        bottom = self.denom * other.num
        return Fraction(top,bottom)
    def invert_copy(self): # Returns COPY Fraction Inverted
        top = self.denom
        bottom = self.num
        return Fraction(top, bottom)
    def invert(self): # Returns ORIGINAL Fraction Inverted
        temp = self.num
        self.num = self.denom
        self.denom = temp
    def __float__(self):
        return self.num / self.denom
    def reduce(self):
        i = 1
        while True:
            if self.num % i == 0 and self.denom % i == 0:
                self.num = int(self.num / i)
                self.denom = int(self.denom / i)
                i = 1
            if i > self.num or i > self.denom:
                break
            i += 1
    def __str__(self):
        self.reduce()
        if self.denom == 1:
            return f"{str(self.num)} "
        else:
            return f"{str(self.num)} / {str(self.denom)}"

# f1 = Fraction(3,4)
# f2 = Fraction(1,4)
# print(f1)
# print(f2)
# f3 = f1 + f2
# print(f3)
# f4 = f1 - f2
# print(f4)
# # f1.invert()
# # print(f1)
# # f5 = f2.invert_copy()
# # print(f2)
# # print(f5)
# print(float(f1))
# f6 = f1 / f2
# print(f6)
# f6.reduce()
# print(f6)
# f3.reduce()
# print(f3)

x = Fraction(20,36)
print(x)
y = Fraction(4,36)
print(y)
a = x + y
print(a)
b = x - y
print(b)
c = x * y
print(c)
d = x / y
print(d)
e = x.invert_copy()
print(e)
# f = float(x)
# print(f)
# g = float(y)
# print(g)
# h = float(a)
# print(h)
# i = float(b)
# print(i)
# j = float(c)
# print(j)
# k = float(d)
# print(k)
# l = float(e)
# print(l)
# x.reduce()
# print(x)
# y.reduce()
# print(y)
a.reduce()
print(a)
b.reduce()
print(b)
c.reduce()
print(c)
d.reduce()
print(d)
z = Fraction(72,144)
z.reduce()
print(z)