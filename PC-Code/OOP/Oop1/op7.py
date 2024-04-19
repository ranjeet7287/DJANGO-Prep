# Reference Variables
    # Reference variables hold the objects
    # We can create objects without reference variable as well
    # An object can have multiple reference variables
    # Assigning a new reference variable to an existing object does not create a new object

# object without a reference
class Person:

    def __init__(self):
        self.name = 'Ranjeet'
        self.gender = 'male'

    
Person()      # yes object created
p = Person()  # p is reference variable 
q = p         # both are pointing to same object 

print(p.name)
print(q.name)
q.name="Singh"
print(p.name)
print(q.name)