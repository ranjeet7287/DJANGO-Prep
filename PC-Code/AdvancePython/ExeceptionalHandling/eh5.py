# finally

#            try     -------------> finally [Always Call either error or Success]
#          /      \
#      except      else
#        /            \
#    When error      When try
#     Occurred    Successfully done

try:
    f = open('sample.txt','r')
except FileNotFoundError:
    print('file not fond')
except Exception as error:
    print(error)
else:
    print(f.read())
finally:
    print('finally i print')
