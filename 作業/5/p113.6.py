import math

class Circle:
    def __init__(self, r):
        self.r=r
    
    def perimeter(self):
        return 2*math.pi*self.r
    
    def square(self):
        return math.pi*self.r**2

c1=Circle(5)
c2=Circle(10)

print('c1 per:',c1.perimeter())
print('c1 squ:',c1.square())
print('c2 per:',c2.perimeter())
print('c2 squ:',c2.square())