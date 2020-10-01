class circle():
    pi=3.14
    def __init__(self, radius):
        self.radius=radius
        self.area=radius*radius*self.pi
    def circumfrence(self):
        return self.radius*self.pi*2
my_circle=circle(50)
print(my_circle.circumfrence())
print(my_circle.radius)
print(my_circle.area)