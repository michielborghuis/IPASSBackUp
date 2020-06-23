class RungeKuttaMethod:
    pass


def calculate_derivatives_rk4(function, initials, t):
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

        Si, Ei, Ii, Ri, Di = dSdt[counter], dEdt[counter], dIdt[counter], dRdt[counter], dDdt[counter]
        yn = Si, Ei, Ii, Ri, Di
        k1 = function(yn, x_inc)

        ynk2 = yn[0]+k1[0]*delta_x/2, yn[1]+k1[1]*delta_x/2, yn[2]+k1[2]*delta_x/2, yn[3]+k1[3]*delta_x/2, yn[4]+k1[4]*delta_x/2
        k2 = function(ynk2, x_inc+delta_x/2)

        ynk3 = yn[0]+k2[0]*delta_x/2, yn[1]+k2[1]*delta_x/2, yn[2]+k2[2]*delta_x/2, yn[3]+k2[3]*delta_x/2, yn[4]+k2[4]*delta_x/2
        k3 = function(ynk3, x_inc+delta_x/2)

        ynk4 = yn[0]+k3[0]*delta_x, yn[1]+k3[1]*delta_x, yn[2]+k3[2]*delta_x, yn[3]+k3[3]*delta_x, yn[4]+k3[4]*delta_x
        k4 = function(ynk4, x_inc+delta_x)

        dSdt.append(yn[0] + 1/6*delta_x*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0]))
        dEdt.append(yn[1] + 1/6*delta_x*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1]))
        dIdt.append(yn[2] + 1/6*delta_x*(k1[2] + 2*k2[2] + 2*k3[2] + k4[2]))
        dRdt.append(yn[3] + 1/6*delta_x*(k1[3] + 2*k2[3] + 2*k3[3] + k4[3]))
        dDdt.append(yn[4] + 1/6*delta_x*(k1[4] + 2*k2[4] + 2*k3[4] + k4[4]))

        x_inc += delta_x
        counter += 1

    return dSdt, dEdt, dIdt, dRdt, dDdt
