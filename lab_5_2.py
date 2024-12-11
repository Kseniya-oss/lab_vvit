class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


radius = 37
one_circle = Circle(radius)
one_circle.set_radius(48)
print(one_circle.get_radius())