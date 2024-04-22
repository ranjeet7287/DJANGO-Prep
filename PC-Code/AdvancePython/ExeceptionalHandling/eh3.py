#  Catching specific exception


#  Junior Dev Code
try:
    f = open('sample.txt','r')
    print(f.read())
    print(m)
except:
    print('Some error')

# Senior Dev Code

try:
    m=5
    f = open('sample.txt','r')
    print(f.read())
    print(m/0)
except FileNotFoundError:
    print('file not found')
except NameError:
    print('variable not found')
except ZeroDivisionError:
    print('zero division error')
except Exception as e:
    print(e)

