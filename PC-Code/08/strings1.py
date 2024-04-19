# String Concat
a = 1 
b = 2
c = 3
print(str(a)+'-'+str(b)+'-'+str(c))

# String Patters
print("%d-%d-%d" % (a,b,c))


# Postional Formating
print("{}-{}-{}".format(a,c,b))

name = "Ranjeet Singh"
age  = 20
print("My name is {} and I am {} years old".format(name,age))

# Indexed Postional Formating
name = "Bravo"
postion ="Deck"
print("Control room {1} this side from {0}".format(postion,name))

# Latest Way of formating

first_name="Ranjeet"
last_name="Singh"
print(f"{first_name} {last_name}")