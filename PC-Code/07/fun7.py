# Packing of Arguments

# arga -> TUPLE
def Packing(*args):
    print(args)
Packing(1,2,"Ranjeet","Navneet",3)


# kwargs -> DICTONARY
def Packing2(**kwargs):
    print(kwargs)
Packing2(name="Ranjeet",love="Navneet")