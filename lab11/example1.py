class silindir:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    def set_radius(self,x):
        self.radius = x
    def set_height(self,x):
        self.height = x
    def base(self):
        return 3.14 * self.radius**2
    def surface(self):
        return 6.28 * self.radius * self.height
    def area(self):
        return 2*base(self) + surface(self)
        
s1 = silindir(3,5)
