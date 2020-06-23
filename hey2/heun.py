class HeunsMethod:
    pass


def calculate_derivatives_heun(function, initials, t):
    lstx = t
    dydt = []   # list of slopes for the graph of susceptible people over time
    # add inital slopes
    dydt.append(initials)

    answers1 = []
    answers2 = []

    counter = 0
    delta_x = 0.1   # steps of x-coordinate
    x_inc = 0
    target_x = t[-1]
    while x_inc < target_x:
        yi = dydt[counter]
        benadering = yi + delta_x * (function(yi, x_inc))
        actual = yi + ((delta_x/2) * (function(yi, x_inc) + function(benadering, x_inc+delta_x)))
        dydt.append(actual)

        x_inc += delta_x
        counter += 1
    return dydt
