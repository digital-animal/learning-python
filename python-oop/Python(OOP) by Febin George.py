# # Classes and Objects
# make an employee class to store and display employee details
# check if an employee has achieved his weekly target or not

# # Classes and Objects
# # class attribute and instance attribute
# # instance method vs static method vs class method
# # abstraction and encapsulation
# # Inheritance
# # # 1.single inheritance
# # # 2.multiple inheritance
# # # 3.multi-level inheritance
# # Access specifiers


# class Employee:
#     number_of_working_hours = 40  # class variable i.e attribute
#     index = 1
#     def __init__(self, name, age, designation, sales_made_this_week):  # this are instance variable
#         self.name = name
#         self.age = age
#         self.designation = designation
#         self.sales_made_this_week = sales_made_this_week
#         self.id = Employee.index
#         Employee.index += 1
#
#     def hasAchievedTarget(self):
#         # if self.sales_made_this_week >= 5:
#         #     print("Target Achieved.")
#         # else:
#         #     print("Target not achieved.")
#
#         if self.sales_made_this_week >= 5:
#             return True
#         else:
#             return False
#
#     def displayMessage(self):
#         print(f"Welcome {self.name} to out company")
#
#     @staticmethod
#     def welcomeMessage():
#         print("Welcome!")
#
#     def __str__(self):
#         return f"## Employee_{str(self.id).zfill(3)}:\nName: {self.name}\
#         \nAge: {self.age}\nDesignation: {self.designation}\
#         \nSales_Amount[Current Week]: {self.sales_made_this_week}\
#         \nTarget Achieved: {self.hasAchievedTarget()}\n"
# #
# #
# # Employee.number_of_working_hours = 45
# # print("<Employee 001>")
# emp1 = Employee("Ben", 26, "Sales Executive", 6)
# # print(f"Name: {emp1.name}")
# # print(f"Age: {emp1.age}")
# # print(f"Designation: {emp1.designation}")
# # print(f"Working Hours: {emp1.number_of_working_hours}")
# # emp1.hasAchievedTarget()
# # print(emp1.__dict__)
# print(emp1)
# # print()
#
# # print("<Employee 002>")
# emp2 = Employee("Smith", 31, "Sales Executive", 4)
# # print(f"Name: {emp2.name}")
# # print(f"Age: {emp2.age}")
# # print(f"Designation: {emp2.designation}")
# # print(f"Working Hours: {emp2.number_of_working_hours}")
# # emp2.hasAchievedTarget()
# print(emp2)
# # print()
# #
# # print("<Employee 003>")
# emp3 = Employee("Mary", 22, "Sales Girl", 7)
# # print(f"Name: {emp3.name}")
# # print(f"Age: {emp3.age}")
# # print(f"Designation: {emp3.designation}")
# # emp3.number_of_working_hours = 36
# # print(f"Working Hours: {emp3.number_of_working_hours}")
# # emp3.hasAchievedTarget()
# print(emp3)
# # print()
# #
# # emp1.displayMessage()
# # emp1.welcomeMessage()
#
#
# # # implement a library management system which handle the following tasks
# # # # # 1. customer should be able to display all he books available to the library
# # # # # 2. handle the process when a customer requests to borrow book
# # # # # 3. update the library collection when customer returns a book

