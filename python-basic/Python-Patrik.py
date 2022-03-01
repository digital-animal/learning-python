"""
OUTLINE:
1. Lists
2. Tuple
3. Dictionary
4. Sets
5. Strings
6. Collections
7. Itertools
8. Lambda Functions
9. Exceptions and Errors
10 Logging
11. JSON
12. Random Numbers
13. Decorators
14. Generators
15. Threading vs Multiprocessing
16. Multithreading
17. Multiprocessing
18. Functional Arguments
19. Shallow vs Deep Copying
20. The Asterisk(*) Operator
21. Context Managers
"""

#####################################
############# 1. LISTS ##############
#####################################

# mylist = ["Banana", "Cherry", "Apple"]
# print(mylist)

# mylist2 = list()
# print(mylist2)

# mylist3 = [5, True, "Mango"]
# print(mylist3)

# item = mylist[0]
# item = mylist[3]
# item = mylist[-1]
# print(item)

# for fruit in mylist:
#     print(fruit)

# if "Banana" in mylist:
#     print("Yes")
# else:
#     print("No")

# print(len(mylist))
# mylist.append("Lemon")
# print(mylist)

# mylist.insert(1, "Blueberry")
# print(mylist)

# item2 = mylist.pop()
# print(item2)

# mylist.remove("Apple")
# print(mylist)

# mylist.clear()
# print(mylist)

# mylist.reverse()
# print(mylist)

# mylist.sort()
# print(mylist)

# new_list = sorted(mylist)
# print(new_list)
# print(mylist)

# numbers = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# print(numbers)

# numbers.sort()
# print(numbers)

# sorted_list = sorted(numbers)
# sorted_list = sorted(numbers, reverse=True)
# print(sorted_list)

# print(numbers[4:9])
# print(numbers[::-1])

# copied_numbers = numbers
# copied_numbers = numbers.copy()
# copied_numbers = list(numbers)
# copied_numbers = numbers[:]

# print(numbers)
# print(copied_numbers)

# print(numbers is copied_numbers)
# print(numbers == copied_numbers)

# copied_numbers.append(-1)

# print(numbers)
# print(copied_numbers)

# squares = [x*x for x in numbers]
# squares = [x*x for x in numbers if x%2==0]
# print(squares)


#####################################
############# 2. TUPLE ##############
#####################################

# mytuple = ("Max", 28, "Boston")
# mytuple = "Max", 28, "Boston"
# mytuple = ("Max")
# print(type(("Max")))
# mytuple = ("Max",)
# print(type(("Max",)))
# print(mytuple)

# mytuple = tuple([4, 9, 2, 3, 5])
# print(mytuple)

# item = mytuple[0]
# item = mytuple[-1]
# print(item)

# for num in mytuple:
#     print(num)

# print(5 in mytuple)
# print(6 in mytuple)

# print(len(mytuple))
# print(mytuple.count(4))
# print(mytuple.index(2))

# mylist = list(mytuple)
# print(mylist)

# print(mytuple[2:4])
# print(mytuple[::-1])
# print(mytuple[::])

# person = "Max", 28, "Boston"
# name, age, city = person
# print(name)
# print(age)
# print(city)
# print(person)

# x, y, z = 4, 9, 2
# print(x, y, z)

# numbers = (4, 9, 2, 3, 5, 7, 8, 1, 6, 0)
# i, *j, k = numbers
# print(i)
# print(j)
# print(k)

# p, q, *r = numbers
# print(p)
# print(q)
# print(r)

# import sys
# L1 = (4, 9, 2, 3, 5, 7, 8, 1, 6, 0)
# L2 = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# print(sys.getsizeof(L1), "Bytes")
# print(sys.getsizeof(L2), "Bytes")

# import timeit

# print(timeit.timeit(stmt="(4, 9, 2, 3, 5, 7, 8, 1, 6, 0)", number=100000000))
# print(timeit.timeit(stmt="[4, 9, 2, 3, 5, 7, 8, 1, 6, 0]", number=100000000))

#########################################
############# 3. DICTIONARIES ###########
#########################################

# di = {"name": "Max", "age": 28, "city": "New York"}
# print(di)
# print(di["name"])
# print(di["age"])
# print(di["city"])
# print(di.get("name"))
# print(di.get("age"))
# print(di.get("city"))

