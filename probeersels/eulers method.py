import numpy as np
import matplotlib.pyplot as plt


def function(x, y):
    return -0.3 * y


def euler(f_prime, initial_x, initial_y, target_x):
    lstx = []
    lsty = []
    lstdydx = []
    lstx.append(initial_x)
    lsty.append(initial_y)
    lstdydx.append(initial_y)

    delta_x = 0.0001
    x_inc = initial_x
    y_inc = initial_y
    while x_inc < target_x:
        y_inc += delta_x * f_prime(x_inc, y_inc)
        lsty.append(y_inc)
        x_inc += delta_x
        lstx.append(x_inc)
        lstdydx.append(y_inc)
    return lstx, lsty, lstdydx


x0 = 0
y0 = 5

answer = euler(function, x0, y0, 20)
print(answer)
plt.plot(answer[0], answer[2])
plt.show()