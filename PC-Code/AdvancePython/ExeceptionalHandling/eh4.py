#  try k success k baad kuch karna ho tho

try:
    f = open('sample.txt','r')
except FileNotFoundError:
    print('file not fond')
except Exception as error:
    print(error)
else:
    print(f.read())

#            try 
#          /      \
#      except      else
#        /            \
#    When error      When try
#     Occurred    Successfully done

