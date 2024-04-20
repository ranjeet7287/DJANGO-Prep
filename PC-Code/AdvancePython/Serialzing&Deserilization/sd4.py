# Serializing and Deserializing custom objects
import json
class Person:

    def __init__(self,fname,lname,age,gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

# format to printed in
# -> Ranjeet Singh age -> 20 gender -> male
person = Person('Ranjeet','Singh',20,'male')

# As a string
def show_object(person):
    if isinstance(person,Person):
        return f"{person.fname} {person.lname} age -> {person.age} gender -> {person.gender}"

def show_object2(person):
    if isinstance(person,Person):
        return {'first_name':person.fname,'last_name':person.lname,'age':person.age,'gender':person.gender}

with open('demo.json','w') as f:
    json.dump(person,f,default=show_object2,indent=4)