import numpy as np
import matplotlib.pyplot as plt
import SHAPE
import MATERIAL

class bending:
    def __init__(self, number_of_suppport, force_total, safety_factor, length, my_shape, my_material):
        self.number_of_support = number_of_suppport
        self.force_distributed = force_total / length * safety_factor
        self.safety_factor = safety_factor
        self.length = length
        self.my_shape = my_shape
        self.my_material = my_material

        if self.number_of_support == 1:
            self.f_y = self.force_distributed * self.length
            self.m_z = self.force_distributed * self.length * length / 2
            self.c_1 = 0
        if self.number_of_support == 2:
            self.f_y = self.force_distributed * self.length / 2
            self.m_z = 0
            self.c_1 = self.force_distributed / 24 * self.length ** 3 - self.f_y / 6 * self.length ** 2
        self.c_2 = 0

        x = np.linspace(0, self.length, 100)
        q = self.displacement(x)
        s = self.stress(x)
        m = [self.my_material.yield_strength] * len(s)
        fig, ax = plt.subplots(2,1)

        ax[0].plot(x,q)
        ax[1].plot(x,s)
        ax[1].plot(x,m)

        ax[0].set_aspect('equal')
        ax[0].set_xlim(0, self.length)

        ax[0].set_xlabel('length [m]')
        ax[0].set_ylabel('displacement [m]')
        ax[1].set_xlabel('length [m]')
        ax[1].set_ylabel('stress [Pa]')

        ax[0].set_title('max: ' + str(np.round(np.max(abs(q)),4)) + ' [m]')
        ax[1].set_title('max: ' + str(np.round(np.max(s),4)) + ' [Pa]')

        plt.show()
        plt.close

    def displacement(self, x):
        return 1 / (self.my_material.e_modulus * self.my_shape.moment_of_inertia) * (self.f_y / 6 * x ** 3 - self.force_distributed / 24 * x ** 4 - self.m_z / 2 * x ** 2 + self.c_1 * x)

    def stress(self, x):
        return (self.f_y * x - self.force_distributed * x * x / 2 - self.m_z) / self.my_shape.moment_of_resistance


battery_rod = bending(2, 2.5 * 9.81 * 10 / 2, 2, 0.043 * 10, SHAPE.my_circle_tube, MATERIAL.my_steel)
battery_rod = bending(2, 2.5 * 9.81 * 12 / 2, 2, 0.043 * 12, SHAPE.my_circle, MATERIAL.my_steel)
#box = bending(2, 2.5 * 9.81 * 12 / 1, 0.043 * 12, 2, SHAPE.my_rectangle, MATERIAL.my_steel)
#box_tube_vw = bending(2, 2.5 * 9.81 * 12 * 8 / 3, 2, 0.141 * 8 / 3, SHAPE.my_rectangle_tube, MATERIAL.my_steel)