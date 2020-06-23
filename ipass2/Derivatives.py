import numpy as np
from ipass2.Plot import plot
from ipass2.EulersMethod import calculate


class Derivatives:
    def __init__(self, population, i0, contacts, spreaddays):

        self.population = population                        # (N) 100 % population
        self.infected = i0                                  # I(t) 0 % of the population is infected in the beginning
        self.susceptible = self.population - self.infected  # S(t) 99 % of the population is susceptible in the beginning
        self.recovered = 0                                  # R(t) 0 % of the population is recoverd in the beginning

        self.contacts = contacts
        self.spreadDays = spreaddays
        self.recovPerDay = 1 / self.spreadDays
        self.r0 = self.contacts / self.recovPerDay

    def set_population(self, population):
        self.population = population

    def susceptible_function(self, S, I):
        return -self.contacts * S * I / self.population

    def infected_function(self, I, S):
        return self.contacts * I * S / self.population - self.recovPerDay * I

    def recovered_function(self, I):
        return self.recovPerDay * I

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
        plot(t, S, I, R)