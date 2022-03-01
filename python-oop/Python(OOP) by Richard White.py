"""
This program allows me to manage my contacts.
@Zahidul Islam
@Version 2020-06-04
"""
# # # example - 01
# def main():
#     print("Contact Manager")
#     name = input(">Enter name: ")
#     phone = input(">Enter phone: ")
#     email = input(">Enter email: ")
#
#     print(f"{name}, {phone}, {email}")
#
#
# if __name__ == "__main__":
#     main()


# # # example - 02
# def main():
#     friends = []
#     for i in range(2):
#         print("Contact Manager")
#         name = input(">Enter name: ")
#         phone = input(">Enter phone: ")
#         email = input(">Enter email: ")
#         friends.append([name,phone,email])
#
#     for i in range(len(friends)):
#         print("Contact info")
#         for j in range(len(friends[i])):
#             print(friends[i][j])
#
#
# if __name__ == "__main__":
#     main()


# # # example - 03
# class Person(object):
#     """
#     The person class defines a person in terms of a name,age,
#     phone numbers and email address
#     """
#     # constructor
#     def __init__(self,name,age,phone,email):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         self.email = email
#
#     # accessor methods (getters)
#     def getName(self):
#         return self.name
#     def getAge(self):
#         return self.age
#     def getPhone(self):
#         return self.phone
#     def getEmail(self):
#         return self.email
#
#     # mutator methods (setters)
#     def setName(self, name):
#         self.name = name
#     def setAge(self, age):
#         self.age = age
#     def setPhone(self, phone):
#         self.phone = phone
#     def setEmail(self, email):
#         self.email = email
#
#     # friend details
#     def __str__(self):
#         return f"Name: {self.name}\nAge: {self.age}\
#         \nPhone: {self.phone}\nEmail: {self.email}"
#
#
# def main():
#     friend1 = Person("Zahid",30,"123-456","zahid@gmail.com")
#     friend2 = Person("Jewel",30,"012-456","jewel@gmail.com")
#     print(friend1.getName())
#     print(friend2.getName())
#
#     friend1.setAge(31)
#     friend2.setPhone("456-789")
#     print()
#
#     print(friend1)
#     print()
#     print(friend2)
#
#
# if __name__ == "__main__":
#     main()


# # example - 04
# class Person(object):
#     """
#     The person class defines a person in terms of a name,age,
#     phone numbers and email address
#     """
#     # constructor
#     def __init__(self,name,age,phone,email):
#         self.name = name
#         self.age = age
#         self.phone = phone
#         self.email = email
#
#     # accessor methods (getters)
#     def getName(self):
#         return self.name
#     def getAge(self):
#         return self.age
#     def getPhone(self):
#         return self.phone
#     def getEmail(self):
#         return self.email
#
#     # mutator methods (setters)
#     def setName(self, name):
#         self.name = name
#     def setAge(self, age):
#         self.age = age
#     def setPhone(self, phone):
#         self.phone = phone
#     def setEmail(self, email):
#         self.email = email
#
#     # friend details
#     def __str__(self):
#         return f"Name: {self.name}\nAge: {self.age}\
#         \nPhone: {self.phone}\nEmail: {self.email}"
#
#
# def enter_a_friend():
#     name = input(">Enter friend's name: ")
#     age = input(">Enter age: ")
#     phone = input(">Enter phone number: ")
#     email = input(">Enter email address: ")
#     return Person(name,age,phone,email)
#
# def lookup_a_friend(friends):
#     found = False
#     name = input(">Enter a name to lookup: ")
#     for friend in friends:
#         if name in friend.getName():
#             print(friend)
#             found = True
#     if not found:
#         print("Not friends match that term")
#
# def show_all_friends(friends):
#     print("Showing all friends")
#     for friend in friends:
#         print(friend)
#         print(end="\n")
#
# def main():
#     friends = []
#     running = True
#     while running:
#         print("\nContacts Manager")
#         print("1) New Contact       2) Lookup")
#         print("3) Show All          4) end")
#         option = input("> ")
#         if option == "1":
#             new_friend = enter_a_friend()
#             friends.append(new_friend)
#         elif option == "2":
#             lookup_a_friend(friends)
#         elif option == "3":
#             show_all_friends(friends)
#         elif option == "4":
#             running = False
#         else:
#             print("Unrecognized input. Please try again.")
#         print("Program ending.")
#
# if __name__ == "__main__":
#     main()