# mydict = dict(name="Marry", age=27, city="Boston")
# print(mydict)
# mydict["email"] = "marry@xyz.com"
# print(mydict)
# del mydict["age"]
# print(mydict)
# mydict.pop("city")
# print(mydict)
# mydict.popitem()
# print(mydict)

# if "name" in di:
#     print(di["name"])

# print(di.keys())
# print(di.values())
# print(di.items())

# for key in di:
#     print(key)

# for key in di.keys():
#     print(key)

# for value in di.values():
#     print(value)

# for key, value in di.items():
#     print(f"{key} - {value}")

# new_dict = di
# new_dict = di.copy()
# new_dict = dict(di)

# print(di)
# print(new_dict)

# new_dict["email"] = "max@gmail.com"
# print(di)
# print(new_dict)

# person_basic = {"name": "Max", "age": 28, "city": "New York"}
# person_info = {"email": "max@gmail.com", "country": "USA", "salary": "100K"}
# print(person_basic)
# print(person_info)

# person_basic.update(person_info)

# print(person_basic)
# print(person_info)

# for k, v in person_basic.items():
#     print(f"{k} - {v}")

# frequency = {3:9, 6:36, 9:81}
# print(frequency)
# print(frequency[3])
# print(frequency[6])
# print(frequency[9])
# print(frequency.get(3))
# print(frequency.get(6))
# print(frequency.get(9))

# for k, v in frequency.items():
#     print(f"{k} - {v}")

# mytuple = (4, 9)
# mydict = {mytuple: 13}
# print(mydict)

#################################
############# 4. SETS ###########
#################################

# myset = {4, 9, 2, 3, 5, 7, 8, 1, 6, 0}
# print(myset)

# new_set = {2, 2, 3, 3, 3, 5, 5, 5, 5, 5}
# print(new_set)

# s = set([4, 9, 2, 3, 2, 9])
# print(s)

# hello = set("Hello")
# print(hello)

# empty_set = set()
# print(empty_set)

# empty_set.add(4)
# empty_set.add(9)
# empty_set.add(2)
# empty_set.add(9)
# empty_set.add(4)
# empty_set.add(6)
# print(empty_set)
# empty_set.remove(9)
# print(empty_set)
# empty_set.discard(4)
# print(empty_set)
# item = empty_set.pop()
# print(item)
# print(empty_set)
# empty_set.clear()
# print(empty_set)

# for num in myset:
#     print(num, end=" ")

# print()

# print(5 in myset)
# print(0 in myset)
# print(-1 in myset)

# A = {4, 9, 2, 3, 5}
# B = {2, 3, 5, 7, 11}
# C = {1, 3, 5, 7, 9}
# D = {2, 4, 6, 8, 10}
# E = {4, 9, 2}

# U = A.union(B)
# U = C.union(D)
# print(U)

# I = A.intersection(B)
# I = B.intersection(C)
# print(I)

# diff = A.difference(B)
# diff = B.difference(C)
# diff = C.difference(B)
# print(diff)

# diff = A.symmetric_difference(B)
# diff = B.symmetric_difference(A)
# print(diff)

# A.update(B)
# print(A)

# A.intersection_update(B)
# print(A)

# A.difference_update(B)
# print(A)

# A.symmetric_difference_update(B)
# print(A)

# print(A.issubset(B))
# print(E.issubset(A))

# print(A.issuperset(B))
# print(A.issuperset(E))
# print(E.issuperset(A))

# print(A.isdisjoint(B))
# print(C.isdisjoint(D))

# F = A
# F = A.copy()
# F = set(A)

# print(A)
# print(F)

# F.add(-1)
# print(A)
# print(F)

# M = frozenset([x*x for x in range(5)])
# print(M)

#################################
########## 5. STRINGS ###########
#################################

# my_string = "a quick brown fox jumps over the lazy dogs"
# print(my_string)
# print(len(my_string))
# print(my_string[:10])
# print(my_string[4:9])
# print(my_string[0])
# print(my_string[-1])
# print(my_string[::-1])

# name = "Zahid"
# greet = "Hello"
# sentence = f"{greet}, {name}"
# print(sentence)

