# Python Object-Oriented Programming
# =================================================
# ===========classes and instances=================
# =================================================
#
# # ex-01
# class Employee:
#     pass
#
# emp_1 = Employee()
# emp_2 = Employee()
#
# print(emp_1)
# print(emp_2)
# #
# emp_1.first = "Corey"
# emp_1.last = "Schafer"
# emp_1.email = "corey.schafer@company.com"
# emp_1.pay = 50000
# #
# emp_2.first = "Test"
# emp_2.last = "User"
# emp_2.email = "test.user@company.com"
# emp_2.pay = 60000
# #
# print(emp_1.email)
# print(emp_2.email)
# print(emp_1.pay)
# print(emp_2.pay)

# # ex-02
# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = f"{first}.{last}@compay.com"
#         self.pay = pay
#
#     def display_fullname(self):
#         return f"{self.first} {self.last}"
#
#
# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)
# #
# print(emp_1)
# print(emp_2)
# #
# print(emp_1.email)
# print(emp_2.email)
# #
# print(f"Full Name: {emp_1.display_fullname()}")
# print(f"Full Name: {emp_2.display_fullname()}")
# #
# print("Full Name: ", Employee.display_fullname(emp_1))
# print("Full Name: ", Employee.display_fullname(emp_2))

# # emp_1.display_fullname() == Employee.display_fullname(emp_1)...exactly same

# =======================================================
# =================class variables=======================
# =======================================================

# # example - 01
# class Employee:
#     raise_amount = 1.04
#     num_of_emps = 0
#
#     def __init__(self, first, last, pay):
#         self.first = first  # instance variable
#         self.last = last
#         self.email = f"{first}.{last}@compay.com"
#         self.pay = pay
#
#         Employee.num_of_emps += 1
#
#     def display_fullname(self):
#         return f"{self.first} {self.last}"
#
#     def apply_raise(self):
#         # self.pay = int(self.pay * raise_amount) # error..class variables...
#         # #... can only be accessed by class
#         # self.pay = int(self.pay * Employee.raise_amount) # correct
#         self.pay = int(self.pay * self.raise_amount) # correct
#
# #
# print(Employee.num_of_emps)
# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)
# print(Employee.num_of_emps)
#
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# # #
# # print(emp_1.__dict__)  # namespace of emp_1
# # print(Employee.__dict__)  # namespace of emp_1
# #
# # Employee.raise_amount = 1.05
# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)  # namespace of emp_1
# # #
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# #
# # # emp_1.raise_amount
# # # Employee.raise_amount
# #
# # print(Employee.num_of_emps)


# =====================================================
# ============ classmethod, staticmethod ==============
# =====================================================
# #
# # ex-01
# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first  # instance variable
#         self.last = last
#         self.email = f"{first}.{last}@compay.com"
#         self.pay = pay
#
#         Employee.num_of_emps += 1
#
#     def display_fullname(self):
#         return f"{self.first} {self.last}"
#
#     def apply_raise(self):
#         # self.pay = int(self.pay * Employee.raise_amount)
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
#
#
# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)
# #
# # Employee.set_raise_amount(1.05)  # Employee.raise_amount = 1.05
# emp_1.set_raise_amount(1.05)
# #
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# ex-02
# # parsing employee information string..
# # to create new employee instances..
# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first  # instance variable
#         self.last = last
#         self.email = f"{first}.{last}@compay.com"
#         self.pay = pay
#
#         Employee.num_of_emps += 1
#
#     def display_fullname(self):
#         return f"{self.first} {self.last}"
#
#     def apply_raise(self):
#         # self.pay = int(self.pay * Employee.raise_amount)
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
#
#     @classmethod
#     def from_string(cls, emp_str): # alternative constructor
#         first, last, pay = emp_str.split("-")
#         # return Employee(first, last, pay)
#         return cls(first, last, pay)  # same thing
#
# #
# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)
#
# emp_str_1 = "John-Doe-70000"
# emp_str_2 = "Steve-Smith-30000"
# emp_str_3 = "Jane-Doe-90000"
#
# # # 1st approach
# # # okay..but manual..and tiresome..repetitive
# # first, last, pay = emp_str_1.split("-")  # use with alternative constructor
# # new_emp_1 = Employee(first, last, pay) # creating new employee object
# # print(new_emp_1.email)
# # print(new_emp_1.pay)
#
# # # 2nd approach..passing to class method..from_string()
# # # automated..efficient
# new_emp_1 = Employee.from_string(emp_str_1) # after returning...new_emp_1 = Employee(first,last,pay)
# new_emp_2 = Employee.from_string(emp_str_2) # new_emp_2 = Employee(first,last,pay)
# new_emp_3 = Employee.from_string(emp_str_3) # new_emp_3 = Employee(first,last,pay)
# #
# print(new_emp_1.email)
# print(new_emp_1.pay)
# print(new_emp_2.email)
# print(new_emp_2.pay)
# print(new_emp_3.email)
# print(new_emp_3.pay)
#
# print(Employee.num_of_emps)

