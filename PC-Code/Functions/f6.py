# Functions are 1st class citizens

# type and id

# function in python act as a datatype
def square(num):
    return num**2
x=square(2)
print(type(square))
print(id(square))

# reassign
x=square
print(x(1))

# deleting a function
del x
# print(x(3))
print(square(3))


# sorting
L=[1,2,3,4,square(5)]
print(sorted(L))


#  returning a function 
def f():
    def x(a,b):
        return a + b
    return x             # returning a function 
val=f()(3,4)
print(val)


# functions as argument

def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_b')
    return z()

print(func_b(func_a))