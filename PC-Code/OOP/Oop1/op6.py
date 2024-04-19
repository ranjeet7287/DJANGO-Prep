# Attribute creation from outside of the class
class Person:

    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input

    def greet(self):
        if self.country == 'india':
            print('Namaste',self.name)
        else:
            print('Hello',self.name)

# what if i try to access non-existent attributes
# obj1= p.gender
# ---------------------------------------------------------------------------
# AttributeError                            Traceback (most recent call last)
# <ipython-input-49-39388d77d830> in <module>
#       1 # what if i try to access non-existent attributes
# ----> 2 p.gender

# AttributeError: 'Person' object has no attribute 'gender'

obj = p.gender = 'male'