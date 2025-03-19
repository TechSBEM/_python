import math

print(
    'Q1---Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.')


class Line:

    def __init__(self, coor1, coor2):
        self.x1, self.y1 = coor1
        self.x2, self.y2 = coor2

    def distance(self):
        return math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)

    def slope(self):
        return (self.y2 - self.y1) / (self.x2 - self.x1)


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
print(f'Distance: {li.distance()}')
print(f'Slope: {li.slope()}')



print('Q2............Cylinder ---------------')
class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        self.pi = 3.14

    def volume(self):
        return self.pi* self.radius**2 *self.height

    def surface_area(self):
        area_base = 2 * self.pi * self.radius**2
        area_curved_surface = 2 * self.pi * self.radius * self.height
        return  area_base + area_curved_surface



c = Cylinder(2,3)
print(f'Volume of the cylinder: {c.volume()}')
print(f'Surface area of the cylinder: {c.surface_area()}')