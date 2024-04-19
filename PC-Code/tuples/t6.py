# Operations on Tuples
# + and *
t1 = (1,2,3,4)
t2 = (5,6,7,8)
print(t1 + t2)

# print(t1*t2) 🚨TypeError: can't multiply sequence by non-int of type 'tuple'🚨
print(t1*2) #(1, 2, 3, 4, 1, 2, 3, 4)

# membership
print(1 in t1) # True
print(9 in t2) # False

# iteration 
for i in t1:
    print(i)
