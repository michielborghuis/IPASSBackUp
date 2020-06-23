class EulersMethod:
    pass


def calculate_derivatives_euler(function, initials, t):
    lstx = t
    dydt = []   # list of slopes for the graph of susceptible people over time
    # add inital slopes
    dydt.append(initials)

    counter = 0
    delta_x = 0.1   # stepsize of x-coordinate
    x_inc = 0
    target_x = t[-1]
    while x_inc < target_x:
        y = dydt[counter]
        ans = function(y, x_inc)
        dydt.append(y + ans * delta_x)
        x_inc += delta_x
        counter += 1
    return dydt
