class Fractions:

    # Parameterized constructor -> providing input 
    def __init__(self,x,y):
        self.num=x
        self.den=y
    
    # Whenever we print object it trigger this 
    def __str__(self):
        return f"{self.num}/{self.den}"
        # return '{}/{}'.format(self.num,self.den)

    def __add__(self,other):
        # return self.num + self.den
        x = self.num * other.den + other.num * self.den
        y = self.den * other.den
        return f"{x}/{y}"
    
    def __sub__(self,other):
        # return self.num + self.den
        x = self.num * other.den - other.num * self.den
        y = self.den * other.den
        return f"{x}/{y}"

    def __mul__(self,other):
        # return self.num + self.den
        x = self.num * other.num 
        y = self.den * other.den
        return f"{x}/{y}"

    def __truediv__(self,other):
        # return self.num + self.den
        x = self.num * other.den 
        y = self.den * other.num
        return f"{x}/{y}"
    
    def convert_to_decimal(self):
        return self.num/self.den

obj1 = Fractions(3,4)
obj2 = Fractions(5,4)

print("Add",obj1+obj2) 
print("Sub",obj1-obj2) 
print("Mul",obj1*obj2) 
print("Div",obj1/obj2) 
print(obj1.convert_to_decimal()) 
