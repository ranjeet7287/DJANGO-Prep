# # Pass by reference 

# class Person:
#     def __init__(self,name,gender):
#             self.name=name
#             self.gender=gender


# # outside the class -> function
# def greet(person):
#     print(f"Hello {person.name}")

# p = Person('Ranjeet','Male')
# greet(p) 


class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

# outside the class -> function
def greet(person):
    print(id(person))
    person.name = 'ankit'
    print(person.name)

p = Person('nitish','male')
print(id(p))
greet(p)
print(p.name)