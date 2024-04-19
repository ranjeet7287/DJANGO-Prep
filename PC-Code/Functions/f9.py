# HOF
    # Map
    # filter
    # reduce 

# Map

# square the items of a list
list(map(lambda x:x**2,[1,2,3,4,5]))

# odd/even labelling of list items
L = [1,2,3,4,5]
list(map(lambda x:'even' if x%2 == 0 else 'odd',L))