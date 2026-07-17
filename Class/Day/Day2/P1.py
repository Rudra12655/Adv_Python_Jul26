class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass
# Child class
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return 2*3.14*self.radius
    
circle = Circle(5)
print(circle.area())