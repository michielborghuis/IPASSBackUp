from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def model(y, t):
    k = 0.3
    dydt = -k * y
    print(dydt)
    return dydt

y0 = 5
t = np.linspace(0, 20, 21)
y = odeint(model, y0, t)
print(y)
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()