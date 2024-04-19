def is_even(num):
    """
    This function returns if given number is even or odd
    input -> any valid integer
    output -> odd/even
    """
    if type(num) == int:
        if num % 2 ==0:
            return 'even'
        else:
            return 'odd'
    else:
        return "int send input send karo"
a = is_even('34rjo')
print(a)

for i in range(1,11):
    x=is_even(i)
    print(x)
