# ================================================
# =============== Class Coordinate ===============
# ================================================
import math

class Coordinate:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.mod = None
        self.arg = None

    def polar(self):
        self.mod = (self.x**2 + self.y**2)**0.5
        self.arg = (math.atan2(self.y,self.x)*180)/(math.pi)
        return f"<{str(self.mod)}, {str(self.arg)} deg>"

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        d = (x_diff_sq + y_diff_sq)**0.5
        return d

    def __str__(self):
        return f"<{str(self.x)}, {str(self.y)}>"

    def __add__(self, other):
        return Coordinate(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Coordinate(self.x-other.x, self.y-other.y)

class Line:
    def __init__(self):
        super().__init__()

    def equation(self):
        pass


c1 = Coordinate(0,0)
c2 = Coordinate(4,3)
c3 = Coordinate(8,6)

# print(c1.distance(c2))
# print(c1.distance(c3))
# print(c2.distance(c1))
# print(c2.distance(c3))
# print(c3.distance(c1))
# print(c3.distance(c2))
# print(c1.distance(c1))
# print(c2.distance(c2))
# print(c3.distance(c3))

# print(c1.polar())
# print(c2.polar())
# print(c3.polar())

# print(c1)
# print(c2)
# print(c3)

# c4 = c1 + c2
# print(c4)
# print(c4.polar())

# c5 = c2 + c3
# print(c5)
# print(c5.polar())
# print(c5.distance(c3))
# print(c5.distance(c2))
# print(c5.distance(c1))

# c6 = c2 - c3
# print(c6)
# print(c5.polar())
# print(c6.distance(c2))
# print(c6.distance(c3))
# print(c6.distance(c5))

# print(c5.distance(c6))