# class Library:
#     def __init__(self, list_of_books):
#         self.available_books = list_of_books
#
#     def displayBooks(self):
#         i = 1
#         print()
#         print("<Available Books>")
#         for book in self.available_books:
#             print(f"{str(i).zfill(3)}: {book}")
#             i += 1
#
#     def lendBook(self, requested_book):
#         if requested_book in self.available_books:
#             print("Avaiable..Issued for Borrow.")
#             self.available_books.remove(requested_book)  # list's remove method
#         else:
#             print("Sorry..Book Not Available Currently.")
#
#     def addBook(self, returned_book):
#         self.available_books.append(returned_book)
#         print("Thank you for returning the book.")
# #
# #
# class Customer:
#
#     def requestBook(self):
#         self.book = input("Enter Book Name > ")
#         return self.book
#
#     def returnBook(self):
#         self.book = input("Enter Book Name > ")
#         return self.book
#
#
# book_list = ["War and Peace", "Anna Karenina", "Crime and Punishment", "And Quiet Flows the Don"]
#
# library = Library(book_list)
# customer = Customer()
#
# while True:
#     print("======================================")
#     print("Enter 1 to display the available books.")
#     print("Enter 2 to request for a book.")
#     print("Enter 3 to return a book. ")
#     print("Enter 4 to exit.")
#     user_choice = int(input("> "))
#
#     if user_choice == 1:
#         library.displayBooks()
#     elif user_choice == 2:
#         requested_book = customer.requestBook()
#         library.lendBook(requested_book)
#     elif user_choice == 3:
#         returned_book = customer.returnBook()
#         library.addBook(returned_book)
#     elif user_choice == 4:
#         quit()
#     print()


# # Inheritance
# # # 1.single inheritance
# # # 2.multiple inheritance
# # # 3.multi-level inheritance

# # # ex-01
# # # 1.single inheritance
#
# class Apple:  # base class
#     manufacturer = "Apple Inc."
#     contact_website = "www.apple.com/contact"
#
#     def contactDetail(self):
#         print("To contact us, long on to", self.contact_website)
#
#
# class MacBook(Apple):  # derived class
#     def __init__(self):
#         # Apple.__init__(self)
#         super().__init__()
#         self.year_of_manufacture = 2017
#
#     def manufactureDetails(self):
#         print(f"This MacBook was manufactured in the year {self.year_of_manufacture} by {self.manufacturer}")
#
#
# macbook1 = MacBook()
# print()
# print("===================================================")
# print(macbook1.manufacturer)
# print(macbook1.contact_website)
# print(macbook1.year_of_manufacture)
# macbook1.manufactureDetails()
# macbook1.contactDetail()

# # # ex-02
# # # 2.multiple inheritance
#
# class OperatingSystem:
#     multitasking = True
#     name = "Mac OS"
#
# class Apple:
#     website = "www.apple.com"
#     name = "Apple"
#
# # class MacBook(OperatingSystem, Apple):
# class MacBook(Apple, OperatingSystem):
#     def __init__(self):
#         if self.multitasking is True:
#             print(f"This is a multi tasking system.\nVisit {self.website} for more details.")
#             print(f"Name: {self.name}")
#
# macbook1 = MacBook()

# # ex-03
# # 3.multi-level inheritance
# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass

# # # ex-04
# # # 3.multi-level inheritance
# class MusicalInstrument:
#     number_of_keys = 12
#
# class StringInstrument(MusicalInstrument):
#     type_of_wood = "Tonewood"
#
# class Guitar(StringInstrument):
#     def __init__(self):
#         self.number_of_strings = 6
#         print(f"This guitar consists of {self.number_of_strings} strings.\
#         \nIt is made of {self.type_of_wood}\
#         \nand it can play {self.number_of_keys} keys\n")
#
# guitar1 = Guitar()

# # Access specifiers
# # # 1.public
# # # 2.protected
# # # 3.private

# # # ex-01
# class Car:
#     number_of_wheels = 4
#     _color = "Black"
#     __year_of_production = 2017 # internally _Car__year_of_production = 2017
#
# class BMW(Car):
#     def __init__(self):
#         print(f"Protected Attribute, color: {self._color}")
#
# car1 = Car()
# print(f"Public attribute, number of wheels: {car1.number_of_wheels}")
# bmw_car1 = BMW()
# # print(f"Private attribute, year of manufacture: {car1.__year_of_production}")
# # print(f"Private attribute, year of manufacture: {car1._Car__year_of_production}")  # enables access
# # print(f"Private attribute, year of manufacture for bmw: {bmw_car1._Car__year_of_production}")  # enables access

