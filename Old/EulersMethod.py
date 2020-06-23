class EulersMethod:
    pass


def calculate_derivatives_euler(function, initials, t):
    lstx = t
    dSdt = []   # list of slopes for the graph of susceptible people over time
    dEdt = []   # list of slopes for the graph of exposed people over time
    dIdt = []   # list of slopes for the graph of infected people over time
    dRdt = []   # list of slopes for the graph of recovered people over time
    dDdt = []   # list of slopes for the graph of dead people over time
    # add inital slopes
    dSdt.append(initials[0])
    dEdt.append(initials[1])
    dIdt.append(initials[2])
    dRdt.append(initials[3])
    dDdt.append(initials[4])

    counter = 0
    delta_x = 0.1   # steps of x-coordinate
    x_inc = 0
    target_x = t[-1]
    while x_inc < target_x:
        y = dSdt[counter], dEdt[counter], dIdt[counter], dRdt[counter], dDdt[counter]
        ans = function(y, x_inc)
        dSdt.append(y[0] + ans[0] * delta_x)
        dEdt.append(y[1] + ans[1] * delta_x)
        dIdt.append(y[2] + ans[2] * delta_x)
        dRdt.append(y[3] + ans[3] * delta_x)
        dDdt.append(y[4] + ans[4] * delta_x)
        x_inc += delta_x
        counter += 1
    return dSdt, dEdt, dIdt, dRdt, dDdt












