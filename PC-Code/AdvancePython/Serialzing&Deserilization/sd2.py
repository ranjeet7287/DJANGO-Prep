import json

with open('demo.json','r') as f:
    d = json.load(f)
    print(d)
    print(type(d))