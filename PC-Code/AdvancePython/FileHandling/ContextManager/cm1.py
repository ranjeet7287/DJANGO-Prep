# Using Context Manager (With)

    # It's a good idea to close a file after usage as it will free up the resources

    # If we dont close it, garbage collector would close it

    # with keyword closes the file as soon as the usage is over


# with also closed the file as work is finish
with open('PC-Code/AdvancePython/FileHandling/Sample3.txt','w') as f:
    f.write('Janny')

# try f.read() now 
with open('PC-Code/AdvancePython/FileHandling/Sample3.txt','r') as f:
    print(f.read())

# moving within a file -> 2 char then 2 char
with open('PC-Code/AdvancePython/FileHandling/Sample3.txt','r') as f:
    print(f.read(2))
    print(f.read(2))
# magic of buffer memory 


# benefits? -> to load a big file in memory

big_l=['hello janny' for i in range(10000)]

with open('PC-Code/AdvancePython/FileHandling/big.txt','w') as f:
    f.writelines(big_l)

with open('PC-Code/AdvancePython/FileHandling/big.txt','r') as f:
    
    chunk_size = 100

    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size),end='')
        f.read(chunk_size)

