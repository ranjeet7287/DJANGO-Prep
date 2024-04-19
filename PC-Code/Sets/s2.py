# Empty
s1={}
print(s1)
print(type(s1)) # <class 'dict'>

# Write way to make a empty set is using the concept of type conversion
s2=set()
print(type(s2))

# 1D and 2D
s3={1,2,3,4}
print(s3)  
# 2D we cannot make
# s4={1,3,4,{2,5,6}}
# print(s4) # 🚨 TypeError: unhashable type: 'set 🚨


# Homo and Hetro
s5={1,'hello',4.5,True}
print(s5)

# {1, 'hello', 4.5} where is true ? Because you cannot have duplicate value in sets
# python treat True as 1 that's why True did'nt printed  

# Using type conversion
s6=set([1,2,3,4,5])
print(s6)

# duplicates not allowed
s7={1,2,1,2,3,5,6}
print(s7)

# Set can't have mutable items
s8={1,2,3,[4,5]}
print(s8) # 🚨 TypeError: unhashable type: 'list' 🚨
