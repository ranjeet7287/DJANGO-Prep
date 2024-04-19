# Adding key value pair
d1={
    'name':'navi'
}
d1['Bday']='1903'
d1['weight']='45'
print(d1) 

# Remove key-value pair
    # 🎃 pop
    # 🎃 popitem
    # 🎃 del
    # 🎃 clear

d1={
    'userId':'vfmhev11o30238njndxx',
    'userName':'utiurjj',
    'first_name':'Ranjeet',
    'last_name' :'singh',
    'mobile_no': 9026728737
}

# pop
d1.pop('mobile_no')
print(d1)

# popitem -> Delete last item from the list
d1.popitem()
print(d1)

# del -> Both specific and whole dict
del d1['userId']
print(d1)
# del d1
# print(d1)

# clear -> give empty dict
d1.clear()
print(d1)
