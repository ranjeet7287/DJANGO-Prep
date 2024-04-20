# serialize and deserialize tuple
import json
t = (1,2,3,4,5)

with open('demo.json','w') as f:
    json.dump(t,f) # serialize in the form of list in json

