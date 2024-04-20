# Problems with working in text mode
    # can't work with binary files like images
    # not good for other data types like int/float/list/tuples

# working with binary file

# with open('PC-Code/AdvancePython/FileHandling/ContextManager/basic-django.png','r') as f:
#     f.read()


with open('PC-Code/AdvancePython/FileHandling/ContextManager/basic-django.png','rb') as f:
    with open('PC-Code/AdvancePython/FileHandling/ContextManager/basic-django_copy.png','wb') as wf:
        wf.write(f.read())
    