# # # Polymorphism
# # # operator overriding
# # # ex-01
# #
# class Employee:
#     def setNumberOfWorkingHours(self):
#         self.number_of_working_hours = 40
#
#     def displayNumberOfWorkingHours(self):
#         print(self.number_of_working_hours)
#
#
# class Trainee(Employee):
#     def setNumberOfWorkingHours(self):  # overriding base class method
#         self.number_of_working_hours = 45
#
#     def resetNumberOfWorkingHours(self):
#         super().setNumberOfWorkingHours()
# #
# #
# emp1 = Employee()
# emp1.setNumberOfWorkingHours()
# print("Number of working hours of employee:", end=" ")
# emp1.displayNumberOfWorkingHours()
# #
# trainee1 = Trainee()
# trainee1.setNumberOfWorkingHours()
# print("Number of working hours of trainee:", end=" ")
# trainee1.displayNumberOfWorkingHours()
# #
# trainee1.resetNumberOfWorkingHours()
# print("Number of working hours of trainee after reset:", end=" ")
# trainee1.displayNumberOfWorkingHours()


# ex-02
# diamond geometric problem in overriding
# case-1: method will not be overridden in class B and class C
# case-2: method will be overridden in class B but not in class C
# case-3: method will be overridden in class C but not in class B
# case-4: method will be overridden in both class B and class C

# # # case-1:
# class A:
#     def method(self):
#         print("This method belongs to class A")
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# class D(B, C):
#     pass
#
# d = D()
# d.method()


# # # case-2:
# class A:
#     def method(self):
#         print("This method belongs to class A")
#
# class B(A):
#     def method(self):
#         print("This method belongs to class B")
#
# class C(A):
#     pass
#
# class D(B, C):
#     pass
#
# d = D()
# d.method()


# # # case-3:
# class A:
#     def method(self):
#         print("This method belongs to class A")
#
# class B(A):
#     pass
#
# class C(A):
#     def method(self):
#         print("This method belongs to class C")
#
# class D(B, C):
#     pass
#
# d = D()
# d.method()


# # # # case-4:
# class A:
#     def method(self):
#         print("This method belongs to class A")
#
# class B(A):
#     def method(self):
#         print("This method belongs to class B")
#
# class C(A):
#     def method(self):
#         print("This method belongs to class C")
#
# # class D(B, C):
# #     pass
# class D(C, B):
#     pass
#
# d = D()
# d.method()


# # # # operator overloading
# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side**2
#
#     def perimeter(self):
#         return 4*self.side
#
#     def __add__(self, other):
#         return self.side * 4 + other.side * 4  # adding perimeters
#
#     # def __add__(sq1, sq2): # exactly same as above method
#     #     return sq1.side*4 + sq2.side*4
#
#     # def __add__(self, other):
#     #     pass  # implement for area adding..rather logical
#
#
# square1 = Square(5)
# square2 = Square(10)
# # # now we want to perform square1 + square2
# # # and get the result 5*4 + 10*4 = 60
# print("Sum of sides of both the squares: ", square1 + square2)
# # print("Sum of sides of both the squares: ", square1.__add__(square2))
# # print("Sum of sides of both the squares: ", Square.__add__(square1, square2))
#
# # # square1 + square2 == square1.__add__(square2)...exactly same
# # # Square.__add__(square1, square2) it is also same


# # # # abstract base class
# # # ex-01
# from abc import ABC
# from abc import ABCMeta
# from abc import abstractmethod
#
# # class Shape(ABC): # forces Square and Rectangle class to implement area() method
# class Shape(metaclass=ABCMeta): # forces Square and Rectangle class to implement area() method
#     @abstractmethod
#     def area(self):
#         return 0
#
# class Square(Shape):
#     side = 4
#     def area(self):
#         print(f"Area of square: {self.side * self.side}")
#
# class Rectangle(Shape):
#     width = 5
#     length = 10
#
#     def area(self):
#         print(f"Area of rectangle: {self.width * self.length}")
#
#
# sq1 = Square()
# rect1 = Rectangle()
# sq1.area()
# rect1.area()
#
# # shape1 = Shape() # TypeError: Can't instantiate abstract class Shape with abstract method


