from ipass5.Derivatives import Derivatives
from ipass5.populations import world_population
from ipass5.Plot import plot

# if __name__ == '__main__':
    # 1. total population
    # 2. initial amount of people exposed by the disease
    # 3. number of days an infected person has and can spread the disease
    # 4. length of incubation period
    # 5. amount of people an infected person infects
    # 6. death rate
    # 7. number of days it takes before someone dies
    # population, e0, contacts, spread days, len inc, death rate, death time

    # model1 = Derivatives(['Netherlands', '2019'], 1, 8, 5, 9.6, 0.02, 13, 10000, 2.4, 2)
    # model1.calculate(99.8, 1000)

    # model1_2 = Derivatives(['Netherlands', '2019'], 1, 8, 5, 9.6, 0.02, 13, 50, 2.4)
    # model1_2.calculate()
    #
    # model1_3 = Derivatives(['Netherlands', '2019'], 1, 8, 5, 9.6, 0.02, 13, 40, 2.4)
    # model1_3.calculate()
    #
    # model1_4 = Derivatives(['Netherlands', '2019'], 1, 8, 5, 9.6, 0.02, 13, 30, 2.4)
    # model1_4.calculate()
    #
    # model2 = Derivatives(['Timor-Leste', '2000'], 5, 10, 4, 8, 0.5, 14, 100, 2)
    # model2.calculate()
    #
    # model2_2 = Derivatives(['Timor-Leste', '2000'], 5, 10, 4, 8, 0.5, 14, 50, 2)
    # model2_2.calculate()
    #
    # model2_3 = Derivatives(['Timor-Leste', '2000'], 5, 10, 4, 8, 0.5, 14, 40, 2)
    # model2_3.calculate()
    #
    # model2_4 = Derivatives(['Timor-Leste', '2000'], 5, 10, 4, 8, 0.5, 14, 30, 2)
    # model2_4.calculate()
    #
    # model3 = Derivatives(1000000, 1, 10, 2, 5, 0.08, 16, 60, 0.3)
    # model3.calculate()

# while_count = 0
# days = 99.8
# steps = 1000
#
# if __name__ == '__main__':
#     model1 = Derivatives(100000000000, 1, 8, 5, 9.6, 0.02, 13, 50, 2.4, 2)
#     t, S, E, I, R, D = model1.calculate2(days, steps)
#     while I[-1] > model1.population/100 or S[-500] > model1.population/100*99:
#         print(days)
#         print(steps)
#
#         print(I[-1] > model1.population/100)
#         print(I[-1])
#         print(model1.population/100)
#
#         print(S[-500] > model1.population/100*99)
#         print(S[-500])
#         print(model1.population/100*99)
#         while_count += 1
#         if while_count > 20:
#             plot(t, S, E, I, R, D)
#         days += 100
#         steps += 1000
#         t, S, E, I, R, D = model1.calculate2(days, steps)
#     plot(t, S, E, I, R, D)
