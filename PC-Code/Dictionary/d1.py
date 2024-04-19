# Dictionary in Python is a collection of keys values, used to store data values like
#  a map, which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'nitish' , 'age' : 33 , 'gender' : 'male' }

# Character:
    # Mutable
    # Indexing has no meaning
    # keys can't be duplicated
    # keys can't be mutable items (list,set,dic itself)


# empty dic
d1={}
print(d1)

# 1D
d1 = {
    'name':'Bravo',
    'gender':'male'
    }
print(d1)

# Mixed Dic
d1={
    (1,2,3):'tuples',
    'hello':'world'
    }
print(d1)

# 2D dictionary
d1={
    'name':'Ranjeet',
    'role':'Junior Software Dev',
    'collage':{
        'sem':6,
        'dsa':80
    }
    }

# using sequence and dict function
# list of of tuples
d1 = dict([(1,1),(2,2),(3,3),(4,4)])
d1 = dict([('name','navi'),('love','ran')])


# 🚨 You cannot have duplicate keys
d1 = {
    'name':'ranj',
    'name':'love'
}

# mutable items as keys
d1 = {'name':'ranjeet',[1,2,3]:2}  # 🚨 Not allowed
d1 = {'name':'ranjeet',(1,2,3):2}  # ⭐ Allowed