# for ch in my_string:
#     print(ch, end=" ")

# print()

# print("fox" in my_string)
# print("cat" in my_string)

# text = "    Hello World    "
# print(text)
# print(len(text))

# print(text.lstrip())
# print(len(text.lstrip()))

# print(text.rstrip())
# print(len(text.rstrip()))

# print(text.strip())
# print(len(text.strip()))

# print(text.upper())
# print(text.lower())

# print(my_string.startswith("A"))
# print(my_string.startswith("a"))
# print(my_string.endswith("g"))
# print(my_string.endswith("s"))

# print(my_string.find('o'))
# print(my_string.find('fox'))
# print(my_string.find('cat'))
# print(my_string.count('o'))
# print(my_string.count('t'))
# print(my_string.replace("fox", "bird"))

# words = my_string.split()
# print(words)
# print(len(words))

# names = "Zahid,Islam,Jewel,Tonmoy,Hasan,Robi"
# print(names)
# word_list = names.split(",")
# print(word_list)
# print(len(word_list))

# new_string = "".join(word_list)
# new_string = " ".join(word_list)
# new_string = " - ".join(word_list)
# print(new_string)

# digits = [4, 9, 2, 3, 5]
# num_string = ""

# for digit in digits:
#     num_string += str(digit)

# print(num_string)
# print(int(num_string)+1)

# from timeit import default_timer as timer

# letters = ['A', 'B', 'C', 'D', 'E']
# letters = ['A', 'B', 'C', 'D', 'E']*100000

# start = timer()
# word = ''.join(letters) # faster
# stop = timer()
# print(word)
# t1 = stop-start
# print(stop-start)

# start = timer()
# new_word = ""
# for letter in letters: # slower
#     new_word += letter
# stop = timer()

# print(new_word)
# t2 = stop-start
# print(stop-start)
# print()
# print(f"Ratio: {t2/t1}")

# name = "Zahid"
# age = 28
# about = "my name is %s and i am %d years old" % (name, age)
# about = "my name is {} and i am {} years old".format(name, age)
# about = f"my name is {name} and i am {age} years old"
# print(about)

# pi = 3.14159265358979323846264
# statement = "the value of pi = %f" % pi
# statement = "the value of pi = %.8f" % pi
# statement = "the value of pi = {}" .format(pi)
# statement = f"the value of pi = {pi}"
# print(statement)

#################################
######## 6. COLLECTIONS #########
#################################
# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# from collections import Counter
# from collections import namedtuple
# from collections import OrderedDict
# from collections import defaultdict
# from collections import deque

# s = "a quick brown fox jumps over the lazy dog"
# my_counter = Counter(s)
# print(my_counter)
# print(my_counter.keys())
# print(my_counter.values())
# print(my_counter.items())
# print(my_counter.most_common(1))
# print(my_counter.most_common(2))
# print(my_counter.most_common(2)[0][1])
# print(my_counter.most_common(2)[1][1])
# print(my_counter.elements())
# print(list(my_counter.elements()))

# Point = namedtuple('Point', 'x,y')
# pt = Point(1, -4)
# print(pt)
# print(pt.x, pt.y)
# print(type(Point))
# print(type(pt))

# ordered_dict = OrderedDict()
# ordered_dict = {}
# ordered_dict["a"]=97
# ordered_dict["b"]=98
# ordered_dict["c"]=99
# ordered_dict["d"]=100
# ordered_dict["e"]=101
# print(ordered_dict)
# ordered_dict["Z"]=90
# print(ordered_dict)

# d = defaultdict(int)
# d = defaultdict(float)
# d = defaultdict(list)

# d['A']=65
# d['B']=66
# print(d)
# print(d['A'])
# print(d['B'])
# print(d['C'])

# d = deque()
# d.append(4)
# d.append(9)
# d.append(2)
# d.append(3)
# d.append(5)
# d.appendleft(-1)
# d.pop()
# d.popleft()
# d.clear()
# d.extend([1, 6, 0])
# d.extendleft([7, 8])
# d.rotate(1)
# d.rotate(2)
# d.rotate(-1)

# print(d)

#################################
######### 7. ITERTOOLS ##########
#################################
# itertools: product, permutations, combinations
# accumulate, groupby, infinite iterators

