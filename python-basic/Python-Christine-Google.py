#!/usr/bin/python
# ========================================
# message = "Welcome to Python Programming"
# print(message)

# ========================================
# friends = ["Alex", "Lee", "Cooper", "Jane"]
# for friend in friends:
#     print(f"Hi {friend}")
    
# ========================================
# length = 10
# width = 2
# area = length * width
# print(f"area = {area}")
    
# ========================================
# length = int(input("Enter length> "))
# width = int(input("Enter width> "))
# area = length * width
# print(f"area = {area}")

# ========================================
# base = 6
# height = 3
# area = (base * height) / 2
# print("area = " + str(area))

# ========================================
# def greeting(name):
#     print(f"Welcome, {name}")

# greeting("Zahid")
# greeting("Jewel")

# ========================================
# def greeting(name, department):
#     print(f"Name: {name}")
#     print(f"Department: {department}")

# greeting("Zahid", "CSE")
# greeting("Jewel", "EEE")

# ========================================
# def area(base, height):
#     return base * height / 2

# t1 = area(4, 9)
# t2 = area(2, 3)
# sum = t1 + t2
# print(f"total area = {sum}")

# ========================================
# def convert_time(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     rem_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, rem_seconds

# # h, m, s = convert_time(33000)
# h, m, s = convert_time(24000)
# print(f"{h} hours {m} minutes {s} seconds")

# ========================================
# def print_lucky_number(name):
#     number = len(name) * 9
#     print(f"Hello {name}, your lucky number is {number}")

# print_lucky_number("Zahid")
# print_lucky_number("Tonmoy ")

# ========================================
# def circle_are(radius):
#     pi = 3.14159
#     return pi * (radius ** 2)

# area = circle_are(5)
# # area = circle_are(10)
# print(f"area = {area}")

# ========================================
# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username. Must be at least 3 characters long")
#     else:
#         print("Valid username")
#         print(f"username = {username}")
        
# hint_username("vi")
# hint_username("vim")

# ========================================
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False

# print(is_even(4))
# print(is_even(9))
 
# ========================================
# def is_even(number):
#     return number % 2 == 0

# print(is_even(4))
# print(is_even(9)) 

# ========================================
# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username. Must be at least 3 characters long")
#     elif len(username) > 15:
#         print("Invalid username. Must be at most 15 characters long")
#     else:
#         print("Valid username")
#         print(f"username = {username}")
        
# hint_username("vi")
# hint_username("vim")
# hint_username("comprehension")
# hint_username("onceuponatimeinthewest")

# ========================================
# num = 0
# while num < 10:
#     print(f"Not there yet, num = {num}")
#     num = num + 1
    
# print(f"num = {num}")

# ========================================
# def attempts(n):
#     x = 1
#     while x <= n:
#         print(f"attempt {x}")
#         x += 1

# attempts(5)

# ========================================
# for num in range(10):
#     print(f"{num}", end=" ")
    
# print(end="\n")
    
# ========================================
# numbers = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# sum = 0
# for num in numbers:
#     sum += num
    
# print(f"sum = {sum}")

# ========================================
# product = 1
# for n in range(1, 10):
#     product *= n

# print(product)

# ========================================
# def to_celsius(x):
#     return (x - 32) * 5 / 9

# for x in range(0, 101, 10):
#     # print(x, to_celsius(x))
#     print(x, round(to_celsius(x), 2))
    
# ========================================
# for i in range(1, 7):
#     for j in range(1, 7):
#         print(f"{(i, j)}", end=" ")
#     print(end="\n")
    
# ========================================
# for i in range(1, 7):
#     for j in range(i, 7):
#         print(f"{(i, j)}", end=" ")
#     print(end="\n")
    
# ========================================
# letters = ["A", "B", "C", "D"]
# for first_letter in letters:
#     for second_letter in letters:
#         if first_letter != second_letter:
#             print(f"{(first_letter, second_letter)}", end=" ")
#     print(end="\n")
    
# ========================================
# def greet_friends(friends):
#     for friend in friends:
#         print(f"Hi {friend}")
        
# friends = ["Alex", "Lee", "Cooper", "Jane", "Anna"]
# greet_friends(friends)
        
# ========================================
# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)

# print(fact(5))
# print(fact(10))

# ========================================
# def fibo(n):
#     if n == 0 or n == 1:
#         return n
#     return fibo(n-1) + fibo(n-2)

# print(fibo(5))
# print(fibo(10))
# # print(fibo(1000)) # RecursionError: maximum recursion depth exceeded in comparison

# ========================================
# text = "education"
# print(text[len(text) - 1])
# print(text[-1])
# print(text[:4])
# print(text[4:6])
# print(text[6:])
# print(text[::-1])

# ========================================
# text = "a quick brown fox jumps over the lazy dog"
# vowels = ["a", "e", "i", "o", "u"]

# count = 0
# for letter in text:
#     if letter in vowels:
#         count += 1
# print(f"total vowels = {count}")

