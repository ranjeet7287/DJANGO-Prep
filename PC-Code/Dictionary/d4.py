# Editing key-value pair
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
d1['subject']['cpp']='6/10'
print(d1)
d1['subject']['python']='1/10'
print(d1)