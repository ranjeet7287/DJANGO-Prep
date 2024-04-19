# Inheritance 

# What gets inherited?
    # Constructor
    # Non Private Attributes
    # Non Private Methods


# Parent Class
class User:
    
    def __init__(self):
        self.name = 'Ranjeet'
    
    def login(self):
        print('login')

# Child Class
class Student(User):
    
    # Method overideing
    # def __init__(self):
    #     self.roll_no=21
    
    def enroll(self):
        print('Enroll into the course')

u=User()
s=Student()
# child using parent class method
s.login()
