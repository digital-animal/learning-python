# # # Point Object
# #
# class Coordinates:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def distance(self, other):
#         x_diff_sq = (self.x - other.x)**2
#         y_diff_sq = (self.y - other.y)**2
#         d = (x_diff_sq + y_diff_sq)**0.5
#         return d
#     def __str__(self):
#         return f"<{self.x}, {self.y}>"
#     def __add__(self, other):
#         print(f"({self.x + other.x}, {self.y + other.y})")
#
# #
# # c = Coordinates(3, 4)
# c = Coordinates(8,6)
# origin = Coordinates(0,0)
# p = Coordinates(4, 3)
# print(type(c))
# # print(c.x,c.y)
# # print(c)
# # print(origin.x,origin.y)
# # print(origin)
# print(type(Coordinates))
# print(isinstance(c,Coordinates))
# # print()
# # print(f"C({c.x}, {c.y})")
# # print(f"O({origin.x}, {origin.y})")
# r = c.distance(origin)
# # r = Coordinates.distance(c, origin)
# print(f"distance between point O({origin.x}, {origin.y}) and C({c.x}, {c.y}) = {r}")
# # print(f"{origin}")
# # print(f"{c}")
# # print()
# # c.__add__(p)
# # f = c + p

# # # Fraction Object
#
##### Try to add a reduce method to reduce the fraction...
##### eg. reduce(8/16) = 1/2

# class Fraction:
#     """
#     A number represented as a fraction
#     """
#     def __init__(self, num, denom):
#         """ nu and denom are integers """
#         assert type(num) == int and type(denom) == int
#         self.num = int(num)
#         self.denom = int(denom)
#
#     def __str__(self):
#         """ Returns a string representation of the fraction """
#         return f"{str(self.num)} / {str(self.denom)}"
#
#     def __add__(self, other):
#         """ Returns a new fraction representing addition of two fractions """
#         top = self.num * other.denom + other.num * self.denom
#         bottom = self.denom * other.denom
#         return Fraction(top, bottom)
#
#     def __sub__(self, other):
#         """ Returns a new fraction representing subtraction of two fractions """
#         top = self.num * other.denom - other.num * self.denom
#         bottom = self.denom * other.denom
#         return Fraction(top, bottom)
#
#     def __float__(self):
#         """ Returns a float value of the fraction """
#         return self.num / self.denom
#
#     def inverse(self):
#         """ Returns a new fraction representing the inverse of old fraction """
#         return Fraction(self.denom, self.num)
#
#     def reduce(self):
#         pass
#
# #
# f = Fraction(1, 4)
# g = Fraction(3, 4)
# print(f)
# print(g)
# # print(f + g)
# # print(f - g)
# print()
# # print(f.__float__())
# # print(Fraction.__float__(f))
# # print(float(f))
# # print()
# # print(g.__float__())
# # print(Fraction.__float__(g))
# # print(float(g))
# # print()
# # print(f.inverse())
# # print(g.inverse())
# # print()
# h = f + g
# print(h)
# # print(float(h))
# # print(h.inverse())
# # print(Fraction.inverse(h))
# k = f-g
# print(k)
# print(float(k))
# print(k.inverse())
# print(float(k.inverse()))


# # Python Classes and Inheritance
import random
# ==================================
# ========== Animal Class ==========
# ==================================
class Animal:
    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return f"Animal : {str(self.name)} : {str(self.age)}"


print("\n<Animal Tests>")
a = Animal(3)
b = Animal(4)
a.set_name("Billy")
b.set_name("Morty")
# # print(a.age)  # allowed but not recommended
# print(a.get_name())
# print(a.get_age())  # recommended
print(a)
#
# print(b.get_name())
# print(b.get_age())  # recommended
print(b)
# print()

# ==================================
# =============Cat Class============
# ==================================
class Cat(Animal):
    # def __init__(self):
    #     Animal.__init__(self)

    # # if __init__ not implemented here..
    # it will inherit from parent..no problem

    def speak(self):
        print("meow")

    def __str__(self):
        return f"Cat: {str(self.name)}: {str(self.age)}"


print("\n<Cat Tests>")
c = Cat(1)
c.set_name("Fluffy")
# print(c.get_name())
# print(c.get_age())
print(c)
c.speak()

