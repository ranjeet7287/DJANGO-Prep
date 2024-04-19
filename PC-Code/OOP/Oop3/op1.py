# Class Relationships
    # Aggregation
    # Inheritance

# Aggregation (Has-A relationship)

class Customer:
    
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
    

class Address:
    def __init__(self,city,pin,state):
        self.__city = city
        self.pin = pin
        self.state = state
    
    def get_city(self):
        return self.__city

add1=Address('Lucknow',226009,'UP')
cust1=Customer('Ranjeet','Male',add1)

cust1.print_address()