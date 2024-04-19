# Method Overriding

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a phone")
    

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")

s=SmartPhone(2000,"Apple",12)
s.buy()
# if we have same two method in parent & child that we give priority to child method