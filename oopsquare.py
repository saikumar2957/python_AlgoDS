class Square:
    def __init__(self,length):
        self.x=length
    def area(self):
        return self.x * self.x
    def perimeter(self):
        return 4*self.x
    def __sub__(self,other):
        return self.x + other.x
l=Square(2)
d=Square(4)
d=Square(8)
print(l.area())
print(l.perimeter())
print(d.area())
print(d.perimeter())
print(l-d)


