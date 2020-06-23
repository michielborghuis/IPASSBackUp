import numpy as np
from ipass4.Plot import plot
from ipass4.EulersMethod import calculate


class Derivatives:
    def __init__(self, population, e0, contacts, spreaddays, leninc, deathrate, deathtime):

        self.population = population                        # total amount of people in the population
        self.exposed = e0                                   # initial amount of people susceptible for the disease
        self.infected = 0                                   # initial amount of people exposed by the disease
        self.susceptible = self.population - self.infected  # initial amount of people infected by the disease
        self.recovered = 0                                  # initial amount of people recovered from the disease
        self.dead = 0                                       # initial amount of people who died from the disease

        self.contacts = contacts                    # amount of people an infected person infects per day
        self.spreadDays = spreaddays                # number of days an infected person has and can spread the disease
        self.recovPerDay = 1 / self.spreadDays      # proportion of infected recovering per day
        self.r0 = self.contacts / self.recovPerDay  # number of people an infected person infects
        self.incubationRate = 1 / leninc            # rate at which exposed people become infected
        self.deathRate = deathrate                  # death rate
        self.deathPerDay = 1/deathtime              # rate at which people die

    def set_population(self, population):
        self.population = population

    def susceptible_function(self, S, I):
        return -self.contacts * S * I / self.population

    def exposed_function(self, S, I, E):
        return self.contacts * S * I / self.population - self.incubationRate * E

    def infected_function(self, E, I):
        return self.incubationRate * E - (1-self.deathRate) * self.recovPerDay * I - self.deathRate * self.deathPerDay * I

    def recovered_function(self, I):
        return (1-self.deathRate) * self.recovPerDay * I

    def dead_function(self, I):
        return self.deathPerDay * self.deathRate * I

    def deriv(self, y):
        S, E, I, R, D = y
        dSdt = self.susceptible_function(S, I)
        dEdt = self.exposed_function(S, I, E)
        dIdt = self.infected_function(E, I)
        dRdt = self.recovered_function(I)
        dDdt = self.dead_function(I)
        return dSdt, dEdt, dIdt, dRdt, dDdt

    def calculate(self):
        S0, E0, I0, R0, D0 = self.susceptible, self.exposed, self.infected, self.recovered, self.dead
        t = np.linspace(0, 99.8, 1000)
        y0 = S0, E0, I0, R0, D0

        S, E, I, R, D = calculate(self.deriv, y0, t)
        plot(t, S, E, I, R, D)