# # static method
# # class method vs static method
# # ex-01
# class Employee:
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first  # instance variable
#         self.last = last
#         self.email = f"{first}.{last}@compay.com"
#         self.pay = pay
#
#         Employee.num_of_emps += 1
#
#     def display_fullname(self):
#         return f"{self.first} {self.last}"
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#     @classmethod
#     def set_raise_amount(cls, amount):
#         cls.raise_amount = amount
#
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split("-")
#         return cls(first, last, pay)
#
#     @staticmethod
#     def is_workday(day):
#         if day.weekday() == 5 or day.weekday() == 6:
#             return False
#         return True
#
#
# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)
# #
# import datetime
# # my_date = datetime.date(2019, 11, 24)
# # my_date = datetime.date(2019, 11, 25)
# my_date = datetime.date(2020, 6, 4)
# print(Employee.is_workday(my_date))

# =======================================================
# ==================== inheritance ======================
# =======================================================
# inheritance
# creating issubclasses
# # ex-01
# class Employee:
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first  # instance variable
#         self.last = last
#         self.email = f"{first}.{last}@compay.com"
#         self.pay = pay
#
#     def display_fullname(self):
#         return f"{self.first} {self.last}"
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#
#
# class Developer(Employee):
#     raise_amount = 1.10
#
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
#
#
# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#
#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)
#
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#
#     def print_emps(self):
#         for emp in self.employees:
#             print("-->", emp.display_fullname())


# dev_1 = Employee("Corey", "Schafer", 50000)
# dev_2 = Employee("Test", "User", 60000)
#
# dev_1 = Developer("Corey", "Schafer", 50000, "C++")
# dev_2 = Developer("Test", "User", 60000, "Python")
# #
# mgr_1 = Manager("Sue", "Smith", 9000, [dev_1])
#
# print(mgr_1.__dict__) # printing namespace
# print(mgr_1.email)
#
# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_1)
# #
# mgr_1.print_emps()

# help(Developer)

# print(dev_1.email)
# print(dev_1.prog_lang)
#
# print(dev_2.email)
# print(dev_2.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# # isinstance() function
# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))
#
# print(isinstance(dev_1, Manager))
# print(isinstance(dev_1, Employee))
# print(isinstance(dev_1, Developer))

# # issubclass() function
# print(issubclass(Manager, Employee))
# print(issubclass(Developer, Employee))
# print(issubclass(Developer, Manager))
# print(issubclass(Manager, Developer))
# print(issubclass(Employee, Developer))
# print(issubclass(Employee, Manager))


# =====================================================
# ========== Special / Dunder / Magic Methods =========
# ==========operator overloading=======================
# =====================================================

# print(1 + 2)
# print('1' + '2')

# class Employee:
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first  # instance variable
#         self.last = last
#         self.email = f"{first}.{last}@compay.com"
#         self.pay = pay
#
#     def display_fullname(self):
#         return f"{self.first} {self.last}"
#
#     def apply_raise(self):
#         # self.pay = int(self.pay * Employee.raise_amount)
#         self.pay = int(self.pay * self.raise_amount)
#
#     def __repr__(self):
#         return f"Employee({self.first}, {self.last}, {self.pay})"
#
#     def __str__(self):
#         return f"{self.display_fullname()} - {self.email}"
#
#     def __add__(self, other):
#         return self.pay + other.pay
#
#     def __len__(self):
#         return len(self.display_fullname())
#
# emp_1 = Employee("Corey", "Schafer", 50000)
# emp_2 = Employee("Test", "User", 60000)

# print(emp_1)

# print(repr(emp_1))
# print(emp_1.__repr__())  # exact same object
# print(str(emp_1))
# print(emp_1.__str__())  # exact same object
#
# print(1+2)
# print(int.__add__(1, 2))
# print((1).__add__(2))

# print('a'+'b')
# print(('a').__add__('b'))
# print(str.__add__("a", "b"))

# print(len("test"))
# print(str.__len__("test"))
# print("test".__len__())

# # task
# # emp_1 + emp_2  should return total salary
# print(emp_1 + emp_2)
#
# print(len(emp_1))
# print(len(emp_2))

# ======================================================
# =============== property decorators ==================
# ======================================================

# # getters(accessor)
# # setter(mutator)
# # deleter(destructor)
# #
# class Employee:
#     raise_amount = 1.04
#
#     def __init__(self, first, last):
#         self.first = first  # instance variable
#         self.last = last
#         self.email = f"{first.lower()}.{last.lower()}@company.com"
#
#     @property
#     def display_email(self):
#         return f"{self.first.lower()}.{self.last.lower()}@company.com"
#
#     @property
#     def display_fullname(self):
#         return f"{self.first} {self.last}"
#
#     @display_fullname.setter
#     def display_fullname(self, name):
#         first, last = name.split()
#         self.first = first
#         self.last = last
#     @display_fullname.deleter
#     def display_fullname(self):
#         print("Delete Name!")
#         self.first = None
#         self.last = None
#
#
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Test", "User")
# #
# emp_1.first = "Jim"
# #
# emp_1.display_fullname = "Corey Schafer"
# #
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.display_fullname)
# print(emp_1.display_email)
# #
# del emp_1.display_fullname
# #
# print(emp_1.display_fullname)
# # print(emp_1.display_email)
