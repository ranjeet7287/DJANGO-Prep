#  Encapsulation 

# Write OOP classes to handle the following scenarios:
    # A user can create and view 2D coordinates
    # A user can find out the distance between 2 coordinates
    # A user can find find the distance of a coordinate from origin
    # A user can check if a point lies on a given line
    # A user can find the distance between a given 2D point and a given line

class Point:

    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y
    
    def __str__(self):
        return f"<{self.x_cord},{self.y_cord}>"

    # Distance between two points
    def euclidean_distance(self,other):
        x = (other.x_cord - self.x_cord)**2
        y = (other.y_cord - self.y_cord)**2
        return (x+y)**0.5

    # Distance from origin 
    def distance_from_origin(self):
        # x = (self.x_cord)**2
        # y = (self.y_cord)**2
        # return (x+y)**0.5
        return self.euclidean_distance(Point(0,0))
    

class Line:

    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    
    def __str__(self):
        return f"{self.A}x + {self.B}y + {self.C} = 0"
    
    def point_on_line(self,point):
        rhs = self.A * point.x_cord + self.B * point.y_cord + self.C
        lhs = 0
        if(rhs == lhs):
            return "lie on line"
        else:
            return "doesn't lie on line"

    def shortest_distance(self,point):
        return abs(self.A*point.x_cord + self.B*point.y_cord + self.C)/(self.A**2 + self.B**2)**0.5

p1=Point(0,0)
p2=Point(1,1)

result = p1.euclidean_distance(p2)
# print(result)

result = p2.distance_from_origin()
# print(result)


l1=Line(1,1,-2)
p1_on_l1 = l1.point_on_line(p2)
print(p1_on_l1)

print(l1.shortest_distance(p2))
# print(l1) 