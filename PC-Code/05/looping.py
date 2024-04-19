# While loop
a = 10
while a > 0:
    print(a)
    a-=1


# for loop
for i in "python":
    print(i)

# range(5)      -> [0,5)  -> 0,1,2,3,4
# range(2,10)   -> [2,10) -> 2,3,4,5...9
# range(1,11,2) -> [1,11) -> 1,3,5,7,9

for i in range(5):
    print(i)

for i in range(2,10):
    print(i)

for i in range(2,10,2):
    print(i)