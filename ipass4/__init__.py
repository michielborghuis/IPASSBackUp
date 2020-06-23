from ipass4.Derivatives import Derivatives

if __name__ == '__main__':
    # 1. total population
    # 2. initial amount of people exposed by the disease
    # 3. amount of people an infected person infects per day
    # 4. number of days an infected person has and can spread the disease
    # 5. length of incubation period
    # 6. death rate
    # 7. number of days it takes before someone dies
    # population, e0, contacts, spread days, len inc, death rate, death time

    model1 = Derivatives(1000000, 1, 1.2, 8, 5, 0.02, 13)
    model1.calculate()

    model2 = Derivatives(1000000, 5, 0.8, 10, 4, 0.5, 14)
    model2.calculate()