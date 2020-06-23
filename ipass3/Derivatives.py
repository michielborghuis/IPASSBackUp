import numpy as np
from ipass3.Plot import plot
from ipass3.EulersMethod import calculate


class Derivatives:
    def __init__(self, population, e0, contacts, spreaddays, leninc):

        self.population = population                        # (N) 100 % population
        self.exposed = e0                                  # I(t) 0 % of the population is infected in the beginning
        self.infected = 0
        self.susceptible = self.population - self.infected  # S(t) 99 % of the population is susceptible in the beginning
        self.recovered = 0                                  # R(t) 0 % of the population is recoverd in the beginning

        self.contacts = contacts
        self.spreadDays = spreaddays
        self.recovPerDay = 1 / self.spreadDays
        self.r0 = self.contacts / self.recovPerDay
        self.lengthOfIncubation = 1/leninc

    def set_population(self, population):
        self.population = population

    def susceptible_function(self, S, I):
        return -self.contacts * S * I / self.population

    def exposed_function(self, I, S, E):
        return self.contacts * I * S / self.population - self.lengthOfIncubation * E

    def infected_function(self, E, I):
        return self.lengthOfIncubation * E - self.recovPerDay * I

    def recovered_function(self, I):
        return self.recovPerDay * I

    def deriv(self, y):
        S, E, I, R = y
        dSdt = self.susceptible_function(S, I)
        dEdt = self.exposed_function(I, S, E)
        dIdt = self.infected_function(E, I)
        dRdt = self.recovered_function(I)
        return dSdt, dEdt, dIdt, dRdt

    def calculate(self):
        S0, E0, I0, R0 = self.susceptible, self.exposed, self.infected, self.recovered
        t = np.linspace(0, 99, 100)
        y0 = S0, E0, I0, R0

        S, E, I, R = calculate(self.deriv, y0, t)
        plot(t, S, E, I, R)
