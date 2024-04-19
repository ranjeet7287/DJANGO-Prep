def div(a,b):
    try:
        return a/b
    except:
        print("Error")
    finally:
        print("Wrapping Up")

div(10,2)
div(10,0)