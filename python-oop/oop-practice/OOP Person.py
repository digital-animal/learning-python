# ================================================
# =============== Class Person ===================
# ================================================
class Person:
    index = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = Person.index
        Person.index += 1
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def __str__(self):
        return f"Person_{str(self.id).zfill(3)} [Name: {self.get_name()}, Age: {self.get_age()}]"


class Employee(Person):
    index = 1
    def __init__(self, name, age, profession, salary):
        # Person.__init__(self, name, age)
        super().__init__(name,age)
        self.profession = profession
        self.salary = salary
        self.id = Employee.index
        Employee.index += 1
    def get_profession(self):
        return self.profession
    def get_salary(self):
        return self.salary
    def __str__(self):
        return f"Employee_{str(self.id).zfill(3)} [Name: {self.get_name()}, Age: {self.get_age()}, Profession: {self.get_profession()}, Salary: {self.get_salary()}]"
class Student(Person):
    index = 1
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
        self.id = Student.index
        Student.index += 1
    def get_major(self):
        return self.major
    def __str__(self):
        return f"Studnet_{str(self.id).zfill(3)} [Name: {self.get_name()}, Age: {self.get_age()}, Major: {self.get_major()}]"

p1 = Person("Zahid", 30)
print(p1)
p2 = Person("Jewel", 31)
print(p2)
p3 = Person("Robi", 32)
print(p3)
print()
emp1 = Employee("Nazmul", 29, "Engineer", 20000)
print(emp1)
emp2 = Employee("Tuhin", 28, "Web Developer", 18000)
print(emp2)
print()
s1 = Student("Talha", 22, "CSE")
print(s1)
s2 = Student("Maliha", 21, "EEE")
print(s2)
s3 = Student("Upama", 20, "BBA")
print(s3)
s4 = Student("Anik", 21, "Math")
print(s4)
s5 = Student("Rahat", 19, "Physics")
print(s5)