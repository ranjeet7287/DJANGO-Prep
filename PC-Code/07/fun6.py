# This Code will give error reason is that their is global x outside of outer 
# def outer():
#     x=10
#     def inner():
#         global x
#         x+=5
#         print(x)
#     inner()
# outer()


# Corrected Version using nonlocal 
def outer():
    x=10
    def inner():
        nonlocal x
        x+=5
        print(x)
    inner()
outer()