# # New Example
# # Clothing Class

"""
This program uses a clothing class to keep track of my wardrobe.
@author Zahidul Islam
@version 2020-06-05 v-1.0
"""
# # example - 01

# class Clothing:
#     """
#     The Clothing class defines a piece of clothing in terms of
#     its name and its cleanliness
#     """
#     def __init__(self, name, clean=True):
#         self.name = name
#         self.clean = clean
#
#     def getName(self):
#         return self.name
#
#     def isClean(self):
#         return self.clean
#
#     def __str__(self):
#         return f"Cloth Name: {self.name}\nisClean: {self.clean}\n"
#
#
# def main():
#     # test the clothing class
#     myJeans = Clothing("blue jeans", False)
#     myShorts = Clothing("shorts")
#
#     print(myJeans.getName())
#     print(myShorts.getName())
#     print()
#     print(myJeans.isClean())
#     print(myShorts.isClean())
#     print()
#     print(myJeans)
#     print(myShorts)
#     print(myJeans.__dict__)
#     print(myShorts.__dict__)
#
# if __name__ == "__main__":
#     main()

# # example - 02
"""
This program uses a clothing class to keep track of my wardrobe.
@author Zahidul Islam
@version 2020-06-05 v-1.1
"""
class Clothing:
    """
    The Clothing class defines a piece of clothing in terms of
    its name and its cleanliness
    """
    def __init__(self, name, clean=True, times_worn = 0, max_wears = 1):
        self.name = name
        self.clean = clean
        self.times_worn = times_worn
        self.max_wears = max_wears

    def getName(self):
        return self.name

    def isClean(self):
        return self.clean

    def wear(self):
        print("Now Wearing..\n")
        self.times_worn += 1
        if self.times_worn >= self.max_wears:
            self.clean = False
    def wash(self):
        print("Washing..\n")
        self.clean = True
        self.times_worn = 0

    def __str__(self):
        return f"\nCloth Name: {self.name} \
        \nisClean: {self.clean} \
        \nTimes Worn: {self.times_worn} \
        \nMax Wears: {self.max_wears}"

class Shirt(Clothing):
    def __init__(self, name, clean=True, times_worn = 0, max_wears = 1, short_sleeves = True):
        super().__init__(name, clean, times_worn , max_wears)
        self.short_sleeves = short_sleeves

    def hasShortSleeves(self):
        return self.short_sleeves

    def __str__(self):
        return f"\nshirt:{super().__str__()} \
        \nShort Sleeves: {str(self.short_sleeves)}\n"

def main():
    # # test the clothing class
    myClothes = []
    myClothes.append(Clothing("Blue Jeans",False))
    myClothes.append(Clothing("Baseball Cap", True, 20, 1000))
    myClothes.append(Clothing("Jacket",True,20,100))
    myClothes.append(Shirt("T-Shirt",True,0,1,True))
    myClothes.append(Shirt("Dress Shirt", True,0,1,False))

    print("\n======= FULL WARDROBE ========")
    for i in range(len(myClothes)):
        print(myClothes[i])

    print("\n======= CLEAN CLOTHES ========")
    for i in range(len(myClothes)):
        if myClothes[i].isClean():
            print(myClothes[i])

    print("\n======= DIRTY CLOTHES ========")
    for i in range(len(myClothes)):
        if not myClothes[i].isClean():
            print(myClothes[i])

    print("\n======= SHIRTS ========")
    for i in range(len(myClothes)):
        if isinstance(myClothes[i],Shirt):
            print(myClothes[i])

    print("\n======= CLEAN SHIRTS ========")
    myClothes[-1].wear()
    for i in range(len(myClothes)):
        if isinstance(myClothes[i],Shirt):
            if myClothes[i].isClean():
                print(myClothes[i])

    print("\n======= DIRTY SHIRTS ========")
    for i in range(len(myClothes)):
        if isinstance(myClothes[i],Shirt):
            if not myClothes[i].isClean():
                print(myClothes[i])

if __name__ == "__main__":
    main()

