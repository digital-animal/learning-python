from abc import ABC
from abc import ABCMeta
from abc import abstractmethod
import random

class Account(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def createAccount(self, firstName, lastName, init_deposit):
       pass
    @abstractmethod
    def authenticate(self, name, account_no):
        pass
    @abstractmethod
    def withdrawBalance(self, withdraw_amount):
        pass
    @abstractmethod
    def depositBalance(self, deposit_amount):
        pass
    @abstractmethod
    def displayBalance(self):
        pass


class SavingsAccount(Account):
    index = random.randint(10000,99999)
    def __init__(self):
        super().__init__()
        self.account_log = {}

    def createAccount(self, firstName, lastName, init_deposit):
        self.fistName = firstName
        self.lastName = lastName
        self.fullName = f"{self.fistName} {self.lastName}"
        self.init_deposit = init_deposit
        self.account_no = SavingsAccount.index

        self.account_log[self.account_no] = [f"{self.fullName}", self.init_deposit]

        print("Account Created Successfully.")
        self.displayBalance()

    def authenticate(self, name, account_no):
        if account_no in self.account_log.keys():
            if self.account_log[account_no][0] == name:
                print("Authentication Successful")
                self.account_no = account_no
                return True
            else:
                print("Authentication Failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withdrawBalance(self, withdraw_amount):
        if withdraw_amount > self.account_log[self.account_no][1]:
            print("Insufficient Balance")
        else:
            self.account_log[self.account_no][1] -= withdraw_amount
            print("Withdrawal Successful")
            self.displayBalance()

    def depositBalance(self, deposit_amount):
        self.account_log[self.account_no][1] += deposit_amount
        print("Deposit Successful")
        self.displayBalance()

    def displayBalance(self):
        print(f"\tACCOUNT DETAILS:")
        print(f"\tAccount No: {self.account_no}")
        print(f"\tAccount Name: {self.account_log[self.account_no][0]}")
        print(f"\tCurrent Balance: {self.account_log[self.account_no][1]}")

class Customer:
    pass

acc = SavingsAccount()

while True:
    print("\t ========== Main Menu ========== ")
    print("\t 1.Create New Account")
    print("\t 2.Access Existing Account")
    print("\t 3.Exit Menu")
    print("\t ========== XXXXXXXXX ========== ")
    user_choice = int(input(">> "))
    if user_choice == 1:
        first_name = input(">> Enter First Name> ")
        last_name = input(">> Enter Last Name> ")
        init_deposit = int(input(">> Enter Initial Deposit> "))
        acc.createAccount(first_name, last_name, init_deposit)
    elif user_choice == 2:
        name = input(">> Enter Your Name> ")
        acc_no = int(input(">> Enter Account No> "))
        authenticate_status = acc.authenticate(name, acc_no)
        if authenticate_status is True:

            while True:
                print("\t=========== USER MENU ===========")
                print("\tEnter 1 to Withdraw")
                print("\tEnter 2 to Deposit")
                print("\tEnter 3 to Display Balance")
                print("\tEnter 4 to Return to Previous Menu")
                print("\tEnter 5 to EXIT")
                print("\t=========== XXXXXXXXX ===========")

                user_choice = int(input(">> "))
                if user_choice == 1:
                    withdraw_amount = int(input("Enter Withdrawal Amount> "))
                    acc.withdrawBalance(withdraw_amount)
                elif user_choice == 2:
                    deposit_amount = int(input("Enter Deposit Amount> "))
                    acc.depositBalance(deposit_amount)
                elif user_choice == 3:
                    acc.displayBalance()
                elif user_choice == 4:
                    break
                elif user_choice == 5:
                    quit()

    elif user_choice == 3:
        quit()
    print()