# ========================================
# pets = "cats & dogs"
# print(pets.index("&"))

# ========================================
# def replace_domain(email, old_domain, new_domain):
#     key = f"@{old_domain}"
#     if key in email:
#         position = email.index(key)
#         new_email = f"{email[:position]}@{new_domain}"
#         return new_email
#     return email

# print(replace_domain("zahid.jewel@yahoo.com", "yahoo.com", "gmail.com"))
# print(replace_domain("zahidulislam.jewel@hotmail.com", "hotmail.com", "gmail.com"))
# print(replace_domain("zahidulislamssf@gmail.com", "hotmail.com", "gmail.com"))

# ========================================
# mountain = "Mountains"
# print(mountain.upper())
# print(mountain.lower())
# print(mountain.capitalize())
# print(mountain.strip())
# print(mountain.count("n"))

# ========================================
# words = ["This", "is", "a", "phrase", "joined", "by", "spaces"]
# sentence = " ".join(words)
# print(sentence)

# splitted_words = sentence.split(" ")
# for word in splitted_words:
#     print(word)

# ========================================
# words = ["This", "is", "a", "phrase", "joined", "by", "hyphen"]
# sentence = "-".join(words)
# print(sentence)

# splitted_words = sentence.split("-")
# for word in splitted_words:
#     print(word)
    
# ========================================
# dialog = """A quick brown fox jumps over the lazy dog.
# Once upon a time in the wild west.
# Something is better than nothing"""
# # print(dialog)

# lines = dialog.splitlines()
# print(lines)
# for line in lines:
#     print(line)

# ========================================
# number = "4923578160"
# word = "westworld"
# password = "abc123"
# print(number.isnumeric())
# print(word.isalpha())
# print(password.isalnum())

# ========================================
# id = [101, 102, 103, 104, 105]
# names = ["Alex", "Lee", "Cooper", "Anna", "Jane"]
# departments = ["CSE", "EEE", "ME", "MME", "CE"]
# makrs = [92, 87, 96, 78, 75]

# hyphen = "-"*10
# double_hyphen = "-"*20
# print(f"{'ID': ^10}|{'Name': ^20}|{'Dept': ^20}|{'Marks': ^10}")
# print(f"{hyphen: ^10}+{double_hyphen: ^20}+{double_hyphen: ^20}+{hyphen: ^10}")
# for i in range(5):
#     print(f"{id[i]: ^10}|{names[i]: ^20}|{departments[i]: ^20}|{makrs[i]: ^10}")

# ========================================
# import math

# def is_prime(num):
#     if num < 2:
#         return False
    
#     ulimit = int(round(math.sqrt(num), 0)) + 1;
#     for i in range(2, ulimit):
#         if num % i == 0:
#             return False
#     return True

# numbers = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# for num in numbers:
#     if is_prime(num):
#         print(f"{num} is prime")
#     elif not is_prime(num):
#         print(f"{num} is not prime")

# ========================================
# def is_prime(num):
#     if num < 2:
#         return False
#     i = 2
#     while i * i <= num:
#         if num % i == 0:
#             return False
#         i += 1
#     return True

# numbers = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# for num in numbers:
#     if is_prime(num):
#         print(f"{num} is prime")
#     elif not is_prime(num):
#         print(f"{num} is not prime")

# ========================================
# numbers = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# print(len(numbers))
# print(numbers)
# print(numbers[:])
# print(numbers[::])
# print(numbers[::-1])

# ========================================
# numbers = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# print(numbers)
# numbers.append(11)
# numbers.insert(0, 13)
# print(numbers)
# sorted_numbers = sorted(numbers)
# print(numbers)
# print(sorted_numbers)
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# numbers.remove(0)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.pop(1)
# print(numbers)

# ========================================
# fullname = ("Zahidul", "Islam", "Jewel")
# print(fullname)

# ========================================
# def random_number():
#     return 4, 9, 2

# numbers = random_number()
# print(numbers)
# num1, num2, num3 = numbers
# print(num1, num2, num3)

# ========================================
# lion_king = ["Mufasa", "Simba", "Nala", "Timon", "Pumba", "Shenzy"]
# print(lion_king)

# for index, character in enumerate(lion_king):
#     print(f"{index + 1} {character}")

# ========================================
# def full_emails(people):
#     result = []
#     for email, name in people:
#         result.append(f"{name} <{email}>")
#     return result

# contacts = [
#     ("zahid.jewel@yahoo.com", "Zahid Jewel"),
#     ("tonmoy.hasan@yahoo.com", "Tonmoy Hasan"),
#     ("zahidulislamssf@gmail.com", "Zahidul Islam"),
# ]
# full_contacts = full_emails(contacts)
# print(full_contacts)

# ========================================
# multiples = [x*7 for x in range(1, 11)]
# print(multiples)

# multiples = [x*7 for x in range(1, 11) if x % 2 == 0 ]
# print(multiples)