# from itertools import product
# from itertools import permutations
# from itertools import combinations
# from itertools import combinations_with_replacement
# from itertools import accumulate
# from itertools import groupby
# from itertools import count, cycle, repeat
# import operator

# A = [1, 2]
# B = [3, 4]
# B = [3]
# prod = product(A,B)
# prod = product(A,B, repeat=2)
# print(prod)
# print(tuple(prod))
# print(list(prod))

# A = [4, 9, 2]
# perm = permutations(A)
# perm = permutations(A, 2)
# print(perm)
# print(list(perm))

# letters = ['A', 'B', 'C', 'D']
# letters = ['A', 'B', 'C']
# p = permutations(letters)
# p = permutations(letters, 2)
# print(p)
# print(list(p))

# L = ['D', 'e', 'g', 'r', 'e', 'e']
# comb = combinations(L, 4)
# print(comb)
# print(list(comb))

# L = ['T', 'h', 'e', 's', 'i', 's']
# comb = combinations(L, 4)
# print(comb)
# print(list(comb))

# L = [1, 2, 3, 4]
# comb = combinations(L, 2)
# print(comb)
# print(list(comb))

# comb_wr = combinations_with_replacement(L, 2)
# print(comb_wr)
# print(list(comb_wr))

# L = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# L = [4, 9, 2, 13, 5, 7, 18, 1, 26, 0]
# acc = accumulate(L)
# acc = accumulate(L, func=operator.mul)
# acc = accumulate(L, func=max)
# print(acc)
# print(list(acc))

# def smaller_than_3(x):
#     return x<3

# L = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# group_obj = groupby(L, key=smaller_than_3)
# group_obj = groupby(L, lambda x:x<3)

# print(group_obj)
# print(list(group_obj))
# for key, value in group_obj:
#     print(key, list(value))
    # print(f"{list(value)} - {key}")

# persons = [
#     {'name':'Alex', 'age':26},
#     {'name':'Lee', 'age':28},
#     {'name':'Shaun', 'age':22},
#     {'name':'Mario', 'age':22},
#     {'name':'Cooper', 'age':29},
#     {'name':'Jim', 'age':26},
# ]

# group_obj = groupby(persons, lambda x: x['age'])
# print(group_obj)

# for key, value in group_obj:
#     print(f"{key} - {list(value)}")

# for i in count(10):
#     print(i)
#     if i == 15:
#         break

# L = [1, 2, 3]
# for i in cycle(L):
#     print(i)

# for i in repeat(1):
#     print(i)

# for i in repeat(1, 10):
#     print(i)

#################################
########## 8. LAMBDAS ###########
#################################
# lambda arguments: expression
# map(func, seq)
# filter(func, seq)
# reduce(func, seq)

# from functools import reduce

# add10 = lambda x:x+10
# print(add10(5))

# mult = lambda x, y: x*y
# print(mult(4, 9))

# points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
# points2D_sorted = sorted(points2D)
# points2D_sorted = sorted(points2D, key=lambda x: x[1])
# points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])

# print(points2D)
# print(points2D_sorted)

# L = [4, 9, 2, 3, 5]
# S = map(lambda x: x*2, L)
# S = map(lambda x: x**2, L)
# print(S)
# print(list(S))

# T = [x*2 for x in L]
# T = [x**2 for x in L]
# print(T)

# L = [4, 9, 2, 3, 5, 7, 8, 1, 6, 0]
# M = filter(lambda x: x%2 == 0, L)
# M = filter(lambda x: x > 5, L)

# print(M)
# print(list(M))

# N = [x for x in L if x > 5]
# print(N)

# L = [4, 9, 2, 3, 5, 7, 8, 1, 6]

# product = reduce(lambda x, y: x*y, L)
# print(product)

#################################
######## 9. EXCEPTIONS ##########
#################################
# Errors and Exceptions
# SyntaxError
# TypeError
# ImportError
# NameError
# FileNotFoundError
# ValueError
# IndexError
# KeyError

# x = -5
# x = 5
# if x < 0:
#     raise Exception('x should be positive')

# x = -5
# x = 5
# assert (x>=0), 'x is not positive'

