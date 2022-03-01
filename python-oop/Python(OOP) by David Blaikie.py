
# # 103 object oriented python

# myint = 2
# mystr = "hello"
#
# print(type(myint))
# print(type(mystr))

# mylist = ['a', 'b', 'c']
# mybool = True
# mynone = None
#
# def myfunc():
#     print("hello")
#
# print(type(mylist))
# print(type(mybool))
# print(type(mynone))
# print(type(myfunc))
#
# this_type = type(mylist)
# print(type(this_type))

# var = 5
# print(dir(var))
# print(var.real)
# print(var.imag)
# print(var.bit_length())

# from decimal import Decimal
#
# # print(Decimal('3.5') + Decimal('3.5'))
#
# num = Decimal('3.5') + Decimal('3.5')
# print(num)
# print(type(num))

# print("Hello, Pycharm")
#
# sum = 0
# max = 10
#
# for num in range(max):
#     sum = 0
#     sum = sum + num
#
# print(f"the sum is {sum}")
#
# def ok_then():
#     pass
#
# def well_then():
#     pass

# var = "hello, world"
# print(type(var))
# print(var.upper())

# # 302 Defining a class
# class MyClass:
#     var = 10
#
# this_obj = MyClass()
# print(this_obj)
#
# that_obj = MyClass()
# print(that_obj)
#
# print(this_obj.var)
# print(that_obj.var)

# # 303 instance methods
class Joe:
    greeting = "Hello, Joe"
    def callme(self):
        # print("calling 'callme' method with instance: ")
        print(self)

thisjoe = Joe()
print(thisjoe)
# print(thisjoe.greeting)
thisjoe.callme()