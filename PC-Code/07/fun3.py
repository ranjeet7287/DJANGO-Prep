# Local and Global Variable

# Global
x=10
def showX():
    print(x)
showX()

# Local 
y=10
def showY():
    y=5
    print(y)
showY()

# Error
z=10
def showZ():
    z+=1
    print(z)
showZ()

