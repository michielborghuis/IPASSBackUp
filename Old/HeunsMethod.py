class HeunsMethod:
    pass


def calculate_derivatives_heun(function, initials, t):
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
        y = Si, Ei, Ii, Ri, Di
        intermediatesHalf = function(y, x_inc)

        intermediateS = Si + delta_x * intermediatesHalf[0]
        intermediateE = Ei + delta_x * intermediatesHalf[1]
        intermediateI = Ii + delta_x * intermediatesHalf[2]
        intermediateR = Ri + delta_x * intermediatesHalf[3]
        intermediateD = Di + delta_x * intermediatesHalf[4]

        y2 = intermediateS, intermediateE, intermediateI, intermediateR, intermediateD
        actualHalf = function(y2, x_inc)

        dSdt.append(Si + (delta_x/2) * (intermediatesHalf[0] + actualHalf[0]))
        dEdt.append(Ei + (delta_x/2) * (intermediatesHalf[1] + actualHalf[1]))
        dIdt.append(Ii + (delta_x/2) * (intermediatesHalf[2] + actualHalf[2]))
        dRdt.append(Ri + (delta_x/2) * (intermediatesHalf[3] + actualHalf[3]))
        dDdt.append(Di + (delta_x/2) * (intermediatesHalf[4] + actualHalf[4]))

        x_inc += delta_x
        counter += 1
    return dSdt, dEdt, dIdt, dRdt, dDdt
