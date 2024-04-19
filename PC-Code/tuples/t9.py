# tuple unpacking
a,b,c = (1,2,3)
print(a)
print(b)
print(c)

a,b = (1,2,3) # error 
    # ^^^
# 🚨 ValueError: too many values to unpack (expected 2) 🚨

