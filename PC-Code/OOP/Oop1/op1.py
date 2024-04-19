class Atm:
    # Constructor
    def __init__(self):
        self.pin=''
        self.balance=0

obj = Atm()
print(type(obj))  #  <class '__main__.Atm'>

# object can access things that are present in a class

# obj.balance=10
# obj.pin='1234'