# try:
#     a = 5 /0
# except:
#     print("an error happened")

# try:
#     a = 5 /0
# except Exception as e:
#     print(e)

# try:
#     a = 5/1
#     # b = a + '10'
#     b = a + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("everything is fine")
# finally:
#     print("i'm finally here")


# class ValueTooHighError(Exception):
#     pass
# class ValueTooSmallError(Exception):
#     def __init__(self, message, value):
#         self.message = message
#         self.value = value

# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError("Value is too high")
#     if x < 100:
#         raise ValueTooSmallError("Value is too small", x)

# test_value(200)
# try:
#     # test_value(200)
#     test_value(1)
# except ValueTooHighError as e:
#     print(e)
# except ValueTooSmallError as e:
#     print(e.message, e.value)


#################################
######### 10. LOGGING ###########
#################################
## timestamp: 2 hours 25 minutes
# import logging

# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")


#################################
########### 11. JSON ############
#################################
## timestamp: 2 hours 42 minutes
# # serialization i.e. encoding
# # converting python dictionary to json
# import json

# person = {
#     "name": "Zahid",
#     "age": 30,
#     "city": "Dhaka",
#     "isMarried": False,
#     "titles": [
#         "Student",
#         "Programmer",
#         "Hiker",
#     ],
#     "Salary": None,
# }

# # writing to json string
# personJSON = json.dumps(person)
# personJSON = json.dumps(person, indent=4)
# personJSON = json.dumps(person, sort_keys=True, indent=4)
# print(personJSON)

# # writing to json file
# with open("person.json", "w") as file:
#     json.dump(person, file, indent=4)

# # deserialization i.e. decoding
# # converting json object to python dictionary/object

# # reading from json string
# personDict = json.loads(personJSON)
# print(personDict)

# # reading from json file
# with open("person.json", "r") as f:
#     personDict = json.load(f)
# print(personDict)

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# user = User("Max", 27)

# # encoding function
# def encodeUser(obj):
#     if isinstance(obj, User):
#         # return {"name": obj.name, "age": obj.age, obj.__class__.__name__:True}
#         return {"name": obj.name, "age": obj.age}
#     else:
#         raise TypeError("Object of type User is not JSON serializable")

# # encoding using JSONEncoder
# from json import JSONEncoder
# class UserEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, User):
#             return {"name": obj.name, "age": obj.age, obj.__class__.__name__:True}
#             # return {"name": obj.name, "age": obj.age}
#         else:
#             raise TypeError("Object of type User is not JSON serializable")

# userJSON = json.dumps(user, indent=4, default=encodeUser)
# userJSON = json.dumps(user, indent=4, cls=UserEncoder)

# # encoding directly using UserEncoder
# userJSON = UserEncoder().encode(user)
# print(userJSON)


# #  decoding JSON
# def decodeUser(dict):
#     if User.__name__ in dict:
#         return User(name=dict["name"], age=dict["age"])
#     return dict

# user  = json.loads(userJSON)
# user  = json.loads(userJSON, object_hook=decodeUser)
# print(user)
# print(type(user))
# print(user.name, user.age)

#################################
######## 12. Random Number ######
#################################
# import random

# a = random.random()
# a = random.uniform(1, 10)
# a = random.randint(1, 10)
# a = random.randrange(1, 10)
# a = random.normalvariate(0, 1)

# print(a)

# L = list("ABCDEFGH")
# print(L)
# a = random.choice(L)
# a = random.sample(L, 4)
# a = random.choices(L, k=4)
# print(a)

# random.shuffle(L)
# print(L)

# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(1)
# print(random.random())
# print(random.randint(1, 10))

# random.seed(2)
# print(random.random())
# print(random.randint(1, 10))

# import secrets

# L = list("ABCDE")
# a = secrets.randbelow(10)
# a = secrets.randbits(4)
# a = secrets.randbits(10)
# a = secrets.choice(L)

# print(a)
# import functools
# import sys

# import numpy as np

# x = np.random.rand(3)
# x = np.random.rand(3, 3)
# x = np.random.randint(0, 10)
# x = np.random.randint(0, 10, 3)
# x = np.random.randint(0, 10, (3, 4))

# print(x)

# arr = np.array([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
# print(arr)
# np.random.shuffle(arr)
# print(arr)

