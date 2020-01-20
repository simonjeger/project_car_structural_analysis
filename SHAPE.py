import numpy as np


class circle:
    def __init__(self, diameter):
        self.diameter = diameter
        self.moment_of_inertia = np.pi * self.diameter ** 4 / 32
        self.moment_of_resistance = np.pi * self.diameter ** 3 / 16


class circle_tube:
    def __init__(self, diameter, thickness):
        self.diameter = diameter
        self.thickness = thickness
        self.moment_of_inertia = np.pi * (self.diameter ** 4 - (self.diameter - 2 * self.thickness) ** 4) / 32
        self.moment_of_resistance = np.pi * (self.diameter ** 4 - (self.diameter - 2 * self.thickness) ** 4) / (16 * self.diameter)


class rectangle:
    def __init__(self, hight, width):
        self.hight = hight
        self.width = width
        self.moment_of_inertia = self.width * self.hight ** 3 / 12
        self.moment_of_resistance = self.width * self.hight ** 2 / 6


class rectangle_tube:
    def __init__(self, hight, width, thickness):
        self.hight = hight
        self.width = width
        self.thickness = thickness
        self.moment_of_inertia = (self.width * self.hight ** 3 - (self.width - self.thickness) * (self.hight - self.thickness) ** 3) / 12
        self.moment_of_resistance = (self.width * self.hight ** 3 - (self.width - self.thickness) * (self.hight - self.thickness) ** 3) / (6 * self.hight)


my_circle = circle(8 * 10 ** -3)
my_circle_tube = circle_tube(8 * 10 ** -3, 2 * 10 ** -3)
my_rectangle = rectangle(30 * 10 ** -3, 10 * 10 ** -3)
my_rectangle_tube = rectangle_tube(25 * 10 ** -3, 10 * 10 ** -3, 2 * 10 ** -3)