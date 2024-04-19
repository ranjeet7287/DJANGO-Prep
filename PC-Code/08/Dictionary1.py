# Un-Ordered List
a={
    "name"  : "Ranjeet",
    "age"   :  20,
    "stack" : ["cpp","python","js"],
}
print(a["name"])

# Adding/Updating values
a['postions']='Software Devloper'
print(a)

# get()
age=a.get('age')
print(age)

# Using keys(), values(), items()
keys = a.keys()
values = a.values() # 
items = a.items()   # Create tuple of every(key,value)
print(keys)  
print(values)
print(items)