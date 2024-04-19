# Problem with w mode
#  introducing append mode

f = open('sample.txt','a')
f.write('\n play thu hai kha')
f.close()

#  write lines
L = ['hello\n','hi\n','one\n','love\n']
f = open('sample.txt','w')
f.writelines(L)



