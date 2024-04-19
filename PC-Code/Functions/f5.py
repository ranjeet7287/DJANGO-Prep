x = 5
def fun():
    global x
    y=x+5
    print(y)
fun()

def f():
    def g():
        print('op dada')
    g()
    print("Jia Hind")

f()
