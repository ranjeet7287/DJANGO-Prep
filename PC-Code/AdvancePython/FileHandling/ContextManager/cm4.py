# working with other data types
# with open('sample.txt','w') as f:
#   f.write(5)
#   TypeError                                 Traceback (most recent call last)
# <ipython-input-26-a8e7a73b1431> in <module>
#       1 # working with other data types
#       2 with open('sample.txt','w') as f:
# ----> 3   f.write(5)

# TypeError: write() argument must be str, not int

with open('sample.txt','w') as f:
    f.write('5')
with open('sample.txt','r') as f:
    print(int(f.read()) + 5)