# Child can't access private members of the class

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    
    def show(self):
        print(self.__price)

class SmartPhone(Phone):

    def check(self):
        print(self.__price)

s = SmartPhone(200000,'Apple',13)
s.check()
