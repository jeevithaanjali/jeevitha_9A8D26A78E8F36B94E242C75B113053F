
class BankAccount:
    def __init__(self,account_no,account_holder_name,initial_balance=0.0):
        self.__account_no = account_no
        self.__account_holder_name = account_holder_name
        self.__initial_balance = initial_balance
    def deposit(self,amount):
        if amount>0:
            self.__initial_balance+=amount
            print("deposited ${}".format(amount,self.__account_holder_name))
        else:
            print("invalid deposit amount.please deposit a positive amount.")
    def withdraw(self,amount):
        if amount>0 and amount<=self.__initial_balance:
            self.__initial_balance-=amount
            print("withdrawal amount",amount,"\nnew account balance ",self.__initial_balance)
        else:
            print("invalid withdrawal amount or insufficient balance")
    def display_balance(self):
        print("account holder name : ",self.__account_holder_name,"\nnew account balance : ",self.__initial_balance)

account = BankAccount(1234567,"jeevitha",70000)
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()