# ⭐ If child doesn't have our constructor then parent constructor intialize ⭐

class Phone:

    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
    
    def buy(self):
        print("Buying a phone")
    

class SmartPhone(Phone):
    pass

user = SmartPhone(20000,'OnePlus','120mp')
user.buy()
