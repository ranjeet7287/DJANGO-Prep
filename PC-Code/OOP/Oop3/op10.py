# Super Keyword -> Whenever we want to use Parent method we use super

class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print("Buying a phone")
    

class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")
        
        # syntax to call parent ka buy method
        super().buy()
    

s=SmartPhone(20000,'Apple',120)
s.buy()
