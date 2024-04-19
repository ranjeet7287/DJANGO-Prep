# Dictionary Functions
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


# 🎃 Len
print(len(d1))

# 🎃 sorted fun -> always gives output in list
print(sorted(d1))
print(sorted(d1,reverse=True))

# 🎃 min -> min key on the base of ASCII
print(min(d1))

# 🎃 max -> max key on the base of ASCII
print(max(d1))

# 🎃 items/keys/values

# 🎃 items -> show all key-value key in the form of list of tuples
print(d1.items())

# 🎃 keys -> show all keys in the form of list
print(d1.keys())

# 🎃 values -> show all values in the form of list 
print(d1.values())


subjects_scores = {
    'Math': 85,
    'Science': 90,
    'English': 75,
    'History': 80,
    'Geography': 88
}

min_score = min(subjects_scores.values())
max_score = max(subjects_scores.values())

print("Minimum score:", min_score)
print("Maximum score:", max_score)

# 🎃 update
d1 ={'name':'ranjeet','email_id':'sranjeet434@gmail.com','phone':901020020}
d2= {'phone':9026728737,'address':'krishna nagar'}
d1.update(d2)
print(d1)