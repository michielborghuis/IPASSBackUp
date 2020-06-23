import sys

import numpy as np
from ipass5.Plot import plot
from ipass5.DerivativesCalculator import calculate_derivatives
import ipass5.populations as pop


class Derivatives:
    def __init__(self, population, e0, spreaddays, leninc, r0, deathrate, deathtime, lockdown, lockdownr0, method):

        self.count_while = 0
        self.count_plot = 0

        self.method = method

        self.population = self.population_function(population)        # total amount of people in the population
        self.exposed = e0                                   # initial amount of people exposed by the disease
        self.infected = 0                                   # initial amount of people infected by the disease
        self.susceptible = self.population - self.exposed   # initial amount of people susceptible for the disease
        self.recovered = 0                                  # initial amount of people recovered from the disease
        self.dead = 0                                       # initial amount of people who died from the disease

        self.spreadDays = spreaddays                # number of days an infected person has and can spread the disease
        self.spreadPerDay = 1 / self.spreadDays      # proportion of infected recovering per day
        self.incubationRate = 1 / leninc            # rate at which exposed people become infected
        self.r0 = r0                                # number of people an infected person infects
        self.deathRate = deathrate                  # death rate
        self.deathPerDay = 1/deathtime              # rate at which people die
        self.lockdown = lockdown                    # day at which a lockdown is implemented
        self.locksownr0 = lockdownr0                # number of people an infected person infects after the lockdown

    def R_0_function(self, t):  # number of people an infected person infects
        if t < self.lockdown:
            return self.r0
        else:
            return self.locksownr0

    def population_function(self, population):  # total amount of people in the population
        if type(population) == int or type(population) == float:
            return population
        else:
            return pop.world_population(population)

    def contacts_function(self, t):     # amount of people an infected person infects per day
        return self.R_0_function(t) * self.spreadPerDay

    def susceptible_function(self, t, S, I):
        return -self.contacts_function(t) * S * I / self.population

    def exposed_function(self, t, S, E, I):
        return self.contacts_function(t) * S * I / self.population - self.incubationRate * E

    def infected_function(self, E, I):
        return self.incubationRate * E - (1-self.deathRate) * self.spreadPerDay * I - self.deathRate * self.deathPerDay * I

    def recovered_function(self, I):
        return (1-self.deathRate) * self.spreadPerDay * I

    def dead_function(self, I):
        return self.deathPerDay * self.deathRate * I

    def deriv(self, y, t):
        S, E, I, R, D = y
        dSdt = self.susceptible_function(t, S, I)
        dEdt = self.exposed_function(t, S, E, I)
        dIdt = self.infected_function(E, I)
        dRdt = self.recovered_function(I)
        dDdt = self.dead_function(I)
        return dSdt, dEdt, dIdt, dRdt, dDdt

    def calculate3(self, days, steps):
        S0, E0, I0, R0, D0 = self.susceptible, self.exposed, self.infected, self.recovered, self.dead
        t = np.linspace(0, days, steps)
        y0 = S0, E0, I0, R0, D0

        S, E, I, R, D = calculate_derivatives(self.deriv, y0, t, self.method)
        while I[-1] > self.population / 100 or S[-500] > self.population/100*99:
            self.count_while += 1
            if self.count_while > 20:
                plot(t, S, E, I, R, D)
            print(I[-1] > self.population / 100)
            print(I[-1])
            print(self.population/100)

            print(S[-500] > self.population/100*99)
            print(S[-500])
            print(self.population/100*99)

            print('--------------------------------')
            try:
                newdays = days + 100
                newsteps = steps + 1000
                t = np.linspace(0, days + 100, steps + 1000)
                S, E, I, R, D = calculate_derivatives(self.deriv, y0, t, self.method)
            except:
                newdays = days + 100.1
                newsteps = steps + 1000
                t = np.linspace(0, days+100.1, steps+1000)
                S, E, I, R, D = calculate_derivatives(self.deriv, y0, t, self.method)
        # return t, S, E, I, R, D
        if self.count_plot == 0:
            plot(t, S, E, I, R, D)
            self.count_plot += 1
        else:
            sys.exit()

    def calculate2(self, days, steps):
        S0, E0, I0, R0, D0 = self.susceptible, self.exposed, self.infected, self.recovered, self.dead
        t = np.linspace(0, days, steps)
        y0 = S0, E0, I0, R0, D0

        S, E, I, R, D = calculate_derivatives(self.deriv, y0, t, self.method)
        return t, S, E, I, R, D

    def calculate(self, days, steps):
        print(days)
        print(steps)

        S0, E0, I0, R0, D0 = self.susceptible, self.exposed, self.infected, self.recovered, self.dead
        t = np.linspace(0, days, steps)
        y0 = S0, E0, I0, R0, D0

        S, E, I, R, D = calculate_derivatives(self.deriv, y0, t, self.method)
        if I[-1] > self.population/100 or S[-500] > self.population/100*99:
            self.count_while += 1
            if self.count_while > 20:
                plot(t, S, E, I, R, D)
            else:
                try:
                    self.calculate(days+100, steps+1000)
                except:
                    self.calculate(days+100.1, steps+1000)
        else:
            plot(t, S, E, I, R, D)
