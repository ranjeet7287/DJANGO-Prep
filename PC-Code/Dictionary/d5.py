# Dictionary Operation
    # -> Membership
    # -> Iteration

d1={
    'userId':'vfmhev11o30238njndxx',
    'userName':'utiurjj',
    'first_name':'Ranjeet',
    'last_name' :'singh',
    'mobile_no': 9026728737,
    'subject':{
        'cpp':'5/10',
        'js':'8/10',
        'native':'9/10',
        
    }
}

# In dict everything is about key 
print('ranjeet' in d1) 
print('userId' in d1)

# print all the key of dict
for i in d1:
    print(i)

# print all the value of dict
for i in d1:
    print(i,d1[i])