# =========================================
# ============ Rabbit Class ===============
# =========================================
class Rabbit(Animal):
    tag = 1  # class variable

    def __init__(self, age, parent1=None, parent2=None):
        # Animal.__init__(self, age)
        super().__init__(age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rabbit_id = Rabbit.tag  # class variable accessed by class
        Rabbit.tag += 1  # class variable accessed and increased by class

    def get_rabbit_id(self):
        return str(self.rabbit_id).zfill(3)

    def get_parent_1(self):
        return self.parent1

    def get_parent_2(self):
        return self.parent2

    def __add__(self, other):
        """returning object of same type as this class"""
        return Rabbit(0, self, other)

    def __str__(self):
        return f"Rabbit: {self.get_rabbit_id()}"
    def __eq__(self, other):
        parents_same = (self.parent1.rabbit_id == other.parent1.rabbit_id) and (self.parent2.rabbit_id == other.parent2.rabbit_id)
        parents_opposite = (self.parent2.rabbit_id == other.parent1.rabbit_id) and (self.parent1.rabbit_id == other.parent2.rabbit_id)

        return parents_same or parents_opposite


print("\n<Rabbit Tests>")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print(f"r1 : {r1}")
print(f"r2 : {r2}")
print(f"r3 : {r3}")
print(f"r1 parent_1: {r1.get_parent_1()}")
print(f"r1 parent_2: {r1.get_parent_2()}")
#
print()
print("<testing rabbit addition>")
r4 = r1 + r2  # r1.__add__(r2)
print(f"r1 : {r1}")
print(f"r2 : {r2}")
print(f"r4 : {r4}")
print(f"r4 parent_1: {r4.get_parent_1()}")
print(f"r4 parent_2: {r4.get_parent_2()}")
#
print()
print("<testing rabbit equality>")
r5 = r3 + r4
r6 = r4 + r3
print(f"r3 : {r3}")
print(f"r4 : {r4}")
print(f"r5 : {r5}")
print(f"r6 : {r6}")
print(f"r5 parent 1: {r5.get_parent_1()}")
print(f"r5 parent 2: {r5.get_parent_2()}")
print(f"r6 parent 1: {r6.get_parent_1()}")
print(f"r6 parent 2: {r6.get_parent_2()}")
#
# print(f"r5 and r6 have same parents? {r5.__eq__(r6)}")
# print(f"r5 and r6 have same parents? {r5 == r6}")
# print(f"r4 and r6 have same parents? {r4.__eq__(r6)}")
print(f"r4 and r6 have same parents? {r4 == r6}")

# ==================================================
# ==================== Human Class =================
# ==================================================
class Human(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age) # inheriting age from Animal class but not the name
        # # super().__str__(age) # alternative to above constructor
        self.set_name(name)  # # very good implementation..
        # .. self.name = name..would work though..but not impressive or efficient
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, friend_name):
        self.friends.append(friend_name)

    def remove_friend(self, friend_name):
        self.friends.remove(friend_name)

    def speak(self):
        print("hello")

    def age_diff(self, other):
        diff = self.age - other.age
        print(f"{abs(diff)} year difference")

    def __str__(self):
        return f"Human: {str(self.name)} : {str(self.age)}"


print("\n<Human Tests>")
p1 = Human("Jack", 30)
p2 = Human("Anna", 26)
print(p1.get_name())
print(p1.get_age())
p1.speak()
# print(p1)
# print(p2.get_name())
# print(p2.get_age())
# p2.speak()
# print(p2)
p1.age_diff(p2)

# =============================================
# ============ Student Class ==================
# =============================================
class Student(Human):
    def __init__(self, name, age, major=None):
        # Human.__init__(self, name, age)
        super().__init__(name,age)
        self.major = major

    def change_major(self, new_major):
        self.major = new_major

    def speak(self):
        r = random.random()
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print("I need to sleep.")
        elif 0.5 <= r < 0.75:
            print("I should eat")
        else:
            print("I am watching tv")

    def __str__(self):
        return f"Student: {str(self.name)}: {str(self.age)}: {str(self.major)}"


print("\n<Student Tests>")
s1 = Student("Dexter", 25, "CSE")
s2 = Student("Alice", 22)
# print(s1.get_name())
# print(s1.get_age())
print(s1)

# print(s2.get_name())
# print(s2.get_age())
print(s2)

print()
print(f"{s1.get_name()} says", end=" ")
s1.speak()
print(f"{s2.get_name()} says", end=" ")
s2.speak()

print()
print()
s2.change_major("EEE")
print(s2)

# ===================================================
# =================== Male Class ====================
# ===================================================
# class Male(Human):
#     pass
#

# ===================================================
# ================== Female Class ===================
# ===================================================
# class Female(Human):
#     pass
