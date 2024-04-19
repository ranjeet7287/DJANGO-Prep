# Global Variable 
x=10
def showX():
    global x
    x+=5
    print(x)
showX()
print(x)