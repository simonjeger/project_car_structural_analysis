import numpy as np


class material:
    def __init__(self, e_modulus, yield_strength):
        self.e_modulus = e_modulus
        self.yield_strength = yield_strength


my_steel = material(210 * 10 ** 9, 415 * 10 ** 6)
my_aluminium = material(70 * 10 ** 9, 310 * 10 ** 6)