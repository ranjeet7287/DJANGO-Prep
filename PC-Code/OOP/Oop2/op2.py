# Collection of objects

# list of objects
class Person:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    
    # getter
    def getName(self):
        return self.__name
    def getGender(self):
        return self.__gender

    # setter
    def setName(self,name):
        if(type(name)==str):
            self.__name=name
        else:
            return "name datatype should be in string"
    
    def setGender(self,gender):
        if(type(gender)==str):
            self.__gender=gender
        else:
            return "Gender should be in string format"

p1=Person('Ranjeet','Male')
p2=Person('Shubham bhaiya','Male')
p3=Person('Pinki Didi','Female')

L = [p1,p2,p3]

for i in L:
    print(i.getName(),i.getGender())
