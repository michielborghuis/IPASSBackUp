from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
#
#
# def plotseird(t, S, E, I, R, D=None, L=None, R0=None, Alpha=None, CFR=None):
#     f, ax = plt.subplots(1, 1, figsize=(10, 4))
#     ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label='Susceptible')
#     ax.plot(t, E, 'y', alpha=0.7, linewidth=2, label='Exposed')
#     ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label='Infected')
#     ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label='Recovered')
#     if D is not None:
#         ax.plot(t, D, 'k', alpha=0.7, linewidth=2, label='Dead')
#         ax.plot(t, S + E + I + R + D, 'c--', alpha=0.7, linewidth=2, label='Total')
#     else:
#         ax.plot(t, S + E + I + R, 'c--', alpha=0.7, linewidth=2, label='Total')
#
#     ax.set_xlabel('Time (days)')
#
#     ax.yaxis.set_tick_params(length=0)
#     ax.xaxis.set_tick_params(length=0)
#     ax.grid(b=True, which='major', c='w', lw=2, ls='-')
#     legend = ax.legend(borderpad=2.0)
#     legend.get_frame().set_alpha(0.5)
#     for spine in ('top', 'right', 'bottom', 'left'):
#         ax.spines[spine].set_visible(False)
#     if L is not None:
#         plt.title("Lockdown after {} days".format(L))
#     plt.show();
#
#     if R0 is not None or CFR is not None:
#         f = plt.figure(figsize=(12, 4))
#
#     if R0 is not None:
#         # sp1
#         ax1 = f.add_subplot(121)
#         ax1.plot(t, R0, 'b--', alpha=0.7, linewidth=2, label='R_0')
#
#         ax1.set_xlabel('Time (days)')
#         ax1.title.set_text('R_0 over time')
#         # ax.set_ylabel('Number (1000s)')
#         # ax.set_ylim(0,1.2)
#         ax1.yaxis.set_tick_params(length=0)
#         ax1.xaxis.set_tick_params(length=0)
#         ax1.grid(b=True, which='major', c='w', lw=2, ls='-')
#         legend = ax1.legend()
#         legend.get_frame().set_alpha(0.5)
#         for spine in ('top', 'right', 'bottom', 'left'):
#             ax.spines[spine].set_visible(False)
#
#     if Alpha is not None:
#         # sp2
#         ax2 = f.add_subplot(122)
#         ax2.plot(t, Alpha, 'r--', alpha=0.7, linewidth=2, label='alpha')
#
#         ax2.set_xlabel('Time (days)')
#         ax2.title.set_text('fatality rate over time')
#         # ax.set_ylabel('Number (1000s)')
#         # ax.set_ylim(0,1.2)
#         ax2.yaxis.set_tick_params(length=0)
#         ax2.xaxis.set_tick_params(length=0)
#         ax2.grid(b=True, which='major', c='w', lw=2, ls='-')
#         legend = ax2.legend()
#         legend.get_frame().set_alpha(0.5)
#         for spine in ('top', 'right', 'bottom', 'left'):
#             ax.spines[spine].set_visible(False)
#
#         plt.show();
#
# def deriv(y, t, N, beta, gamma, delta):
#     S, E, I, R = y
#     dSdt = -beta * S * I / N
#     dEdt = beta * S * I / N - delta * E
#     dIdt = delta * E - gamma * I
#     dRdt = gamma * I
#     return dSdt, dEdt, dIdt, dRdt
#
#
# N = 1000
# D = 4.0 # infections lasts four days
# gamma = 1.0 / D
# delta = 1.0 / 5.0  # incubation period of five days
# R_0 = 5.0
# beta = R_0 * gamma  # R_0 = beta / gamma, so beta = R_0 * gamma
# S0, E0, I0, R0 = N-1, 1, 0, 0  # initial conditions: one exposed
# print(S0, E0, I0, R0)
#
# t = np.linspace(0, 99, 100) # Grid of time points (in days)
# y0 = S0, E0, I0, R0 # Initial conditions vector
#
# print(deriv(y0, t, N, beta, gamma, delta))  #klopt niet
# print(y0)                                   #klopt
# print(N)                                    #klopt
# print(beta)                                 #klopt
# print(gamma)                                #klopt
# print(delta)                                #klopt
# print(t)                                    #klopt
#
# # Integrate the SIR equations over the time grid, t.
# ret = odeint(deriv, y0, t, args=(N, beta, gamma, delta))
# S, E, I, R = ret.T
#
# plotseird(t, S, E, I, R)

# print(np.linspace(0, 20, 21))
print(992/1000)
t = np.linspace(0, 99.9, 1000)
print(t)
print(len(t))