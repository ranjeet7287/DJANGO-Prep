# Types of Inheritance
    # Single Inheritance
    # Multilevel Inheritance
    # Hierarchical Inheritance
    # Multiple Inheritance(Diamond Problem)
    # Hybrid Inheritance


# single inheritance
class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone):
    pass

SmartPhone(1000,"Apple","13px").buy()


