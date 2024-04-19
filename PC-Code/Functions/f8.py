# Higher Order functions

def square(x):
    return x**2

# transform is HOF
def transform(fun,li):
    out=[]
    for i in li:
        out.append(fun(i))
    return out
L = [1,2,3,4,5]
res=transform(square,L)
print(res)

# HOF
    # Map
    # filter
    # reduce 
