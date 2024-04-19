# Set Operations
s1={1,2,3,4,5}
s2={6,7,8,9,10,3}

# Union (|), Unique elements
print(s1|s2)

# Intersection (&)
print(s1 & s2)

# Difference (-)
print(s1-s2)
print(s2-s1)

# Symmetric Difference 
print(s1 ^ s2) # not contain common element

# Membership Test
print(1 in s1)

# Iteration
for i in s1:
    print(i)
