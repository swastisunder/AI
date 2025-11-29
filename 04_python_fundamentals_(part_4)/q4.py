'''
Create a class Shape with a method area().
Then create subclasses Circle, Rectangle, and Triangle, and override the area() method in each subclass.
'''

class Shape:
    def area():
        return 0
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
        
    def area(self):
        return self.length * self.width
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    
    def area(self):
        return 0.5 * self.base * self.height
    
c = Circle(5)
print("Circle Area:", c.area())

r = Rectangle(4, 6)
print("Rectangle Area:", r.area())

t = Triangle(10, 8)
print("Triangle Area:", t.area())