# # # project-01
# # # banking system
#
# from abc import ABCMeta, abstractmethod
# from random import randint
#
#
# class Account(metaclass=ABCMeta):
#     @abstractmethod
#     def createAccount(self):
#         return 0
#
#     @abstractmethod
#     def authenticate(self):
#         return 0
#
#     @abstractmethod
#     def withdraw(self):
#         return 0
#
#     @abstractmethod
#     def deposit(self):
#         return 0
#
#     @abstractmethod
#     def displayBalance(self):
#         return 0
#
#
# class SavingsAccount(Account):
#     def __init__(self):
#         # dict[key][0] = name  # dict[key][1] = balance
#         self.savings_account = {}  # dictionary
#
#     def createAccount(self, name, initial_deposit):
#         self.account_number = randint(10000, 99999)
#         self.savings_account[self.account_number] = [name, initial_deposit]
#         print(f"Congratulation! Account creation has been successful!\nYour account number is: {self.account_number}")
#
#     def authenticate(self, name, account_number):
#         if account_number in self.savings_account.keys():
#             if self.savings_account[account_number][0] == name:
#                 print("Authentication Successful")
#                 self.account_number = account_number
#                 return True
#             else:
#                 print("Authentication Failed")
#                 return False
#         else:
#             print("Authentication Failed")
#             return False
#
#     def withdraw(self, withdrawal_amount):
#         if withdrawal_amount > self.savings_account[self.account_number][1]:
#             print("Insufficient Balance")
#         else:
#             self.savings_account[self.account_number][1] -= withdrawal_amount
#             # print(f"Withdrawal was successful!\nCurrent Balance: {self.savings_account[self.account_number][1]}")
#             print("Withdrawal was successful!")
#             self.displayBalance()
#
#     def deposit(self, deposit_amount):
#         self.savings_account[self.account_number][1] += deposit_amount
#         # print(f"Deposit was scuccessful!\nCurrent Balance: {self.savings_account[self.account_number][1]}")
#         print("Deposit was scuccessful!")
#         self.displayBalance()
#
#     def displayBalance(self):
#         print(f"### Account Number: {self.account_number}\n### Name: {self.savings_account[self.account_number][0]}\n### Current Balance: {self.savings_account[self.account_number][1]}")
#
# print("=================================================")
# savings_account_obj = SavingsAccount()
# while True:
#     print("Enter 1 to create a new account.")
#     print("Enter 2 to access an existing account.")
#     print("Enter 3 to exit.")
#     user_choice = int(input("> "))
#     if user_choice == 1:
#         name = input("Enter your name: ")
#         deposit = int(input("Enter initial deposit: "))
#         savings_account_obj.createAccount(name, deposit)
#     elif user_choice == 2:
#         name = input("Enter your name: ")
#         acc_no = int(input("Enter your account number: "))
#         authentication_status = savings_account_obj.authenticate(name, acc_no)
#
#         if authentication_status is True:
#             while True:
#                 print("# Enter 1 to withdraw.")
#                 print("# Enter 2 deposit.")
#                 print("# Enter 3 display current balance.")
#                 print("# Enter 4 to go back to previous menu.")
#                 customer_choice = int(input("> "))
#                 if customer_choice == 1:
#                     withdrawal_amount_obj = float(input("Enter an withdrawal amount> "))
#                     savings_account_obj.withdraw(withdrawal_amount_obj)
#
#                 elif customer_choice == 2:
#                     deposit_amount_obj = float(input("Enter your deposit amount> "))
#                     savings_account_obj.deposit(deposit_amount_obj)
#                 elif customer_choice == 3:
#                     savings_account_obj.displayBalance()
#                 elif customer_choice == 4:
#                     break
#         else:
#             print("Please enter correct username and account number..")
#     elif user_choice == 3:
#         print("Goodbye!")
#         print()
#         quit()
#     print("=================================================")
