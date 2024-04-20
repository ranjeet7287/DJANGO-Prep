# more complex data
d = {
    'name':'ranjeet',
    'age' : 20,
    'gender':'male'
}

with open('sample.txt','w') as f:
    f.write(str(d))

with open('sample.txt','r') as f:
    print(f.read())
    print(type(f.read()))