# np.random.seed(1)
# print(np.random.rand(3, 3))

# np.random.seed(1)
# print(np.random.rand(3, 3))


#################################
######### 13. Decorators ########
#################################
# # function decorators vs class decorators

# import functools

# def start_end_decorator(func):

#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Start")
#         result = func(*args, **kwargs)
#         print("End")
#         return result
#     return wrapper

# @start_end_decorator
# def print_name():
#     print("Alex")

# start_end_decorator(print_name())
# print_name()

# print_name = start_end_decorator(print_name)
# print_name()

# @start_end_decorator
# def add5(x):
#     return x + 5

# add5(10)
# result = add5(10)
# print(result)

# print(help(add5))
# print(add5.__name__)

# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return  decorator_repeat

# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello {name}")

# greet("Alex")

# # class decorator

# # timestamp: 3 hours 30 minutes

#################################
######### 14. Generators ########
#################################

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# g = my_generator()
# print(g)

# for i in g:
#     print(i)

# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)

# print(sum(g))
# print(sorted(g))

# def countdown(num):
#     print("Starting")
#     while num > 0:
#         yield num
#         num -= 1

# cd = countdown(4)
# print(cd)
# value = next(cd)
# print(value)

# value = next(cd)
# print(value)

# value = next(cd)
# print(value)

# value = next(cd)
# print(value)

# for x in cd:
#     print(x)


# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# def firstn_generator(n):
#     num = 0
#     while num < n:
#         yield num
#         num = num + 1

# mylist = firstn(10)
# mylist = firstn(1000000)
# print(mylist)
# print(sys.getsizeof(mylist))
# print(sum(mylist))

# mylist2 = firstn_generator(10)
# mylist2 = firstn_generator(1000000)
# print(mylist2)
# print(sys.getsizeof(mylist2))
# print(sum(mylist2))

# for x in mylist2:
#     print(x, end=" ")

# def fibonacci(limit):
#     a, b = 0, 1
#     while a < limit:
#         yield a
#         a, b = b, a+b

# fib = fibonacci(100)
# fib = fibonacci(1000)
# fib = fibonacci(10000)
# print(sys.getsizeof(fib))
# for x in fib:
#     print(x, end=" ")

# # generator expression

# my_generator = (i for i in range(100) if i % 2 ==0)
# print(my_generator)
# for x in my_generator:
#     print(x, end=" ")
# print()

# print(list(my_generator))

################################################
######## 15. Threading vs Multiprocessing ######
################################################
# # process vs thread

# from multiprocessing import Process
# from threading import Thread
# import os
# import time

# def square_numbers():
#     for i in range(100):
#         print(i * i)
#         time.sleep(0.1)

# processes = []
# num_processes = os.cpu_count()
# print(num_processes)

# threads = []
# num_threads = os.cpu_count()
# print(num_threads)

# for i in range(num_processes):
#     p = Process(target=square_numbers)

# start
# for p in processes:
#     p.start()

# join
# for p in processes:
#     p.join()

# print("end main")

# for i in range(num_threads):
#     t = Thread(target=square_numbers)
#     threads.append(t)

# start
# for t in threads:
#     t.start()

# join
# for t in threads:
#     t.join()

# print("end main")


#################################
######### 16. Threading #########
#################################

# # timestamp: 4 hours 8 minutes


#################################
###### 17. Multiprocessing ######
#################################

# # timestamp: 4 hours 31 minutes


####################################
###### 18. Function Arguments ######
####################################
# # positional vs keyword arguments
# def print_name(name):
#     print(f"Hello {name}")

# print_name("Alex")

# def foo(a, b, c):
#     print(a, b, c)

# foo(a=4, b=9, c=2)
# foo(b=9, c=2, a=4)
# foo(4, c=2, b=9)

# def bar(a, b, c, d=3):
#     print(a, b, c, d)

# bar(4,9,2)
# bar(4, 9, 2)
# bar(4, b = 9, c = 2)
# bar(4, b = 9, c = 2, d = 6)

# # variable length argument
# def foo(a, b, *args, **kwargs):
#     print(a, b)
#     for arg in args:
#         print(arg)
    # for key, value in kwargs:
    #     print(f"{key} - {value}")
    # for key in kwargs:
    #     print(f"{key} - {kwargs[key]}")

