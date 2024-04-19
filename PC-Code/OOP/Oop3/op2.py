class Customer:
    
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
    
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state) 



class Address:
    def __init__(self,city,pin,state):
        self.__city = city
        self.pin = pin
        self.state = state
    
    def get_city(self):
        return self.__city
    
    def edit_address(self,new_city,new_pin,new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state
    

add1=Address('Lucknow',226009,'UP')
cust1=Customer('Ranjeet','Male',add1)
cust1.edit_profile('Navneet','Noorpur',246734,'UP')

cust1.print_address()