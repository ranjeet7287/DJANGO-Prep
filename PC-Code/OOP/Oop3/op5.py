# constructor example 2

class Phone:
    
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("Inside SmartPhone constructor")

s=SmartPhone("Android", 2)
s.brand
# Error because Phone constructor didn't intialize yet that's why show error 
# Agar child ka khud ka constructor hai na isley parent ka constructor call nhi hua

