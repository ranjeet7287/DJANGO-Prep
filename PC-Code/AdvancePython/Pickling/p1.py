# Pickling
    # Pickling is the process whereby a Python object hierarchy is converted into a 
    # byte stream, and unpickling is the inverse operation, whereby a
    # byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

import pickle
class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print('Hi my name is',self.name,'and I am ',self.age,'years old')
    
p = Person('Ranjeet',21)

with open('person.pkl','wb') as f:
    pickle.dump(p,f)

with open('person.pkl','rb') as f:
    p = pickle.load(f)
    print(p.display_info())