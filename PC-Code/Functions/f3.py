# *args and **kwargs
# Are special python keyword that are used to pass the variable length of argument to a function

# *args 
# allows us to pass a variable number of non-keyword argument to a functions

def multiply(*args):
    mul = 1
    for i in args:
        mul = mul*i
    return mul

res=multiply(2,3,4,5)
print(res)

# **kwargs
# **kwargs allows us to pass any number of keyword arguments
# Keyword arguments means that they contain key-value pair, like a dict

def display(**kwargs):
    for (key,value) in kwargs.items():
        print(key,'->',value)

display(India='Delhi',Pakistan='Islamabad',Nepal='Kathmandu',Srilanka='Colombo')
