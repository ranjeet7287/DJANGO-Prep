#   Accessing items
d1={
    'name':'ranjeet',
    'role':'software dev',
    'age':20,
    'subject':{
        'cpp':'5/10',
        'js':'8/10',
        'native':'9/10'
    }

}
# 🚨 Indexing concept not allowed 🚨
# print(d1[0])

# []
print(d1['name'])
print(d1['subject']['native'])

# get
print(d1.get('name'))
print(d1.get('subject').get('native'))
