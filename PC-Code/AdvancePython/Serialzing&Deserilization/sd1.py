# Serialization and Deserialization
    # Serialization -> process of converting python data types to JSON format
    # Deserialization -> process of converting JSON to python data types

# serialization using json module
# list
import json
L = [1,3,4,4]

with open('demo.json','w') as f:
    json.dump(L,f) # what to dump,file handler   

# dict

d={
    'name':'ranjeet',
    'age':20,
    'gender':'male'
}

with open('demo.json','w') as f:
    json.dump(d,f,indent=4)