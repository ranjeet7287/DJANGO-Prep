# reading from files

# using read()
f = open('AdvancePython/FileHandling/Sample3.txt','r')
s = f.read()
print(s)
f.close()


# reading upto n chars
f = open('AdvancePython/FileHandling/Sample3.txt','r')
s = f.read(2)
print(s)
f.close()


# readline() -> to read line by line 
f = open('sample.txt','r')
print(f.readline(),end='')
print(f.readline(),end='')

f.close()
