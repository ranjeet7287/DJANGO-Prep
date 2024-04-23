# raise Exception
# In Python programming, exceptions are raised when errors occur at runtime. 
# We can also manually raise exceptions using the raise keyword.

# We can optionally pass values to the exception to clarify why that exception was raised

# raise NameError('chill bro')

class Bank:
    
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        if amount < 0:
            raise Exception('amount cannot be negative')
        if amount > self.balance:
            raise Exception('Abbey Garib')
        self.balance = self.balance-amount


obj=Bank(10000)
try:
    obj.withdraw(2232)
except Exception as e:
    print(e)
else:
    print(obj.balance)

# raise -> except
# throw -> catch