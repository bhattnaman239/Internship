#Encapsulation
print("\nEncapsulation\n")
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print(account.get_balance())
account.__balance = 1000 # This will not change the balance
print(account.get_balance())
