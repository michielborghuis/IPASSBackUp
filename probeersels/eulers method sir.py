import numpy as np
import matplotlib.pyplot as plt
from ipass.EulersMethod import calculate


class Derivatives:
    def __init__(self, population, i0, contacts, healed):

        self.population = population                        # (N) 100 % population
        self.infected = i0                                  # I(t) 0 % of the population is infected in the beginning
        self.susceptible = self.population - self.infected  # S(t) 99 % of the population is susceptible in the beginning
        self.recovered = 0                                  # R(t) 0 % of the population is recoverd in the beginning

        self.contacts = contacts
        self.healed = healed

    def plot(self, t, S, I, R, D=None, L=None, Alpha=None, CFR=None):
        f, ax = plt.subplots(1, 1, figsize=(10, 4))
        ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
        ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
        ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
        ax.set_xlabel('Time (days)')
        plt.show()

    def set_population(self, population):
        self.population = population

    def susceptible_function(self, S, I):
        return -self.contacts * S * I / self.population

    def infected_function(self, I, S):
        return self.contacts * I * S / self.population - self.healed * I

    def recovered_function(self, I):
        return self.healed * I

    def deriv(self, y):
        S, I, R = y
        dSdt = self.susceptible_function(S, I)
        dIdt = self.infected_function(I, S)
        dRdt = self.recovered_function(I)
        return dSdt, dIdt, dRdt


    def calculate(self):
        S0, I0, R0 = self.susceptible, self.infected, self.recovered
        t = np.linspace(0, 99.8, 1000)
        y0 = S0, I0, R0

        S, I, R = calculate(self.deriv, y0, t)
        self.plot(t, S, I, R)


hey2 = Derivatives(27000, 10, 1.3, 0.1)
hey2.calculate()
