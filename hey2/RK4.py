class RK4:
    pass

def calculate_derivatives_rk4(function, initials, t):
    lstx = t
    dydt = []

    dydt.append(initials)

    counter = 0
    delta_x = 0.1
    x_inc = 0
    target_x = t[-1]

    while x_inc < target_x:
        yn = dydt[counter]

        k1 = function(yn, x_inc)
        k2 = function(yn + delta_x*k1/2, x_inc + delta_x/2)
        k3 = function(yn + delta_x*k2/2, x_inc + delta_x/2)
        k4 = function(yn + delta_x*k3, x_inc+delta_x)

        actualy = yn + 1/6*delta_x*(k1+2*k2+2*k3+k4)
        dydt.append(actualy)

        x_inc += delta_x
        counter += 1
    return dydt