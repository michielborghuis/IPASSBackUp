from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

class Derivatives:
    def __init__(self, ):
        self.population = 1000       # (N) 100 % population
        self.susceptible = self.population - 1       # S(t) 99 % of the population is susceptible in the beginning
        self.infected = 1           # I(t) 0 % of the population is infected in the beginning
        self.recovered = 0          # R(t) 0 % of the population is recoverd in the beginning

        self.contacts = 0.8
        self.healed = 0.1

    def plot(self, t, S, I, R):
        print(S, I, R)
        f, ax = plt.subplots(1, 1, figsize=(10, 4))
        ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
        ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
        ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
        ax.plot(t, S + I + R, 'c--', alpha=0.7, linewidth=2, label='Total')
        ax.set_xlabel('Time (days)')

        plt.show()

    def set_population(self, population):
        self.population = population


    def okesusceptible(self, S, I):
        return -self.contacts * S * I / self.population

        # self.susceptible = -self.beta * self.susceptible * self.infected / self.population
        # return self.susceptible

    def okeinfected(self, I, S):
        return self.contacts * I * S / self.population - self.healed * I

        # self.infected = self.delta * self.exposed - self.gamma * self.infected
        # return self.infected

    def okerecovered(self, I):
        return self.healed * I

        # self.recovered = self.gamma * self.infected
        # return self.recovered

    def deriv(self, y, t):
        S, I, R = y
        dSdt = self.okesusceptible(S, I)
        dIdt = self.okeinfected(I, S)
        dRdt = self.okerecovered(I)
        print(dSdt, dIdt, dRdt)
        return dSdt, dIdt, dRdt

    def derivatives_calculator(self):
        pass

    def calculate(self):
        S0, I0, R0 = self.susceptible, self.infected, self.recovered
        t = np.linspace(0, 100, 100)
        y0 = S0, I0, R0
        ret = odeint(self.deriv, y0, t)
        S, I, R = ret.T
        self.plot(t, S, I, R)


# hey = Derivatives()
# hey.set_R_0(10)
# hey.calculate()

hey2 = Derivatives()

hey2.calculate()