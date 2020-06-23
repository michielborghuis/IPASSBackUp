from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

class Derivatives:
    def __init__(self, ):
        self.population = 1000       # (N) 100 % population
        self.susceptible = self.population - 1       # S(t) 99 % of the population is susceptible in the beginning
        self.exposed = 1            # E(t) 1 % of the population is exposed in the beginning
        self.infected = 0           # I(t) 0 % of the population is infected in the beginning
        self.recovered = 0          # R(t) 0 % of the population is recoverd in the beginning

        self.days = 4.0
        self.gamma = 1.0 / self.days
        self.delta = 1.0 / 5.0
        self.R_0 = 100.0
        self.beta = self.R_0 * self.gamma

    def plot(self, t, S, E, I, R):
        f, ax = plt.subplots(1, 1, figsize=(10, 4))
        ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
        ax.plot(t, E, 'y', alpha=0.7, linewidth=2, label='Exposed')
        ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
        ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
        ax.plot(t, S + E + I + R, 'c--', alpha=0.7, linewidth=2, label='Total')
        ax.set_xlabel('Time (days)')

        plt.show()

    def set_population(self, population):
        self.population = population

    def set_R_0(self, R_0):
        self.R_0 = R_0

    def set_days(self, days):
        self.days = days

    def okesusceptible(self, S, I):
        return -self.beta * S * I / self.population

        # self.susceptible = -self.beta * self.susceptible * self.infected / self.population
        # return self.susceptible

    def okeexposed(self, S, I, E):
        return self.beta * S * I / self.population - self.delta * E

        # self.exposed = self.beta * self.susceptible * self.infected / self.population - self.delta * self.exposed
        # return self.exposed

    def okeinfected(self, E, I):
        return self.delta * E - self.gamma * I

        # self.infected = self.delta * self.exposed - self.gamma * self.infected
        # return self.infected

    def okerecovered(self, I):
        return self.gamma * I

        # self.recovered = self.gamma * self.infected
        # return self.recovered

    def deriv(self, y, t):
        S, E, I, R = y
        dSdt = -self.beta * S * I / self.population
        dEdt = self.beta * S * I / self.population - self.delta * E
        dIdt = self.delta * E - self.gamma * I
        dRdt = self.gamma * I
        return dSdt, dEdt, dIdt, dRdt

    def deriv2(self, y, t):
        S, E, I, R = y
        dSdt = self.okesusceptible(S, I)
        dEdt = self.okeexposed(S, I, E)
        dIdt = self.okeinfected(E, I)
        dRdt = self.okerecovered(I)
        print(dSdt, dEdt, dIdt, dRdt)
        return dSdt, dEdt, dIdt, dRdt

    def calculate(self):
        S0, E0, I0, R0 = self.susceptible, self.exposed, self.infected, self.recovered
        t = np.linspace(0, 99.9, 1000)
        y0 = S0, E0, I0, R0
        ret = odeint(self.deriv, y0, t)
        S, E, I, R = ret.T
        self.plot(t, S, E, I, R)

    def calculate2(self):
        S0, E0, I0, R0 = self.susceptible, self.exposed, self.infected, self.recovered
        t = np.linspace(0, 99, 100)
        y0 = S0, E0, I0, R0
        ret = odeint(self.deriv2, y0, t)
        print(ret)
        print(ret.T)
        S, E, I, R = ret.T
        self.plot(t, S, E, I, R)


# hey = Derivatives()
# hey.set_R_0(10)
# hey.calculate()

hey2 = Derivatives()
print(hey2.R_0)
hey2.set_R_0(2)
print(hey2.R_0)
hey2.calculate2()