# languages = ["Bash", "Assembly", "C", "C++", "Java", "Python", "JS"]
# lengths = [len(lang) for lang in languages]
# print(lengths)

# ========================================
# person = {
#     "name": "Zahid",
#     "email": "zahid.jewel@yahoo.com",
#     "department": "CSE"
# }
# print(type(person))
# print(person)
# print(person["name"])
# print(person["email"])
# print(person["department"])

# print(person.get("name"))
# print(person.get("email"))
# print(person.get("department"))

# person["profession"] = "Student"

# for key in person.keys():
#     print(f"{key}: {person[key]}")
    
# for value in person.values():
#     print(f"{value}")

# for key, value in person.items():
#     print(f"{key}: {value}")
# print(person)

# del person["department"]
# print(person)

# ========================================
# def count_letters(text):
#     result = {}
#     for letter in text:
#         if letter not in result:
#             result[letter] = 0
#         result[letter] += 1
#     return result

# text = """A quick brown fox jumps over the lazy dog.
# Once upon a time in the wild west.
# Something is better than nothing"""
# letter_frequency = count_letters(text)
# # print(letter_frequency)
# for k, v in letter_frequency.items():
#     print(f"{k} - {v}")
    
# ========================================
# A = {2, 3, 5, 7, 11, 13, 17, 19}
# B = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
# C = A.intersection(B)
# D = A.union(B)
# E = A.difference(B)
# F = B.difference(A)
# print(f"A = {A}")
# print(f"B = {B}")
# print(f"C = {C}")
# print(f"D = {D}")
# print(f"E = {E}")
# print(f"F = {F}")
    
# ========================================
# class Apple:
#     color = ""
#     flavor = ""

# apple1 = Apple()
# apple1.color = "Red"
# apple1.flavor = "Sweet"
# print(apple1)
# print(apple1.color)
# print(apple1.flavor)

# ========================================
# class Piglet:
#     name = "Piglet"
#     years = 0
    
#     def __init__(self):
#         pass
    
#     def speak(self):
#         print(f"Oink! I'm {self.name}! Oink!")
    
#     def pig_years(self):
#         return self.years * 18
        
# hamlet = Piglet()
# hamlet.name = "Hamlet"
# hamlet.speak()
# print(hamlet.pig_years())
# hamlet.years = 2
# print(hamlet.pig_years())

# petunia = Piglet()
# petunia.name = "Petunia"
# petunia.speak()
# print(petunia.pig_years())
# petunia.years = 4
# print(petunia.pig_years())

# ========================================
# class Apple:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
    
#     def __str__(self):
#         return f"Apple[color={self.color}, flavor={self.flavor}]"

# jonagold = Apple("red", "sweet")
# print(jonagold)
# print(help(Apple))

# ========================================
# def to_seconds(hours, minutes, seconds):
#     """Returns the amount of seconds in the given hours, minutes and seconds"""
#     return hours * 3600 + minutes * 60 + seconds

# print(to_seconds(4, 9, 2))
# print(help(to_seconds))

# ========================================
# class Fruit:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor
#     def __str__(self):
#         return f"(color={self.color}, flavor={self.flavor})"
        
# class Apple(Fruit):
#     def __init__(self, color, flavor):
#         super().__init__(color, flavor)
        
#     def __str__(self):
#         return super().__str__()
        
# class Grape(Fruit):
#     def __init__(self, color, flavor):
#         super().__init__(color, flavor)
    
#     def __str__(self):
#         return super().__str__()
        
# generic_fruit = Fruit("undefined", "undefined")
# granny_smith = Apple("green", "tart")
# carnelian = Grape("purple", "sweet")

# print(generic_fruit)
# print(granny_smith)
# print(carnelian)

# ========================================
# class Animal:
#     sound = ""
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print(f"{self.sound} I'm {self.name}!")

# class Piglet(Animal):
#     sound = "Oink!"

# class Cow(Animal):
#     sound = "Moooo!"
    
# hamlet = Piglet("Hamlet")
# hamlet.speak()
    
# milky = Cow("Milky White")
# milky.speak()

# ========================================
# class Package:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
        
# class Reoisitory:
#     def __init__(self):
#         self.packages = {}
        
#     def add_package(self, package):
#         self.packages[package.name] = package
        
#     def remove_package(self, package):
#         del self.packages[package.name]
    
#     def total_size(self):
#         result = 0
#         for package in self.packages.values():
#             result += package.size
#         return result

# ========================================
# import random

# for i in range(1, 10):
#     print(random.randint(1, 101))

# ========================================
# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.day)
# print(now.month)
# print(now.year)
# print(now + datetime.timedelta(days=28))

# ========================================
# names = ["Alex", "Lee", "Copper", "Anna", "David", "Hannah"]
# sorted_names = sorted(names)
# sorted_names = sorted(names, reverse=True)
# sorted_names = sorted(names, key=len)
# sorted_names = sorted(names, key=len, reverse=True)
# print(names)
# print(sorted_names)

# ========================================
# Final Project - Word Cloud