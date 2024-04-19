# Enclosure
def outer():
    x="local"
    def inner():
        print(x)
    inner()
    print(x)
outer()