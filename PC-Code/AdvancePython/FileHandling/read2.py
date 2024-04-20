#  reading entire using readlines
f = open('PC-Code/AdvancePython/FileHandling/Sample3.txt','r')

while True:
    data = f.readline()
    if data == '':
        break
    else:
        print(data,end='')

f.close()