# a = 4
# b = 9
# L = { 4, 9, 2, 3, 5}
# D = {
#     "name":"Zahid",
#     "age": 30,
#     "salary": None,
# }

# foo(a, b)
# foo(a, b, L)
# foo(a, b, L, D)

# foo(4, 9)
# foo(4, 9, 2)
# foo(4, 9, three=3, five=5)

# # packing and unpacking

# def pack_unpack(a, b, c):
#     print(a, b, c)

# L = [4, 9, 2]
# pack_unpack(*L)

# def pack_unpack(name, age, salary):
#     print(name, age, salary)

# D = {
#     "name":"Zahid",
#     "age": 30,
#     "salary": None,
# }

# pack_unpack(**D)

# # global vs local

# # call by object
# # call by object reference


###################################
###### 19. Asterisk Operator ######
###################################

# # unpacking
# numbers = [4, 9, 2, 3, 5, 7]

# *beginning, end = numbers
# beginning, *end = numbers
# beginning, *mid, end = numbers
# print(beginning)
# print(mid)
# print(end)

# my_list = [3, 5, 7]
# my_tuple = (4, 9, 2)
# my_set = {8, 1, 6}

# new_list = [*my_tuple, *my_list, *my_set]
# print(new_list)

# dict_A = {"a": 1, "b": 2}
# dict_B = {"c": 3, "d": 4}
# dict_C = {**dict_A, **dict_B}
# print(dict_C)


######################################
###### 19. Shallow vs Deep Copy ######
######################################

# org = 5
# copy = org
# final = 5
# print(org.__hash__)
# print(copy.__hash__)
# print(final.__hash__)

# L1 = [4, 9, 2]
# L2 = L1
# L3 = [4, 9, 2]
# print(L1 == L2)
# print(L1 is L2)

# print(L1 == L3)
# print(L1 is L3)

# print(L2 == L3)
# print(L2 is L3)

# import copy

# L1 = [4, 9, 2]
# L2 = copy.copy(L1)
# L2 = L1.copy()
# L2 = list(L1)
# L2 = L1[:]
# print(L1 == L2)
# print(L1 is L2)

# M = [
#     [4, 9, 2],
#     [3, 5, 7],
#     [8, 1, 6],
# ]
# N = M.copy()
# N = copy.deepcopy(M)

# print(M)
# print(N)
# M[0][0] = -4
# print(M)
# print(N)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Company:
#     def __init__(self, boss, emp):
#         self.boss = boss
#         self.emp = emp


# p1 = Person("Alex", 21)
# p2 = p1
# p2 = copy.copy(p1)

# p2.age = 26

# print(p1.age)
# print(p2.age)

# p1 = Person("Alex", 28)
# p2 = Person("Lee", 24)

# c1 = Company(p1, p2)
# c2  = c1
# c2  = copy.copy(c1)
# c2  = copy.deepcopy(c1)

# print("# Before Changing")
# print(c1.boss.name)
# print(c1.boss.age)

# print(c2.boss.name)
# print(c2.boss.age)

# c2.boss.name = "Cooper"
# c2.boss.age = 33

# print("# After Changing")
# print(c1.boss.name)
# print(c1.boss.age)

# print(c2.boss.name)
# print(c2.boss.age)


######################################
####### 21. Context Managers # #######
######################################

# with open("notes.txt", "w") as file:
#     file.write("Some text here..")

# with open("notes.txt", "r") as f:
#     str = f.read()
#     print(str)

# # context manager class
# class ManagedFile:
#     def __init__(self, filename):
#         print("init")
#         self.filename = filename
#
#     def __enter__(self):
#         print("enter")
#         self.file = open(self.filename, "w")
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#         print("exit")


# with ManagedFile("notes.txt") as note:
#     print("inside context manager")
#     note.write("Testing Context Managers..")


# from contextlib import contextmanager

# @contextmanager
# def open_managed_file(filename):
#     f = open(filename, "w")
#     try:
#         yield f
#     except:
#         pass
#     finally:
#         f.close()

# with open_managed_file("notes.txt") as n:
#     n.write("Testing context manager generator")
