# # # Data Structure in Python (Lucid Programming)
# # # 01 - stack - stack data structure
#
#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def is_empty(self):
#         if self.items == []:
#             return True
#         return False
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#
#     def get_stack(self):
#         return self.items
#
#
# s = Stack()
# # s.push("A")
# # s.push("B")
# # s.push("C")
# # s.push("D")
# # print(s.get_stack())
# # print(s.pop())
# # print(s.pop())
# # print(s.get_stack())
# # print(s.is_empty())
# # print(s.pop())
# # print(s.pop())
# # print(s.is_empty())
# # # print(s.pop())
# # s.push("D")
# # print(s.get_stack())
#
# # print(s.peek())
# # print(s.get_stack())
# # s.pop()
# # print(s.peek())
# # print(s.get_stack())
#
# s2 = Stack()
#
# for i in range(1, 11):
#     s2.push(i)
# print(s2.get_stack())
#
# print(s2.peek())
#
# for i in range(5):
#     s2.pop()
#
# print(s2.is_empty())
# print(s2.get_stack())
# print(s2.peek())
# print(s2.get_stack())
# print(s2.pop())
# print(s2.get_stack())


# # # 02 stack - determine if parenthesis are balanced
"""
use s stack to check whether or not a string has balanced
usage of parenthesis.
example:
        (), ()(), (({[]})) ==> balanced
        ((), {{{)}], [][]]] ==> not balanced
balanced example: {[]}
non-balanced example: (()
non-balanced example: ))
"""

# from stack import Stack
#
#
# def is_match(p1, p2):
#     if p1 == "(" and p2 == ")":
#         return True
#     elif p1 == "{" and p2 == "}":
#         return True
#     elif p1 == "[" and p2 == "]":
#         return True
#     else:
#         return False
#
#
# def is_paren_balanced(paren_string):
#     s = Stack()
#     is_balanced = True
#     index = 0
#
#     while index < len(paren_string):
#         paren = paren_string[index]
#         if paren in "({[":
#             s.push(paren)
#
#         elif paren in ")}]" and s.is_empty():
#             is_balanced = False
#
#         elif paren in ")}]" and not s.is_empty():
#             top = s.pop()
#             if not is_match(top, paren):
#                 is_balanced = False
#         index += 1
#
#     if s.is_empty() and is_balanced:
#         print(s.get_stack())
#         return True
#     else:
#         print(s.get_stack())
#         return False
#
#
# # t = "("
# # t = "()"
# # t = "(()"
# # t = "(())"
# # t = "(()))"
# # t = "((()))"
# # t = "[][]"
# # t = "[(}]"
# # t = "[()]"
# # t = "[{()]"
# # t = "[{()}]"
# # t = "(({[]}))"
# # t = "{{{)}]"
# # t = "))"
# # t = "))("
# # t = ")("
# # t = "()("
# # t = "()()"
# # t = "A+(B+C)"
# # t = "(A+B)(A+C) = A(B+C)"
# # print(is_paren_balanced(t))


# # approach - 2
#
# from stack import Stack
#
#
# def is_match(p1, p2):
#     if p1 == "(" and p2 == ")":
#         return True
#     elif p1 == "{" and p2 == "}":
#         return True
#     elif p1 == "[" and p2 == "]":
#         return True
#     else:
#         return False
#
#
# def paren_test(input_string):
#     s = Stack()
#     is_balanced = True
#
#     for ch in input_string:
#         if ch in "({[":
#             s.push(ch)
#
#         elif ch in ")}]":
#             if s.is_empty():
#                 is_balanced = False
#             else:
#                 top = s.pop()
#                 if is_match(top, ch):
#                     is_balanced = True
#
#     if s.is_empty() and is_balanced:
#         print(s.get_stack())
#         return True
#     else:
#         print(s.get_stack())
#         return False
#
# # # t = "("
# # t = "()"
# # t = "(()"
# # t = "(())"
# # t = "(()))"
# # t = "((()))"
# # t = "[][]"
# # t = "[(}]"
# # t = "[()]"
# # t = "[{()]"
# # t = "[{()}]"
# # t = "(({[]}))"
# # t = "{{{)}]"
# # t = "))"
# # t = "))("
# # t = ")("
# # t = "()("
# # t = "()()"
# t = "A+(B+C)"
# t = "(A+B)(A+C) = A(B+C)"
# print(paren_test(t))


# # # 03 - stack - convert integer to binary
"""
use a stack data structure to convert integer values to binary
example: 242
242 / 2 = 121 ==> 0
121 / 2 = 60  ==> 1
60 / 2 = 30   ==> 0
30 / 2 = 15   ==> 0
15 / 2 = 7    ==> 1
7 / 2 = 3     ==> 1
3 / 2 = 1     ==> 1
1 / 2 = 0     ==> 1
"""


# # print(int("11110010", 2))
#
# from stack import Stack
#
#
# def to_binary(dec_num):
#     s = Stack()
#
#     while dec_num > 0:
#         remainder = dec_num % 2
#         s.push(remainder)
#         dec_num = dec_num // 2
#
#     bin_num = ""
#     while not s.is_empty():
#         bin_num += str(s.pop())
#
#     return bin_num
#
#
# print(to_binary(242))
# print(bin(242))
# print(to_binary(8))
# print(bin(8))


# # # 08 - reversing s string using stack
# # # input string ==> "Hello"
# # # output string ==> "olleH"
#
# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]
#
#     def get_stack(self):
#         return self.items
#
#     def is_empty(self):
#         if self.items == []:
#             return True
#         return False
#
# def reverse_string(input_str):
#
#     s = Stack()
#     # loop through the string and push contents
#     # character by character onto stack
#     for ch in input_str:
#         s.push(ch)
#
#     # print(s.items)
#
#     rev_str = ""
#     while not s.is_empty():
#         rev_str += s.pop()
#     # print(rev_str)
#     return rev_str
#
#
#
# input_str = "Hello"
# print(f"reverse of '{input_str}' is '{reverse_string(input_str)}'")
