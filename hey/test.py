from Old.HeunsMethod import calculate_derivatives_heun
import numpy as np

class VB:
    def __init__(self, big):
        self.big = big

    def deriv(self, y, t):
        dydt = y
        return dydt

    def calculate(self):
        y0 = 0
        t = np.linspace(0, self.big)
        y = calculate_derivatives_heun(self.deriv, y0, t)
