# empty tuple
t1=()
print(t1) # ()

# create a tuple with a single item
t2=(2)
print(t2) # 2
print(type(t2)) #int

# write way to make single element tuple is 
t3=(2,)
print(t3)
print(type(t3))

# homo -> all element have same datatype
t4=(1,2,3,4)
print(t4)

# hetro 
t5=(1,'navi',2.4,True)
print(t5)

# 2d tuple
t6=(1,3,4,t4,('p','q','r','s'))
print(t6)

# using type conversion
t7=tuple('hello')
print(t7)