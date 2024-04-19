# Benefits of using a function
    # Code Modularity
    # Code Readbility
    # Code Reuseability
    
# Lambda Functions
# A lambda function is a small anonymous functions
# A lambda function can take any number of arguments, but can only have one expression.

lf=lambda a,b : a + b
print(lf(5,5))

# Diff between lambda vs Normal Function
    # No name
    # lambda has no return value(infact,returns a function)
    # lambda is written in 1 line
    # not reusable

# Then why use lambda functions?
# They are used with HOF

# check if a string a in string
a = lambda st : 'a' in st
print(a('hello'))

# odd or even
a = lambda x : 'even' if x%2==0 else 'odd'
print(a(5))
print(a(6))