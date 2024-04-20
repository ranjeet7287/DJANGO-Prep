# seek and tell function

with open('PC-Code/AdvancePython/FileHandling/big.txt','r') as f:
    print(f.read(10))
    print(f.tell()) # tell where is my buffer
    f.seek(0)       # shift buffer from 10 -> 0 
    #  apni file kahi bhi ja sakte ho 
    print(f.read(10))
    print(f.tell()) 

with open('PC-Code/AdvancePython/FileHandling/big.txt','w') as f:
    f.write('Hello')
    f.seek(0)
    f.write('X')