# Object ki mutability
class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# outside the class -> function
def greet(person):
    person.name = 'ankit'
    return person
    
p = Person('nitish','male')
print(id(p))
p1 = greet(p)