# Difference b/w Tuples and Lists
# Syntax
# Mutability
# Speed
# Memory
# Built in functionality
# Error prone
# Usability

# Speed
import time 
L = list(range(100000000))
T = tuple(range(100000000))

start = time.time()
for i in L:
    i*5
print('List time',time.time()-start)

start = time.time()
for i in T:
    i*5
print('Tuple time',time.time()-start)



# Memory
import sys
L = list(range(1000))
T = tuple(range(1000))
print('List size',sys.getsizeof(L))
print('Tuple size',sys.getsizeof(T))

# Error prone
a = [1,2,3]
b = a
a.append(4)
print(a) 
print(b)
# 👻 Same output because pointing to same memory location


c = (1,2,3)
d = c
c = c + (4,)
print(c) # (1,2,3,4)
print(d) # (1,2,3)


# Usability
# Read Only functionality 👍
