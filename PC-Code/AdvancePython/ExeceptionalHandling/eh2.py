# Exceptions
    # If things go wrong during the execution of the program(runtime). It generally happens when something unforeseen has happened.

# Exceptions are raised by python runtime
    # You have to takle is on the fly

# Examples
    # Memory overflow
    # Divide by 0 -> logical error
    # Database error


# Why is it important to handle exceptions
    # how to handle exceptions
    # -> Try except block

with open('sample.txt','w') as f:
    f.write('jai mata di')

# Whenever you are daling with external pice of code 
# use try except block 

try:
    with open('sample55.txt','r') as f:
        print(f.read())
except:
    print("Sorry file not found")
