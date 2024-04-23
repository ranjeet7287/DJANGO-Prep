# Custom 
class MyException(Exception):
    def __init__(self,message):
        print(message)

class Bank:

    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,amount):
        if amount < 0:
            raise MyException('amount cannot be -ve')
        if self.balance < amount:
            raise MyException('paise nai hai tere paas')
        self.balance = self.balance - amount

obj = Bank(10000)
try:
    obj.withdraw(5000)
except MyException as e:
    pass
else:
    print(obj.balance)