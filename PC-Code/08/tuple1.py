a = 1,2
print(type(a))
print(a)

# Un-packing assingnment in tuple
c,d = a
print(c)
print(d)

# swaping
x = 1
y = 5
x , y = y, x 
print(x,y)

# list to tuple
l = [1,2,3,4,5]
t = tuple(l)
print(t)

# tuple to list 
t = (1,2,3,4,5)
l = list(t)
print(l)

#  Returning multiple values from a functions
def addSub(a,b):
    return a+b,a-b
a,s = addSub(5,4)
print(a)
print(s)