#Abstraction
print("\nABSTRACTION\n")
from abc import ABC, abstractmethod

class Payment(ABC): 
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} using PayPal.")

payment1 = CreditCardPayment()
payment1.make_payment(100) 
payment2 = PayPalPayment()
payment2.make_payment(200)  
