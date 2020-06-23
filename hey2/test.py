from hey2.euler import calculate_derivatives_euler
from hey2.heun import calculate_derivatives_heun
from hey2.RK4 import calculate_derivatives_rk4
import matplotlib.pyplot as plt
import numpy as np
from hey2.plot import plot
import math

class VB:
    def __init__(self):
        pass

    def deriv(self, y, t):
        dydt = y - 4
        return dydt

    def calculate(self):
        e = [1, 2.7182818285, 7.3890560989, 20.0855369232, 54.4981500331, 148.4131591026]
        y0 = 1
        t = np.linspace(0, 4.8, 50)
        print(t)
        y = calculate_derivatives_euler(self.deriv, y0, t)

        y2 = calculate_derivatives_heun(self.deriv, y0, t)

        y3 = calculate_derivatives_rk4(self.deriv, y0, t)

        f, ax = plt.subplots(1, 1, figsize=(10, 4))
        ax.plot([0, 1, 2, 3, 4, 5], e, 'r', alpha=0.7, linewidth=2, label='actual')
        ax.plot(t, y, 'g', alpha=0.7, linewidth=2, label='eulers method')
        ax.plot(t, y2, 'c', alpha=0.7, linewidth=2, label='heuns method')
        ax.plot(t, y3, 'b', alpha=0.7, linewidth=2, label='rk4')
        legend = ax.legend(borderpad=2.0)
        legend.get_frame().set_alpha(0.5)
        plt.show()

        for i in range(50):
            print(y[i], y2[i], y3[i], t[i])
