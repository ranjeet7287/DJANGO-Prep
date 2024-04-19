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
        
        # print(super().brand)
        # AttributeError: 'super' object has no attribute 'brand' 
        # We can not access attribute using super only access methods

    

s=SmartPhone(20000,'Apple',120)
s.buy()


# Summary Point

    #  1.Super cannot access variables

    #  2.Super cannot be used outside a class
    
    #  3.Super is used inside a child class


# Inheritance in summary

    # A class can inherit from another class.

    # Inheritance improves code reuse

    # Constructor, attributes, methods get inherited to the child class

    # The parent has no access to the child class

    # Private properties of parent are not accessible directly in child class

    # Child class can override the attributes or methods. This is called method overriding

    # super() is an inbuilt function which is used to invoke the parent class methods and constructor
